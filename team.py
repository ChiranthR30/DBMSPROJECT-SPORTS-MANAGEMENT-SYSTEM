import streamlit as st
from database import add_team_details

def add_team():

    event_id=st.text_input('Event_id')
    team1=st.text_input('Team1')
    team2=st.text_input('Team2')

    if st.button('Enter team details'):
        add_team_details(event_id,team1,team2)
        st.success('{} vs {} '.format(team1,team2))

