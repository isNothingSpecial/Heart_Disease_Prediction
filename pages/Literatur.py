import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('afterdrop.csv')

st.title(''' DETEKSI PENYAKIT JANTUNG DI HUNGARIA ''')
st.write('Prediksi Data Baru')

lit = ['Cp', 'Trestbps', 'Chol', 'Fbs','Restecg','Thalach','Exang','Oldpeak']

literatur = st.selectbox('Pilih Literatur yang ingin anda ketahui', lit)
        
        if literatur == 'Cp':
                st.header('')
                st.subheader('Prediction : ')
                st.write('Terindikasi Tidak sedang sakit jantung')

        elif literatur == 'Trestbps':
                st.header('')
                st.subheader('Prediction : ')
                st.write('Terindikasi Tidak sedang sakit jantung')

        elif literatur == 'Chol':
                st.header('')
                st.subheader('Prediction : ')
                st.write('Terindikasi Tidak sedang sakit jantung')

        elif algorithm == 'Fbs':
                st.header('')
                st.subheader('Prediction : ')
                st.write('Terindikasi Tidak sedang sakit jantung')

        elif algorithm == 'Restecg':
                st.header('')
                st.subheader('Prediction : ')
                st.write('Terindikasi Tidak sedang sakit jantung')

        elif literatur == 'Thalach':
                st.header('')
                st.subheader('Prediction : ')
                st.write('Terindikasi Tidak sedang sakit jantung')

        elif algorithm == 'Exang':
                st.header('')
                st.subheader('Prediction : ')
                st.write('Terindikasi Tidak sedang sakit jantung')

        elif algorithm == 'Oldpeak':
                st.header('')
                st.subheader('Prediction : ')
                st.write('Terindikasi Tidak sedang sakit jantung')
        # Continue the same indentation pattern for the other algorithms...

else:
        st.subheader('Prediction : ')
