from flask import request
from flask_restful import Resource
from models import Appearance, Episode, Guest, db
from sqlalchemy.exc import IntegrityError


class Episodes(Resource):

    def get(self):
        # Get all episodes as a list of dictionaries
        episode_list = Episode.query.all()
        episode_dict_list = [
            episode.to_dict(rules=('-appearances', ))
            for episode in episode_list
        ]
        return episode_dict_list


class EpisodeByID(Resource):

    def get(self, id):
        # Get a single episode by its ID as a dictionary
        episode = db.session.get(Episode, id)
        errors = []

        try:
            if not episode:
                raise ValueError(f'Episode not found')

            episode_dict = episode.to_dict(rules=('-appearances.episode', ))

            return episode_dict
        except ValueError as e:
            errors.append(str(e))
        except:
            return {'errors': ['An unknown error occurred']}, 500
        return {'errors': errors}, 400

class Guests(Resource):

    def get(self):
        # Get all guests as a list of dictionaries
        guest_list = Guest.query.all()

        guest_dict_list = [
            guest.to_dict(rules=('-appearances', )) for guest in guest_list
        ]

        return guest_dict_list
    
class Appearances(Resource):

    def post(self):
        # Create a new appearance record
        # Get the JSON data from the request
        data = request.json
        errors = []

        try:
            rating = data['rating']
            episode_id = data['episode_id']
            guest_id = data['guest_id']

            episode = db.session.get(Episode, episode_id)
            guest = db.session.get(Guest, guest_id)

            if not episode:
                raise ValueError('Invalid episode_id')
            if not guest:
                raise ValueError('Invalid guest_id')

            new_appearance = Appearance(guest_id=guest_id, episode_id=episode_id, rating=rating)
            db.session.add(new_appearance)
            db.session.commit()

            new_appearance_dict = new_appearance.to_dict()

            return new_appearance_dict, 201
        # checks for missing required fields 
        except KeyError as e:
            errors.append(f'Missing required field: {e}')
        except ValueError as e:
            errors.append(str(e))
        except IntegrityError as e:
            # Checks for uniquness in the appearance table
            if 'UNIQUE' in str(e):
                errors.append(
                    f'Appearance already exists. Create new appearance')
        except:
            return {'errors': ['Uknown Error!!']}, 500
        return {'errors': errors}, 400


