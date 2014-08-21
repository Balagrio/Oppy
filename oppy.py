# Importanweisung
import numpy as np
from oct2py import octave
from scipy import optimize

# Fitnessfunktion
def ffun(x): return octave.call("myfun.m", x)*(-1)