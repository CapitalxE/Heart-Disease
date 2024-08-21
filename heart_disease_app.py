import streamlit as st
import pandas as pd
import pickle

loaded_model=pickle.load(open("train_model.sav",'rb'))

# Create a Streamlit app
def main():
    st.title("Heart Disease Prediction App")
    st.write("Enter the details below to predict the likelihood of heart disease:")

    # Input form
    age = st.number_input("Age", min_value=1, max_value=120)
    sex = st.selectbox("Sex", ["Male", "Female"])
    chest_pain_type = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY","TA"])
    resting_bp = st.number_input("Resting Blood Pressure", min_value=80, max_value=200)
    cholesterol = st.number_input("Cholesterol", min_value=80, max_value=603)
    fasting_bs = st.selectbox("Fasting Blood Sugar", ["Normal", "High"])
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST","LVH"])
    max_hr = st.number_input("Maximum Heart Rate", min_value=50, max_value=220)
    exercise_angina = st.radio("Exercise-Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, value=0.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat","Down"])
    
    # Convert categorical features to numerical
    sex_mapping = {"Male": 1, "Female": 0}
    chest_pain_mapping = {"ATA": 1, "NAP": 2, "ASY": 0,"TA":3}
    fasting_bs_mapping = {"Normal": 0, "High": 1}
    resting_ecg_mapping = {"Normal": 1, "ST": 2,"LVH":0}
    exercise_angina_mapping = {"No": 0, "Yes": 1}
    st_slope_mapping= {'Up':2,'Flat':1,"Down":0}
    
    
    sex = sex_mapping[sex]
    chest_pain_type = chest_pain_mapping[chest_pain_type]
    fasting_bs = fasting_bs_mapping[fasting_bs]
    resting_ecg = resting_ecg_mapping[resting_ecg]
    exercise_angina = exercise_angina_mapping[exercise_angina]
    st_slope= st_slope_mapping[st_slope]
    
    # Create a DataFrame with user input
    user_data = pd.DataFrame({
        "Age": [age],
        "Sex": [sex],
        "ChestPainType": [chest_pain_type],
        "RestingBP": [resting_bp],
        "Cholesterol": [cholesterol],
        "FastingBS": [fasting_bs],
        "RestingECG": [resting_ecg],
        "MaxHR": [max_hr],
        "ExerciseAngina": [exercise_angina],
        "Oldpeak": [oldpeak],
        "ST_Slope": [st_slope]
    })

    if st.button("Predict"):
        # Assuming you have a trained model called 'loaded_model'
        # Replace this with your actual prediction code
        prediction = loaded_model.predict(user_data)

        # Display prediction result
        if prediction[0] == 0:
            st.success("The predicted result: No heart disease")
        else:
            st.error("The predicted result: Heart disease detected")

if __name__ == "__main__":
    main()
