import json
import pandas as pd
import os


def create_json():
    json_input = list()
    for index in range(1, 11):
        json_input_ = dict()
        json_input_['Ref'] = f'ABC_{index}'
        json_input_['sample'] = f'sample_status_{index}'
        json_input.append(json_input_)

    json_dump = json.dumps(json_input)
    json_load = json.loads(json_dump)
    
    return json_load

excel_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'excel_database.xlsx')

data_set = pd.read_excel(excel_file, sheet_name='Sheet1')
i = 1
excel_input = list()
for item in json_load:
    item = json.dumps(item)
    item = json.loads(item)
    data_set = data_set.append({'Index': i, 'Reference_Key': item['Ref'], 'Status': item['sample']}, ignore_index=True)
    i += 1

data_set.to_excel(excel_file, index=False)
