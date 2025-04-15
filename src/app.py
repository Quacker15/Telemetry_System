import streamlit as st

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply custom CSS
load_css("assets/styles.css")

# Your Streamlit app content
st.title("Enhanced Streamlit App")
st.button("Click Me")
