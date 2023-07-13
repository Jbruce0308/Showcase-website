import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1, col2, = st.columns(2)
col3, col4 = st.columns(2)


with col1:
    st.image("images/jesse.JPG", width=600)

with col2:
    st.title("Jesse Johnson Bruce")
    content = """
    Hello, I am Jesse! I am a cloud engineer that loves finance and learning new tech skills. I live in the USA and have worked
    in the cloud space for 3 years
    """
    st.info(content)

content2 = """Below you can find some of the apps i have built in Python. Feel free to contact me soon!"""
st.write(content2)


df = pandas.read_csv("data.csv",sep=";")



with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])