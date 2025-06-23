from app import app
from models import db, Country

with app.app_context():
    db.drop_all()
    db.create_all()

    countries = [
        Country(
            name="Germany",
            code="de",
            startup_tip="Visit https://startupgermany.com to register your business.",
        ),
        Country(
            name="Albania",
            code="al",
            startup_tip="Go to https://e-albania.al for digital business services.",
        ),
        Country(
            name="USA",
            code="us",
            startup_tip="Check https://sba.gov for startup guides and grants.",
        ),
    ]

    for country in countries:
        db.session.add(country)
    db.session.commit()
    print("Database seeded successfully!")
