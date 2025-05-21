import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model dan preprocessing tools
model = joblib.load('logreg_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoder = joblib.load('label_encoder.pkl')

st.title("🎓 Prediksi Status Mahasiswa")

st.header("📋 Data Diri Mahasiswa")

# Input data diri (tampil vertikal)
marital_status = st.selectbox("Marital Status", ['single', 'married', 'divorced', 'widower'])
course = st.selectbox("Course", [
    'Biofuel Production Technologies', 'Animation and Multimedia Design', 'Social Service',
    'Agronomy', 'Informatics Engineering', 'Equinculture',
    'Veterinary Nursing', 'Management', 'Social Work'
])
attendance = st.selectbox("Daytime/Evening Attendance", ['daytime', 'evening'])
scholarship = st.selectbox("Scholarship Holder?", ['yes', 'no'])
age = st.number_input("Age at Enrollment", 15, 70, 20)

st.header("📚 Data Akademik")

# Layout sejajar untuk fitur semester 1 dan 2
col1, col2 = st.columns(2)

with col1:
    st.subheader("Semester 1")
    f1 = st.number_input("1st Sem (credited)", 0, 10, 0)
    f2 = st.number_input("1st Sem (enrolled)", 0, 20, 0)
    f3 = st.number_input("1st Sem (evaluations)", 0, 20, 0)
    f4 = st.number_input("1st Sem (approved)", 0, 20, 0)
    f5 = st.number_input("1st Sem (grade)", 0.0, 20.0, 10.0)

with col2:
    st.subheader("Semester 2")
    f6 = st.number_input("2nd Sem (credited)", 0, 10, 0)
    f7 = st.number_input("2nd Sem (enrolled)", 0, 20, 0)
    f8 = st.number_input("2nd Sem (evaluations)", 0, 20, 0)
    f9 = st.number_input("2nd Sem (approved)", 0, 20, 0)
    f10 = st.number_input("2nd Sem (grade)", 0.0, 20.0, 10.0)

# Proses input
input_data = pd.DataFrame([{
    'Marital Status': marital_status,
    'Course': course,
    'Daytime/evening attendance': attendance,
    'Scholarship holder': 1 if scholarship == 'yes' else 0,
    'Age at enrollment': age,
    'Curricular units 1st sem (credited)': f1,
    'Curricular units 1st sem (enrolled)': f2,
    'Curricular units 1st sem (evaluations)': f3,
    'Curricular units 1st sem (approved)': f4,
    'Curricular units 1st sem (grade)': f5,
    'Curricular units 2nd sem (credited)': f6,
    'Curricular units 2nd sem (enrolled)': f7,
    'Curricular units 2nd sem (evaluations)': f8,
    'Curricular units 2nd sem (approved)': f9,
    'Curricular units 2nd sem (grade)': f10,
}])

# Encoding sama seperti training
input_data['Marital Status'] = input_data['Marital Status'].astype('category').cat.codes
input_data['Course'] = input_data['Course'].astype('category').cat.codes
input_data['Daytime/evening attendance'] = input_data['Daytime/evening attendance'].astype('category').cat.codes

# Scaling sesuai pipeline
scaled_input = scaler.transform(input_data)

# Prediksi
if st.button("🎯 Prediksi Status"):
    prediction = model.predict(scaled_input)[0]
    prediction_proba = model.predict_proba(scaled_input)[0]

    pred_label = label_encoder.inverse_transform([prediction])[0]

    st.subheader("📊 Hasil Prediksi")
    # Warna berdasarkan label
    color_map = {
        'Dropout': 'red',
        'Graduate': 'green',
        'Enrolled': 'orange'
    }

    color = color_map.get(pred_label, 'gray')  # fallback warna
    st.markdown(
        f"<h4>Status Mahasiswa: <span style='color:{color}'>{pred_label}</span></h4>",
        unsafe_allow_html=True
    )

    st.subheader("🔍 Probabilitas Kelas")

    # Tampilkan versi berwarna (markdown)
    for label, prob in zip(label_encoder.classes_, prediction_proba):
        color = color_map.get(label, 'gray')
        st.markdown(f"<span style='color:{color}'>{label}</span>: **{prob*100:.2f}%**", unsafe_allow_html=True)

