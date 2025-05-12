import streamlit as st

def visualize_structure(structure):
    st.json({f"campo_{i+1}": name for i, name in enumerate(structure)})