import streamlit as st
from send_email import send_email

st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email address")
    user_message = st.text_area("Your message")
    message = f"""\ 
    Subject: New email from {user_email}
    
    From: {user_email}
    {user_message}
    """
    button = st.form_submit_button("Submit your email")
    if button:
        send_email(message, user_email)
        st.info("Your email was sent successfully")
