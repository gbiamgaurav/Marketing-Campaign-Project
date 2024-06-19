import streamlit as st
import pandas as pd
import joblib
import warnings
warnings.filterwarnings("ignore")

# Load the model and preprocessor
model = joblib.load("finalized_model/model.joblib")
preprocessor = joblib.load("finalized_model/preprocessor.joblib")

def main():
    st.title('Marketing Campaign Prediction')
    st.markdown("Please fill the details below for the Prediction")

    # Create a form for input
    with st.form("Marketing Campaign Prediction"):
        customer_id = st.slider('ID', 1, 56, step=1, value=1)
        age = st.slider('Age', 25, 52, step=1, value=25)
        gender = st.selectbox('Gender', ['Male', 'Female'])
        annual_income = st.slider('Annual Income', 1, 110000, step=1, value=50000)
        credit_score = st.slider('Credit Score', 600, 820, step=1, value=700)
        employed = st.selectbox('Employed', ['Yes', 'No'])
        marital_status = st.selectbox('Marital Status', ['Married', 'Single'])
        no_of_children  = st.slider('Number of Children', 0, 3, step=1, value=0)

        submit_button = st.form_submit_button("Submit")

    if submit_button:
        try:
            input_data = pd.DataFrame({
                'customer_id': [customer_id],
                'age': [age],
                'gender': [gender],
                'annual_income': [annual_income],
                'credit_score': [credit_score],
                'employed': [employed],
                'marital_status': [marital_status],
                'no_of_children': [no_of_children]
            })

            # Preprocess the input data
            X_transformed = preprocessor.transform(input_data)

            # Make the prediction
            prediction = model.predict(X_transformed)[0]

            result_text = "Customer will respond" if prediction == 0 else "Customer will not respond"
            st.write(f"Predicted Result: {result_text}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
