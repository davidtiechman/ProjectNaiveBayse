from data_analysis_for_training import dict_buy, dict_no_buy, custom_but, custom_no_but

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
def formula_calculation(age,income,studend,credit_rating):
    age = categorize_age(30)
    parameters = [f'{age}',f'{income}',f'student_{studend}',f'rating_{credit_rating}']
    statistics_yes = 1
    statistics_no = 1
    a = custom_but + custom_no_but
    for parameter in parameters:
        statistics_yes *= dict_buy[parameter]
    statistics_yes *= custom_but/a
    for parameter in parameters:
        statistics_no *= dict_no_buy[parameter]
    statistics_no *= custom_no_but/a
    print(f'statistics yes is: {statistics_yes}')
    print(f'statistics no is: {statistics_no}')
    apparently = False
    if statistics_yes > statistics_no:
        apparently = True
    elif statistics_no == statistics_yes:
        apparently = 'equal'
    print(f'the statistic of the customer wthis buys is {apparently}')
# formula_calculation(30,'high','yes','fair')