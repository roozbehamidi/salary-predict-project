import streamlit as st
import numpy as np
import pandas as pd
import joblib

# -----------------------------
# تنظیمات اولیه
# -----------------------------

# لیست آدرس‌ها
from utils import encode_country,encode_edlevel,country_list, edlevel_list,columns 
# بارگذاری مدل
model = joblib.load('gbr_model.joblib')

# ستون‌های ورودی مدل: ویژگی‌های عددی + dummy آدرس‌ها به ترتیب الفبایی
columns = columns + sorted(country_list)+ sorted(edlevel_list)

st.title('Salary Prediction')

# -----------------------------
# دریافت ورودی‌ها از کاربر
# -----------------------------
years = st.number_input("Years", 1, 50, step=1, format="%d")

country = st.selectbox("Country:", country_list)
edlevel = st.selectbox("EdLevel:", edlevel_list)

# -----------------------------
# تابع تبدیل آدرس به one-hot
# -----------------------------
    # ویژگی‌های عددی/باینری
row = {
    "Years": years
}

# دیتافریم نهایی با صفر
X = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

# مقداردهی به ویژگی‌های عددی/باینری
for col, val in row.items():
    if col in X.columns:
        X.at[0, col] = val

country_encoding = encode_country(country, columns)
for col, val in country_encoding.items():
    if col in X.columns:
        X.at[0, col] = val

edlevel_encoding = encode_edlevel(edlevel, columns)
for col, val in edlevel_encoding.items():
    if col in X.columns:
        X.at[0, col] = val  

# -----------------------------
# تابع پیش‌بینی
# -----------------------------
def predict(x):          
    # پیش‌بینی
    prediction = model.predict(x)
    st.write("Predicted Salary:", f"{prediction[0]:,.0f} $")

# -----------------------------
# دکمه پیش‌بینی
# -----------------------------
if st.button("Predict"):
    predict(X)
