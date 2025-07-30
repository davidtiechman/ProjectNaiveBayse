class Row:
    def __init__(self, parameters, model_result, correct_result):
        self.record = {
            'age': parameters[0],
            'income': parameters[1],
            'student': parameters[2],
            'credit_rating': parameters[3],
            'model_result': model_result,
            'correct_result': correct_result
        }

    def get_record(self):
        return self.record
# parameters = [35,'low','no','fair']
# row = Row(parameters,True,True)
# new_row = row.get_record()
# writ = TableScoreModel()
# writ.writing_to_json(new_row)