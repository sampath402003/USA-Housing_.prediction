import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# Set page config
st.set_page_config(page_title="USA Housing Price Predictor", layout="centered")

st.title("🏠 USA Housing Price Predictor")
st.markdown("Enter property details below to get an instant price prediction")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('USA_Housing.csv')

# Train models
@st.cache_resource
def train_models(data):
    scaler = StandardScaler()
    X = data.drop(['Price', 'Address'], axis=1)
    y = data['Price']
    cols = X.columns
    
    X_scaled = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=101)
    
    # Train Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    lr_pred = lr.predict(X_test)
    lr_r2 = r2_score(y_test, lr_pred)
    
    # Train KNN with optimal k
    best_k = 5
    knn = KNeighborsRegressor(n_neighbors=best_k)
    knn.fit(X_train, y_train)
    knn_pred = knn.predict(X_test)
    knn_r2 = r2_score(y_test, knn_pred)
    
    return {
        'scaler': scaler,
        'lr_model': lr,
        'knn_model': knn,
        'X_columns': cols,
        'X_test': X_test,
        'y_test': y_test,
        'lr_pred': lr_pred,
        'knn_pred': knn_pred,
        'lr_r2': lr_r2,
        'knn_r2': knn_r2
    }

data = load_data()
models = train_models(data)

data = load_data()
models = train_models(data)

# Main Prediction Interface
st.markdown("---")
st.subheader("📋 Property Details")

col1, col2 = st.columns(2)

with col1:
    avg_area_income = st.number_input(
        "Average Area Income ($)",
        value=65000,
        step=1000,
        min_value=0,
        help="Average income in the area"
    )
    avg_area_house_age = st.number_input(
        "Average House Age (years)",
        value=15,
        step=1,
        min_value=0,
        help="Average age of houses in the area"
    )
    avg_area_number_of_rooms = st.number_input(
        "Average Number of Rooms",
        value=5.0,
        step=0.5,
        min_value=0.0,
        help="Average rooms per house"
    )

with col2:
    avg_area_number_of_bedrooms = st.number_input(
        "Average Number of Bedrooms",
        value=3.0,
        step=0.5,
        min_value=0.0,
        help="Average bedrooms per house"
    )
    area_population = st.number_input(
        "Area Population",
        value=50000,
        step=1000,
        min_value=0,
        help="Total population in the area"
    )

st.markdown("---")

# Create feature list
features_list = [
    avg_area_income,
    avg_area_house_age,
    avg_area_number_of_rooms,
    avg_area_number_of_bedrooms,
    area_population
]

# Scale features
features_scaled = models['scaler'].transform([features_list])

# Make predictions
lr_prediction = models['lr_model'].predict(features_scaled)[0]
knn_prediction = models['knn_model'].predict(features_scaled)[0]
avg_prediction = (lr_prediction + knn_prediction) / 2

# Display predictions with visual emphasis
st.subheader("💰 Price Predictions")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Linear Regression",
        f"${lr_prediction:,.2f}",
        delta=None
    )

with col2:
    st.metric(
        "KNN Model",
        f"${knn_prediction:,.2f}",
        delta=None
    )

with col3:
    st.metric(
        "Average Prediction",
        f"${avg_prediction:,.2f}",
        delta=None
    )

# Show input summary
st.markdown("---")
st.subheader("📊 Property Summary")

summary_df = pd.DataFrame({
    'Feature': [
        'Avg Area Income',
        'Avg House Age',
        'Avg Rooms',
        'Avg Bedrooms',
        'Area Population'
    ],
    'Value': [
        f"${avg_area_income:,.0f}",
        f"{avg_area_house_age} years",
        f"{avg_area_number_of_rooms:.1f}",
        f"{avg_area_number_of_bedrooms:.1f}",
        f"{area_population:,}"
    ]
})

st.table(summary_df)

# Additional information
with st.expander("ℹ️ Model Information"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Linear Regression Model**")
        st.write(f"- R² Score: {models['lr_r2']:.4f}")
        st.write("- Simple and interpretable")
        st.write("- Good for linear relationships")
    
    with col2:
        st.write("**KNN Model**")
        st.write(f"- R² Score: {models['knn_r2']:.4f}")
        st.write("- Non-parametric approach")
        st.write("- Captures local patterns")

st.markdown("---")
st.caption("USA Housing Price Prediction | Built with Streamlit & Machine Learning")
