import random
from datetime import datetime

from app import app
from dateutil.relativedelta import relativedelta
from faker import Faker
from models import Appearance, Episode, Guest, db


def seed_data():
  
    # Seed the database with fake data
    # Initialize faker
    fake = Faker()
    print('Setting up database')
    
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    
    no_of_guests = 50
    no_of_ep = 100
    no_of_app = 150
    
    # seed guests data
    print(f'{no_of_guests} Guests seeding')
    for _ in range(50):
        name = fake.unique.name()
        occupation = fake.job()
        guest = Guest(name=name, occupation=occupation)
        db.session.add(guest)
        db.session.commit()
    print(f'Guests seeded successfully!')

    # Seed episodes data
    print(f'{no_of_ep} Episodes seeding ')
    # Start date for the episodes
    start_date = datetime(1989, 10, 1)
    for i in range(no_of_ep):
        # Generate the date string
        date = start_date + relativedelta(months=i)
        date_string = date.strftime('%m/%d/%y')

        # Create the episode and add to session
        episode = Episode(date=date_string, number=i + 1)
        db.session.add(episode)
        db.session.commit()
    print(f'Episodes seeded successfully.')

    # Seed appearances data
    
    print(f'{no_of_app} appearances seeding')
    episodes = Episode.query.all()
    guests = Guest.query.all()
    
    app_set = set() # Set to store the unique (episode_id, guest_id) pairs

    while len(app_set) < no_of_app:  # Loop until the set has the required number of appearances
        episode = random.choice(episodes)
        guest = random.choice(guests)
        rating = random.choice(range(1, 5 + 1))

        # Check if the pair is already in the set
        if (episode.id, guest.id) not in app_set:
            # Add the pair to the set
            app_set.add((episode.id, guest.id))
            # Create the appearance and add to session
            appearance = Appearance(episode_id=episode.id, guest_id=guest.id, rating=rating)
            db.session.add(appearance)
    # Commit the session
    db.session.commit()
    print(f'{no_of_app} appearances Successfully seeded!')


if __name__ == '__main__':
    with app.app_context():
        seed_data()
        print('Complete.')