import streamlit as st
import pandas as pd

df = pd.read_csv('afterdrop.csv')

st.title(''' DETEKSI PENYAKIT JANTUNG DI HUNGARIA ''')
st.write('Prediksi Data Baru')

lit = ['Cp', 'Trestbps', 'Chol', 'Fbs', 'Restecg', 'Thalach', 'Exang', 'Oldpeak']

literatur = st.selectbox('Pilih Literatur yang ingin anda ketahui', lit)

if literatur == 'Cp':
    st.header('Chest Pain')
    st.subheader('Chest Pain atau Nyeri Dada')
    st.write('Terindikasi Tidak sedang sakit jantung')
    litcp = ['Chest Pain Type 0', 'Chest Pain Type 1', 'Chest Pain Type 2', 'Chest Pain Type 3']
    literaturcp = st.selectbox('Pilih literatur Chest Pain yang ingin anda ketahui', litcp)
    if literaturcp == 'Chest Pain Type 0':
        st.header('Chest Pain Type 0')
        st.subheader('Chest Pain Type 0 atau Nyeri Dada Type Asimtomatik')
        st.write('Nyeri dada asimtomatik adalah nyeri dada yang tidak memiliki tanda atau gejala yang jelas, atau memiliki gejala yang tidak khas dari masalah jantung. Hal ini dapat disebabkan oleh berbagai kondisi, seperti iskemia miokard, serangan jantung diam, emboli paru, gagal jantung, atau gangguan kardiovaskular, muskuloskeletal, gastrointestinal, paru, atau kejiwaan lainnya. Nyeri dada tanpa gejala bisa sulit didiagnosis dan mungkin memerlukan tes lebih lanjut untuk menyingkirkan kondisi serius.')
    else:
        st.write('pilih Tipikal Chest Pain di atas')

elif literatur == 'Trestbps':
    st.header('Rest Blood Pressure')
    st.subheader('Rest Blood Pressure atau Tekanan Darah')
    st.write('Tekanan Darah dalam penyakit jantung sangat mempengaruhi, karena semakin tinggi tekanan darah dalam tubuh semakin tinggi, maka akan menyebabkan Hipertensi. Hipertensi atau tekanan darah tinggi adalah peningkatan tekanan darah sistolik lebih dari 140 mmHg dan tekanan darah diastolik lebih dari 90 mmHg pada dua kali pengukuran dengan selang waktu lima menit dalam keadaan cukup istirahat/tenang')

elif literatur == 'Chol':
    st.header('Cholesterol')
    st.subheader('Chol atau Kolesterol')
    # Add your content for cholesterol...

elif literatur == 'Fbs':
    st.header('Fasting Blood Sugar')
    st.subheader('Fbs atau Gula Darah Puasa')
    # Add your content for fasting blood sugar...

elif literatur == 'Restecg':
    st.header('Resting Electrocardiographic Results')
    st.subheader('Restecg atau Hasil Elektrokardiografi Istirahat')
    # Add your content for resting electrocardiographic results...

elif literatur == 'Thalach':
    st.header('Maximum Heart Rate Achieved')
    st.subheader('Thalach atau Denyut Jantung Maksimum yang Dicapai')
    # Add your content for maximum heart rate achieved...

elif literatur == 'Exang':
    st.header('Exercise Induced Angina')
    st.subheader('Exang atau Angina yang Dipicu Olahraga')
    # Add your content for exercise induced angina...

elif literatur == 'Oldpeak':
    st.header('ST Depression Induced by Exercise')
    st.subheader('Oldpeak atau Depresi ST yang Dipicu oleh Olahraga')
    # Add your content for ST depression induced by exercise...

else:
    st.subheader('Pilih literatur yang ingim anda ketahui ')
