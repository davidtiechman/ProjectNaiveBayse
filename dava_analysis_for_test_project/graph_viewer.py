import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import os

ACCESS_CODE = "1234"
DATA_FILE = "training_record_table.json"

# ========== טעינת נתונים ==========
# @st.cache_data
def load_data():
    if not os.path.exists(DATA_FILE):
        return pd.DataFrame()
    return pd.read_json(DATA_FILE, lines=True)

# ========== שמירת רשומה ==========
# def save_record(record):
#     with open(DATA_FILE, "a") as f:
#         f.write(json.dumps(record) + "\n")

# ========== ניווט ==========
st.sidebar.title("ניווט")
view_option = st.sidebar.radio("בחר תצוגה", ["אחוז הצלחה", "טבלת נתונים", "הוסף רשומה"])

# ========== תצוגת גרף ==========
if view_option == "אחוז הצלחה":
    df = load_data()
    if df.empty:
        st.warning("אין נתונים זמינים להצגה.")
    else:
        df['correct_prediction'] = df['model_result'] == df['correct_result']
        accuracy = df['correct_prediction'].mean()

        st.title("אחוזי הצלחה של המודל")
        fig, ax = plt.subplots()
        ax.pie([accuracy, 1 - accuracy],
               labels=['True', 'False'],
               autopct='%1.1f%%',
               colors=['green', 'red'])
        st.pyplot(fig)
        st.snow()

# ========== תצוגת טבלה ==========
elif view_option == "טבלת נתונים":
    df = load_data()
    if df.empty:
        st.warning("אין נתונים להצגה.")
    else:
        df['correct_prediction'] = df['model_result'] == df['correct_result']

        st.title("טבלת נתונים")

        with st.expander("🎛 סינון נתונים"):
            income_filter = st.multiselect("הכנסה (income)", df['income'].unique(), default=df['income'].unique())
            student_filter = st.multiselect("סטודנט (student)", df['student'].unique(), default=df['student'].unique())
            credit_filter = st.multiselect("דירוג אשראי (credit_rating)", df['credit_rating'].unique(), default=df['credit_rating'].unique())
            only_errors = st.checkbox("הצג רק טעויות של המודל")

        filtered_df = df[
            df['income'].isin(income_filter) &
            df['student'].isin(student_filter) &
            df['credit_rating'].isin(credit_filter)
        ]

        if only_errors:
            filtered_df = filtered_df[filtered_df['correct_prediction'] == False]

        st.dataframe(filtered_df)
        st.download_button("📥 הורד כ־CSV", data=filtered_df.to_csv(index=False), file_name="filtered_data.csv", mime="text/csv")

elif view_option == "הוסף רשומה":
    st.warning("כרגע אי אפשר לעדכן מכאן")

