import streamlit as st
import joblib

model = joblib.load("Models/logistic_fake_news_model.pkl")
vectorizer = joblib.load("vectorizers/tfidf_vectorizer.pkl")

st.title("Fake News Detection")

news = st.text_input("Enter news headline")

if st.button("Check"):

    news_vector = vectorizer.transform([news])

    prediction = model.predict(news_vector)[0]

    if prediction == 1:
        st.success("True News")
    else:
        st.error("Fake News")