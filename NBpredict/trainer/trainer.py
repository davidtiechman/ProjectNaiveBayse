from load_file_data import load_data
import json
class Analysis:
    def __init__(self):
        self.dict_buy = {}
        self.dict_no_buy = {}
        self.custom_buy = 0
        self.custom_no_buy = 0
        self.df = load_data()
    def analysis_dict(self):
        # איסוף כל הגילאים מהטבלה
        age_yes = self.df[self.df['buys_computer'] == 'yes'].groupby('age').size()
        age_no = self.df[self.df['buys_computer'] == 'no'].groupby('age').size()
        self.custom_buy, self.custom_no_buy = self.get_len_list()
        # איסוף נתונים ההכנסות של הלקוחות
        income_yes = self.df[self.df['buys_computer'] == 'yes'].groupby('income').size()
        income_no = self.df[self.df['buys_computer'] == 'no'].groupby('income').size()
        # איסוף סוג הלקוח סטודנט/לא סטודנט
        student_yes = self.df[self.df['buys_computer'] == 'yes'].groupby('student').size()
        student_no = self.df[self.df['buys_computer'] == 'no'].groupby('student').size()
        # איסוף סוג הדירוג של הלקוח
        rating_yes = self.df[self.df['buys_computer'] == 'yes'].groupby('credit_rating').size()
        rating_no = self.df[self.df['buys_computer'] == 'no'].groupby('credit_rating').size()
        for age, count in age_yes.items():
            if count < 1:
                count = 1
            self.dict_buy[age] = count / self.custom_buy
        for age, count in age_no.items():
            if count < 1:
                count = 1
            self.dict_no_buy[age] = count / self.custom_no_buy
        for income, count in income_yes.items():
            if count < 1:
                count = 1
            self.dict_buy[income] = count / self.custom_buy
        for income, count in income_no.items():
            if count < 1:
                count = 1
            self.dict_no_buy[income] = count / self.custom_no_buy
        for student, count in student_yes.items():
            if count < 1:
                count = 1
            self.dict_buy[f'student_{student}'] = count / self.custom_buy
        for student, count in student_no.items():
            if count < 1:
                count = 1
            self.dict_no_buy[f'student_{student}'] = count / self.custom_no_buy
        for rating, count in rating_yes.items():
            if count < 1:
                count = 1
            self.dict_buy[f'rating_{rating}'] = count / self.custom_buy
        for rating, count in rating_no.items():
            if count < 1:
                count = 1
            self.dict_no_buy[f'rating_{rating}'] = count / self.custom_no_buy
        self.wirtes_model_to_file(self.dict_buy,self.dict_no_buy)
        return self.dict_buy, self.dict_no_buy


    def get_len_list(self):
        self.custom_buy = len(self.df[self.df['buys_computer'] == 'yes'])
        self.custom_no_buy = len(self.df[self.df['buys_computer'] == 'no'])
        self.wirtes_len_dict_to_file(self.custom_buy,self.custom_no_buy)
        return self.custom_buy, self.custom_no_buy

    def wirtes_model_to_file(self,dict_but,dict_no_buy):
        with open('/shared_data/training_record_table.json','w') as j:
            j.write(json.dumps({'dict_buy': dict_but,'dict_no_buy': dict_no_buy},indent=4))
    def wirtes_len_dict_to_file(self,dict_but,dict_no_buy):
        with open('/shared_data/training_len_table.json','w') as j:
            j.write(json.dumps({'len_dict_buy': dict_but,'len_dict_no_buy': dict_no_buy},indent=4))
if __name__ == "__main__":
    analysis = Analysis()
    dict_buy, dict_no_buy = analysis.analysis_dict()
    print("Analysis complete.")
