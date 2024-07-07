import streamlit as st
import random

def gen_unique(text):
    rand = random.randint(0, 100000000)
    return str(rand) + text

def get_index(list, value):
    try:
        return list.index(value)
    except ValueError:
        return -1

def get_active_season():
    if 'seasons_df' in st.session_state:
        # Filter the DataFrame for the active season
        active_season_df = st.session_state.seasons_df[st.session_state.seasons_df['status'] == 'active']
        
        # Check if there is any active season
        if not active_season_df.empty:
            # Return the 'season' value of the active season
            return active_season_df['season'].values[0]
        else:
            st.error("No active season found.")
            return ''
    else:
        st.error("Seasons data is not loaded.")
        return ''

def get_active_week():
    if 'seasons_df' in st.session_state:
        # Filter the DataFrame for the active season
        active_season_df = st.session_state.seasons_df[st.session_state.seasons_df['status'] == 'active']
        
        # Check if there is any active season
        if not active_season_df.empty:
            # Return the 'default_week' value of the active season
            return active_season_df['default_week'].values[0]
        else:
            st.error("No active season found.")
            return 1
    else:
        st.error("Seasons data is not loaded.")
        return 1