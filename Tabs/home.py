"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Welcome to Parkinson’s disease predictor!")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
        """<div style="text-align: justify; font-size: 18px; line-height: 1.6;">
            <p>
            Parkinson's Disease Predictor
            </p>
            <p>
             This is a simple and easy-to-use tool that can help you understand if you or someone you know may have Parkinson’s a simple Web App developed in Python using Streamlit library that predicts whether a person has Parkinson’s disease or not based on symptoms and other parameters. 
             </p>
             <p>
            The model uses machine learning algorithms, specifically a neural network model,
            aims to predict whether a person is at risk of Parkinson's disease or has the disease at a minor or acute level. It analyzes various feature values using the Random Forest Classifier, providing insights into potential pathological scenarios.
            </p>
            <p>
                Parkinson's disease is a progressive disorder that affects the nervous system and the parts of the body controlled by the nerves. Symptoms start slowly. The first symptom may be a barely noticeable tremor in just one hand. Tremors are common, but the disorder may also cause stiffness or slowing of movement.
            </p>
            <p>
            In the early stages of Parkinson's disease, your face may show little or no expression. Your arms may not swing when you walk. Your speech may become soft or slurred. Parkinson's disease symptoms worsen as your condition progresses over time.
            </p>
            <p>
            Although Parkinson's disease can't be cured, medications might significantly improve your symptoms. Occasionally, your health care provider may suggest surgery to regulate certain regions of your brain and improve your symptoms.
            </p>
        </div>
        """, unsafe_allow_html=True)