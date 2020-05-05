import json
import pandas as pd
import os
import sys

sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import properties.config as config


def create_sample_json():
    json_input = list()
    for index in range(1, 11):
        json_input_ = dict()
        json_input_['Ref'] = f'ABC_{index}'
        json_input_['sample'] = f'sample_status_{index}'
        json_input.append(json_input_)

    json_dump = json.dumps(json_input)
    json_load = json.loads(json_dump)
    
    return json_load


class ExcelHandling:

    def __init__(self, json_load=None):

        self.data_set = pd.read_excel(config.excel_file, sheet_name='Sheet1')
        self.json_load = json_load
    
    def write_to_excel(self):
        
        i = 1
        for item in self.json_load:
            item = json.dumps(item)
            item = json.loads(item)
            self.data_set = self.data_set.append({'Index': i, 'Reference_Key': item['Ref'], 'Status': item['sample']}, ignore_index=True)
            i += 1

        self.data_set.to_excel(config.excel_file, index=False)
        return True

if __name__ == '__main__':
    test_json = create_sample_json()
    excel_obj = ExcelHandling(json_load=test_json)
    result = excel_obj.write_to_excel()
    print(result)
