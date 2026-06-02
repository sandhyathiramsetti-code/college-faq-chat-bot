import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from fetcher import get_page_text
from pages import get_pages, get_college_name

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


# ── Piece 2: build the menu + system instruction ──
def build_menu():
    lines = [f"- {p['label']}: {p['url']} ({p['description']})" for p in get_pages()]
    return "\n".join(lines)

SYSTEM_INSTRUCTION = f"""You are a helpful FAQ assistant for {get_college_name()}.

You can use the fetch_page tool to read any of the pages listed below.
When the user asks a question:
1. Decide which page most likely contains the answer.
2. Call fetch_page with that page's exact URL.
3. Answer using ONLY the information from the fetched page(s).
4. If a page doesn't have the answer, you may fetch a different one.
5. If you truly can't find it, say so honestly — never make up facts.

Keep answers clear and concise.

Available pages:
{build_menu()}
"""

# ── Piece 1: the tool ──
fetch_page_declaration = types.FunctionDeclaration(
    name="fetch_page",
    description="Fetches and returns the text content of a web page given its URL.",
    parameters={
        "type": "object",
        "properties": {
            "url": {"type": "string",
                    "description": "The exact URL to fetch (from the available pages list)."}
        },
        "required": ["url"],
    },
)
tools = types.Tool(function_declarations=[fetch_page_declaration])

config = types.GenerateContentConfig(
    system_instruction=SYSTEM_INSTRUCTION,
    tools=[tools],
    # We run the loop ourselves, so disable the SDK's auto-calling
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True),
)


def _log(title, text):
    """Print a clearly bordered debug block."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")
    print(text)
    print(f"{'='*60}\n")


# ── Piece 3: the agentic loop ──
def answer_question(question, max_steps=5):
    contents = [types.Content(role="user", parts=[types.Part(text=question)])]

    for step in range(max_steps):
        # Log what we're sending to Gemini this turn
        prompt_summary = "\n".join(
            f"  [{c.role}] " + (
                c.parts[0].text[:200] if hasattr(c.parts[0], "text") and c.parts[0].text
                else str(c.parts[0])[:200]
            )
            for c in contents
        )
        _log(f"CALL #{step + 1} → sending {len(contents)} message(s) to Gemini", prompt_summary)

        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=contents,
            config=config,
        )

        # Case A: Gemini wants to call our tool
        if response.function_calls:
            fc = response.function_calls[0]
            url = fc.args.get("url")

            _log(f"CALL #{step + 1} ← Gemini response: TOOL CALL", f"  fetch_page(url='{url}')")

            page_text = get_page_text(url) or "Could not load this page."
            page_text = page_text[:8000]  # trim to stay fast / within limits

            _log(f"TOOL RESULT (first 500 chars)", page_text[:500])

            # Append Gemini's request, then our tool's result
            contents.append(response.candidates[0].content)
            contents.append(types.Content(
                role="user",
                parts=[types.Part.from_function_response(
                    name="fetch_page",
                    response={"content": page_text},
                )],
            ))
            continue  # loop again with the new info

        # Case B: no tool call → final answer
        _log(f"CALL #{step + 1} ← Gemini response: FINAL ANSWER", response.text[:500])
        return response.text

    return "Sorry, I couldn't find a clear answer to that."


if __name__ == "__main__":
    print(f"FAQ bot for {get_college_name()}. Type 'quit' to exit.")
    while True:
        q = input("\nYou: ")
        if q.lower() in ("quit", "exit"):
            break
        print("Bot:", answer_question(q))
