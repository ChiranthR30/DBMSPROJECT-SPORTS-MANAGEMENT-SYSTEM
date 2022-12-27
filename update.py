import pandas as pd
import streamlit as st
from database import view_events,update_venue,update_date
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pesu_sports"
)

def update():
    res=view_events()
    events=pd.DataFrame(res,columns=['Event-name','start_date','end_date','venue','sport','Indoor/Outdoor','Description','event_id'])

    with st.expander("Current Data"):
        st.dataframe(events)

    choices=st.selectbox("Do you want to change the venue or the dates",['Venue','Dates'])
    for_id=st.text_input("Enter the event id")

    if choices=='Venue':
        new_venue=st.text_input("Enter new venue")
        if st.button("Update(venue)"):
            update_venue(for_id,new_venue)
            st.success("Updated venue successfully for event {}".format(for_id))

    if choices=='Dates':
        new_sd=st.date_input("Enter new start date")
        new_ed=st.date_input("Enter new end date")
        if st.button("Update(Date)"):
            update_date(for_id,new_sd,new_ed)
            st.success("Updated dates successfully")

    new_res=view_events()
    df=pd.DataFrame(new_res,columns=['Event-name','start_date','end_date','venue','sport','Indoor/Outdoor','Description','event_id'])

    with st.expander("Updated values"):
        st.dataframe(df)
