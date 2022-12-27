import streamlit as st
from database import add_data,view_events
import pandas as pd
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pesu_sports"
)


c=mydb.cursor()
result=view_events()
#df = pd.DataFrame(result,columns=[''])

def book_event():
    flag=0
    col1, col2,col3,col4 = st.columns(4)

    with col1:
        #event_id=st.text_input("Event Id")
        event_id=st.text_input("Event Id")
        event_name=st.text_input("Event name")

    with col2:
        start_date=st.date_input("Enter start-date")
        end_date=st.date_input("Enter end-date")

    with col3:
        sport=st.text_input("Sport")
        i_o=st.selectbox("Indoor/outdoor",['indoor','outdoor'])

    with col4:
        venue=st.text_input("Venue")
        description=st.text_area("Description of event")

    #if start_date and end_date in result:
        #st.write("Venue already booked for these dates")

    #c.execute("SET @M")

    if st.button("add event"):
        

        #c.execute('DECLARE @M TEXT')
        # c.execute('CALL check_date({},{},@M)'.format(start_date,end_date))
        # c.execute('SELECT @M')
        # data=c.fetchall()
        args=[start_date,end_date,0]
        ans=c.callproc('check_date',args)
        data=ans[2]
        #st.write(data)
        if data=='End-date cant be lesser':
                st.warning("End-date cant be lesser")
                flag=1
            
                        
        #st.write(event_name)
        if event_id=='':
            st.warning("Event_id cant be empty")
            flag=1
        elif event_name=='':
            st.warning("Event_name cant be empty")
            flag=1
        elif sport=='':
            st.warning("Sport cant be empty")
            flag=1

        elif venue=='':
            st.warning("Venue cant be empty")
            flag=1


        
        for i in range(len(result)):
            if result[i][3]==venue and result[i][1]<=str(start_date)<=result[i][2]:
                #st.warning('Already booked for these dates')
                #st.write('already booked')
                flag=1
        if flag==0:
            try:
                add_data(event_name,start_date,end_date,venue,sport,i_o,description,event_id)
            except mysql.connector.Error as e:
                try:
                    st.write("{}".format(e.args[1]))
                except IndexError:
                        print("MySQL Error: %s") % str(e)
                        return None
            finally:
               #st.warning('Already booked')
                st.success("Added event at {} for sport {}".format(venue,sport))


