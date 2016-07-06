'''Functions to load scenario data from files.'''

import yaml

def import_yaml(file):
    '''Import scenario from YAML file format.'''
    with open(file, 'r') as file:
        scenario = yaml.load(file)
    scenario['board'] = scenario['board'].replace('|', '')
    return scenario
