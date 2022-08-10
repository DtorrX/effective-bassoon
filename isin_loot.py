import json
from pprint import pprint
from stdnum import isin
import os
import re
import pandas as pd
from deep_translator import (GoogleTranslator)
f = open('old data/id22=36595.json')
data = json.load(f)
datalist = data.split()
isin_ = [x for x in datalist if 'Регистрационный' in x][0][:-15]
tin = [x for x in datalist if 'ИНН эмитента' in x]

# extrat data from old data.



path_to_json = 'somedir/'
json_files = [pos_json for pos_json in os.listdir('new data/') if pos_json.endswith('.json')]
# print((json_files[0:11]))  # for me this prints ['foo.json']


# new data
f = open('new data/?id22=652254.json')
g = open('old data/id22=36656.json')

def old_isin(isindata):
    data = json.load(isindata)
    data = data.split()
    isin = [x for x in data if x.startswith('RU')==True]
    return(isin)


def new_isin(isindata):
    data = json.load(isindata)
    data = data.split()
    isin = [x for x in data if 'RU' in x]
    return(isin)

old_isin(g)
new_isin(f)