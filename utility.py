# coding: utf-8
""" Utility functions

"""
import pandas as pd
from collections import Counter

# import numpy as np

def flatten(nested_list):
    """flatten nested list"""
    return [e for inner_list in nested_list for e in inner_list]
def make_couples(array, count_start = 0):
    """ make combination of array component"""
    result = []
    for i in range(len(array)):
        for j in range(i+count_start, len(array)):
            couple = list([str(array[i]).lower(), str(array[j]).lower()])
            couple.sort()
            result.append(tuple(couple))
    return result
def convert_counter(counter):
    result = pd.DataFrame.from_dict(counter, orient='Index').reset_index()
    result.columns = ['word', 'count']
    result = result.sort_values(by='count', ascending=False)
    result['_1'] = [x[0] for x in result['word']]
    result['_2'] = [x[1] for x in result['word']]
    result = result[['_1', '_2', 'count']]
    return result
def make_freq_by_items(data, code, items):
    result  = {}
    for item in items:
        res = {x:0 for x in code.values()}
        for i in data[data['_1'] == item].index:
            row = data.loc[i]
            res[code.get(row['_2'], np.nan)] += row['count']
        for i in data[data['_2'] == item].index:
            row = data.loc[i]
            res[code.get(row['_1'], np.nan)] += row['count']
        result[item] = res
    return pd.DataFrame(result).T

def search_occur(data, target):
    return [i for i,x in data.items() if target in x]

def count(data, name='_n'):
    processed_data =  flatten([list(data[x]) for x in data])
    counter = Counter(processed_data)
    result = pd.DataFrame.from_dict(counter, orient='Index').reset_index()
    result.columns = [name, 'count']
    result = result.sort_values(by='count', ascending=False)
    return result


def get_freq_table(target, in_data, out_data):
    target_ids = search_occur(in_data, target)
    target_word = []
    for i in target_ids:
        if out_data.get(i):
            target_word += out_data[i]
    word_freq = Counter(target_word)
    result = pd.DataFrame.from_dict(word_freq, orient='Index').reset_index()
    result.columns = ['word', 'count']
    result = result.sort_values(by='count', ascending=False)
    return result

def result_freq_by_index(in_data, out_data, filename=None, rank_under=100, cutoff=20):
    generate_list = count(in_data)
    x = generate_list.iloc[0]['_n']
    result = get_freq_table(x, in_data, out_data)[:cutoff].reset_index(drop=True)
    result.columns = ['index', x]
    result = result.set_index('index')
    for x in list(generate_list[1:rank_under]['_n']):
        row = get_freq_table(x, in_data, out_data)[:cutoff].reset_index(drop=True)
        row.columns = ['index',x]
        row = row.set_index('index')
        result = pd.merge(result, row, how='outer',left_index=True,right_index=True)
    result = result.fillna(0)
    if filename:
        result.to_csv(filename, sep='\t')
    return result





