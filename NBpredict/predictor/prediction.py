from load_model import return_model

class Naive_byase():
    def __init__(self):
        model_result = return_model()
        self.dict_buy = model_result[0]
        self.dict_no_buy = model_result[1]
        self.len_buy = model_result[2]
        self.len_no_buy = model_result[3]

    def naive_byase(self, age, income, student, credit_rating):
        age = self.categorize_age(age)
        parameters = [f'{age}', f'{income}', f'student_{student}', f'rating_{credit_rating}']

        statistics_yes = 1
        statistics_no = 1
        total = self.len_buy + self.len_no_buy

        for parameter in parameters:
            if parameter not in self.dict_buy:
                statistics_yes *= 1
            else:
                statistics_yes *= self.dict_buy[parameter]

        statistics_yes *= self.len_buy / total

        for parameter in parameters:
            if parameter not in self.dict_no_buy:
                statistics_no *= 1
            else:
                statistics_no *= self.dict_no_buy[parameter]

        statistics_no *= self.len_no_buy / total

        if statistics_yes > statistics_no:
            prediction = True
        elif statistics_yes == statistics_no:
            prediction = 'equal'
        else:
            prediction = False

        return statistics_yes, statistics_no, prediction

    def categorize_age(self, age):
        if age <= 30:
            return '<=30'
        elif 30 < age <= 40:
            return '31...40'
        else:
            return '>40'
