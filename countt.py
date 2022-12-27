from database import count_teams

import streamlit as st
import pandas as pd

def countt():

    x=st.text_input('Enter event_id for which you want to see no of teams')


    if st.button('Count teams'):
        df=pd.DataFrame(count_teams(x),columns=['Count of teams'])
        st.dataframe(df)
