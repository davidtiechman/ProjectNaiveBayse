from prediction import Naive_byase
def entering_parameters(age: int,income: str,
    student: str,
    credit_rating: str):
    model_results = Naive_byase()
    model_results.naive_byase(age,income,student,credit_rating)
    def print_results(model_results):
        if model_results[0]> model_results[1]:
            return True
        elif model_results[0] == model_results[1]:
            return '=='
        else:
            return False