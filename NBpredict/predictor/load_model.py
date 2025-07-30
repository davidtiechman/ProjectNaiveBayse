import json

def return_model():
    with open('/shared_data/training_record_table.json') as f:
        model_data = json.load(f)
    with open('/shared_data/training_len_table.json') as f:
        len_data = json.load(f)
    dict_buy = model_data['dict_buy']
    dict_no_buy = model_data['dict_no_buy']
    len_buy = len_data['len_dict_buy']
    len_no_buy = len_data['len_dict_no_buy']
    return dict_buy, dict_no_buy, len_buy, len_no_buy
