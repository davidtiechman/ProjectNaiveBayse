from prediction import Naive_byase
def entering_parameters(age: int,
    income: str,
    student: str,
    credit_rating: str):
    return (age,income,student,credit_rating)
def print_results(parameters):
    model_resutl = Naive_byase()
    results =  model_resutl.naive_byase(parameters[0],parameters[1],parameters[2],parameters[3])
    if results[0]> results[1]:
        return True
    elif results[0] == results[1]:
        return '=='
    else:
        return False
paramers = entering_parameters(30,'low','no','fair')
print(print_results(paramers))