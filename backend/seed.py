from app import app
from models import db, Country

with app.app_context():
    db.drop_all()
    db.create_all()

    countries = [
        Country(
            name="Germany",
            code="de",
        ),
        Country(
            name="Albania",
            code="al",
        ),
        Country(
            name="USA",
            code="us",
        ),
    ]

    for country in countries:
        db.session.add(country)
    db.session.commit()
    print("Database seeded successfully!")
