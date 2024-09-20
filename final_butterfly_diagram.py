#This python code is written for the generation of the butterfly diagram using synoptic maps.
#Written by Soumitra.
#Date: June 15, 2020

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d
from scipy.signal import convolve as scipy_convolve
from scipy.io import readsav
from astropy.io import fits
from matplotlib import rc
import matplotlib.style
import glob

drive='/home/soumitra/Final_Study/Butterfly_diagram_final_plot/Final_Plot/'
bfly=np.zeros((615,180))

#KITT Peak National Observatory (KPNO) data from CR 1625 to 1639
cr_start1=1625
cr_end1=1639
#KITT peak data from CR 1645 to 2007
cr_start2=1645
cr_end2=2007
#SOLIS data from CR 2008 to 2014.
cr_start3=2008
cr_end3=2014
#MDI data from CR 2015 to 2017
cr_start4=2015
cr_end4=2017
#SOLIS data from CR 2018 to 2025
cr_start5=2018
cr_end5=2025
#MDI data from CR 2026
cr_start6=2026
#SOLIS data from CR 2027 to 2034
cr_start7=2027
cr_end7=2034
#MDI data for CR 2035
cr_start8=2035
#SOLIS data from CR 2036 to 2039
cr_start9=2036
cr_end9=2039
#MDI data from CR 2040 to 2042
cr_start10=2040
cr_end10=2042
#SOLIS data from 2043 to 2058
cr_start11=2043
cr_end11= 2058
#GONG data from CR 2059 to 2188
cr_start12=2059
cr_end12=2188
#SOLIS data for CR 2189
cr_start13=2189
#GONG data from CR 2190 to 2230
cr_start14=2190
cr_end14=2230 

#End map is needed for the calculation of polar field.
#Modify this when the butterfly diagram will be updated.

end_map=cr_end14

#Note: Resolution of KPNO, GONG and SOLIS data is 360*180
#Resolution of MDI data is 3600*1080.

#KITT Peak National observatory data from CR 1625 to CR 1639
path=drive + '/data1/'
file1=sorted(glob.glob(path+'*.fits'))
cr=cr_start1
for cs in range(len(file1)): 
    hdulist = fits.open(file1[cs])
    br0 = hdulist[0].data
    brheader=hdulist[0].header
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1
      
#Data of CR 1640 to CR 1644 is abscent. There is no data from any observatory.
#KITT Peak data is again present from CR 1645 to CR 2007.

