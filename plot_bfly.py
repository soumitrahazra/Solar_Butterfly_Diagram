import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib.style
from scipy.io import readsav
## Plotting canvas properties.
params = {'legend.fontsize': 12,
          'axes.labelsize': 12,
          'axes.titlesize': 12,
          'xtick.labelsize' :10,
          'ytick.labelsize': 10,
          'grid.color': 'k',
          'grid.linestyle': ':',
          'grid.linewidth': 0.5,
          'mathtext.fontset' : 'stix',
          'mathtext.rm'      : 'serif',
          'font.family'      : 'serif',
          'font.serif'       : "Times New Roman", # or "Times"          
         }
matplotlib.rcParams.update(params)
s= readsav('butterfly_diagram_data.sav')
time=s.dates
latitude=s.latitude
bfly=s.bfly

## Plot the data

fig = plt.figure()
bmax = 12
ax = fig.add_subplot(111)
ax.axhline(y=0.0,color='grey',linestyle='dashed')
ax.axhline(y=45.0,color='grey',linestyle='dashed')
ax.axhline(y=-45.0,color='grey',linestyle='dashed')
a1 = ax.pcolormesh(time, latitude, bfly,cmap=plt.cm.bwr)
a1.set_clim(vmin=-bmax, vmax=bmax)
plt.colorbar(a1, extend='both')
ax.set_xlabel('Time (Yrs)')
ax.set_ylabel('Latitude')

plt.savefig('bfly_final.png',dpi=500)
plt.show()
