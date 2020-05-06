import sys
import os
import pytest
sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json_to_excel.json_to_excel as  source_code

def test_create_sample_json():
    count=1
    test_json = source_code.create_sample_json(count=count)
    assert isinstance(test_json, list)
    assert test_json[0]['Ref'] == f'ABC_{count}'
    assert test_json[0]['sample'] == f'sample_status_{count}'


def test_create_sample_json_error():
    test_json = source_code.create_sample_json(count='1')
    assert test_json == "Exception occured!"
    with pytest.raises(Exception):
        test_json = source_code.create_sample_json(count=1)
        assert test_json[1]['Ref'] == f'ABC_{1}'
