import sys
from horn_1_3 import run_sweep_d1_d3

d1_prec = int(sys.argv[1])

n = 20000
min_d1, max_d1, step_d1 = 0.01, 0.25, 10**(-d1_pres)
min_d3, max_d3, step_d3 = 0.1, 5.0, 0.1
res_arr = run_sweep_d1_d3(n, min_d1, max_d1, step_d1, min_d3, max_d3, step_d3)

_f = f'outputs/sat_sweep_d1_precision_{d1_prec}.tsv'
with open(_f, 'w') as f:
    print('d1\td3\th\tsat', file=f)
    for d1,d3,h,sat in res_arr:
        print(f'{d1:0.6f}\t{d3:0.1f}\t{h}\t{sat:0.6f}', file=f)

#  Run as:
#python get_sat_sweep.py 5
