from app import create_app
from models import db, Country, Tip, ChecklistStep

app = create_app()


with app.app_context():
    db.drop_all()
    db.create_all()

    # --- Extended Countries ---
    countries = [
        Country(name="Germany", code="de"),
        Country(name="Albania", code="al"),
        Country(name="USA", code="us"),
        Country(name="United Kingdom", code="gb"),
        Country(name="France", code="fr"),
        Country(name="Netherlands", code="nl"),
        Country(name="Spain", code="es"),
        Country(name="Italy", code="it"),
        Country(name="Poland", code="pl"),
        Country(name="Sweden", code="se"),
        Country(name="Austria", code="at"),
        Country(name="Switzerland", code="ch"),
        Country(name="Canada", code="ca"),
        Country(name="Australia", code="au"),
        Country(name="Japan", code="jp"),
        Country(name="Singapore", code="sg"),
    ]

    for country in countries:
        db.session.add(country)
    db.session.commit()

    # --- Comprehensive Tips by Country ---
    tips = [
        # Germany Tips
        Tip(
            content="Register your business with local authorities (Gewerbeamt)",
            category="Legal",
            country_id=1,
        ),
        Tip(
            content="Open a dedicated business bank account",
            category="Finance",
            country_id=1,
        ),
        Tip(
            content="Register for VAT (Umsatzsteuer) if annual revenue exceeds €22,000",
            category="Tax",
            country_id=1,
        ),
        Tip(
            content="Get business liability insurance (Betriebshaftpflichtversicherung)",
            category="Insurance",
            country_id=1,
        ),
        Tip(
            content="Understand German employment laws before hiring",
            category="HR",
            country_id=1,
        ),
        Tip(
            content="Consider EXIST grants for university spin-offs",
            category="Funding",
            country_id=1,
        ),
        Tip(
            content="Join local startup accelerators like Rocket Internet or TechStars",
            category="Networking",
            country_id=1,
        ),
        Tip(
            content="Comply with GDPR data protection regulations",
            category="Legal",
            country_id=1,
        ),
        # Albania Tips
        Tip(
            content="Check available grants for startups",
            category="Funding",
            country_id=2,
        ),
        Tip(
            content="Register at National Registration Center (QKR)",
            category="Legal",
            country_id=2,
        ),
        Tip(
            content="Obtain necessary permits for your business type",
            category="Legal",
            country_id=2,
        ),
        Tip(
            content="Connect with Albanian Investment Development Agency (AIDA)",
            category="Support",
            country_id=2,
        ),
        Tip(
            content="Consider EU funding opportunities as a candidate country",
            category="Funding",
            country_id=2,
        ),
        # USA Tips
        Tip(content="Understand local tax obligations", category="Tax", country_id=3),
        Tip(
            content="Choose between LLC, Corporation, or Partnership",
            category="Legal",
            country_id=3,
        ),
        Tip(
            content="Get an EIN (Employer Identification Number)",
            category="Legal",
            country_id=3,
        ),
        Tip(content="Consider SBA loans for funding", category="Funding", country_id=3),
        Tip(
            content="Protect intellectual property with patents/trademarks",
            category="Legal",
            country_id=3,
        ),
        Tip(
            content="Understand state-specific business requirements",
            category="Legal",
            country_id=3,
        ),
        # UK Tips
        Tip(content="Register with Companies House", category="Legal", country_id=4),
        Tip(content="Set up PAYE for employees", category="Tax", country_id=4),
        Tip(
            content="Consider Seed Enterprise Investment Scheme (SEIS)",
            category="Funding",
            country_id=4,
        ),
        Tip(
            content="Get professional indemnity insurance",
            category="Insurance",
            country_id=4,
        ),
        Tip(
            content="Understand Making Tax Digital requirements",
            category="Tax",
            country_id=4,
        ),
        # France Tips
        Tip(
            content="Choose appropriate legal structure (SARL, SAS, etc.)",
            category="Legal",
            country_id=5,
        ),
        Tip(
            content="Register with INSEE for SIRET number",
            category="Legal",
            country_id=5,
        ),
        Tip(
            content="Understand French labor laws (Code du travail)",
            category="HR",
            country_id=5,
        ),
        Tip(
            content="Consider BPI France funding programs",
            category="Funding",
            country_id=5,
        ),
        Tip(content="Join French Tech ecosystem", category="Networking", country_id=5),
        # Netherlands Tips
        Tip(
            content="Register with KvK (Chamber of Commerce)",
            category="Legal",
            country_id=6,
        ),
        Tip(
            content="Get a BSN (Burgerservicenummer) for business",
            category="Legal",
            country_id=6,
        ),
        Tip(
            content="Understand Dutch tax advantages for startups",
            category="Tax",
            country_id=6,
        ),
        Tip(
            content="Consider Innovation Box tax regime for IP",
            category="Tax",
            country_id=6,
        ),
        Tip(content="Join StartupDelta network", category="Networking", country_id=6),
        # Add more countries as needed...
        # Canada Tips
        Tip(
            content="Register federally or provincially",
            category="Legal",
            country_id=13,
        ),
        Tip(
            content="Apply for SR&ED tax credits for R&D", category="Tax", country_id=13
        ),
        Tip(
            content="Consider Canadian business immigration programs",
            category="Legal",
            country_id=13,
        ),
        # Australia Tips
        Tip(
            content="Get an Australian Business Number (ABN)",
            category="Legal",
            country_id=14,
        ),
        Tip(
            content="Register for GST if turnover exceeds $75,000",
            category="Tax",
            country_id=14,
        ),
        Tip(
            content="Consider R&D Tax Incentive program",
            category="Funding",
            country_id=14,
        ),
        # Japan Tips
        Tip(
            content="Choose between KK (株式会社) or GK (合同会社)",
            category="Legal",
            country_id=15,
        ),
        Tip(
            content="Understand Japanese employment practices",
            category="HR",
            country_id=15,
        ),
        Tip(
            content="Consider JETRO support for foreign entrepreneurs",
            category="Support",
            country_id=15,
        ),
        # Singapore Tips
        Tip(
            content="Register with ACRA (Accounting and Corporate Regulatory Authority)",
            category="Legal",
            country_id=16,
        ),
        Tip(
            content="Take advantage of Singapore's startup tax exemptions",
            category="Tax",
            country_id=16,
        ),
        Tip(
            content="Consider applying for Tech.Pass for tech talents",
            category="HR",
            country_id=16,
        ),
    ]

    for tip in tips:
        db.session.add(tip)

    # --- Enhanced Checklist Steps by Country ---
    checklist_steps = [
        # Germany Checklist
        ChecklistStep(
            step_number=1,
            content="Research market demand and competition",
            country_id=1,
        ),
        ChecklistStep(
            step_number=2, content="Write a comprehensive business plan", country_id=1
        ),
        ChecklistStep(
            step_number=3,
            content="Choose legal structure (GmbH, UG, etc.)",
            country_id=1,
        ),
        ChecklistStep(
            step_number=4, content="Register business with Gewerbeamt", country_id=1
        ),
        ChecklistStep(
            step_number=5, content="Open business bank account", country_id=1
        ),
        ChecklistStep(
            step_number=6, content="Register for taxes and VAT", country_id=1
        ),
        ChecklistStep(step_number=7, content="Get business insurance", country_id=1),
        ChecklistStep(step_number=8, content="Set up accounting system", country_id=1),
        # Albania Checklist
        ChecklistStep(
            step_number=1, content="Choose a business structure", country_id=2
        ),
        ChecklistStep(
            step_number=2,
            content="Register with National Registration Center",
            country_id=2,
        ),
        ChecklistStep(
            step_number=3, content="Obtain business permits and licenses", country_id=2
        ),
        ChecklistStep(
            step_number=4, content="Open business bank account", country_id=2
        ),
        ChecklistStep(step_number=5, content="Register for taxes", country_id=2),
        # USA Checklist
        ChecklistStep(
            step_number=1, content="Register your company name", country_id=3
        ),
        ChecklistStep(
            step_number=2,
            content="Choose business structure (LLC, Corp, etc.)",
            country_id=3,
        ),
        ChecklistStep(step_number=3, content="Get EIN from IRS", country_id=3),
        ChecklistStep(
            step_number=4, content="Register for state and local taxes", country_id=3
        ),
        ChecklistStep(
            step_number=5, content="Open business bank account", country_id=3
        ),
        ChecklistStep(
            step_number=6, content="Get business licenses and permits", country_id=3
        ),
        ChecklistStep(step_number=7, content="Get business insurance", country_id=3),
        # UK Checklist
        ChecklistStep(
            step_number=1,
            content="Choose company name and check availability",
            country_id=4,
        ),
        ChecklistStep(
            step_number=2, content="Register with Companies House", country_id=4
        ),
        ChecklistStep(
            step_number=3, content="Set up business bank account", country_id=4
        ),
        ChecklistStep(
            step_number=4, content="Register for Corporation Tax", country_id=4
        ),
        ChecklistStep(
            step_number=5, content="Register for VAT if required", country_id=4
        ),
        ChecklistStep(step_number=6, content="Get business insurance", country_id=4),
        # France Checklist
        ChecklistStep(step_number=1, content="Choose legal structure", country_id=5),
        ChecklistStep(step_number=2, content="Register with INSEE", country_id=5),
        ChecklistStep(
            step_number=3, content="Open business bank account", country_id=5
        ),
        ChecklistStep(
            step_number=4, content="Register for social security", country_id=5
        ),
        ChecklistStep(
            step_number=5, content="Get professional insurance", country_id=5
        ),
        # Netherlands Checklist
        ChecklistStep(
            step_number=1,
            content="Register with Chamber of Commerce (KvK)",
            country_id=6,
        ),
        ChecklistStep(
            step_number=2, content="Get BSN for business purposes", country_id=6
        ),
        ChecklistStep(
            step_number=3, content="Open business bank account", country_id=6
        ),
        ChecklistStep(
            step_number=4,
            content="Register for taxes with Belastingdienst",
            country_id=6,
        ),
        ChecklistStep(step_number=5, content="Get business insurance", country_id=6),
        # Canada Checklist
        ChecklistStep(
            step_number=1, content="Choose business structure", country_id=13
        ),
        ChecklistStep(step_number=2, content="Register business name", country_id=13),
        ChecklistStep(
            step_number=3, content="Get business number from CRA", country_id=13
        ),
        ChecklistStep(
            step_number=4, content="Register for GST/HST if required", country_id=13
        ),
        ChecklistStep(
            step_number=5, content="Open business bank account", country_id=13
        ),
        # Australia Checklist
        ChecklistStep(
            step_number=1, content="Get Australian Business Number (ABN)", country_id=14
        ),
        ChecklistStep(
            step_number=2, content="Register business name with ASIC", country_id=14
        ),
        ChecklistStep(
            step_number=3, content="Register for GST if required", country_id=14
        ),
        ChecklistStep(
            step_number=4, content="Open business bank account", country_id=14
        ),
        ChecklistStep(step_number=5, content="Get business insurance", country_id=14),
        # Japan Checklist
        ChecklistStep(step_number=1, content="Choose company structure", country_id=15),
        ChecklistStep(
            step_number=2, content="Register with Legal Affairs Bureau", country_id=15
        ),
        ChecklistStep(
            step_number=3, content="Open business bank account", country_id=15
        ),
        ChecklistStep(step_number=4, content="Register for taxes", country_id=15),
        # Singapore Checklist
        ChecklistStep(
            step_number=1, content="Register company with ACRA", country_id=16
        ),
        ChecklistStep(
            step_number=2, content="Open corporate bank account", country_id=16
        ),
        ChecklistStep(
            step_number=3, content="Register for GST if required", country_id=16
        ),
        ChecklistStep(step_number=4, content="Get business licenses", country_id=16),
    ]

    for step in checklist_steps:
        db.session.add(step)
    db.session.commit()
    print("Database seeded successfully!")
