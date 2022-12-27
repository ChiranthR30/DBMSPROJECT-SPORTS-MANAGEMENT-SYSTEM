import pandas as pd
import streamlit as st
from database import view_events,delete_data
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pesu_sports"
)

def delete():
    res=view_events()
    events=pd.DataFrame(res,columns=['Event-name','start_date','end_date','venue','sport','Indoor/Outdoor','Description','event_id'])

    with st.expander("Current Data"):
        st.dataframe(events)

    eid=st.text_input('Enter event_id you want to delete')

    if st.button("Delete event"):
        try:

            delete_data(eid)
    
               
        except mysql.connector.Error as e:
                try:
                    st.write("{}".format(e.args[1]))
                except IndexError:
                        print("MySQL Error: %s") % str(e)
                        return None
        finally:

            st.success("Deleted event")


    new_res=view_events()
    df2=pd.DataFrame(new_res,columns=['Event-name','start_date','end_date','venue','sport','Indoor/Outdoor','Description','event_id'])
    with st.expander("Updated event list"):
        st.dataframe(df2)


    