# pages.py
# Holds the page menus for multiple colleges.
# Switch colleges by changing ACTIVE_COLLEGE below — nothing else needs to change.
# All site URLs below were verified against each college's sitemap
# (Pragati: https://pragati.ac.in/page-sitemap.html, Aditya: https://www.adityauniversity.in/sitemap.xml).

COLLEGES = {
    # ──────────────────────────────────────────────────────────
    "pragati": {
        "name": "Pragati Engineering College",
        "base_url": "https://pragati.ac.in",
        "pages": [
            {"url": "https://pragati.ac.in/about-us/", "label": "About Us",
             "description": "College overview, history, vision and mission"},
            {"url": "https://pragati.ac.in/admissions/", "label": "Courses / Admissions",
             "description": "Programs and courses offered, admission criteria"},
            {"url": "https://pragati.ac.in/departments/", "label": "Departments",
             "description": "List of all engineering departments"},
            {"url": "https://pragati.ac.in/computer-science-engineering/about-cse-department/", "label": "CSE Department",
             "description": "Computer Science and Engineering department"},
            {"url": "https://pragati.ac.in/electronics-communication-engineering/about-ece-department/", "label": "ECE Department",
             "description": "Electronics and Communication Engineering department"},
            {"url": "https://pragati.ac.in/information-technology/about-it-department/", "label": "IT Department",
             "description": "Information Technology department"},
            {"url": "https://pragati.ac.in/mechanical-engineering/about-me-department/", "label": "Mechanical Department",
             "description": "Mechanical Engineering department"},
            {"url": "https://pragati.ac.in/electrical-electronics-engineering/about-eee-department/", "label": "EEE Department",
             "description": "Electrical and Electronics Engineering department"},
            {"url": "https://pragati.ac.in/civil-engineering/about-civil-department/", "label": "Civil Department",
             "description": "Civil Engineering department"},
            {"url": "https://pragati.ac.in/career-development-centre/placement-statistics/", "label": "Placements",
             "description": "Placement stats, recruiters, salary packages"},
            {"url": "https://pragati.ac.in/campus-life/", "label": "Campus Life",
             "description": "Clubs, sports, cultural activities, student life"},
            {"url": "https://pragati.ac.in/examinations/", "label": "Examinations",
             "description": "Exam schedules, results, examination rules"},
            {"url": "https://pragati.ac.in/facilities/", "label": "Facilities",
             "description": "Labs, hostel, transport, infrastructure"},
            {"url": "https://pragati.ac.in/nirf/", "label": "NIRF",
             "description": "NIRF rankings and data"},
            {"url": "https://pragati.ac.in/naac/", "label": "NAAC / Accreditation",
             "description": "NAAC accreditation, quality reports and rankings"},
            {"url": "https://pragati.ac.in/library/", "label": "Library",
             "description": "Library resources, timings, collections and services"},
            {"url": "https://pragati.ac.in/ugc/committee/hostel/", "label": "Hostel",
             "description": "Hostel facilities and accommodation details"},
            {"url": "https://pragati.ac.in/ugc/committee/transport-committee/", "label": "Transport",
             "description": "College bus routes and transport facilities"},
            {"url": "https://pragati.ac.in/ugc/committee/fee-reimbursement/", "label": "Scholarships / Fee Reimbursement",
             "description": "Fee reimbursement and scholarship information"},
            {"url": "https://pragati.ac.in/about-us/committees/anti-ragging-committee/", "label": "Anti-Ragging",
             "description": "Anti-ragging policy and committee"},
            {"url": "https://pragati.ac.in/alumni/", "label": "Alumni",
             "description": "Alumni association, events and network"},
            {"url": "https://pragati.ac.in/contact/", "label": "Contact",
             "description": "Address, phone, email and how to reach the college"},
            {"url": "https://admission.pragati.ac.in/", "label": "Admission Portal",
             "description": "Online admission application portal"},
        ],
    },

    # ──────────────────────────────────────────────────────────
    "aditya": {
        "name": "Aditya University",
        "base_url": "https://www.adityauniversity.in",
        "pages": [
            {"url": "https://www.adityauniversity.in/about-us/overview", "label": "About Us",
             "description": "University overview, about the institution"},
            {"url": "https://www.adityauniversity.in/about-us/leadership", "label": "Leadership",
             "description": "Chancellor, leadership team"},
            {"url": "https://www.adityauniversity.in/about-us/governance", "label": "Governance",
             "description": "Governing body, board of management, academic council"},
            {"url": "https://www.adityauniversity.in/admissions/overview", "label": "Admissions Overview",
             "description": "Admission process, how to apply"},
            {"url": "https://www.adityauniversity.in/admissions/programs-eligibility-fee-structure", "label": "Programs & Fees",
             "description": "Programs offered, eligibility criteria, fee structure"},
            {"url": "https://www.adityauniversity.in/schools/school-of-engineering", "label": "School of Engineering",
             "description": "Engineering programs and departments"},
            {"url": "https://www.adityauniversity.in/schools/school-of-business", "label": "School of Business",
             "description": "Business and management programs (MBA)"},
            {"url": "https://www.adityauniversity.in/schools/school-of-science", "label": "School of Science",
             "description": "Science programs"},
            {"url": "https://www.adityauniversity.in/schools/school-of-pharmacy", "label": "School of Pharmacy",
             "description": "Pharmacy programs"},
            {"url": "https://www.adityauniversity.in/placements/overview", "label": "Placements Overview",
             "description": "Placement cell, training, career support"},
            {"url": "https://www.adityauniversity.in/placements/placements-record", "label": "Placements Record",
             "description": "Placement statistics, packages, year-wise data"},
            {"url": "https://www.adityauniversity.in/placements/our-recruiters", "label": "Our Recruiters",
             "description": "Companies that recruit from the university"},
            {"url": "https://www.adityauniversity.in/programs/master-of-computer-applications", "label": "MCA Program",
             "description": "Master of Computer Applications course details"},
            {"url": "https://www.adityauniversity.in/programs/doctor-of-philosophy-phd", "label": "PhD Programs",
             "description": "Doctoral / PhD programs"},
            {"url": "https://www.adityauniversity.in/admissions/faqs", "label": "Admission FAQs",
             "description": "Frequently asked questions about admissions"},
            {"url": "https://www.adityauniversity.in/faqs", "label": "General FAQs",
             "description": "General frequently asked questions about the university"},
            {"url": "https://www.adityauniversity.in/admissions/hostel-fee", "label": "Hostel & Fees",
             "description": "Hostel accommodation and fee details"},
            {"url": "https://www.adityauniversity.in/facilities", "label": "Facilities",
             "description": "Campus facilities and infrastructure"},
            {"url": "https://www.adityauniversity.in/why-us/life-at-aditya-university", "label": "Campus Life",
             "description": "Student life, clubs, societies and activities"},
            {"url": "https://www.adityauniversity.in/about-us/approvals-accreditations", "label": "Approvals & Accreditations",
             "description": "Approvals, accreditations and recognitions"},
            {"url": "https://www.adityauniversity.in/why-us/overview", "label": "Why Aditya",
             "description": "Key reasons to choose Aditya — rankings, achievements, differentiators"},
            {"url": "https://www.adityauniversity.in/research/overview", "label": "Research",
             "description": "Research overview, projects and publications"},
            {"url": "https://www.adityauniversity.in/contact-us", "label": "Contact",
             "description": "Address, phone, email and how to reach the university"},
            {"url": "https://apply.adityauniversity.in/", "label": "Admission Portal",
             "description": "Online admission application portal"},
        ],
    },
}

# ─── THE TOGGLE ───────────────────────────────────────────────
# Change this to "pragati" or "aditya" to switch the whole bot.
ACTIVE_COLLEGE = "aditya"


# Convenience helpers — use these everywhere else in your code
def get_college():
    return COLLEGES[ACTIVE_COLLEGE]

def get_pages():
    return COLLEGES[ACTIVE_COLLEGE]["pages"]

def get_college_name():
    return COLLEGES[ACTIVE_COLLEGE]["name"]
