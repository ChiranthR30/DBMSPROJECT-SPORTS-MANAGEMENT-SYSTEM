import streamlit as st
from database import add_user,view_users
import pandas as pd
from app import app

def main():
    st.title('PESU Sports Event Management')
    result=view_users()
    df = pd.DataFrame(result,columns=['user','pass'])

    with st.form(key='my_form'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        choice1=st.form_submit_button('Login')
        choice2=st.form_submit_button('New user?')

    if choice1:
            #if username and password in df:
                app()

            #else:
                #st.write('Incorrect user and password')
            



    if choice2:
        new_user = st.text_input('New username')
        new_pass=st.text_input('New password')
        confirm_pass=st.text_input('Confirm password')

        if new_pass!=confirm_pass:
            st.write('Confirm password correctly')
        
        else:

            add_user(new_user,new_pass)

main()