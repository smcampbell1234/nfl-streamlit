import streamlit as st
from initialize import initialize
from constants.logos import team_logos
from utils.general_utils import gen_unique, get_index, get_active_season, get_active_week
from utils.crud_utils import handle_update_game, handle_create_user, handle_bet, handle_refresh_week, update_season_leaderboard, handle_set_season, handle_set_week, handle_add_game
from style.style import app_css

from data_handling.data_handling import bets_file_path, users_file_path, create_download_button

# betters = ['Lane', 'Russell', 'Delia', 'Sean', 'Shane']
teams = [
    "Lions", "Bengals", "Texans", "Buccaneers", "Panthers", "Cardinals", "Jaguars", "49ers",
    "Titans", "Raiders", "Eagles", "Rams", "Dolphins", "Packers", "Cowboys", "Bills",
    "Chiefs", "Browns", "Ravens", "Vikings", "Falcons", "Commanders", "Colts", "Steelers",
    "Saints", "Broncos", "Patriots", "Seahawks", "Chargers", "Bears", "Giants", "Jets"
]
statuses = [
    'Pending',
    'Under Way',
    'Final',
    'Canceled'
]

# **** INITIALIZE (This runs once on first render) ********
if "render_count" not in st.session_state:
    initialize()
    st.session_state.render_count = 1

# Allows you to use style
st.markdown(app_css, unsafe_allow_html=True)

def filter_games(games_df, status_list):
    return games_df[games_df['status'].isin(status_list)]


def display_selected_user_without_bets(game_id, selected_user):
    games_df = st.session_state.games_df
    bets_df = st.session_state.bets_df
    users_df = st.session_state.users_df
    
    # Get all bets for this game
    game_bets = bets_df[bets_df['game_id'] == game_id]
    users_with_bets = game_bets['user'].unique()

    # Check if selected_user has placed a bet
    if selected_user not in users_with_bets:
        st.markdown(f"<span style='color: red; font-size: 24px; height: 30px;'>{selected_user} has not placed a bet.</span>", unsafe_allow_html=True)
    else:
        # dummy div to keep space consistent
        st.markdown(f"<div style='background-color: transparent; height: 30px;'></div>", unsafe_allow_html=True)


def weekly_leaderboard(current_week):
    st.header(f"Week {current_week} Leaderboard")
    if st.button('Refresh Weeks Leaderboard'):
        handle_refresh_week(current_week)
    bets_df = st.session_state.get('bets_df')
    games_df = st.session_state.get('games_df')

    if bets_df is None or games_df is None or bets_df.empty or games_df.empty:
        st.write("No bets or games data available.")
        return

    weekly_games = filter_games(games_df[games_df['week'] == current_week], ['Pending','Under Way', 'Final'])
    weekly_bets = bets_df[bets_df['game_id'].isin(weekly_games['game_id'])]

    if weekly_bets.empty:
        st.write("No bets have been placed for this week yet.")
        return

    leaderboard = weekly_bets.groupby(['user', 'outcome']).size().unstack(fill_value=0)
    # Ensure all outcome columns exist
    for outcome in ['win', 'loss', 'draw']:
        if outcome not in leaderboard.columns:
            leaderboard[outcome] = 0
    
    leaderboard['total'] = leaderboard.sum(axis=1)
    leaderboard.sort_values(by='win', ascending=False, inplace=True)

    count = 0
    for index, row in leaderboard.iterrows():
        count += 1
        win_count = row.get('win', 0)  # Safely get win count
        loss_count = row.get('loss', 0)  # Safely get loss count
        win_percent = 0.00
        if (win_count + loss_count) > 0:
            win_percent = round((win_count / (win_count + loss_count)) * 100, 2)
        total_bets = row['total']
        st.markdown(f"{count}. <div class='space-between' style='margin: 0;'><div style='width: 160px; font-weight: bold'>{index}</div> <div style='width: 170px;'>Wins: {win_count}&nbsp;&nbsp;&nbsp;&nbsp;L: {loss_count} &nbsp; ({win_percent}%)</div><div style='width: 135px;'>Total Bets: {total_bets}</div></div>", unsafe_allow_html=True)

    if isEditMode:
        if st.checkbox('See Table'):
            st.table(leaderboard)


