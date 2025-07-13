from formula_calculation import entering_parameters, formula_calculation
from test_model import receiving_data

def option():
    exit = False
    while(not exit):
        user_option = input("pleas select option (1-3)")
        match (user_option):
            case '1':
                try:
                    parameters = entering_parameters()
                    formula_calculation(parameters[0],parameters[1],parameters[2],parameters[3])
                except Exception as e:
                    print(e)
            case '2':
                receiving_data()
                pass
            case '#':
                exit = True
if __name__ == '__main__':
    option()