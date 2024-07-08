import os
import pandas as pd
import streamlit as st
from datetime import datetime

games_file_path = os.path.join('data', 'games.csv')
users_file_path = os.path.join('data', 'users.csv')
bets_file_path = os.path.join('data', 'bets.csv')
seasons_file_path = os.path.join('data', 'season.csv')
leaderboard_file_path = os.path.join('data', 'leaderboard.csv')
new_season_file_path = os.path.join('data', 'nfl2024.csv')

# Games
def create_games():
    # status: 'Pending' | 'Under Way' | 'Final' | 'Canceled'
    if not os.path.exists(games_file_path):
        games_df = pd.DataFrame(columns=['game_id', 'date_time', 'season', 'week', 'away_team', 'home_team', 'away_score', 'home_score', 'away_ml', 'home_ml', 'spread', 'winner', 'notes', 'status'])
        new_games_df = pd.read_csv(new_season_file_path)
        new_games = []
        count = 0
        for index, row in new_games_df.iterrows():
            count += 1
            game_id = f"game_{count}"  # Creating new game_id
            date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Using the current time; adjust format as needed
            new_game = {
                'game_id': game_id,
                'date_time': date_time,
                'season': row['season'],
                'week': row['week'],
                'away_team': row['Away'],
                'home_team': row['Home'],
                'away_score': 0,
                'home_score': 0,
                'away_ml': 0,
                'home_ml': 0,
                'spread': 0.0,
                'winner': 'draw',
                'notes': '',
                'status': 'Pending'
            }
            new_games.append(new_game)

        # Add games to games_df
        # Update games_df with new games
        games_df = pd.concat([games_df, pd.DataFrame(new_games)], ignore_index=True)
        # Write updated DataFrame to csv file
        games_df.to_csv(games_file_path, index=False)
        # Read games.csv into games_df session_state (Note: st.session_state.games_df is different than the above local game_df)
        st.session_state.games_df = pd.read_csv(games_file_path)
        

def create_users():
    if not os.path.exists(users_file_path):
        users_df = pd.DataFrame(columns=['user', 'weeks_won', 'games_won', 'color', 'img', 'quote'])
        users_df.to_csv(users_file_path, index=False)

def create_bets():
    # bet_type: pick_winner | ml | spread
    # outcome: 'win' | 'loss' | 'draw' | 'unknown'
    # status: 'Pending' | 'Under Way' | 'Final' | 'Canceled'
    if not os.path.exists(bets_file_path):
        bets_df = pd.DataFrame(columns=['user', 'game_id', 'season', 'week', 'bet_type', 'selected_team', 'outcome', 'pick_winner_payout', 'ml_payout', 'spread_payout', 'status'])
        bets_df.to_csv(bets_file_path, index=False)

def create_seasons():
    # season: string year ex 2024
    # default_week: int the selected week will be set to this on init
    # status: string 'active' | 'inactive' - the app is set to the active season on init
    if not os.path.exists(seasons_file_path):
        # seasons_df = pd.DataFrame(columns=['season', 'default_week', 'status'])
        # seasons_df.to_csv(seasons_file_path, index=False)
            # Create DataFrame for seasons from 2010 to 2050
        years = range(2010, 2051)
        data = {
            'season': years,
            'default_week': [1] * len(years),
            'status': ['inactive'] * len(years)
        }
        seasons_df = pd.DataFrame(data)
        # Set the status of 2024 to 'active'
        seasons_df.loc[seasons_df['season'] == 2024, 'status'] = 'active'
        # Save to CSV
        seasons_df.to_csv(seasons_file_path, index=False)

def create_leaderboard():
    if not os.path.exists(leaderboard_file_path):
        leaderboard = pd.DataFrame(columns=['season', 'user', 'week_wins', 'wins', 'losses', 'draws', 'bets'])
        leaderboard.to_csv(leaderboard_file_path, index=False)

def get_games():
    return pd.read_csv(games_file_path)

def get_users():
    return pd.read_csv(users_file_path)

def get_bets():
    return pd.read_csv(bets_file_path)

def get_seasons():
    return pd.read_csv(seasons_file_path)

def get_leaderboard():
    return pd.read_csv(leaderboard_file_path)

def update_game(game_id, **kwargs):
    # Load games if not already in session state or reload if necessary
    if 'games_df' not in st.session_state:
        st.session_state.games_df = get_games()
    
    if game_id in st.session_state.games_df['game_id'].values:
        game_index = st.session_state.games_df.index[st.session_state.games_df['game_id'] == game_id].tolist()[0]
        # Update the game details
        for key, value in kwargs.items():
            if value is not None:
                st.session_state.games_df.at[game_index, key] = value

        # Update 'winner' based on scores if scores are modified
        if 'home_score' in kwargs or 'away_score' in kwargs:
            home_score = st.session_state.games_df.at[game_index, 'home_score']
            away_score = st.session_state.games_df.at[game_index, 'away_score']
            if home_score > away_score:
                st.session_state.games_df.at[game_index, 'winner'] = st.session_state.games_df.at[game_index, 'home_team']
            elif away_score > home_score:
                st.session_state.games_df.at[game_index, 'winner'] = st.session_state.games_df.at[game_index, 'away_team']
            else:
                st.session_state.games_df.at[game_index, 'winner'] = 'draw'
            # st.session_state.games_df.at[game_index, 'status'] = 'Under Way'

        st.session_state.games_df.to_csv(games_file_path, index=False)
        st.session_state.games_df = pd.read_csv(games_file_path)
    else:
        st.error(f"Game with game_id {game_id} does not exist.")


