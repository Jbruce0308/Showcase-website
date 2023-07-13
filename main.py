import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)



with col1:
    st.image("images/jesse.JPG", width=600)

with col2:
    st.title("Jesse Johnson Bruce")
    content = """
    Hello, I am Jesse! I am a cloud engineer that loves finance and learning new tech skills. I live in the USA and have worked
    in the cloud space for 3 years
    """
    st.info(content)