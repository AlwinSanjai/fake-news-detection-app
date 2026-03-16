📰 Fake News Detection Web App

A machine learning web application that predicts whether a news headline is Fake or True using Natural Language Processing (NLP).

This project trains multiple machine learning models and deploys the best-performing model in a web application built with Streamlit.

---

🚀 Project Overview

The spread of misinformation on the internet and social media has become a serious problem. Fake news can influence public opinion and create confusion.

This project aims to automatically detect fake news headlines using machine learning techniques.

The system analyzes a news headline and predicts whether it is Fake or True.

---

🧠 Machine Learning Models Trained

The following models were trained and evaluated:

- Logistic Regression
- Support Vector Machine (SVM)
- Naive Bayes
- Random Forest
- BERT (Deep Learning Model)

After comparing performance, Logistic Regression was selected for deployment because it provides:

- High accuracy
- Very fast predictions
- Low memory usage
- Efficient web deployment

---

🛠 Technologies Used

- Python
- Scikit-learn
- Pandas
- NumPy
- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Streamlit (for web application)

---

📂 Project Structure

fake-news-detection
│
├── app/
│   └── app.py
│
├── Models/
│   └── logistic_fake_news_model.pkl
│
├── vectorizers/
│   └── tfidf_vectorizer.pkl
│
├── Notebooks/
│   ├── logistic_regression.ipynb
│   ├── SVM.ipynb
│   ├── Naive_Bayes.ipynb
│   ├── Random_forest.ipynb
│   └── BERT.ipynb
│
├── requirements.txt
└── README.md

---

⚙️ How to Run the App

Install dependencies

pip install -r requirements.txt

Run the Streamlit application

streamlit run app/app.py

The application will open in your browser.

---

🌐 Web Application

Users can enter a news headline in the text box and the system will predict:

- ✅ True News
- ❌ Fake News

The prediction is generated using a trained Logistic Regression model with TF-IDF vectorization.

---

📊 Dataset

The dataset used in this project was collected from publicly available fake news datasets such as:

- Fake and Real News Dataset
- GossipCop Dataset
- Politifact Dataset

Large datasets are not included in this repository due to GitHub file size limits.

---

👨‍💻 Author

Alwin Sanjai

Machine Learning / Data Science Project
