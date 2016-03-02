import os
from utils import configs

current_dir = os.path.dirname(os.path.realpath(__file__))


def test_load_config_dict_py_not_existing_file():
    config = configs.load_config_dict_py('not_existing_config_file.py')
    assert config == {}


def test_load_config_dict_py():
    config = configs.load_config_dict_py('{}/fake_configs/config_base.py'.format(current_dir))
    assert config == {
        'bool_v': True,
        'none_v': None,
        'string_v': 'asdada',
        'dict_v': {
            'two': {
                '2_2': 'some2',
                '2_1': 'some1'
            },
            'one': 1
        },
        'list_v': [],
        'bytes_v': b'asdada',
        'int_v': 12
    }


def test_load_configs():
    config = configs.load_configs([
        '{}/fake_configs/config_base.py'.format(current_dir),
        '{}/fake_configs/config_child.py'.format(current_dir)
    ])

    assert config == {
        'bool_v': True,
        'none_v': {},
        'string_v': 'asdada',
        'dict_v': {
            'two': {
                '2_2': 'some2',
                '2_1': 'somex',
                '2_3': 'some3'
            },
            'one': 1
        },
        'list_v': [],
        'bytes_v': b'asdada',
        'int_v': 12,
        'new': 'new'
    }