path=drive + '/data2/'
file2=sorted(glob.glob(path+'*.fits'))
cr=cr_start2
for cs in range(len(file2)): 
    hdulist = fits.open(file2[cs])
    br0 = hdulist[0].data
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#SOLIS observatory data from CR 2008 to CR 2014
path=drive + '/data3/'
file3=sorted(glob.glob(path+'*.fits'))
cr=cr_start3
for cs in range(len(file3)): 
    hdulist = fits.open(file3[cs])
    br0 = hdulist[0].data
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#MDI data is from CR 2015 to 2017.
#We have used directly radial magnetic field data.
#No line of sight to radial magnetic field conversion is necessary.
path=drive + '/data4/'
file4=sorted(glob.glob(path+'*.fits'))
cr=cr_start4
for cs in range(len(file4)): 
    mdilist=fits.open(file4[cs])
    brmdi=mdilist[0].data 
    brmdi = np.nan_to_num(brmdi)
    brmdi[brmdi < -3000]=0
    #No line of sight to radial conversion is necessary.
    #If necessary for some data set, please comment off next three line
    #for j in range(0, 1079):
    #   los2r[:,j]= 1.1*550./np.sqrt(550.*550. - (j-540.)*(j-540.)) 
    #brmdi=los2r*brmdi
    #Now Blur to KPNO resolution (10 by 6)
    kernal=np.zeros((15,9))
    kernal[:,:]=1./(15.*9.)
    brmdis = scipy_convolve(brmdi, kernal, mode='same')
    #Resize to KPNO standard by interpolation.
    theta= np.linspace(-np.pi/2, np.pi/2, 1080)
    phi= np.linspace(0, 2*np.pi, 3600)
    theta_new=np.linspace(-np.pi/2, np.pi/2, 180)
    phi_new=np.linspace(0, 2*np.pi, 360)
    brim=interp2d(phi, theta, brmdis, kind='cubic', copy=True, bounds_error=False, fill_value=0)
    brd=brim(phi_new, theta_new)
    ave=np.sum(brd, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#SOLIS observatory data from CR 2018 to CR 2025
path=drive + '/data5/'
file5=sorted(glob.glob(path+'*.fits'))
cr=cr_start5
for cs in range(len(file5)): 
    hdulist = fits.open(file5[cs])
    br0 = hdulist[0].data
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#MDI data is for CR 2026.
#We have used directly radial magnetic field data.
#No line of sight to radial magnetic field conversion is necessary.
path=drive + '/data6/'
file6=sorted(glob.glob(path+'*.fits'))
cr=cr_start6
for cs in range(len(file6)): 
    mdilist=fits.open(file6[cs])
    brmdi=mdilist[0].data 
    brmdi = np.nan_to_num(brmdi)
    brmdi[brmdi < -3000]=0
    #No line of sight to radial conversion is necessary.
    #If necessary for some data set, please comment off next three line
    #for j in range(0, 1079):
    #   los2r[:,j]= 1.1*550./np.sqrt(550.*550. - (j-540.)*(j-540.)) 
    #brmdi=los2r*brmdi
    #Now Blur to KPNO resolution (10 by 6)
    kernal=np.zeros((15,9))
    kernal[:,:]=1./(15.*9.)
    brmdis = scipy_convolve(brmdi, kernal, mode='same')
    #Resize to KPNO standard by interpolation.
    theta= np.linspace(-np.pi/2, np.pi/2, 1080)
    phi= np.linspace(0, 2*np.pi, 3600)
    theta_new=np.linspace(-np.pi/2, np.pi/2, 180)
    phi_new=np.linspace(0, 2*np.pi, 360)
    brim=interp2d(phi, theta, brmdis, kind='cubic', copy=True, bounds_error=False, fill_value=0)
    brd=brim(phi_new, theta_new)
    ave=np.sum(brd, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#SOLIS observatory data from CR 2027 to CR 2034
path=drive + '/data7/'
file7=sorted(glob.glob(path+'*.fits'))
cr=cr_start7
for cs in range(len(file7)): 
    hdulist = fits.open(file7[cs])
    br0 = hdulist[0].data
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#MDI data is for CR 2035.
#We have used directly radial magnetic field data.
#No line of sight to radial magnetic field conversion is necessary.
path=drive + '/data8/'
file8=sorted(glob.glob(path+'*.fits'))
cr=cr_start8
for cs in range(len(file8)): 
    mdilist=fits.open(file8[cs])
    brmdi=mdilist[0].data 
    brmdi = np.nan_to_num(brmdi)
    brmdi[brmdi < -3000]=0
    #No line of sight to radial conversion is necessary.
    #If necessary for some data set, please comment off next three line
    #for j in range(0, 1079):
    #   los2r[:,j]= 1.1*550./np.sqrt(550.*550. - (j-540.)*(j-540.)) 
    #brmdi=los2r*brmdi
    #Now Blur to KPNO resolution (10 by 6)
    kernal=np.zeros((15,9))
    kernal[:,:]=1./(15.*9.)
    brmdis = scipy_convolve(brmdi, kernal, mode='same')
    #Resize to KPNO standard by interpolation.
    theta= np.linspace(-np.pi/2, np.pi/2, 1080)
    phi= np.linspace(0, 2*np.pi, 3600)
    theta_new=np.linspace(-np.pi/2, np.pi/2, 180)
    phi_new=np.linspace(0, 2*np.pi, 360)
    brim=interp2d(phi, theta, brmdis, kind='cubic', copy=True, bounds_error=False, fill_value=0)
    brd=brim(phi_new, theta_new)
    ave=np.sum(brd, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#SOLIS observatory data from CR 2036 to CR 2039
path=drive + '/data9/'
file9=sorted(glob.glob(path+'*.fits'))
cr=cr_start9
for cs in range(len(file9)): 
    hdulist = fits.open(file9[cs])
    br0 = hdulist[0].data
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#MDI data from CR 2040 to 2042.
#We have used directly radial magnetic field data.
#No line of sight to radial magnetic field conversion is necessary.
path=drive + '/data10/'
file10=sorted(glob.glob(path+'*.fits'))
cr=cr_start10
for cs in range(len(file10)): 
    mdilist=fits.open(file10[cs])
    brmdi=mdilist[0].data 
    brmdi = np.nan_to_num(brmdi)
    brmdi[brmdi < -3000]=0
    #No line of sight to radial conversion is necessary.
    #If necessary for some data set, please comment off next three line
    #for j in range(0, 1079):
    #   los2r[:,j]= 1.1*550./np.sqrt(550.*550. - (j-540.)*(j-540.)) 
    #brmdi=los2r*brmdi
    #Now Blur to KPNO resolution (10 by 6)
    kernal=np.zeros((15,9))
    kernal[:,:]=1./(15.*9.)
    brmdis = scipy_convolve(brmdi, kernal, mode='same')
    #Resize to KPNO standard by interpolation.
    theta= np.linspace(-np.pi/2, np.pi/2, 1080)
    phi= np.linspace(0, 2*np.pi, 3600)
    theta_new=np.linspace(-np.pi/2, np.pi/2, 180)
    phi_new=np.linspace(0, 2*np.pi, 360)
    brim=interp2d(phi, theta, brmdis, kind='cubic', copy=True, bounds_error=False, fill_value=0)
    brd=brim(phi_new, theta_new)
    ave=np.sum(brd, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#SOLIS observatory data from CR 2043 to CR 2058
path=drive + '/data11/'
file11=sorted(glob.glob(path+'*.fits'))
cr=cr_start11
for cs in range(len(file11)): 
    hdulist = fits.open(file11[cs])
    br0 = hdulist[0].data
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#GONG observatory data from CR 2059 to CR 2188
path=drive + '/data12/'
file12=sorted(glob.glob(path+'*.fits'))
cr=cr_start12
for cs in range(len(file12)): 
    hdulist = fits.open(file12[cs])
    br0 = hdulist[0].data
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#SOLIS observatory data for CR 2189
path=drive + '/data13/'
file13=sorted(glob.glob(path+'*.fits'))
cr=cr_start13
for cs in range(len(file13)): 
    hdulist = fits.open(file13[cs])
    br0 = hdulist[0].data
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#GONG observatory data from CR 2190 to CR 2230
path=drive + '/data14/'
file14=sorted(glob.glob(path+'*.fits'))
cr=cr_start14
for cs in range(len(file14)): 
    hdulist = fits.open(file14[cs])
    br0 = hdulist[0].data
    br0 = np.nan_to_num(br0)
    br0[br0 < -3200]=0
    ave=np.sum(br0, axis=1)/360
    bfly[cr-1623,:]=ave
    cr=cr+1

#Some Comment: One can also add HMI synoptic map data. Then
#One has to follow similar method like MDI because resolution
#is different. As oldest available KPNO data is 360*180,
#We have to covert HMI data to 360*180 by interpolation. 

#Date and latitude based on the carington rotation.
#CR 1623 corresonds to year 1975.
dates=np.zeros((615,180))
latitude=np.zeros((615, 180))
for i in range(615):
   for j in range(180):
          dates[i,j]=1975.0 + i*(27.27/365.25)
          latitude[i,j]=-90.0 + j*1.0

#If one wants to cut any particular solar cycle like cycle23.
# cycle 23 is from 1996.577 to 2009.0455
times=dates[289:457, 1]
latitudes=latitude[1,:]
bflya=bfly[289:457, :]

#Calculation of polar fields in Northen and Southern Hemisphere.
#15 pixel corresponds to 15 degree; as resolution along latitude 1 degree.
date=np.zeros((end_map - 1623 + 1))
North=np.zeros((end_map - 1623 + 1))
South=np.zeros((end_map - 1623 + 1))
npix=14
df_polarfield=pd.DataFrame()
for cs in range(1623, cr_end14+1):
   date[cs-1623]=1975.0 + 27.27*(cs-1623)/365.25
   North[cs-1623]=np.sum(bfly[cs-1623, (180-npix):179])/npix
   South[cs-1623]=np.sum(bfly[cs-1623, 0:(npix-1)])/npix
   
df_polarfield['Date']=date
df_polarfield['Northern_Polar_Field']=North
df_polarfield['Southern_Polar_Field']=South
#df_polarfield.columns['Date', 'Northern_Polar_Field', 'Southern_Polar_Field']
df_polarfield.to_csv('Average_Polar_Field_Data.csv', sep='\t', index = False)

#Plot of Average polar field strength taken over 15 degrees.
plt.plot(date, North, '-k', label='North')
plt.plot(date, South, '--r', label='South')
plt.legend()
plt.xlim([1975, 2020])
plt.xlabel('Time (Years)')
plt.ylabel('Average Polar Field (Gauss)')
plt.savefig('polar_field.png', dpi=500)
plt.show()

#Plotting of the butterfly diagram

fig = plt.figure()
bmax = 12
ax = fig.add_subplot(111)
ax.axhline(y=0.0,color='grey',linestyle='dashed')
ax.axhline(y=45.0,color='grey',linestyle='dashed')
ax.axhline(y=-45.0,color='grey',linestyle='dashed')
a1 = ax.pcolormesh(dates,latitude, bfly,cmap=plt.cm.bwr)
a1.set_clim(vmin=-bmax, vmax=bmax)
plt.colorbar(a1, extend='both')
ax.set_xlabel('Time (Yrs)')
ax.set_ylabel('Latitude')

plt.savefig('butterfly_diagram.png',dpi=500)
plt.show()  

















    

