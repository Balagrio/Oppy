# Importanweisung
import numpy as np
from oct2py import octave
from scipy import optimize

# Fitnessfunktion
def ffun(x): return octave.call("myfun.m", x)*(-1)

# Grenzen, z.B.
xmin    = [10.,3.,2.,0.05,0.05]
xmax    = [60.,5.,5.,1.5,1.5]
