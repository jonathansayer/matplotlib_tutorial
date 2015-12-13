import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.,5.,0.2) #returns array between 0 and 5 in 0.2 steps

plt.plot(t,t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
