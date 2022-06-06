# Parallel Positive Unit Propagation algorithm on a random Horn-SAT formula

This repository contains code to run an empirical analysis of the Parallel Positive Unit Resolution (PPUR) algorithm on a random 1-3-Horn-SAT formula instance. The Horn formula model is described in [this paper](https://onlinelibrary.wiley.com/doi/abs/10.1002/rsa.20176).

**Requires:** 
* `python3.8`, `numpy` (to run code)
* `jupyterlab`, `ipython`, `pandas`, `matplotlib`, `seaborn`, `ipympl`, `nodejs`, `pillow` (to run the Jupyter notebook to produce figures)

## Reproducing results

* Clone this repository and `cd` into it
```
$ git clone https://github.com/AnanthHari/PPUR-random-Horn-SAT.git
$ cd PPUR-random-Horn-SAT
```
* Reproducing the results on the maximum depth of the PPUR algorithm on random Horn-SAT input for various `n` (number of variables) --- Suitable commands are present at the end of `get_h_sweep.py` file
```
 $ python get_h_sweep.py 0.171 0.176 5
```
  * Explanation of the input arguments: The last 3 arguments are: min value of `d1` to start the search, max value of `d1` to end the search, and finally, the precision of `d1` parameter.
  * Outputs will be generated in the `outputs` subdirectory.
* Reproducing the results on the probability of satisfiability of the PPUR algorithm on random Horn-SAT input for various `d1` and `d3` values for a fixed `n`
```
 $ python get_sat_sweep.py 5
```
  * Explanation of the input arguments: The last argument is the precision of `d1` parameter to be used.
  * Outputs will be generated in the `outputs` subdirectory.
* Reproducing the figures:
  * Run the Jupyter notebook after installing the needed packages. The output figures would be stored in `figures` subdirectory.
