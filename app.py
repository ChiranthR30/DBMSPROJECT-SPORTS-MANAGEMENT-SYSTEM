
import streamlit as st
from event import book_event
from database import view_team,view_results,show_coach_details,view_entry,view_events,query
from individual_entry import individual
from team import add_team
from result import add_result
from coach import add_coach
import pandas as pd
from delete import delete
from update import update
from countt import countt

import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pesu_sports"
)


result=view_team()
result1=view_results()
result2=show_coach_details()
result3=view_entry()
eve=view_events()

#df=pd.DataFrame(view_team(),columns=['Event_id','Team1','Team2','Event-name','Start-date','End-date','Venue','sport','Indoor/Outdoor','Description','id'])
#df=df.iloc[:, :-1]
df2=pd.DataFrame(result1,columns=['Event_name','Winner','runnerup','dept of winner','cash price'])
df3=pd.DataFrame(result2,columns=['SRN','Coached/No','Coachname','Sport'])
#df4=pd.DataFrame(result3,columns=['SRN','INTIME','indoor/outdoor','Sport','guard_name'])
events=pd.DataFrame(eve,columns=['Event-name','start_date','end_date','venue','sport','Indoor/Outdoor','Description','event_id'])


def app():

    #st.balloons()
    #st.write(view_team())

    st.header("PES Sports Event Management")
    menu = ["Book Event",
            "Show booked events",
             "Normal individual entry",
             "Show entries",
              "Update event", 
              "Delete event details",
                "Add team details",
              "Display team details",
              "No of teams",
              "Add results",
              "Display results",
              "Add coach details",
              "Show coach details",
              "Write query"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice=="Book Event":
        st.subheader('Book venue for the sport event')
        book_event()
    
    elif choice=="Show booked events":
        st.header("All booked events")
        st.dataframe(events)

    elif choice=="Normal individual entry":
        st.subheader('Entry before entering a sports venue(not for event)')
        individual()

    elif choice=="Add team details":
        st.subheader('Add team details here for event')
        add_team()

    elif choice=="Display team details":
        st.subheader('All team details')
        st.dataframe(view_team())
        #st.write(result)

    elif choice=='Add results':
        st.subheader('Add all winner details')
        add_result()

    elif choice=='Display results':
        st.subheader('Results at differnt venues')
        st.dataframe(df2)

    elif choice=="Add coach details":
        st.subheader("Add coach details for a student")
        add_coach()

    elif choice=="Show coach details":
        st.subheader("Coach details for student")
        st.dataframe(df3)

    
    elif choice=="Show entries":
        st.subheader("See all entries here")
        st.dataframe(df4)

    elif choice=="Delete event details":
        st.subheader("Delete event details")
        delete()

    elif choice=="Update event":
        st.subheader("Update any event details")
        update()

    elif choice=="No of teams":
        st.subheader("Count no of teams")
        countt()

    elif choice=="Write query":
        st.subheader("Write query")
        q=st.text_input("Write query")

        result=query(q)
 
        if st.button("Show result"):
            df=pd.DataFrame(result)
            st.dataframe(df)

app()