"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Game
from levelupapi.models import Event
from levelupreports.views import Connection


def userevent_list(request):
    """Function to build an HTML report of games by user"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all games, with related user info.
            # db_cursor.execute("""
            #     SELECT
            #         g.id,
            #         g.title,
            #         g.maker,
            #         g.game_type_id,
            #         g.number_of_players,
            #         g.skill_level,
            #         u.id user_id,
            #         u.first_name || ' ' || u.last_name AS full_name
            #     FROM
            #         levelupapi_game g
            #     JOIN
            #         levelupapi_gamer gr ON g.gamer_id = gr.id
            #     JOIN
            #         auth_user u ON gr.user_id = u.id
            # """)
            db_cursor.execute("""
                SELECT
                    e.id,
                    e.title,
                    e.game_id,
                    e.date,
                    e.time,
                    e.description,
                    e.host_id,
                    g.title as g_title,
                    u.id user_id,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM 
                    levelupapi_event e
                JOIN 
                    levelupapi_game g ON e.game_id = g.id
                JOIN
                    auth_user u ON e.host_id = u.id

            """)

            dataset = db_cursor.fetchall()

            # Take the flat data from the database, and build the
            # following data structure for each gamer.
            #
            # {
            #     1: {
            #         "gamer_id": 1,
            #         "full_name": "Molly Ringwald",
            #         "events": [
            #             {
            #                 "id": 5,
            #                 "date": "2020-12-23",
            #                 "time": "19:00",
            #                 "game_name": "Fortress America"
            #             }
            #         ]
            #     }
            # }

            events_by_user = {}

            for row in dataset:
                # Crete a Game instance and set its properties
                event = Event()
                event.title = row["title"]
                event.description = row["description"]
                event.date = row["date"]
                event.g_title = row["g_title"]
                event.game_id = row["game_id"]
                event.host_id = row["host_id"]

                # Store the user's id
                uid = row["user_id"]

                # If the user's id is already a key in the dictionary...
                if uid in events_by_user:

                    # Add the current game to the `games` list for it
                    events_by_user[uid]['events'].append(event)

                else:
                    # Otherwise, create the key and dictionary value
                    events_by_user[uid] = {}
                    events_by_user[uid]["id"] = uid
                    events_by_user[uid]["full_name"] = row["full_name"]
                    events_by_user[uid]["events"] = [event]

        # Get only the values from the dictionary and create a list from them
        list_of_events_with_games = events_by_user.values()

        # Specify the Django template and provide data context
        template = 'users/list_with_events.html'
        context = {
            'userevent_list': list_of_events_with_games
        }

        return render(request, template, context)
