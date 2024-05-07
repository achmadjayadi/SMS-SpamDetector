import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

#LoadModel
model_fraud = pickle.load(open('penipuan_model.sav','rb'))

TfidfVectorizer = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(pickle.load(open("feature-tfidf.sav", "rb"))))

#Title Halaman
st.title('Prediksi SMS Penipuan')

clean_teks = st.text_input('Masukan Teks SMS')

fraud_detection = ''

if st.button('Hasil Deteksi'):
    predict_fraud = model_fraud.predict(loaded_vec.fit_transform([clean_teks]))  # Perbaikan penulisan predict
    
    if predict_fraud == 0:  # Perbaikan penulisan predict_fraud
        fraud_detection = 'SMS Normal'
    elif predict_fraud == 1:
        fraud_detection = 'SMS Penipuan'
    else:
        fraud_detection = 'SMS Promo'
st.success(fraud_detection)
