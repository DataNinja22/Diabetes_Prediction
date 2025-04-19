import streamlit as st
import pandas as pd
import pickle

# Loading the trained model
with open('Models/Diabetes.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Loading the scaler
with open('Models/standardScalar.pkl', 'rb') as scaler_file: 
    scaler = pickle.load(scaler_file)

st.set_page_config(page_title='Diabetes Prediction App', page_icon='💉', layout='centered')

st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>Diabetes Prediction App</h1>", unsafe_allow_html=True)


st.image('https://miro.medium.com/v2/resize:fit:1400/1*3xBqh5Df8qJj98VNi2GS0w.jpeg', use_column_width=True, caption='Take control of your health')

# Using a sidebar
st.sidebar.title("Enter Your Details:")

pregnancies = st.sidebar.number_input(
    'Pregnancies', 
    min_value=0, 
    max_value=20, 
    value=0, 
    step=1,
    help='Number of times pregnant (0 to 20)'
)

glucose = st.sidebar.number_input(
    'Glucose Level (mg/dL)', 
    min_value=0, 
    max_value=200, 
    value=0, 
    step=1,
    help='Plasma glucose concentration (0 to 200 mg/dL)'
)

blood_pressure = st.sidebar.number_input(
    'Blood Pressure (mm Hg)', 
    min_value=0, 
    max_value=150, 
    value=0, 
    step=1,
    help='Diastolic blood pressure (0 to 150 mm Hg)'
)

skin_thickness = st.sidebar.number_input(
    'Skin Thickness (mm)', 
    min_value=0, 
    max_value=100, 
    value=0, 
    step=1,
    help='Triceps skinfold thickness (0 to 100 mm)'
)

insulin = st.sidebar.number_input(
    'Insulin Level (mu U/ml)', 
    min_value=0, 
    max_value=900, 
    value=0, 
    step=1,
    help='2-Hour serum insulin (0 to 900 mu U/ml)'
)

bmi = st.sidebar.number_input(
    'BMI', 
    min_value=0.0, 
    max_value=70.0, 
    value=0.0, 
    step=0.1,
    help='Body mass index (0 to 70 kg/m²)'
)

dpf = st.sidebar.number_input(
    'Diabetes Pedigree Function', 
    min_value=0.0, 
    max_value=2.5, 
    value=0.0, 
    step=0.01,
    help='Diabetes pedigree function (0.0 to 2.5)'
)

age = st.sidebar.number_input(
    'Age', 
    min_value=1, 
    max_value=120, 
    value=1, 
    step=1,
    help='Age in years (1 to 120)'
)

# Adding a predict button
if st.sidebar.button('Predict'):
    # Creating a DataFrame for the input
    input_data = pd.DataFrame({
        'Pregnancies': [pregnancies],
        'Glucose': [glucose],
        'BloodPressure': [blood_pressure],
        'SkinThickness': [skin_thickness],
        'Insulin': [insulin],
        'BMI': [bmi],
        'DiabetesPedigreeFunction': [dpf],
        'Age': [age]
    })

    # Scaling the input data using the loaded scaler
    scaled_input = scaler.transform(input_data)

    # Making the prediction
    prediction = model.predict(scaled_input)[0]

    # Display the result
    if prediction == 1:
        st.markdown("<h2 style='text-align: center; color: #FF4B4B;'>⚠️ The model predicts that you have diabetes.</h2>", unsafe_allow_html=True)
    else:
        st.markdown("<h2 style='text-align: center; color: #4CAF50;'>✅ The model predicts that you do not have diabetes.</h2>", unsafe_allow_html=True)

st.markdown("""
### About This App
This application uses a machine learning model trained on the Pima Indians Diabetes Database to predict whether an individual has diabetes based on their medical information. The model was trained using the following features:

- **Pregnancies**: Number of times pregnant
- **Glucose**: Plasma glucose concentration a 2 hours in an oral glucose tolerance test (mg/dL)
- **BloodPressure**: Diastolic blood pressure (mm Hg)
- **SkinThickness**: Triceps skinfold thickness (mm)
- **Insulin**: 2-Hour serum insulin (mu U/ml)
- **BMI**: Body mass index (weight in kg/(height in m)^2)
- **Diabetes Pedigree Function**: Diabetes pedigree function (a function which scores likelihood of diabetes based on family history)
- **Age**: Age in years

""")

