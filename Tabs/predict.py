"""This module contains data about the prediction page"""

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# Import necessary functions from web_functions
from web_functions import predict

# Hide Streamlit style elements
hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

def app(df, X, y):
    """This function creates the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of Parkinson's disease.
            </p>
        """, unsafe_allow_html=True)

    with st.expander("View attribute details"):
        st.markdown("""
        - **MDVP:Fo(Hz)** - Average vocal fundamental frequency
        - **MDVP:Fhi(Hz)** - Maximum vocal fundamental frequency
        - **MDVP:Flo(Hz)** - Minimum vocal fundamental frequency
        - **Jitter & Shimmer metrics** - Various measures of frequency and amplitude variation
        - **NHR, HNR** - Measures of noise to tonal components in the voice
        - **RPDE, D2, DFA** - Nonlinear dynamical complexity measures
        - **PPE** - Nonlinear measure of fundamental frequency variation
        """)

    # Take feature input from the user
    st.subheader("Enter Values:")

    # Replacing sliders with number input boxes for user input
    avff = st.number_input("Average vocal fundamental frequency", int(df["AVFF"].min()), int(df["AVFF"].max()))
    mavff = st.number_input("Maximum vocal fundamental frequency", int(df["MAVFF"].min()), int(df["MAVFF"].max()))
    mivff = st.number_input("Minimum vocal fundamental frequency", int(df["MIVFF"].min()), int(df["MIVFF"].max()))
    jitddp = st.number_input("Jitter:DDP", float(df["Jitter:DDP"].min()), float(df["Jitter:DDP"].max()))
    mdvpjit = st.number_input("MDVP:Jitter(%)", float(df["MDVP:Jitter(%)"].min()), float(df["MDVP:Jitter(%)"].max()))
    mdvprap = st.number_input("MDVP-RAP", float(df["MDVP:RAP"].min()), float(df["MDVP:RAP"].max()))
    mdvpapq = st.number_input("MDVP-APQ", float(df["MDVP:APQ"].min()), float(df["MDVP:APQ"].max()))
    mdvpppq = st.number_input("MDVP-PPQ", float(df["MDVP:PPQ"].min()), float(df["MDVP:PPQ"].max()))
    mdvpshim = st.number_input("MDVP-Shimmer", float(df["MDVP:Shimmer"].min()), float(df["MDVP:Shimmer"].max()))
    shimdda = st.number_input("Shimmer-DDA", float(df["Shimmer:DDA"].min()), float(df["Shimmer:DDA"].max()))
    shimapq3 = st.number_input("Shimmer-APQ3", float(df["Shimmer:APQ3"].min()), float(df["Shimmer:APQ3"].max()))
    shimapq5 = st.number_input("Shimmer-APQ5", float(df["Shimmer:APQ5"].min()), float(df["Shimmer:APQ5"].max()))
    nhr = st.number_input("NHR", float(df["NHR"].min()), float(df["NHR"].max()))
    hnr = st.number_input("HNR", float(df["HNR"].min()), float(df["HNR"].max()))
    rpde = st.number_input("RPDE", float(df["RPDE"].min()), float(df["RPDE"].max()))
    dfa = st.number_input("DFA", float(df["DFA"].min()), float(df["DFA"].max()))
    d2 = st.number_input("D2", float(df["D2"].min()), float(df["D2"].max()))
    ppe = st.number_input("PPE", float(df["PPE"].min()), float(df["PPE"].max()))

    # Store features in a list
    features = [avff, mavff, mivff, jitddp, mdvpjit, mdvprap, mdvpapq, mdvpppq, mdvpshim, shimdda, shimapq3, shimapq5, nhr, hnr, rpde, dfa, d2, ppe]

    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns = ["AVFF", "MAVFF", "MIVFF", "Jitter:DDP", "MDVP:Jitter(%)", "MDVP:RAP", "MDVP:APQ", "MDVP:PPQ", "MDVP:Shimmer", 
                   "Shimmer:DDA", "Shimmer:APQ3", "Shimmer:APQ5", "NHR", "HNR", "RPDE", "DFA", "D2", "PPE"]
    st.dataframe(df3)

    st.sidebar.info("The parameters contributing most to Parkinson's disease detection are D2 and PPE.")

    # Prediction button
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)

        # Display the prediction result
        if prediction == 1:
            st.error("The person either has Parkinson's disease or is at risk.")
            if (ppe > 0.13 and ppe < 0.25 or d2 > 2.0 and d2 < 3.0):
                st.warning("There is a risk of Early-onset Parkinson's Disease.")
            elif (ppe > 0.26 and ppe < 0.36 or d2 > 3.0):
                st.warning("There is a risk of Idiopathic Parkinson's Disease. There may also be a risk of Schizophrenia.")
            elif (ppe > 0.37 and avff > 200):
                st.warning("There is a risk of nervous miscoordination and hard grip. Encourage gripping exercises.")
            elif (ppe > 0.42 and mavff > 350):
                st.warning("There is a risk of Acute Parkinson's Disease.")
            elif (mdvpshim + shimdda + shimapq3 + shimapq5 > 0.20 and d2 > 2):
                st.warning("There may be slight tremor in the fingers.")
        else:
            st.success("The person is safe from Parkinson's disease.")
            if avff > 240:
                st.warning("However, there is a risk of vocal trembling or Secondary PD.")

        # Display model accuracy
        st.sidebar.write(f"The model used has an accuracy of {round(score * 100, 2)}%.")
