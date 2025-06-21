# server/seed.py
from app import app
from models import db, Plant

with app.app_context():
    print("Seeding data...")
    db.session.query(Plant).delete()

    p1 = Plant(
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
        is_in_stock=True
    )

    db.session.add(p1)
    db.session.commit()
    print("Done.")
