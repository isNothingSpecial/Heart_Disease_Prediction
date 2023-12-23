import streamlit as st
import pandas as pd

df = pd.read_csv('afterdrop.csv')

st.title('''LITERATUR ISTILAH-ISTILAH DALAM DATA DETEKSI PENYAKIT JANTUNG DI HUNGARIA''')
st.write('literatur singkat terkait istilah-istilah yang dipakai dalam data ini')

lit = ['Cp', 'Trestbps', 'Chol', 'Fbs', 'Restecg', 'Thalach', 'Exang', 'Oldpeak']

literatur = st.selectbox('Pilih Literatur yang ingin anda ketahui', lit)

if literatur == 'Cp':
    st.header('Chest Pain')
    st.subheader('Chest Pain atau Nyeri Dada')
    litcp = ['Chest Pain Type 1', 'Chest Pain Type 2', 'Chest Pain Type 3', 'Chest Pain Type 4']
    literaturcp = st.selectbox('Pilih literatur Chest Pain yang ingin anda ketahui : ', litcp)
    
    if literaturcp == 'Chest Pain Type 1':
        st.header('Chest Pain Type 1')
        st.subheader('Chest Pain Type 1 atau Nyeri Dada Type Asimtomatik')
        st.write('Nyeri dada asimtomatik adalah nyeri dada yang tidak memiliki tanda atau gejala yang jelas, atau memiliki gejala yang tidak khas dari masalah jantung. Hal ini dapat disebabkan oleh berbagai kondisi, seperti iskemia miokard, serangan jantung diam, emboli paru, gagal jantung, atau gangguan kardiovaskular, muskuloskeletal, gastrointestinal, paru, atau kejiwaan lainnya. Nyeri dada tanpa gejala bisa sulit didiagnosis dan mungkin memerlukan tes lebih lanjut untuk menyingkirkan kondisi serius.')
    
    elif literaturcp == 'Chest Pain Type 2':
        st.header('Chest Pain Type 2')
        st.subheader('Chest Pain Type 2 atau Nyeri Dada Tipe Atipikal Angina')
        st.write('Angina atipikal mengacu pada nyeri dada atau ketidaknyamanan yang tidak memiliki karakteristik khas angina klasik. Ini mungkin hadir dengan gejala yang berbeda atau mungkin tidak mengikuti pola nyeri dada yang biasa terkait dengan masalah jantung.')
        
    elif literaturcp == 'Chest Pain Type 3':
        st.header('Chest Pain Type 3')
        st.subheader('Chest Pain Type 3 atau Nyeri Dada Tipe non tipikal Angina')
        st.write('Angina non-tipikal mengacu pada nyeri dada yang tidak berasal dari jantung dan kadang-kadang tidak mewakili gejala iskemik angina pada kasus penyakit jantung yang khas.')
    
    elif literaturcp == 'Chest Pain Type 4':
        st.header('Chest Pain Type 4')
        st.subheader('Chest Pain Type 4 atau Nyeri Dada Tipe tipikal Angina')
        st.write('Angina khas, juga dikenal sebagai angina stabil, adalah nyeri dada atau ketidaknyamanan yang terjadi ketika otot jantung tidak menerima aliran darah yang cukup, biasanya selama aktivitas fisik atau stres. Ini ditandai dengan pola yang dapat diprediksi, sering dipicu oleh kegiatan seperti olahraga atau stres emosional, dan cenderung mereda dengan istirahat atau obat-obatan.')
  
    else:
        st.write('pilih Tipikal Chest Pain di atas')

elif literatur == 'Trestbps':
    st.header('Rest Blood Pressure')
    st.subheader('Rest Blood Pressure atau Tekanan Darah')
    st.write('Tekanan Darah dalam penyakit jantung sangat mempengaruhi, karena semakin tinggi tekanan darah dalam tubuh semakin tinggi, maka akan menyebabkan Hipertensi. Hipertensi atau tekanan darah tinggi adalah peningkatan tekanan darah sistolik lebih dari 140 mmHg dan tekanan darah diastolik lebih dari 90 mmHg pada dua kali pengukuran dengan selang waktu lima menit dalam keadaan cukup istirahat/tenang')

elif literatur == 'Chol':
    st.header('Cholesterol')
    st.subheader('Chol atau Kolesterol,adalah Kadar Kolesterol yang terkandung dalam tubuh,dimana kadar kolesterol makin tinggi,semakin tinggi pula risiko penyakit jantung')
    # Add your content for cholesterol...

elif literatur == 'Fbs':
    st.header('Fasting Blood Sugar')
    st.subheader('Fbs atau Gula Darah apabila Gula Darah lebih dari 120 mg/dl maka bisa dikategorikan gula darah dalam tubuh tergolong tinggi,dan semakin tinggi gula darah dalam tubuh,maka risiko terkena penyakit jantung makin besar')
    # Add your content for fasting blood sugar...

elif literatur == 'Restecg':
    st.header('Resting Electrocardiographic Results')
    st.subheader('Restecg atau Hasil Elektrokardiografi')
    # Add your content for resting electrocardiographic results...

elif literatur == 'Thalach':
    st.header('Maximum Heart Rate Achieved')
    st.subheader('Thalach atau Denyut Jantung Maksimum yang Dicapai')
    # Add your content for maximum heart rate achieved...

elif literatur == 'Exang':
    st.header('Exercise Induced Angina')
    st.subheader('Exang atau Angina yang Dipicu oleh Ecercise atau pengujian')
    # Add your content for exercise induced angina...

elif literatur == 'Oldpeak':
    st.header('ST Depression Induced by Exercise')
    st.subheader('Oldpeak atau Depresi ST yang Dipicu oleh hasil dari Exercise')
    # Add your content for ST depression induced by exercise...

else:
    st.subheader('Pilih literatur yang ingin anda ketahui ')


# The rest of your code remains unchanged for other conditions...
