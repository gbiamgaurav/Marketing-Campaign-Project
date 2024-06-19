import gradio as gr
import pandas as pd
import joblib
import warnings
warnings.filterwarnings("ignore")

# Load the model and preprocessor
model = joblib.load("finalized_model/model.joblib")
preprocessor = joblib.load("finalized_model/preprocessor.joblib")

def predict_marketing_campaign(customer_id, age, gender, annual_income, credit_score, employed, marital_status, no_of_children):
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
        return result_text

    except Exception as e:
        return f"An error occurred: {str(e)}"

iface = gr.Interface(
    fn=predict_marketing_campaign,
    inputs=[
        gr.Slider(1, 56, step=1, label='ID', value=1),
        gr.Slider(25, 52, step=1, label='Age', value=25),
        gr.Radio(['Male', 'Female'], label='Gender', value='Male'),
        gr.Slider(1, 110000, step=1, label='Annual Income', value=50000),
        gr.Slider(600, 820, step=1, label='Credit Score', value=700),
        gr.Radio(['Yes', 'No'], label='Employed', value='Yes'),
        gr.Radio(['Married', 'Single'], label='Marital Status', value='Married'),
        gr.Slider(0, 3, step=1, label='Number of Children', value=0)
    ],
    outputs=gr.Textbox(label="Predicted Result"),
    title="Marketing Campaign Prediction",
    description="Please fill the details below for the Prediction"
)

if __name__ == "__main__":
    iface.launch(share=True)
