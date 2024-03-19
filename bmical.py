# bmi_calculator_streamlit.py

import streamlit as st

def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    Formula: BMI = weight(kg) / (height(m) ** 2)
    """
    return weight / (height ** 2)

def interpret_bmi(bmi):
    """
    Interpret BMI value and return corresponding category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")

    # Get user input for weight and height
    weight = st.number_input("Enter your weight in kilograms", min_value=0.0, step=0.1)
    height = st.number_input("Enter your height in meters", min_value=0.0, step=0.01)

    if st.button("Calculate BMI"):
        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Interpret BMI
        category = interpret_bmi(bmi)

        # Display results
        st.write(f"Your BMI is: {bmi:.2f}")
        st.write(f"You are categorized as: {category}")

if __name__ == "__main__":
    main()
