# Importanweisung
import numpy as np
from oct2py import octave
from scipy import optimize

# Fitnessfunktion
def ffun(x): return octave.myfun(x)*(-1)

# Grenzen, z.B.
#xmin    = [10.,3.,2.,0.05,0.05]
#xmax    = [60.,5.,5.,1.5,1.5]
xmin    = [0.,0.,0.,0.,0.]
xmax    = [0.,0.,0.,0.,0.] 

# Grenzen ueberschreiben
xmin[0] = float(raw_input("Minimaler Winkel: "))
xmax[0] = float(raw_input("Maximaler Winkel: "))
xmin[1] = float(raw_input("Minimale Zahnbreite: "))
xmax[1] = float(raw_input("Maximale Zahnbreite: "))
xmin[2] = float(raw_input("Minimale Zahnlaenge: "))
xmax[2] = float(raw_input("Maximale Zahnlaenge: "))
xmin[3] = float(raw_input("Minimaler Winkel R1: "))
xmax[3] = float(raw_input("Maximaler Winkel R1: "))
xmin[4] = float(raw_input("Minimaler Winkel R2: "))
xmax[4] = float(raw_input("Maximaler Winkel R2: "))

# Startpunkt
x0      = [(xmax[0]-xmin[0])/2, (xmax[1]-xmin[1])/2, (xmax[2]-xmin[2])/2, (xmax[3]-xmin[3])/2, (xmax[4]-xmin[4])/2]

# Konfiguration 'basinhopping' mit Grenzen
bounds  = [(low, high) for low, high in zip(xmin, xmax)]
minimizer_kwargs = dict(method="L-BFGS-B", bounds=bounds)

# Optimierung
ret = optimize.basinhopping(ffun, x0, minimizer_kwargs=minimizer_kwargs, niter=10) 
print("====================================================")
print("x = [%.4f, %.4f, %.4f, %.4f, %.4f], f(x) = %.4f" % (ret.x[0], ret.x[1], ret.x[2], ret.x[3], ret.x[4], ret.fun*(-1)))
