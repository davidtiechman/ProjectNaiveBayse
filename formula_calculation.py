from data_analysis_for_training import data_analysis
data = data_analysis()
data.load_data('true')
cuont_buy,cuont_no_buy = data.get_len_list()
dict_buy,dict_no_buy = data.analysis()
def entering_parameters():
    age = int(input("pleas enter the customer's age"))
    income = input("pleas enter the customer's income (high/medium/low)")
    student = input('pleas enter whether he is a student or not (yes/no)')
    credit_rating = input("pleas enter the customer's credit rating (fair/excellent)")
    return age,income,student,credit_rating
def categorize_age(age):
    if age <= 30:
        return '<=30'
    elif 30 < age <= 40:
        return '31...40'
    else:
        return '>40'
def formula_calculation(age,income,student,credit_rating):
    print(len(dict_buy)+len(dict_buy))
    age = categorize_age(age)
    parameters = [f'{age}',f'{income}',f'student_{student}',f'rating_{credit_rating}']
    statistics_yes = 1
    statistics_no = 1
    a = data.custom_buy + data.custom_no_buy
    for parameter in parameters:
        if parameter not in parameters:
            dict_buy[parameter] =1
        statistics_yes *= dict_buy[parameter]
    statistics_yes *= data.custom_buy/a
    for parameter in parameters:
        if  parameter not in dict_no_buy:
            dict_no_buy[parameter] = 1
        statistics_no *= dict_no_buy[parameter]
    statistics_no *= data.custom_no_buy/a
    print(f'statistics yes is: {statistics_yes}')
    print(f'statistics no is: {statistics_no}')
    apparently = False
    if statistics_yes > statistics_no:
        apparently = True
    elif statistics_no == statistics_yes:
        apparently = 'equal'
    print(f'the statistic of the customer wthis buys is {apparently}')
    return (statistics_yes,statistics_no,apparently)
def parse_age(age_str):
    if '...' in age_str:
        start, end = map(int, age_str.split('...'))
        return (start + end) // 2
    if age_str.startswith('<='):
        return int(age_str[2:])
    if age_str.startswith('>'):
        return int(age_str[1:]) + 1
    return int(age_str)
# print(data.custom_buy)
# print(data.custom_no_buy)
formula_calculation(30,'medium','yes','fair')