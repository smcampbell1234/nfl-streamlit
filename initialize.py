import streamlit as st
from data_handling.data_handling import get_games, get_users, get_bets, get_seasons, create_games, create_users, create_bets, create_leaderboard, create_seasons, get_leaderboard

def initialize():
    create_games()
    st.session_state.games_df = get_games()
    create_users()
    st.session_state.users_df = get_users()
    create_bets()
    st.session_state.bets_df = get_bets()
    create_seasons()
    st.session_state.seasons_df = get_seasons()
    create_leaderboard()
    st.session_state.leaderboard_df = get_leaderboard()
