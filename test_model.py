import os.path
import pandas as pd

from data_analysis_for_training import data_analysis
from formula_calculation import formula_calculation, entering_parameters, parse_age


def receiving_data():
    print("You have 2 options\nTo enter manually enter 1\nTo enter a data file enter 2")
    select = False
    option = ""
    while (not select and option != '#'):
        option = input("pleas select option (1-2)")
        if option == '1':
            try:
                parameters = entering_parameters()
                result = formula_calculation(parameters[0],parameters[1],parameters[2],parameters[3])
                rele_data = real_data()
                if rele_data:
                    test_documentation(result,rele_data)
                elif not rele_data:
                    print('pleas enter the real result')
            except Exception as e:
                print(e)
            # select = True
        elif option == '2':
            print("You can insert a file in (csv/json/xl/txt) format.")
            file = input("Pleas enter the file whit you want to testing")
            extension = check_file(file)
            match extension:
                case 'csv':
                    if os.path.exists(file):
                        df = pd.read_csv(file)
                        for index,row in df.iterrows():
                            age = parse_age(row['age'])
                            income = row['income']
                            student = row['student']
                            cratic_reding = row['credit_rating']
                            formula_calculation(age,income,student,cratic_reding)

                        # select = True
                    else:
                        print("the file is not find")
                case _ :
                    print('The file is not compatible with the software')

def test_documentation(result_test,rele_data):
    with open("test_results.txt",'w',encoding='utf-8') as f:
        f.write(f"the test result is - {result_test}\n")
        f.write('='*40 + '\n')
        test_cases = [
            ({'age': 35},'yes')
        ]


def real_data():
    print("To enter real data manually input 1\nTo enter real data from the input file 2")
    option = input("pleas enter an option")
    if option == "1":
        real_rsult = input("pleas enter the real result (true/false")
    elif option == '2':
        real_rsult = None
    return real_rsult



def check_file(file):
    extension = os.path.splitext(file)[1][1:]
    return extension
receiving_data()