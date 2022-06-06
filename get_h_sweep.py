import sys
from horn_1_3 import run_sweep_d1

assert len(sys.argv) == 4, 'Please provide min_d1, max_d1 and d1_precision as arguments'


min_d1, max_d1, d1_prec = float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3])

num_n = 10
list_of_n = [(10**i) for i in range(4, 4+num_n)]
step_d1 = 10**(-d1_prec)
min_d3, max_d3, step_d3 = 0.1, 3.0, 0.1
n_vs_h = {i: [] for i in list_of_n}
for i in list_of_n:
    data = run_sweep_d1(i, min_d1, max_d1, step_d1, min_d3, max_d3, step_d3)
    n_vs_h[i] = max(data, key=lambda x: x[1])

res_arr = [(n, round(res[0], d1_prec), res[1]) for n,res in n_vs_h.items()]

_f = f'outputs/h_sweep_d1_precision_{d1_prec}.tsv'
with open(_f, 'w') as f:
    print('n\td1\tmax_h', file=f)
    for n,d1,h in res_arr:
        print(f'{n}\t{d1}\t{h}', file=f)

#  Run as:
#python get_h_sweep.py 0.1 0.2 2
#python get_h_sweep.py 0.1 0.2 3
#python get_h_sweep.py 0.11 0.18 4
#python get_h_sweep.py 0.171 0.176 5
