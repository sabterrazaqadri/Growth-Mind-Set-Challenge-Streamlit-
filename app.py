import streamlit as st

st.title("The Best Way to Build Python Apps")
st.write("Streamlit allows you to build interactive web apps in Python easily!")

#Simple Interactive Feture

name = st.text_input("Enter Your Name")
if name:
    st.success(f"Hello {name}, welcome to Streamlit!")

st.header("Why Choose Streamlit?")
st.write("- Simple and Fast")
st.write("- No need for frontend coding (HTML/CSS)")
st.write("- Supports Data Science & ML Integration")

    
st.header("Demo: Simple Chart")

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(50,4), columns=["A","B","C","D"])
st.line_chart(df)

st.header("Streamlit App Deployment Guide (Short & Simple)")
st.write("You can deploy your Streamlit app easily on Streamlit Cloud or other platforms like Render, Hugging Face, or AWS. Here’s a quick guide for deploying on Streamlit Community Cloud (free & easy).")

st.subheader("1 - Push Code to GitHub")
st.write("""Make sure your project has these files:

1 - app.py (Your main Streamlit app file)

2 - requirements.txt (Dependencies list)

Create requirements.txt (if not already):

pip freeze > requirements.txt

Then push your code to GitHub.""")

st.subheader("2 - Deploy on Streamlit Cloud")
st.write("""1 - Go to → https://share.streamlit.io

2 - Sign in with GitHub

3 - Click "New App"

4 - Select Your GitHub Repo

5 - Set Main File Path → app.py

6 - Click Deploy """)

st.subheader("3 - Access & Share Your App")
st.write("Once deployed, you’ll get a public URL to share your app!")

st.subheader("Build your own Python apps effortlessly with Streamlit!")