def create_user(new_user):
    # Load the existing users DataFrame
    users_df = pd.read_csv(users_file_path)
    
    # Convert new_user dictionary to DataFrame
    new_user_df = pd.DataFrame([new_user])
    
    # Concatenate the new user DataFrame to the existing users DataFrame
    updated_users_df = pd.concat([users_df, new_user_df], ignore_index=True)
    
    # Save the updated DataFrame back to the CSV
    updated_users_df.to_csv(users_file_path, index=False)
    
    # Reload users into the session state
    st.session_state.users_df = get_users()
    
    # Provide feedback to the user
    st.success(f"User '{new_user['user']}' added successfully!")


def create_bet(new_bet):
    bets_df = pd.read_csv(bets_file_path)
    bets_df = pd.concat([bets_df, pd.DataFrame([new_bet])], ignore_index=True)
    
    # overwrite csv and update global data frame
    bets_df.to_csv(bets_file_path, index=False)
    st.session_state.bets_df = pd.read_csv(bets_file_path)

def update_bet(new_bet):
    user = new_bet['user']
    game_id = new_bet['game_id']
    team = new_bet['selected_team']

    bets_df = pd.read_csv(bets_file_path)
    bets_df.loc[(bets_df['user'] == user) & (bets_df['game_id'] == game_id), 'selected_team'] = team
    
    # overwrite csv and update global data frame
    bets_df.to_csv(bets_file_path, index=False)
    st.session_state.bets_df = pd.read_csv(bets_file_path)

def update_bets(game_id):
    bets_df = pd.read_csv(bets_file_path)  # Reload bets dataframe
    game_row = st.session_state.games_df[st.session_state.games_df['game_id'] == game_id].iloc[0]
    winner = game_row['winner']

    for index, bet in bets_df[bets_df['game_id'] == game_id].iterrows():
        if bet['selected_team'] == winner:
            outcome = 'win'
        elif winner == 'draw':
            outcome = 'draw'
        else:
            outcome = 'loss'
        bets_df.at[index, 'outcome'] = outcome

    # overwrite csv and update global data frame
    bets_df.to_csv(bets_file_path, index=False)
    st.session_state.bets_df = pd.read_csv(bets_file_path)
    # st.experimental_rerun()  # Optionally, you can rerun to refresh the display


def update_season(new_season):
    seasons_df = st.session_state.seasons_df
    # Set all current seasons to 'inactive'
    seasons_df['status'] = 'inactive'

    # Check if the new season already exists
    if new_season in seasons_df['season'].values:
        # # Set all seasons to 'inactive'
        # seasons_df['status'] = 'inactive'

        # Set the new season to 'active'
        seasons_df.loc[seasons_df['season'] == new_season, 'status'] = 'active'
    else:
        # Create a new season entry
        new_season_entry = pd.DataFrame({
            'season': [new_season],
            'default_week': [1],
            'status': ['active']
        })

        # # Set all current seasons to 'inactive'
        # seasons_df['status'] = 'inactive'

        # Append the new season entry
        seasons_df = pd.concat([seasons_df, new_season_entry], ignore_index=True)
    
    # Save the updated seasons data back to the file
    seasons_df.to_csv(seasons_file_path, index=False)
    st.session_state.seasons_df = pd.read_csv(seasons_file_path)

def update_active_week(new_week, season):
    seasons_df = st.session_state.seasons_df

    # Check if the season already exists
    if season in seasons_df['season'].values:
        # Set the new season to 'active'
        seasons_df.loc[seasons_df['season'] == season, 'default_week'] = new_week
    else:
        # Create a new season entry
        new_season_entry = pd.DataFrame({
            'season': [season],
            'default_week': [new_weak],
            'status': ['active']
        })

        # Set all current seasons to 'inactive'
        seasons_df['status'] = 'inactive'

        # Append the new season entry
        seasons_df = pd.concat([seasons_df, new_season_entry], ignore_index=True)
    
    # Save the updated seasons data back to the file
    seasons_df.to_csv(seasons_file_path, index=False)
    st.session_state.seasons_df = pd.read_csv(seasons_file_path)


def add_game(new_game):
    games_df = st.session_state.games_df
    
    # Convert new_game dictionary to DataFrame
    new_game_df = pd.DataFrame([new_game])
    
    # Concatenate the new game DataFrame to the existing games DataFrame
    updated_games_df = pd.concat([games_df, new_game_df], ignore_index=True)
    
    # Save the updated DataFrame back to the CSV
    updated_games_df.to_csv(games_file_path, index=False)
    
    # Reload games into the session state
    st.session_state.games_df = pd.read_csv(games_file_path)