def display_leaderboard():
    # Assuming season leaderboard is calculated and stored as described in previous discussions
    if 'leaderboard_df' not in st.session_state or st.session_state.leaderboard_df.empty:
        st.write("Season leaderboard is not available or has not been generated.")
        return

    leaderboard_df = st.session_state.leaderboard_df

    # Ensure all relevant columns exist and initialize them with zeros if they do not
    for outcome in ['wins', 'losses', 'draws']:
        if outcome not in leaderboard_df.columns:
            leaderboard_df[outcome] = 0

    leaderboard_df.sort_values(by=['wins', 'week_wins'], ascending=False, inplace=True)

    count = 0
    for index, row in leaderboard_df.iterrows():
        count += 1
        user = row['user']
        wins = row['wins']
        losses = row['losses']
        draws = row['draws']
        total_bets = row.get('bets', 0)
        weeks_won = row.get('week_wins', 0)
        win_percentage = 0.0
        if (wins + losses) > 0:
            win_percentage = round((wins / (wins + losses)) * 100, 2)      

        st.markdown(f"{count}. <div class='space-between' style='margin: 0;'><div style='font-weight: bold;'>{user}</div><div>Wins {wins} ({win_percentage}%)</div><div>Weeks Won: {weeks_won}</div><div>L: {losses} &nbsp;D: {draws} &nbsp;Bets: {total_bets}</div></div>", unsafe_allow_html=True)

    if isEditMode:
        if st.checkbox('See Season Leaderboard Table'):
            st.table(leaderboard_df)


# *****************************************
# APP STARTS HERE
# *****************************************
selected_season = get_active_season()
st.header(f'NFL {selected_season} Season')
st.markdown(f"<div class='h5 italic margin-bottom-15' style='font-weight: normal;'>Brought to you by your Comissioner.</div>", unsafe_allow_html=True)
isEditMode = False
if st.checkbox('Edit Mode'):
    # isEditMode = True
    isEditMode = st.text_input('Edit Mode Password', placeholder='Edit').lower() == 'edit'

if isEditMode:
    st.markdown(f"<div class='h3 red italic easy-top-bottom-margin '>Edit Mode</div>", unsafe_allow_html=True)
st.write('')
st.write('')

if isEditMode:
    seasons_list = [''] + st.session_state.seasons_df['season'].unique().tolist()
    active_season = get_active_season()
    st.selectbox(
        'Active Season',
        seasons_list,
        key='set_active_season',
        index=(get_index(seasons_list, active_season)),
        on_change=handle_set_season,
        args=['set_active_season'],
        )
    st.write('')

    active_week = get_active_week()
    st.number_input(
        'Set Active Week',
        value=active_week,
        min_value=1,
        max_value=30,
        step=1,
        key="Set Active Week",
        on_change=handle_set_week,
        args=['Set Active Week', active_season],
        )
    st.write('')
    st.write('')
    st.write('')
    st.write('')
st.write('')
st.write('')

active_week = get_active_week()
selected_week = active_week
if not isEditMode:
    selected_week = st.number_input(
        'Week',
        value=active_week,
        min_value=1,
        max_value=30,
        step=1,
        key="Weeks Select"
        )


users = [''] + st.session_state.users_df['user'].unique().tolist()
selected_user = st.selectbox("Place your bets", users, index=0)

if isEditMode:
    if st.checkbox("Add a new better"):
        handle_create_user()
    st.write('')
    st.write('')

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
# Season Leaderboard
st.header("Season Leaderboard")
if isEditMode:
    if st.button('Refresh Season Leaderboard'):
        update_season_leaderboard(selected_season)
display_leaderboard()

# Weeks Wins Leaderboard goes here
weekly_leaderboard(selected_week)




week_games = st.session_state.games_df[st.session_state.games_df['week'] == selected_week]

