import streamlit as st

st.title("🔲 Primary Button Demo")

st.header("`st.button`:")
st.button("Primary Button", type='primary')
st.button("Disabled Primary Button", type='primary', disabled=True)
st.button("Default (Secondary) Button")
st.button("Disabled Secondary Button", disabled=True)

st.header("`st.form_submit_button`:")
with st.form("my_form"):
   st.subheader("Primary Form Button")
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   submitted = st.form_submit_button("Submit", type='primary')

with st.form("other_form"):
   st.subheader("Default (Secondary) Form Button")
   slider_val = st.slider("Form 2 slider")
   checkbox_val = st.checkbox("Form 2 checkbox")

   submitted = st.form_submit_button("Submit")