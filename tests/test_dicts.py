import os
from utils import dicts

test_dict_1 = {
    'k1': 'v1',
    'k2': {
        'k3': 'v3',
        'k4': 'v4'
    }
}

test_dict_2 = {
    'k2': {
        'k4': {},
        'k5': 'v5'
    },
    'k3': 'v3'
}

expected_dict = {
    'k1': 'v1',
    'k2': {
        'k3': 'v3',
        'k4': {},
        'k5': 'v5'
    },
    'k3': 'v3'
}


def test_merge_dicts():
    config = dicts.merge_dicts(test_dict_1, test_dict_2)
    assert config == expected_dict


def test_merge_dict_list():
    config = dicts.merge_dict_list([test_dict_1, test_dict_2])
    assert config == expected_dict