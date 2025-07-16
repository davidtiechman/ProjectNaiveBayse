from scipy.constants import micro

from formula_calculation import FormulaCalculation
from datetime import datetime

class WiresToFile():
    def __init__(self):
        self.Parameters = []
        self.Model_result = ''
        self.Correct_result = bool
        self.Result_folder = ''
        self.Now = str(datetime.now())
        self.Training = False
    def wires_to_file(self,parameters,model_result,correct_result,training : bool,file='test_results.txt'):
        self.Result_folder = file
        self.Parameters = parameters
        self.Model_result = model_result
        self.Training = training
        if self.Training:
            self.Correct_result = correct_result
        else:
            self.Correct_result = None
        with open(self.Result_folder,'a') as result_folder:
            if self.Training:
                result_folder.write(f"\n#The test is for training purposes only.#\n")
            else:
                result_folder.write(f"\n#The test is for real purposes.#\n")
            result_folder.write(f'{self.Now}\n')
            result_folder.write(f"The parameters of the clyent is: {self.Parameters}\n")
            result_folder.write(f"statistics yes is: {self.Model_result[0]}\n")
            result_folder.write(f"statistics no is: {self.Model_result[1]}\n")
            result_folder.write(f"the statistic of the customer that buys is: {self.Model_result[2]}\n")
            if self.Training:
                result_folder.write(f"{self.Correct_result}\n")
            result_folder.write('========================================')

# wires = WiresToFile()
# parameters = [30,'low','no','fair']
# forma = FormulaCalculation('true')
# model_result = forma.formula_calculation(parameters[0],parameters[1],parameters[2],parameters[3])
# wires.wires_to_file(parameters,model_result,False)

