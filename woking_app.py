import gradio as gr
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(SeniorCitizen, tenure, Contract_Month_to_month, Contract_One_year,
        Contract_Two_year, PaymentMethod_Bank_transfer_automatic, PaymentMethod_Credit_card_automatic,
        PaymentMethod_Electronic_check, PaymentMethod_Mailed_check,
        TechSupport_No, TechSupport_No_internet_service, TechSupport_Yes,
        InternetService_DSL, InternetService_Fiber_optic, InternetService_No,
        OnlineSecurity_No, OnlineSecurity_No_internet_service, OnlineSecurity_Yes,
        OnlineBackup_No, OnlineBackup_No_internet_service, OnlineBackup_Yes,
        PaperlessBilling_No, PaperlessBilling_Yes, StreamingTV_No,
        StreamingTV_No_internet_service, StreamingTV_Yes, StreamingMovies_No,
        StreamingMovies_No_internet_service, StreamingMovies_Yes, gender_Female,
        gender_Male, Partner_No, Partner_Yes, Dependents_No, Dependents_Yes,
        PhoneService_No, PhoneService_Yes, MultipleLines_No, 
        MultipleLines_No_phone_service, MultipleLines_Yes,
        DeviceProtection_No, DeviceProtection_No_internet_service, DeviceProtection_Yes):
    prediction = model.predict([[SeniorCitizen, tenure, Contract_Month_to_month, Contract_One_year,
        Contract_Two_year, PaymentMethod_Bank_transfer_automatic, PaymentMethod_Credit_card_automatic,
        PaymentMethod_Electronic_check, PaymentMethod_Mailed_check,
        TechSupport_No, TechSupport_No_internet_service, TechSupport_Yes,
        InternetService_DSL, InternetService_Fiber_optic, InternetService_No,
        OnlineSecurity_No, OnlineSecurity_No_internet_service, OnlineSecurity_Yes,
        OnlineBackup_No, OnlineBackup_No_internet_service, OnlineBackup_Yes,
        PaperlessBilling_No, PaperlessBilling_Yes, StreamingTV_No,
        StreamingTV_No_internet_service, StreamingTV_Yes, StreamingMovies_No,
        StreamingMovies_No_internet_service, StreamingMovies_Yes, gender_Female,
        gender_Male, Partner_No, Partner_Yes, Dependents_No, Dependents_Yes,
        PhoneService_No, PhoneService_Yes, MultipleLines_No, 
        MultipleLines_No_phone_service, MultipleLines_Yes,
        DeviceProtection_No, DeviceProtection_No_internet_service, DeviceProtection_Yes]])
    
    # Return the prediction as a string
    return 'Churn' if prediction == 1 else 'No churn'

inputs = [
    gr.inputs.Number(label='SeniorCitizen (0 or 1)'),
    gr.inputs.Number(label='tenure (in months)'),
    gr.inputs.Slider(minimum=0, maximum=1, label='Contract: Month-to-month'),
    gr.inputs.Slider(minimum=0, maximum=1, label='Contract: One year'),
    gr.inputs.Slider(minimum=0, maximum=1, label='Contract: Two year'),
    gr.inputs.Slider(minimum=0, maximum=1, label='PaymentMethod: Bank transfer (automatic)'),
    gr.inputs.Slider(minimum=0, maximum=1, label='PaymentMethod: Credit card (automatic)'),
    gr.inputs.Slider(minimum=0, maximum=1, label='PaymentMethod: Electronic check'),
    gr.inputs.Slider(minimum=0, maximum=1, label='PaymentMethod: Mailed check'),
    gr.inputs.Slider(minimum=0, maximum=1, label='TechSupport: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='TechSupport: No internet service'),
    gr.inputs.Slider(minimum=0, maximum=1, label='TechSupport: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='InternetService: DSL'),
    gr.inputs.Slider(minimum=0, maximum=1, label='InternetService: Fiber optic'),
    gr.inputs.Slider(minimum=0, maximum=1, label='InternetService: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='OnlineSecurity: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='OnlineSecurity: No internet service'),
    gr.inputs.Slider(minimum=0, maximum=1, label='OnlineSecurity: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='OnlineBackup: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='OnlineBackup: No Internet Service'),
    gr.inputs.Slider(minimum=0, maximum=1, label='OnlineBackup: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='PaperlessBilling: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='PaperlessBilling: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='StreamingTV: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='StreamingTV: No Internet Service'),
    gr.inputs.Slider(minimum=0, maximum=1, label='StreamingTV: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='StreamingMovies: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='StreamingMovies: No Internet Service'),
    gr.inputs.Slider(minimum=0, maximum=1, label='StreamingMovies: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='Female'),
    gr.inputs.Slider(minimum=0, maximum=1, label='Male'),
    gr.inputs.Slider(minimum=0, maximum=1, label='Partner: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='Partner: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='Dependents: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='Dependents: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='PhoneService: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='PhoneService: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='MultipleLines: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='MultipleLines: No Phone Service'),
    gr.inputs.Slider(minimum=0, maximum=1, label='MultipleLines: Yes'),
    gr.inputs.Slider(minimum=0, maximum=1, label='DeviceProtection: No'),
    gr.inputs.Slider(minimum=0, maximum=1, label='DeviceProtection: No Internet Service'),
    gr.inputs.Slider(minimum=0, maximum=1, label='DeviceProtection: Yes')]

    #gr.inputs.Slider(minimum=0, maximum=1, label='InternetService: No

outputs = gr.outputs.Textbox()

gr.Interface(fn=predict, inputs=inputs, outputs=outputs, title='Churn Prediction App',
             description='Enter customer data to predict churn').launch()