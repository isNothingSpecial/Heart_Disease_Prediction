import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

## data

df = pd.read_csv('hungarian.csv')

df_proc = pd.read_csv('afterdrop.csv')

st.set_page_config(page_title="Homepage",layout="wide")
#side bar
st.sidebar.header("PENGOLAHAN DATA SAKIT JANTUNG DI HUNGARIA DENGAN MENGGUNAKAN ALGORITMA NAIVE BAYES DAN SVM")
#st.sidebar.image("1835901.jpg")

##layout

st.title(''' PENGOLAHAN DATA DETEKSI PENYAKIT JANTUNG DI HUNGARIA DENGAN ALGORITMA KNN ''')
st.write('Bagus Rahma Aulia Chandra - A11.2017.10295')
st.markdown('''   Dataset yang akan dianalisa adalah data pasien yang terindikasi penyakit jantung dan yang tidak terindikasi sakit jantung,ditinjau melalui,data-data seperti :
- CP (Constrictive Pericarditis)
- Trestbps (The Resting Blood Pressure)
- Chol (Cholesterol)
- FBS (Fasting Blood Sugar)
- Restecg Result (Resting Electrographic Result)
- Thalach (Maximum Heart Rated Achieved)
- Exang (Excercise Incduced Angina)
- Oldpeak 
 ''')

st.write(df)

st.markdown(''' Setelah dilakukan proses data cleaning dan data processing antara lain:  
            - Pengecheckan NULL Value
            - Menghapus kolom yang tidak diperlukan
            - Mengidentifikasi Target Class
            - Ditampilkan dalam bentuk diagram (Visualisasi Data
            - Pemrosesan dengan menggunakan algoritma yang tersedia
        
Berikut adalah contoh data yang sudah di Grouping berdasar Kolom Dates dibuang ''')

st.write(df_proc)
