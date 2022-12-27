import streamlit as st
from database import add_entry,view_entry,view_events
from datetime import date
import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pesu_sports"
)

result=view_events()
def individual():

    col1,col2=st.columns(2)

    with col1:
        srn=st.text_input('SRN')
        i_o=st.selectbox('Out/Indoor',['Outdoor','Indoor'])
    
    with col2:
        sp=st.text_input('Sport')
        gname=st.text_input('Enter Guard name')


    if st.button('Enter details'):
        flag=0

        if srn=='':
            st.warning("SRN cant be empty")
            flag=1
            
        for i in range(len(result)):
            if result[i][2]<str(date.today())<result[i][3]:
                st.write('Sorry Event is going on for these days')
                flag=1
        if flag==0:
            try:
                add_entry(srn,i_o,sp,gname)

            except mysql.connector.Error as e:
                try:
                    st.write("{}".format(e.args[1]))
                    st.write("Warning other student's SRN")
                except IndexError:
                        print("MySQL Error: %s") % str(e)
                        return None
            finally:
                st.success('Added details for srn {}'.format(srn))


