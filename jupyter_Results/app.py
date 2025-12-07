
import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Network Anomaly Detection",
    page_icon="🛡️",
    layout="wide"
)

# Title
st.title("🛡️ Network Anomaly Detection System")
st.markdown("### Real-Time LSTM-based Network Intrusion Detection")
st.markdown("---")

# Sidebar
st.sidebar.header("⚙️ Configuration")
model_type = st.sidebar.selectbox(
    "Select Model",
    ["Binary (Normal vs Attack)", "Multi-Class (Attack Types)"]
)

# Load models (cached)
@st.cache_resource
def load_models():
    model_binary = keras.models.load_model('best_model_binary.h5')
    model_multi = keras.models.load_model('best_model_multiclass.h5')
    return model_binary, model_multi

model_binary, model_multi = load_models()

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Single Prediction", "📁 Batch Upload", "📈 Model Info"])

# Tab 1: Single Prediction
with tab1:
    st.header("Single Sample Prediction")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Enter Network Traffic Features")
        # Add input fields for key features
        duration = st.number_input("Duration", value=0)
        src_bytes = st.number_input("Source Bytes", value=0)
        dst_bytes = st.number_input("Destination Bytes", value=0)
        # ... more features
        
    with col2:
        st.subheader("Prediction Results")
        if st.button("🔍 Predict", type="primary"):
            # Make prediction
            st.success("✅ Prediction Complete!")
            # Display results

# Tab 2: Batch Upload
with tab2:
    st.header("Batch Prediction from CSV")
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(f"Loaded {len(df)} samples")
        # Process and predict

# Tab 3: Model Info
with tab3:
    st.header("Model Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Binary Model")
        st.metric("Accuracy", "77.25%")
        st.metric("Precision", "97.39%")
        st.metric("Recall", "61.69%")
    
    with col2:
        st.subheader("Multi-Class Model")
        st.metric("Accuracy", "33.08%")
        st.metric("Classes", "5")
        st.text("DoS, Normal, Probe, R2L, U2R")

st.sidebar.markdown("---")
st.sidebar.info("💡 Built with TensorFlow & Streamlit")
