# Solar Butterfly Diagram
This codes generate the solar butterfly diagram from observed synoptic maps. We have synoptic maps from different observatory. We have taken longitudinal average of these
synoptic maps and stacked together. Resulting plot is the butterfly diagram.

Oldest available synoptic data is from the KITT Peak National Solar Observatory. Resolution of KPNO synoptic map is 360*180. We have used KPNO synoptic map data from CR 1643 to CR
2007. We have used SOLIS and MDI data from CR 2008 to CR 2058. We have used mostly SOLIS data. However, SOLIS synoptic map data is missing sometimes. We filled that gap by MDI data.
Recently GONG synoptic map data is available. We have used GONG synoptic map data from CR 2059 to CR 2230.

Polar field is calculated by taking the average over 15 degrees in northern (165 degree to 180 degree colatitude) and southern (0 degree to 15 degree colatitude) hemispheres.

Source of the dataset:

KITT Peak data:  ftp://nispdata.nso.edu/kpvt/synoptic/mag/

MDI data: http://soi.stanford.edu/magnetic/synoptic/carrot/M/

SOLIS data: https://solis.nso.edu/0/vsm/vsm_maps.php

GONG data: https://gong2.nso.edu/archive/run_quick_products?dpname=mrnqs_l&drname=83.202.190.79_200625122252&query_result_type=s&menutype=z&calendar=y&long_name=Integral%20synoptic%20map%20FITS%20data

We have both PYTHON and IDL code for the generation of the butterfly diagram.

Running the python code:
1. In the terminal, type ipython
   
2. run the command: %edit final_butterfly_diagram.py
   
or simply run the command: python final_butterfly_diagram.py
It will generate plots for both polar field and the butterfly diagram.

Running the IDL code:

IDL>> .r bfly_Final.pro

IDL>> bfly_Final

It will generate a butterfly_diagram.sav file. Sav file contains the information regarding time,
latitude and the butterfly diagram. IDL code will also generate the plot for the polar field.
Then use the python program named plot_bfly.py to generate the butterfly diagram.

