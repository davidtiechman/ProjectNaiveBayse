import numpy as np
import pandas as pd
df = pd.read_csv('buy_computer_data_hidden.csv')
dict_buy = {}
dict_no_buy = {}
# איסוף כל הגילאים מהטבלה
age_yes = df[df['buys_computer'] == 'yes'].groupby('age').size()
age_no = df[df['buys_computer'] == 'no'].groupby('age').size()
custom_but =len(df[df['buys_computer'] == 'yes'])
custom_no_but =len(df[df['buys_computer'] == 'no'])
# איסוף נתונים ההכנסות של הלקוחות
income_yes = df[df['buys_computer'] == 'yes'].groupby('income').size()
income_no = df[df['buys_computer'] == 'no'].groupby('income').size()
# איסוף סוג הלקוח סטודנט/לא סטודנט
student_yes = df[df['buys_computer'] == 'yes'].groupby('student').size()
student_no = df[df['buys_computer'] == 'no'].groupby('student').size()
# איסוף סוג הדירוג של הלקוח
rating_yes = df[df['buys_computer'] == 'yes'].groupby('credit_rating').size()
rating_no = df[df['buys_computer'] == 'no'].groupby('credit_rating').size()
for age,count in age_yes.items():
    dict_buy[age] = count/custom_but
for age,count in age_no.items():
    dict_no_buy[age] = count/custom_no_but
for income, count in income_yes.items():
    dict_buy[income] = count/custom_but
for income, count in income_no.items():
    dict_no_buy[income] = count/custom_no_but
for student, count in student_yes.items():
    dict_buy[f'student_{student}'] = count/custom_but
for student, count in student_no.items():
    dict_no_buy[f'student_{student}'] = count/custom_no_but
for rating, count in rating_yes.items():
    dict_buy[f'rating_{rating}'] = count/custom_but
for rating, count in rating_no.items():
    dict_no_buy[f'rating_{rating}'] = count/custom_no_but
print(f"the dict of customer's how bought: {dict_buy} the dictionary of customer's not bought: {dict_no_buy}")
print(custom_but,custom_no_but)