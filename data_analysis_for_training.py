import numpy as np
import pandas as pd
class data_analysis:
    def __init__(self):
        self.df = None
        self.dict_buy = {}
        self.dict_no_buy = {}
        self.custom_buy = 0
        self.custom_no_buy = 0
    def load_data(self,status):
        test = self.chang_model_status(status)
        if not test:
            self.df = pd.read_csv('directory folders data/buy_computer_data_full.csv')
        elif test:
            self.df = pd.read_csv('directory folders data/buy_computer_data_hidden_70%.csv')
        print("Loading file:", "hidden" if test else "full")
    def analysis(self):
        # איסוף כל הגילאים מהטבלה
        age_yes = self.df[self.df['buys_computer'] == 'yes'].groupby('age').size()
        age_no = self.df[self.df['buys_computer'] == 'no'].groupby('age').size()
        self.custom_buy,self.custom_no_buy = self.get_len_list()
        # איסוף נתונים ההכנסות של הלקוחות
        income_yes = self.df[self.df['buys_computer'] == 'yes'].groupby('income').size()
        income_no = self.df[self.df['buys_computer'] == 'no'].groupby('income').size()
        # איסוף סוג הלקוח סטודנט/לא סטודנט
        student_yes = self.df[self.df['buys_computer'] == 'yes'].groupby('student').size()
        student_no = self.df[self.df['buys_computer'] == 'no'].groupby('student').size()
        # איסוף סוג הדירוג של הלקוח
        rating_yes = self.df[self.df['buys_computer'] == 'yes'].groupby('credit_rating').size()
        rating_no = self.df[self.df['buys_computer'] == 'no'].groupby('credit_rating').size()
        for age,count in age_yes.items():
            if count <1:
                count = 1
            self.dict_buy[age] = count/self.custom_buy
        for age,count in age_no.items():
            if count <1:
                count = 1
            self.dict_no_buy[age] = count/self.custom_no_buy
        for income, count in income_yes.items():
            if count <1:
                count = 1
            self.dict_buy[income] = count/self.custom_buy
        for income, count in income_no.items():
            if count <1:
                count = 1
            self.dict_no_buy[income] = count/self.custom_no_buy
        for student, count in student_yes.items():
            if count <1:
                count = 1
            self.dict_buy[f'student_{student}'] = count/self.custom_buy
        for student, count in student_no.items():
            if count <1:
                count = 1
            self.dict_no_buy[f'student_{student}'] = count/self.custom_no_buy
        for rating, count in rating_yes.items():
            if count <1:
                count = 1
            self.dict_buy[f'rating_{rating}'] = count/self.custom_buy
        for rating, count in rating_no.items():
            if count <1:
                count = 1
            self.dict_no_buy[f'rating_{rating}'] = count/self.custom_no_buy
        # print(f"the dict of customer's how bought: {dict_buy}\nthe dictionary of customer's not bought: {dict_no_buy}")
        # print(custom_but,custom_no_but)
        # print(self.df)
        # print(self.dict_buy.keys())
        # print(self.dict_no_buy.keys())
        # print(self.custom_buy)
        # print(self.custom_no_buy)
        return self.dict_buy,self.dict_no_buy
    def get_len_list(self):
        self.custom_buy =len(self.df[self.df['buys_computer'] == 'yes'])
        self.custom_no_buy =len(self.df[self.df['buys_computer'] == 'no'])
        return self.custom_buy,self.custom_no_buy
    def chang_model_status(self,true):
        self.status = False
        if true == 'true':
            self.status = True
        return self.status

# a = data_analysis()
# a.load_data("true")
# a.analysis()
