import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to simulate financial growth
def simulate_growth(principal, annual_return, years, additional_contribution=0):
    growth = []
    current_balance = principal
    for year in range(1, years + 1):
        current_balance = (current_balance + additional_contribution) * (1 + annual_return / 100)
        growth.append((year, current_balance))
    return pd.DataFrame(growth, columns=["Year", "Balance"])

# Function to explain the AI model
@st.cache
def explain_model(principal, annual_return, years):
    explanation = f"The projection is based on a principal amount of ₹{principal}, an annual return of {annual_return}%, and a duration of {years} years. "
    explanation += "We assume compound growth with reinvestment of all returns."
    return explanation

# Streamlit UI setup
st.title("Financial Decision Simulation")
st.write("Explore how your financial decisions today could impact your future.")

# Input parameters
principal = st.number_input("Enter your initial investment/savings amount (₹):", min_value=0, value=5000, step=1000)
annual_return = st.slider("Select the expected annual return rate (%):", min_value=0, max_value=20, value=10, step=1)
years = st.slider("Select the investment duration (years):", min_value=1, max_value=30, value=5)
additional_contribution = st.number_input("Enter additional yearly contribution (₹):", min_value=0, value=0, step=1000)

# Run simulation
if st.button("Simulate"):
    results = simulate_growth(principal, annual_return, years, additional_contribution)

    # Display results
    st.subheader("Simulation Results")
    st.write(results)

    # Plot results
    fig, ax = plt.subplots()
    ax.plot(results["Year"], results["Balance"], marker="o", label="Projected Balance")
    ax.set_title("Financial Growth Over Time")
    ax.set_xlabel("Year")
    ax.set_ylabel("Balance (₹)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

    # Provide explainable AI insights
    st.subheader("How We Calculated This")
    explanation = explain_model(principal, annual_return, years)
    st.write(explanation)
