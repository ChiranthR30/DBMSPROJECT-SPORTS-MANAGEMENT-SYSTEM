import streamlit as st
from database import add_results

def add_result():

    col1,col2=st.columns(2)

    with col1:
        winner=st.text_input('Winner')
        runner=st.text_input('Runner up')
        dept=st.text_input('Department of winners')

    with col2:
        event_name=st.text_input('Event name')
        cash=st.text_input('Cash price given')

    if st.button('Add results'):
        add_results(event_name,winner,runner,dept,cash)
        st.success('Added result for event {}'.format(event_name))
        
    