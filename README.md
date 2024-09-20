# Solar Butterfly Diagram
This codes generate the solar butterfly diagram from observed synoptic maps. We have synoptic maps from different observatory. We have taken longitudinal average of these
synoptic maps and stacked together. Resulting plot is the butterfly diagram.

Oldest available synoptic data is from the KITT Peak National Solar Observatory. Resolution of KPNO synoptic map is 360*180. We have used KPNO synoptic map data from CR 1643 to CR
2007. We have used SOLIS and MDI data from CR 2008 to CR 2058. We have used mostly SOLIS data. However, SOLIS synoptic map data is missing sometimes. We filled that gap by MDI data.
Recently GONG synoptic map data is available. We have used GONG synoptic map data from CR 2059 to CR 2230.

Polar field is calculated by taking the average over 15 degrees in northern (165 degree to 180 degree colatitude) and southern (0 degree to 15 degree colatitude) hemispheres.

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

