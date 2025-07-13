from formula_calculation import FormulaCalculation

class WiresToFile():
    def __init__(self):
        self.Parameters = []
        self.Model_result = ''
        self.Correct_result = bool
        self.Result_folder = ''
    def wires_to_file(self,parameters,model_result,correct_result,file='test_results.txt'):
        self.Result_folder = file
        self.Parameters = parameters
        self.Model_result = model_result
        self.Correct_result = correct_result
        with open(self.Result_folder,'a') as result_folder:
            result_folder.write(f"{self.Parameters}\n")
            result_folder.write(f"statistics yes is:{self.Model_result[0]}")
            result_folder.write(f"statistics no is:{self.Model_result[1]}")
            result_folder.write(f"'the statistic of the customer that buys is: {self.Model_result[2]}\n")
            result_folder.write(f"{self.Correct_result}\n")

# wires = WiresToFile()
# parameters = [30,'low','no','fair']
# forma = FormulaCalculation('true')
# model_result = forma.formula_calculation(parameters[0],parameters[1],parameters[2],parameters[3])
# wires.wires_to_file('test_results.txt',parameters,model_result,False)

