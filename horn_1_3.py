import sys
from math import exp
import numpy as np

def get_prob_unsat(d1, d2, d3):
    x, y = exp(-d1*d2), exp(-d1*d1*d3)
    return 1 - (x * y)

def iterate(n, d1, d2, d3):
    _n = (1 - d1) * n
    _d1 = d1 * (d2 + d1 * d3)
    _d2 = (1 - d1) * (d2 + 2 * d1 * d3)
    _d3 = (1 - d1)**2 * d3
    halt = False
    if _d1 >= 1:
        halt = True
        _d1 = 1
    elif _d1*_n < 1:
        halt = True
        _d1 = 1/_n
    _prob = get_prob_unsat(_d1, _d2, _d3)
    return halt, _n, _d1, _d2, _d3, _prob

def print_param(i, n, d1, d2, d3, prob=None):
    if prob:
        print(f'i:\t{i}\t{n:0.2f}\t{d1:0.3f}\t{d2:0.3f}\t{d3:0.3f}\t{1-cumm_prob:0.3f}')
    else:
        print(f'i:\t{i}\t{n:0.2f}\t{d1:0.3f}\t{d2:0.3f}\t{d3:0.3f}')

def calc_prob_sat(list_prob):
    cumm_prob = [0.0] * len(list_prob)
    for i in range(len(list_prob)):
        cumm_prob[i] = list_prob[i]
        for j in range(i):
            cumm_prob[i] *= 1 - list_prob[j]
    return 1-sum(cumm_prob)

def get_h(n, d1, d2, d3, display=False):
    list_prob = []
    i = 0
    if display:
        print_param(i, n, d1, d2, d3)
    while True:
        halt, n, d1, d2, d3, prob_t = iterate(n, d1, d2, d3)
        i += 1
        list_prob.append(prob_t)
        if display:
            print_param(i, n, d1, d2, d3, list_prob[-1])
        if halt:
            break
    prob_sat = calc_prob_sat(list_prob)
    return i, n, d1, d2, d3, prob_sat 

def run_sweep_d1_d3(n, min_d1, max_d1, step_d1, min_d3, max_d3, step_d3):
    num_d1 = round(1 + (max_d1 - min_d1)/step_d1)
    num_d3 = round(1 + (max_d3 - min_d3)/step_d3)
    result_array = [(0, 0.0, 0, 0.0)] * num_d1 * num_d3
    i = 0
    for d1 in np.linspace(min_d1, max_d1, num_d1):
        for d3 in np.linspace(min_d3, max_d3, num_d3):
            h, _, _, _, _, prob_sat = get_h(n, d1, 0, d3)
            result_array[i] = (d1, d3, h, prob_sat)
            i += 1
    return result_array

def get_max_h(n, d1, min_d3, max_d3, step_d3):
    num_d3 = round(1 + (max_d3 - min_d3)/step_d3)
    result_array = [0] * num_d3 
    for idx, d3 in enumerate(np.linspace(min_d3, max_d3, num_d3)):
        h, _, _, _, _, _  = get_h(n, d1, 0, d3)
        result_array[idx] = h  # (h, d3)
    return max(result_array)

def run_sweep_d1(n, min_d1, max_d1, step_d1, min_d3, max_d3, step_d3):
    num_d1 = round(1 + (max_d1 - min_d1)/step_d1)
    result_array = [(0, 0.0, 0.0)] * num_d1
    for idx, d1 in enumerate(np.linspace(min_d1, max_d1, num_d1)):
        result_array[idx] = (d1, get_max_h(n, d1, min_d3, max_d3, step_d3))
    return result_array

if __name__ == '__main__':
    n = 20000
    min_d1, max_d1, step_d1 = 0.01, 0.25, 0.01
    min_d3, max_d3, step_d3 = 0.1, 5.0, 0.1
    res_arr = run_sweep_d1_d3(n, min_d1, max_d1, step_d1, min_d3, max_d3, step_d3)
    # --- all ---
    print('d1\td3\th\tsat')
    for d1,d3,h,sat in res_arr:
        print(f'{d1:0.2f}\t{d3:0.1f}\t{h}\t{sat:0.6f}')
