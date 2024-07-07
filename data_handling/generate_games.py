#!/usr/bin/env python3

import pandas as pd
import os
from datetime import datetime, timedelta

# Define the file path for storing games data
games_file_path = os.path.join('data', 'games.csv')

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

# Define teams
teams = [
    "Lions", "Bengals", "Texans", "Buccaneers", "Panthers", "Cardinals", "Jaguars", "49ers",
    "Titans", "Raiders", "Eagles", "Rams", "Dolphins", "Packers", "Cowboys", "Bills",
    "Chiefs", "Browns", "Ravens", "Vikings", "Falcons", "Commanders", "Colts", "Steelers",
    "Saints", "Broncos", "Patriots", "Seahawks", "Chargers", "Bears", "Giants", "Jets"
]

# Generate game times
def generate_game_times():
    base_date = datetime(2024, 9, 1)  # Start date for the 2024 season
    game_times = ["10:05:00", "13:30:00", "16:30:00", "18:00:00"]  # Sunday times
    game_times_mon_thu = ["18:05:00"]  # Monday and Thursday times

    times = []
    for week in range(17):
        week_start = base_date + timedelta(weeks=week)
        for i in range(14):
            times.append(week_start.strftime("%Y-%m-%dT") + game_times[i % len(game_times)])
        # Adding Monday and Thursday games
        times.append((week_start + timedelta(days=1)).strftime("%Y-%m-%dT") + game_times_mon_thu[0])
        times.append((week_start + timedelta(days=4)).strftime("%Y-%m-%dT") + game_times_mon_thu[0])
    return times

game_times = generate_game_times()

# Check if the file exists, if not create it
if not os.path.exists(games_file_path):
    games_list = []
    game_id = 1
    for week in range(1, 18):
        for i in range(16):
            away_team, home_team = teams[i], teams[(i+1) % len(teams)]
            game_info = {
                'game_id': f"game_{game_id}",
                'date_time': game_times[game_id-1],
                'season': '2024',
                'week': week,
                'away_team': away_team,
                'home_team': home_team,
                'away_score': 0,
                'home_score': 0,
                'away_ml': 100 + (game_id % 10) * 10,
                'home_ml': -100 - (game_id % 10) * 10,
                'spread': -7.5,
                'winner': 'draw',
                'notes': '',
                'status': 'Pending',
            }
            games_list.append(game_info)
            game_id += 1
    games_df = pd.DataFrame(games_list)
    games_df.to_csv(games_file_path, index=False)
    print(f'Mock data generated and saved to {games_file_path}')
else:
    games_df = pd.read_csv(games_file_path)
    print(f'Loaded existing data from {games_file_path}')
