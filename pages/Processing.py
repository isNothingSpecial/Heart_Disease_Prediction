import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.naive_bayes import GaussianNB,BernoulliNB, MultinomialNB, ComplementNB
from sklearn import svm

st.sidebar.write('Bagus Rahma Aulia Chandra - A11.2017.10295')

df = pd.read_csv('afterdrop.csv')

st.title(''' DETEKSI PENYAKIT JANTUNG DI HUNGARIA ''')
st.write('Prediksi Data Baru')

alg = ['Gaussian', 'Multinomial', 'Bernoulli', 'Complementary','SVM']

input_age = st.number_input ("age")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_sex = st.number_input ("sex")
st.caption('Input 0 for Male,1 for Female')
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_cp = st.number_input ("Cp")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_trestbps = st.number_input ("Trestbps")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_chol = st.number_input ("Chol")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_fbs = st.number_input ("Fbs")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_restecg = st.number_input ("Restecg")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_thalach = st.number_input ("Thalach")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_exang = st.number_input ("Exang")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

input_oldpeak = st.number_input ("Oldpeak")
#min_value=df('precipation').min()
#max_value=df('precipation').max()

algorithm = st.selectbox('Pilih Algoritma', alg)

result = "-"

X = df.iloc[:, :-1]
y = df['num']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

Predict = st.button("Predict")
        
if Predict:
    if input_age != str(0.00) and input_sex != str(0.00) and input_cp != str(0.00) and input_trestbps != str(0.00) and input_chol != str(0.00) and input_fbs != str(0.00) and input_restecg != str(0.00) and input_thalach != str(0.00) and input_exang != str(0.00) and input_oldpeak != str(0.00):
        age = float(input_age)
        sex = float(input_sex)
        cp = float(input_cp)
        trestbps = float(input_trestbps)
        chol = float(input_chol)
        fbs = float(input_fbs)
        restecg = float(input_restecg)
        thalach = float(input_thalach)
        exang = float(input_exang)
        oldpeak = float(input_oldpeak)

        if algorithm == 'Gaussian':
            nb = GaussianNB()
            nb.fit(X_train, y_train)
            nb_predict = nb.predict(X_test)
            nb_acc_score = accuracy_score(y_test, nb_predict)
            precision = precision_score(y_test, nb_predict, average='weighted')
            recall = recall_score(y_test, nb_predict, average='weighted')
            f1 = f1_score(y_test, nb_predict, average='weighted')   
            prediction = nb.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak]])[0]
            result = str(prediction)
            
            if result == '0':
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Tidak sedang sakit jantung')
                st.caption (f"Tingkat Akurasi : {nb_acc_score}")
                st.caption (f"Tingkat Presisi : {precision}")
                st.caption (f"Nilai Recall : {recall}")
                st.caption (f"f1 Score : {f1}")
            else:
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Sakit Jantung,SEGERA LARIKAN KE RUMAH SAKIT!!')
                st.caption (f"Tingkat Akurasi : {nb_acc_score}")
                st.caption (f"Tingkat Presisi : {precision}")
                st.caption (f"Nilai Recall : {recall}")
                st.caption (f"f1 Score : {f1}")

        elif algorithm == 'Multinomial':
            nb_m = MultinomialNB()
            nb_m.fit(X_train, y_train)
            nb_m_predict = nb_m.predict(X_test)
            nb_m_score = accuracy_score(y_test, nb_m_predict)
            precision = precision_score(y_test, nb_m_predict, average='weighted')
            recall = recall_score(y_test, nb_m_predict, average='weighted')
            f1 = f1_score(y_test, nb_m_predict, average='weighted')
            prediction = nb_m.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak]])[0]
            result = str(prediction)

            if result == '0':
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Tidak sedang sakit jantung')
                st.caption (f"Tingkat Akurasi : {nb_m_score}")
                st.caption (f"Tingkat Presisi : {precision}")
                st.caption (f"Nilai Recall : {recall}")
                st.caption (f"f1 Score : {f1}")
            else:
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Sakit Jantung,SEGERA LARIKAN KE RUMAH SAKIT!!') 
                st.caption (f"Tingkat Akurasi : {nb_m_score}")
                st.caption (f"Tingkat Presisi : {precision}")
                st.caption (f"Nilai Recall : {recall}")
                st.caption (f"f1 Score : {f1}")

        elif algorithm == 'Bernoulli':
            nb_b = BernoulliNB()
            nb_b.fit(X_train, y_train)
            nb_b_predict = nb_b.predict(X_test)
            nb_b_score = accuracy_score(y_test, nb_b_predict)
            precision = precision_score(y_test, nb_b_predict, average='weighted')
            recall = recall_score(y_test, nb_b_predict, average='weighted')
            f1 = f1_score(y_test, nb_b_predict, average='weighted')
            prediction = nb_b.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak]])[0]
            result = str(prediction)

            if result == '0':
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Tidak sedang sakit jantung')
                st.caption (f"Tingkat Akurasi : {nb_b_score}")
                st.caption (f"Tingkat Presisi : {precision}")
                st.caption (f"Nilai Recall : {recall}")
                st.caption (f"f1 Score : {f1}")
            else:
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Sakit Jantung,SEGERA LARIKAN KE RUMAH SAKIT!!') 
                st.caption (f"Tingkat Akurasi : {nb_b_score}")
                st.caption (f"Tingkat Presisi : {precision}")
                st.caption (f"Nilai Recall : {recall}")
                st.caption (f"f1 Score : {f1}")

        elif algorithm == 'Complementary':
            nb_b = ComplementNB()
            nb_b.fit(X_train, y_train)
            nb_b_predict = nb_b.predict(X_test)
            nb_c_score = accuracy_score(y_test, nb_c_predict)
            precision = precision_score(y_test, nb_c_predict, average='weighted')
            recall = recall_score(y_test, nb_c_predict, average='weighted')
            f1 = f1_score(y_test, nb_c_predict, average='weighted')
            prediction = nb_b.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak]])[0]
            result = str(prediction)

            if result == '0':
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Tidak sedang sakit jantung') 
                st.caption (f"Tingkat Akurasi : {nb_c_score}")
                st.caption (f"Tingkat Presisi : {precision}")
                st.caption (f"Nilai Recall : {recall}")
                st.caption (f"f1 Score : {f1}")
            else:
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Sakit Jantung,SEGERA LARIKAN KE RUMAH SAKIT!!')  
                st.caption (f"Tingkat Akurasi : {nb_c_score}")
                st.caption (f"Tingkat Presisi : {precision}")
                st.caption (f"Nilai Recall : {recall}")
                st.caption (f"f1 Score : {f1}")

        elif algorithm == 'SVM':
            model = svm.SVC(kernel="linear", C=5)
            model.fit(X_train, y_train)
            pred = model.predict(X_test)
            accuracy = model.score(X_test, y_test)
            prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak]])[0]
            result = str(prediction)

            if result == '0':
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Tidak sedang sakit jantung')
                st.caption (f"Tingkat Akurasi : {accuracy}")
            else:
                st.subheader(f"Prediction : {result}")
                st.write('Terindikasi Sakit Jantung,SEGERA LARIKAN KE RUMAH SAKIT!!')
                st.caption (f"Tingkat Akurasi : {accuracy}")
        # Continue the same indentation pattern for the other algorithms...

    else:
        result = "Please complete the form above!"
else:
        st.subheader('Prediction : ')
