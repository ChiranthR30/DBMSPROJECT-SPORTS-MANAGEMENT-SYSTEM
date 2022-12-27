import streamlit as st
from database import add_coach_details

def add_coach():

    col1,col2=st.columns(2)

    with col1:
        srn=st.text_input("SRN")
        cyn=st.selectbox("Did he take a coach/no",['yes','no'])

    with col2:
        cname=st.text_input("Coach name")
        sport=st.text_input("Sport")

    if st.button("Add coach details"):
        add_coach_details(srn,cyn,cname,sport)
        st.success("SRN {} coached by {}".format(srn,cname))

