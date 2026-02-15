import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# App ka Title
st.title("Loan Prediction App")

# Example code (Aap ise apne logic se replace kar sakte hain)
try:
    le = LabelEncoder()
    st.success("Libraries successfully load ho gayi hain!")
    
    # Aapka aage ka model prediction code yahan aayega...
    
except Exception as e:
    st.error(f"Error: {e}")
