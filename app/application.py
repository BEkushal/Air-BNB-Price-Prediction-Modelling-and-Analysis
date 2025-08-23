import streamlit as st
import requests

# The URL for your running API
API_URL = "https://airbnb-fastapi.onrender.com/predict"

st.title("Airbnb Rental Price Prediction")
st.write("Enter the details of your property to get the predicted rental price.")

accommodates = st.number_input("Accommodates", min_value=1, max_value=16, value=1, step=1)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=8, step=1, value=1)
bedrooms = st.number_input("Bedrooms", min_value=0, max_value=10, value=0, step=1) # 0 allowed for studios
beds = st.number_input("Beds", min_value=1, max_value=18, value=1, step=1)
review_scores_rating = st.number_input("Review Score (0-100)", min_value=0, max_value=100, value=0)

room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
cancellation_policy = st.selectbox("Cancellation Policy", ["strict", "moderate", "flexible"])
cleaning_fee = st.radio("Cleaning Fee Charged?", ["Yes", "No"])
instant_bookable = st.radio("Instant Bookable?", ["Yes", "No"])

# One-hot encoding for room_type
room_type_Private_room = 1 if room_type == "Private room" else 0
room_type_Shared_room = 1 if room_type == "Shared room" else 0

# One-hot for cancellation_policy
cancellation_policy_moderate = 1 if cancellation_policy == "moderate" else 0
cancellation_policy_strict = 1 if cancellation_policy == "strict" else 0

# Cleaning fee/Instant bookable as int
cleaning_fee_val = 1 if cleaning_fee == "Yes" else 0
instant_bookable_val = 1 if instant_bookable == "Yes" else 0


if st.button("Predict Price"):
    json_data = {
        "accommodates": accommodates,
        "bathrooms": bathrooms,
        "cleaning_fee": cleaning_fee_val,
        "instant_bookable": instant_bookable_val,
        "review_scores_rating": review_scores_rating,
        "bedrooms": bedrooms,
        "beds": beds,
        "room_type_Private_room": room_type_Private_room,
        "room_type_Shared_room": room_type_Shared_room,
        "cancellation_policy_moderate": cancellation_policy_moderate,
        "cancellation_policy_strict": cancellation_policy_strict
    }
    try:
        response = requests.post(API_URL, json=json_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Price: ${result['predicted_price']:,}")
            st.write(f"(Log price prediction: {result['log_price_prediction']})")
        else:
            st.error("Error in prediction. Please check your input and try again.")
    except Exception as e:
        st.error(f"Failed to connect to prediction API: {e}")