st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
game_count = 0
for index, row in week_games.iterrows():
     game_count += 1
     with st.container():
        away_team = row['away_team']
        home_team = row['home_team']
        away_score = row['away_score']
        home_score = row['home_score']
        winner = row['winner']
        game_id = row['game_id']
        status = row['status']
        game_open_for_betting = status == 'Pending'

        c1, c2 = st.columns([4,1])

        if isEditMode:
            c1.header(f'Game {game_count}')
            # Status
            field_key = gen_unique(game_id + '_Status')
            row_key = "status"
            status_input = c2.selectbox(
                label="Status",
                options=([''] + statuses),
                index=(1 + get_index(statuses, status)),
                label_visibility="hidden",
                key=field_key,
                on_change=handle_update_game,
                args=[field_key, row_key, game_id],
                )

            if c2.button('Refresh', key=f"{game_id}_Refres_Btn"):
                st.experimental_rerun()
        else:
            c1.header(f'Game {game_count}')
            c2.write(status)
            if c2.button('Refresh', key=f"{game_id}_Refres_Btn"):
                st.experimental_rerun()


        col1, col2 = st.columns(2)

        with col1:
            st.image(team_logos[away_team], width=75)
            # Away Team
            if isEditMode:
                field_key = gen_unique(game_id + '_Away')
                row_key = "away_team"
                away_team_input = st.selectbox(
                    label="Away Team",
                    options=([''] + teams),
                    index=(1 + get_index(teams, away_team)),
                    label_visibility="hidden",
                    key=field_key,
                    on_change=handle_update_game,
                    args=[field_key, row_key, game_id],
                    )
            else:
                if away_team == winner:
                    st.markdown(f"<div class='h2 game-score-top-bottom-margin'>{away_team}&nbsp;&nbsp;&nbsp;<span style='color: lime; font-size: 2.1rem;'>&#10003;</span></div>", unsafe_allow_html=True)
                else:
                    st.header(away_team)
            # Away Score
            if status == 'Final':
                st.header(away_score)
            else:
                field_key = gen_unique(game_id + '_Away_Score')
                row_key = "away_score"
                away_score_input = st.number_input(
                    'Away Score',
                    min_value=0,
                    value=int(away_score),
                    key=field_key,
                    label_visibility="hidden",
                    on_change=handle_update_game,
                    args=[field_key, row_key, game_id],
                    )

            if selected_user and game_open_for_betting:
                if st.button(f"{selected_user} selects {away_team}", key=f"{game_id}_bet_away"):
                    handle_bet(selected_user, row, away_team, 'away')
            bets_df = st.session_state.bets_df
            away_betters = ', '.join(bets_df[(bets_df['game_id'] == row['game_id']) & (bets_df['selected_team'] == away_team)]['user'].tolist())
            st.markdown(f"{away_betters}")

        with col2:
            st.image(team_logos[home_team], width=75)
            # Home Team
            if isEditMode:
                field_key = gen_unique(game_id + '_Home')
                row_key = "home_team"
                away_team_input = st.selectbox(
                    label="Home Team",
                    options=([''] + teams),
                    index=(1 + get_index(teams, home_team)),
                    label_visibility="hidden",
                    key=field_key,
                    on_change=handle_update_game,
                    args=[field_key, row_key, game_id],
                    )
            else:
                if home_team == winner:
                    st.markdown(f"<div class='h2 game-score-top-bottom-margin'>{home_team}&nbsp;&nbsp;&nbsp;<span style='color: lime; font-size: 2.1rem;'>&#10003;</span></div>", unsafe_allow_html=True)
                else:
                    st.header(home_team)
            # Home Score
            if status == 'Final':
                st.header(home_score)
            else:
                field_key = gen_unique(game_id + '_Home_Score')
                row_key = "home_score"
                home_score_input = st.number_input(
                    'Home Score',
                    min_value=0,
                    value=int(home_score),
                    key=field_key,
                    label_visibility="hidden",
                    on_change=handle_update_game,
                    args=[field_key, row_key, game_id],
                    )


            if selected_user and game_open_for_betting:
                if st.button(f"{selected_user} selects {home_team}", key=f"{game_id}_bet_home"):
                    handle_bet(selected_user, row, home_team, 'home')
            bets_df = st.session_state.bets_df
            home_betters = ', '.join(bets_df[(bets_df['game_id'] == row['game_id']) & (bets_df['selected_team'] == home_team)]['user'].tolist())
            st.markdown(f"{home_betters}")
        st.write(' ')
        # Callout anyone who has not yet made a bet on this game
        if selected_user and game_open_for_betting:
            display_selected_user_without_bets(game_id, selected_user)
        else:
            # dummy div to keep space consistent
            st.markdown(f"<div style='background-color: transparent; height: 30px;'></div>", unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        st.write(' ')

if isEditMode:
    with st.form("add_game_form"):
        st.header('Add New Game')

        colu1, colu2 = st.columns(2)
        
        # Initialize or get existing values for the session state before widgets
        if 'new_away' not in st.session_state:
            st.session_state['new_away'] = teams[0]
        if 'new_home' not in st.session_state:
            st.session_state['new_home'] = teams[0]
        
        with colu1:
            # Away Team
            away_team_input = st.selectbox(
                label="Away Team",
                key="new_away",
                options=teams,
                index=teams.index(st.session_state['new_away'])  # Use the current session state to set the index
            )

        with colu2:
            # Home Team
            home_team_input = st.selectbox(
                label="Home Team",
                key="new_home",
                options=teams,
                index=teams.index(st.session_state['new_home'])  # Use the current session state to set the index
            )

        if away_team_input and home_team_input:
            # Button to submit form
            submitted = st.form_submit_button("Add Game")
            if submitted:
                handle_add_game(away_team_input, home_team_input, active_season, selected_week)


if isEditMode:
    st.write('')
    st.write('')
    st.write('')
    if st.checkbox('Download DBs'):
        st.write("Download CSV Files:")
        create_download_button('games')
        create_download_button('users')
        create_download_button('bets')
        create_download_button('seasons')
        create_download_button('leaderboard')
    
    st.write('')
    st.write('')
    st.write('')
    if st.checkbox('View Bets DataFrame'):
        st.header('st.session_state.bets_df')
        st.table(st.session_state.bets_df)
    st.write('')
    st.write('')
    st.write('')
    if st.checkbox('View Games DataFrame'):
        st.header('st.session_state.games_df')
        st.write(week_games)

