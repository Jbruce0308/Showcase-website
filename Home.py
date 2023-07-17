import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1, col2, = st.columns(2)

content2 = """Below you can find some of the apps i have built in Python. Feel free to contact me soon!"""
st.write(content2)
col3, empty_col, col4 = st.columns([1.5,0.5,1.5])


with col1:
    st.image("jesse.JPG", width=600)

with col2:
    st.title("Jesse Johnson Bruce")
    content = """
    Hello, I am Jesse! I am a cloud engineer that loves finance and learning new tech skills. I live in the USA and have worked
    in the cloud space for 3 years
    """
    st.info(content)




df = pandas.read_csv("data.csv",sep=";")



with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")