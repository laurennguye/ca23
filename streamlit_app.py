import streamlit as st

st.title("Main Title")

col1, col2 = st.columns(2)

with col1:
    st.header("Column 1")
    st.text("Hello")

with col2:
    st.header("Column 2")
    st.text("World")

with st.expander("Click to expand"):
    st.text("Here you could put in some really, really explanatory stuff.")
