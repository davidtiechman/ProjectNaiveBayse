from data_analysis_for_training import data_analysis
from displays_graphs import dict_buy, dict_no_buy


class FormulaCalculation():
    def __init__(self,status):
        self.status = status
        self.data = data_analysis()
        self.data.load_data(self.status)
        self.count_buy,self.count_no_buy = self.data.get_len_list()
        self.dict_buy,self.dict_no_buy = self.data.analysis()
    def entering_parameters(self):
        age = int(input("pleas enter the customer's age"))
        income = input("pleas enter the customer's income (high/medium/low)")
        student = input('pleas enter whether he is a student or not (yes/no)')
        credit_rating = input("pleas enter the customer's credit rating (fair/excellent)")
        return age,income,student,credit_rating
    def categorize_age(self,age):
        if age <= 30:
            return '<=30'
        elif 30 < age <= 40:
            return '31...40'
        else:
            return '>40'
    def formula_calculation(self,age,income,student,credit_rating):
        # print(len(self.dict_buy)+len(self.dict_buy))
        age = self.categorize_age(age)
        parameters = [f'{age}',f'{income}',f'student_{student}',f'rating_{credit_rating}']
        statistics_yes = 1
        statistics_no = 1
        a = self.data.custom_buy + self.data.custom_no_buy
        for parameter in parameters:
            if parameter not in self.dict_buy:
                self.dict_buy[parameter] =1
                print(self.dict_buy)
            statistics_yes *= self.dict_buy[parameter]
        statistics_yes *= self.data.custom_buy/a
        for parameter in parameters:
            if  parameter not in self.dict_no_buy:
                self.dict_no_buy[parameter] = 1
                print(self.dict_no_buy)
            statistics_no *= self.dict_no_buy[parameter]
        statistics_no *= self.data.custom_no_buy/a
        print(f'statistics yes is: {statistics_yes}')
        print(f'statistics no is: {statistics_no}')
        apparently = False
        if statistics_yes > statistics_no:
            apparently = True
        elif statistics_no == statistics_yes:
            apparently = 'equal'
        print(f'the statistic of the customer wthis buys is {apparently}')
        return (statistics_yes,statistics_no,apparently)
    def parse_age(self,age_str):
        if '...' in age_str:
            start, end = map(int, age_str.split('...'))
            return (start + end) // 2
        if age_str.startswith('<='):
            return int(age_str[2:])
        if age_str.startswith('>'):
            return int(age_str[1:]) + 1
        return int(age_str)
# a = FormulaCalculation()
# a.formula_calculation(40,'medium','yes','fair')
# print(dict_buy)
# print(dict_no_buy)