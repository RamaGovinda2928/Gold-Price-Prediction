import streamlit as st
import pandas as pd
import pickle
import calendar as cd

# Function to create the page layout
def create_page():
    st.title('Gold Price Prediction for year 2022')
    st.image('gold_image.jpeg', use_column_width=True)  # Added image of gold
    
    # Dropdown for selecting month
    month = st.selectbox('Choose prediction month', range(1, 13))
    
    # Converted selected month to DataFrame
    pred_date = pd.DataFrame({'year': [2022], 'month': [month], 'day': [1]})
    features_timestamp = pd.to_datetime(pred_date)
    
    return month, features_timestamp

# Load the model
with open('pred.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

# Get features and make prediction
selected_month, features_timestamp = create_page()
if st.button('Submit'):
    res = loaded_model.predict(start=features_timestamp.iloc[0], end=features_timestamp.iloc[0])
    st.subheader('Predicted Result')
    month_name_str = cd.month_name[selected_month]
    st.write(f"Price of gold for {month_name_str} is {round(res[0],2)}")