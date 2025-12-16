import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Custom CSS for background and font
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(135deg, #a8e6cf, #dcedc1); /* Shades of green and blue */
            color: black; /* Black font for better contrast */
        }
        .stApp {
            font-family: "Arial", sans-serif;
        }
        .css-1aumxhk {
            background: transparent !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Simulate Business Data for the Digital Twin
def generate_business_data():
    np.random.seed(42)
    data = {
        'num_cows': np.random.randint(1, 20, 500),
        'milk_price': np.random.randint(30, 60, 500),  # Milk price in ₹/liter
        'loan_amount': np.random.randint(5000, 50000, 500),  # Loan in ₹
        'feed_cost': np.random.randint(2000, 8000, 500),  # Feed cost in ₹
        'other_expenses': np.random.randint(1000, 5000, 500),  # Other expenses in ₹
    }
    df = pd.DataFrame(data)

    # Simulate outcome variables based on the inputs
    df['monthly_income'] = df['num_cows'] * df['milk_price'] * 30  # Assuming 30 liters per cow per day
    df['total_expenses'] = df['feed_cost'] + df['other_expenses'] + df['loan_amount'] / 12  # Monthly expenses
    df['monthly_profit'] = df['monthly_income'] - df['total_expenses']  # Monthly profit
    df['risk'] = (df['total_expenses'] > df['monthly_income']).astype(int)  # 1: High risk, 0: Low risk

    return df

# Load data for the digital twin simulation
data = generate_business_data()
X = data[['num_cows', 'milk_price', 'loan_amount', 'feed_cost', 'other_expenses']]
y = data[['monthly_profit', 'risk']]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
profit_model = RandomForestRegressor(n_estimators=100, random_state=42)
risk_model = RandomForestRegressor(n_estimators=100, random_state=42)
profit_model.fit(X_train, y_train['monthly_profit'])
risk_model.fit(X_train, y_train['risk'])

# Streamlit UI for Business Simulation
st.title("🌟 Digital Twin for Lakshmi's Dairy Business")

# Sidebar Inputs for the User (Lakshmi's Inputs)
st.sidebar.header("Business Inputs")
num_cows = st.sidebar.number_input("🐄 Number of Cows:", min_value=1, value=5, step=1)
milk_price = st.sidebar.number_input("🥛 Milk Price (₹/liter):", min_value=30, value=40, step=5)
loan_amount = st.sidebar.number_input("💳 Loan Amount (₹):", min_value=0, value=10000, step=1000)
feed_cost = st.sidebar.number_input("🌾 Feed Cost (₹):", min_value=1000, value=3000, step=500)
other_expenses = st.sidebar.number_input("📋 Other Expenses (₹):", min_value=1000, value=2000, step=500)

# Prepare input data for prediction
user_input = pd.DataFrame([[num_cows, milk_price, loan_amount, feed_cost, other_expenses]],
                          columns=['num_cows', 'milk_price', 'loan_amount', 'feed_cost', 'other_expenses'])

# Predict the outcome using the trained models
predicted_profit = profit_model.predict(user_input)[0]
predicted_risk = risk_model.predict(user_input)[0]

# Display the predicted monthly profit and risk status
st.subheader("📊 Business Outcome")
st.markdown(f"📈 *Predicted Monthly Profit*: ₹{predicted_profit:,.2f}")
if predicted_risk == 1:
    st.markdown("⚠ *High Risk*: Your expenses exceed your income. Consider reducing costs or increasing income.")
else:
    st.markdown("✅ *Low Risk*: Your business is in a good financial position.")

# Traffic Light System for Risk
if predicted_risk == 1:
    risk_status = "🔴 High Risk"
    color = "#F44336"
else:
    risk_status = "🟢 Low Risk"
    color = "#4CAF50"

st.markdown(f'<h3 style="color:{color};">{risk_status}</h3>', unsafe_allow_html=True)

# Risk Visualization (Traffic Light)
fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=(1 if predicted_risk == 1 else 0),
    title={'text': "Risk Status"},
    gauge={
        'axis': {'range': [0, 1]},
        'steps': [
            {'range': [0, 0.5], 'color': "#4CAF50"},
            {'range': [0.5, 1], 'color': "#F44336"}
        ],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': 0.5
        }
    }
))

st.plotly_chart(fig)

# AI Recommendations for Business Adjustments
st.subheader("💡 AI Recommendations")

if predicted_risk == 1:
    st.markdown("### 🛑 *Critical Risk*")
    st.write("""
    - *Reduce Feed Costs*: Look for cheaper suppliers or adjust feeding practices.
    - *Negotiate Loan Terms*: Try to get a lower interest rate or extend the loan period.
    - *Increase Milk Price*: Explore opportunities to raise milk prices or offer value-added products.
    - *Join a Cooperative*: To stabilize income and reduce risks.
    """)
else:
    st.markdown("### 👍 *Stable Business*")
    st.write("""
    - *Consider Investing in Growth*: Invest profits into expanding the number of cows or improving infrastructure.
    - *Diversify Income Streams*: Explore offering dairy products like cheese or yogurt.
    - *Build an Emergency Fund*: Put aside a portion of profits for future uncertainties.
    """)

# Visualize Profit and Risk Comparison
st.subheader("📈 Profit and Risk Analysis")
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(['Profit', 'Risk'], [predicted_profit, predicted_risk], color=['#4CAF50', '#F44336' if predicted_risk == 1 else '#4CAF50'])
ax.set_xlabel("Amount")
ax.set_title("Business Outcome: Profit vs Risk")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
st.pyplot(fig)

# Simulate adjustments (Dynamic Feedback)
st.subheader("🔄 Dynamic Feedback: Adjust Business Variables")
adjusted_cows = st.number_input("Adjusted Number of Cows:", min_value=1, value=num_cows, step=1)
adjusted_milk_price = st.number_input("Adjusted Milk Price (₹/liter):", min_value=30, value=milk_price, step=5)
adjusted_loan_amount = st.number_input("Adjusted Loan Amount (₹):", min_value=0, value=loan_amount, step=1000)

# Predict adjusted outcomes
adjusted_input = pd.DataFrame([[adjusted_cows, adjusted_milk_price, adjusted_loan_amount, feed_cost, other_expenses]],
                              columns=['num_cows', 'milk_price', 'loan_amount', 'feed_cost', 'other_expenses'])
adjusted_profit = profit_model.predict(adjusted_input)[0]
adjusted_risk = risk_model.predict(adjusted_input)[0]

st.markdown(f"📈 *Adjusted Monthly Profit*: ₹{adjusted_profit:,.2f}")
if adjusted_risk == 1:
    st.markdown("⚠ *High Risk*: Your expenses exceed your income. Consider reducing costs or increasing income.")
else:
    st.markdown("✅ *Low Risk*: Your business is in a good financial position.")

# Display dynamic risk visualization for adjustments
if adjusted_risk == 1:
    risk_status = "🔴 High Risk"
    color = "#F44336"
else:
    risk_status = "🟢 Low Risk"
    color = "#4CAF50"

st.markdown(f'<h3 style="color:{color};">{risk_status}</h3>', unsafe_allow_html=True)

# Risk Visualization for Adjustments
fig = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=(1 if adjusted_risk == 1 else 0),
    title={'text': "Adjusted Risk Status"},
    gauge={
        'axis': {'range': [0, 1]},
        'steps': [
            {'range': [0, 0.5], 'color': "#4CAF50"},
            {'range': [0.5, 1], 'color': "#F44336"}
        ],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': 0.5
        }
    }
))

st.plotly_chart(fig)
