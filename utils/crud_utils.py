from data_handling.data_handling import update_game, create_user, create_bet, update_bet, update_bets, games_file_path, bets_file_path, leaderboard_file_path, update_season, update_active_week, add_game
import streamlit as st

from data_handling.data_handling import bets_file_path
import pandas as pd

def handle_update_game(field_key, row_key, game_id):
    try:
        new_val = st.session_state[field_key]
        # Dynamically create a dictionary with the key and new value
        kwargs = {row_key: new_val}
        update_game(game_id, **kwargs)
        update_bets(game_id)
    except Exception as e:
        st.error(f"Failed to update {row_key} for game {game_id}. Error: {str(e)}")

def handle_create_user():
    users_df = st.session_state.users_df
    # Form
    st.header("Add a New Better")
    username = st.text_input('Username', max_chars=15)
    st.write(username.lower())
    lower_case_usernames = users_df['user'].str.lower().values
    is_disabled = False
    if username.lower() in lower_case_usernames:
        is_disabled = True
        st.error('Username already exists. Please choose a different username.')
    color = st.color_picker('Favorite Color', '#00f900')
    img = st.text_input('Image URL')
    quote = st.text_area('Quote (max 100 characters)', max_chars=100)

    # Form Submit
    if not is_disabled and username != '':            
        if st.button("Add New Better"):
            new_user = {
                'user': username,
                'weeks_won': 0,
                'games_won': 0,
                'color': color,
                'img': img,
                'quote': quote
            }
            create_user(new_user)

    st.subheader("Existing Betters")
    st.table(st.session_state.users_df[['user', 'weeks_won', 'games_won', 'color', 'quote']])


def handle_bet(selected_better, game_obj, team, bet_side):
    try:
        bets_df = st.session_state.bets_df
        new_bet = {
            'user': selected_better,
            'game_id': game_obj['game_id'],
            'season': game_obj['season'],
            'week': game_obj['week'],
            'bet_type': 'pick_winner',
            'selected_team': team,
            'outcome': 'unknown',
            'pick_winner_payout': 1,
            'ml_payout': 0,
            'spread_payout': 0,
            'status': game_obj['status']
        }
        existing_bet = bets_df[(bets_df['user'] == selected_better) & (bets_df['game_id'] == game_obj['game_id'])]
        if not existing_bet.empty:
            # User already has bet
            existing_bet_team = existing_bet.iloc[0]['selected_team']
            if existing_bet_team == team:
                # User is trying to make same bet
                st.info(f"{selected_better} already bet on {team}. No change needed.")
            else:
                # User is change bet to other team
                update_bet(new_bet)
        else:
            # User is placing new bet
            create_bet(new_bet)
    except Exception as e:
        st.error(f"Failed to add bet for team {team}. Error: {str(e)}")

def handle_refresh_week(week):
    update_bets(game_id)


def handle_refresh_week(week):
    # Load dataframes
    games_df = st.session_state.games_df
    bets_df = st.session_state.bets_df
    
    # Filter games for the specified week
    week_games = games_df[games_df['week'] == week]

    # Update winner in games_df based on scores
    for index, game in week_games.iterrows():
        home_score = game['home_score']
        away_score = game['away_score']
        if home_score > away_score:
            winner = game['home_team']
        elif away_score > home_score:
            winner = game['away_team']
        else:
            winner = 'draw'
        
        # Update the 'winner' field in the DataFrame
        st.session_state.games_df.at[index, 'winner'] = winner

        # Update bet outcomes based on the game result
        game_bets = bets_df[bets_df['game_id'] == game['game_id']]
        for bet_index, bet in game_bets.iterrows():
            if bet['selected_team'] == winner:
                result = 'win' if winner != 'draw' else 'draw'
            else:
                result = 'loss' if winner != 'draw' else 'draw'
            
            st.session_state.bets_df.at[bet_index, 'outcome'] = result

    # Save the updated DataFrames back to their respective CSV files
    st.session_state.games_df.to_csv(games_file_path, index=False)
    st.session_state.bets_df.to_csv(bets_file_path, index=False)
    st.success("Week and bet outcomes refreshed successfully!")


def update_season_leaderboard(season):
    try:
        bets_df = st.session_state.bets_df

        # Filter bets for the current season
        season_bets = bets_df[bets_df['season'] == season]

        # Initialize an empty DataFrame for the leaderboard
        columns = ['season', 'user', 'week_wins', 'wins', 'losses', 'draws', 'bets']
        leaderboard_df = pd.DataFrame(columns=columns)

        # Get results by user across the season
        season_results = season_bets.groupby('user')['outcome'].value_counts().unstack(fill_value=0)
        season_results['total_bets'] = season_bets.groupby('user').size()
        season_results['week_wins'] = 0  # Initialize week wins

        # Find weekly winners for all weeks in the season and sum it
        if 'win' in season_results.columns:
            for week in season_bets['week'].unique():
                weekly_bets = season_bets[season_bets['week'] == week]
                weekly_results = weekly_bets.groupby('user')['outcome'].value_counts().unstack(fill_value=0)
                if 'win' in weekly_results.columns:
                    max_wins = weekly_results['win'].max()
                    weekly_winners = weekly_results[weekly_results['win'] == max_wins].index.tolist()
                    season_results.loc[weekly_winners, 'week_wins'] += 1

        # Create new leaderboard entries
        for user, results in season_results.iterrows():
            user_row = {
                'season': season,
                'user': user,
                'week_wins': results.get('week_wins', 0),
                'wins': results.get('win', 0),
                'losses': results.get('loss', 0),
                'draws': results.get('draw', 0),
                'bets': results['total_bets']
            }
            leaderboard_df = pd.concat([leaderboard_df, pd.DataFrame([user_row])], ignore_index=True)

        # Save updated leaderboard
        leaderboard_df.to_csv(leaderboard_file_path, index=False)
        st.session_state.leaderboard_df = pd.read_csv(leaderboard_file_path)
    except Exception as e:
        st.error(f"Failed to update Season Leaderboard. Error: {str(e)}")


def handle_set_season(field_key):
    try:
        new_season = st.session_state[field_key]
        update_season(new_season)
    except Exception as e:
        st.error(f"Failed to update Seasons. Error: {str(e)}")

def handle_set_week(field_key, season):
    try:
        new_active_week = st.session_state[field_key]
        update_active_week(new_active_week, season)
    except Exception as e:
        st.error(f"Failed to update Active Week. Error: {str(e)}")

def handle_add_game(away_team_input, home_team_input, active_season, selected_week):
    try:
        # Create a new game entry
        l = len(st.session_state.games_df) + 1
        g_id = 'game_' + str(l)
        new_game = {
            'game_id': g_id,  # Incremental game ID
            'date_time': pd.Timestamp.now(),  # Current timestamp for simplification
            'season': active_season,
            'week': selected_week,
            'away_team': away_team_input,
            'home_team': home_team_input,
            'away_score': 0,  # No score yet
            'home_score': 0,
            'away_ml': 0,  # Moneyline, spread, and other betting lines not set
            'home_ml': 0,
            'spread': 0,
            'winner': 'draw',
            'notes': '',
            'status': 'Pending'
        }
        add_game(new_game)
        st.success(f"Game added successfully between {away_team_input} and {home_team_input} for week {selected_week} of the {active_season} season.")
    except Exception as e:
        # Confirmation message
        st.error(f"Error Failed to Add Game.")
