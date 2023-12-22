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
                st.header('Chest Pain')
                st.subheader('Chest Pain atau Nyeri Dada')
                st.write('Terindikasi Tidak sedang sakit jantung')
                litcp = ['Chest Pain Type 0', 'Chest Pain Type 1', 'Chest Pain Type 2', 'Chest Pain Type 3']
                literaturcp = st.selectbox('Pilih literatur Chest Pain yang ingin anda ketahui', litcp)
if literaturcp == 'Chest Pain Type 0':
                st.header('Chest Pain Type 0')
                st.subheader('Chest Pain Type 0atau Nyeri Dada Type Asimtomatik')
                st.write('Nyeri dada asimtomatik adalah nyeri dada yang tidak memiliki tanda atau gejala yang jelas, atau memiliki gejala yang tidak khas dari masalah jantung. Hal ini dapat disebabkan oleh berbagai kondisi, seperti iskemia miokard, serangan jantung diam, emboli paru, gagal jantung, atau gangguan kardiovaskular, muskuloskeletal, gastrointestinal, paru, atau kejiwaan lainnya. Nyeri dada tanpa gejala bisa sulit didiagnosis dan mungkin memerlukan tes lebih lanjut untuk menyingkirkan kondisi serius.')
else :
                st.write('pilih Tipikal Chest Pain di atas')
      
elif literatur == 'Trestbps':
                st.header('Rest Blood Pressure')
                st.subheader('Rest Blood Pressure atau Tekanan Darah')
                st.write('Tekanan Darah dalam penyakit jantung sangat mempengaruhi,karena semakin tinggi tekanan darah dalam tubuh semakin tinggi,maka akan menyebabkan Hipertensi.Hipertensi atau tekanan darah tinggi adalah peningkatan tekanan darah sistolik lebih dari 140 mmHg dan tekanan darah diastolik lebih dari 90 mmHg pada dua kali pengukuran dengan selang waktu lima menit dalam keadaan cukup istirahat/ tenang')

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
