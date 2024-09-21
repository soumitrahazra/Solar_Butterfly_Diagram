
pro fitsdata, filename, data, byteswap=byteswap
data= readfits(filename)
end

pro magbfly
  drive='/home/soumitra/Final_Study/Butterfly_diagram_final_plot/Final_Plot/'
;goto, data

bfly=fltarr(615,180) 
mask=fltarr(360,180)
;KPNO data from CR 1625 TO 1639
cr_start1=1625
cr_end1=1639
;KITT Peak National Observatory (KPNO) data from CR 1645 to 2007
cr_start2=1645
cr_end2=2007
;SOLIS data from CR 2008 to 2014
cr_start3=2008
cr_end3=2014
; MDI data is from CR 2015 to 2017
cr_start4=2015
cr_end4=2017
;SOLIS data is from CR 2018 TO 2025
cr_start5= 2018
cr_end5= 2025
;MDI data for CR 2026
cr_start6=2026
;SOLIS data is from CR 2027 to 2034
cr_start7= 2027
cr_end7=2034
;MDI data is for CR 2035
cr_start8= 2035
;SOLIS dara is from CR 2036 to 2039
cr_start9= 2036
cr_end9=2039
; MDI data is from CR 2040 to 2042
cr_start10= 2040
cr_end10=2042
;SOLIS data is from CR 2043 to 2058
cr_start11=2043
cr_end11= 2058
;GONG data is from CR 2059 to 2188
cr_start12= 2059
cr_end12=2188
;SOLIS data is for CR 2189
cr_start13 = 2189
;GONG data is from CR 2190 to 2230
cr_start14=2190
cr_end14=2230 


date=fltarr(cr_end14 - 1623 + 1)
North=fltarr(cr_end14 - 1623 + 1)
South=fltarr(cr_end14 - 1623 + 1)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; Loop through series of images
;

path= drive + '/data1/'
files1= findfile(path + '*.fits')
n_files1= n_elements(files1)
cr= cr_start1
  for cs=0,(n_files1 -1L) do begin
;
; Read in Kitt Peak National Observatory
; magnetic field synoptic map data.
;
    fitsdata, files1[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
; Loop through series of images
;
path= drive + '/data2/'
files2= findfile(path + '*.fits')
n_files2= n_elements(files2)
cr= cr_start2
  for cs=0,(n_files2 -1L) do begin
;
; Read in Kitt Peak National Observatory
; magnetic field synoptic map data.
;
    fitsdata, files2[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor  

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; Loop through series of images
;
path= drive + '/data3/'
files3= findfile(path + '*.fits')
n_files3= n_elements(files3)
cr= cr_start3
  for cs=0,(n_files3 -1L) do begin
;
; Read in SOLIS integral Synoptic map data
; magnetic field synoptic map data.
;
    fitsdata, files3[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor  

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; MDI Data
;

path= drive + '/data4/'
files4= findfile(path + '*.fits')
n_files4= n_elements(files4)
cr= cr_start4
  for cs=0,(n_files4 -1L) do begin

; Read in SOHO/MDI
; magnetic field synoptic map data.
;    fitsdata,path+'synop_M_0.'+rotation+'.fits',map2,/byteswap
    fitsdata,files4[cs],map2,/byteswap
    index=where(map2 lt -3000.,count)
    if (count ne 0) then map2(index)=0.
;
; Line-of-sight to radial conversion (Needs B-angle correction)
;
;    los2r=map2
;    for j=0,1079 do los2r(*,j)=1.1*550./sqrt(550.*550. - (j-540.)*(j-540.))
;    map2=los2r*map2

; New data has this conversion done

;
; Blur to KPNO resolution (10 by 6)
;
    kernal=fltarr(15,9)
    kernal(*,*)=1./(15.*9.)
    map2=convol(map2,kernal)
;
; Resize to KPNO standard
;
    map=congrid(map2,360,180,cubic=-0.5)
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr=cr+1
  endfor

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;SOLIS data
; Loop through series of images
;
path= drive + '/data5/'
files5= findfile(path + '*.fits')
n_files5= n_elements(files5)
cr= cr_start5
  for cs=0,(n_files5 -1L) do begin
;
; Read in SOLIS integral Synoptic map data
; magnetic field synoptic map data.
;
    fitsdata, files5[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor  

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; MDI Data
;

path= drive + '/data6/'
files6= findfile(path + '*.fits')
n_files6= n_elements(files6)
cr= cr_start6
  for cs=0,(n_files6 -1L) do begin

; Read in SOHO/MDI
; magnetic field synoptic map data.
;    fitsdata,path+'synop_M_0.'+rotation+'.fits',map2,/byteswap
    fitsdata,files6[cs],map2,/byteswap
    index=where(map2 lt -3000.,count)
    if (count ne 0) then map2(index)=0.
;
; Line-of-sight to radial conversion (Needs B-angle correction)
;
;    los2r=map2
;    for j=0,1079 do los2r(*,j)=1.1*550./sqrt(550.*550. - (j-540.)*(j-540.))
;    map2=los2r*map2

; New data has this conversion done

;
; Blur to KPNO resolution (10 by 6)
;
    kernal=fltarr(15,9)
    kernal(*,*)=1./(15.*9.)
    map2=convol(map2,kernal)
;
; Resize to KPNO standard
;
    map=congrid(map2,360,180,cubic=-0.5)
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr=cr+1
  endfor

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;SOLIS data
; Loop through series of images
;
path= drive + '/data7/'
files7= findfile(path + '*.fits')
n_files7= n_elements(files7)
cr= cr_start7
  for cs=0,(n_files7 -1L) do begin
;
; Read in SOLIS integral Synoptic map data
; magnetic field synoptic map data.
;
    fitsdata, files7[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; MDI Data
;
path= drive + '/data8/'
files8= findfile(path + '*.fits')
n_files8= n_elements(files8)
cr= cr_start8
  for cs=0,(n_files8 -1L) do begin

; Read in SOHO/MDI
; magnetic field synoptic map data.
;    fitsdata,path+'synop_M_0.'+rotation+'.fits',map2,/byteswap
    fitsdata,files8[cs],map2,/byteswap
    index=where(map2 lt -3000.,count)
    if (count ne 0) then map2(index)=0.
;
; Line-of-sight to radial conversion (Needs B-angle correction)
;
;    los2r=map2
;    for j=0,1079 do los2r(*,j)=1.1*550./sqrt(550.*550. - (j-540.)*(j-540.))
;    map2=los2r*map2

; New data has this conversion done

;
; Blur to KPNO resolution (10 by 6)
;
    kernal=fltarr(15,9)
    kernal(*,*)=1./(15.*9.)
    map2=convol(map2,kernal)
;
; Resize to KPNO standard
;
    map=congrid(map2,360,180,cubic=-0.5)
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr+1
  endfor

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;SOLIS data
; Loop through series of images
;
path= drive + '/data9/'
files9= findfile(path + '*.fits')
n_files9= n_elements(files9)
cr= cr_start9
  for cs=0,(n_files9 -1L) do begin
;
; Read in SOLIS integral Synoptic map data
; magnetic field synoptic map data.
;
    fitsdata, files9[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; MDI Data
;
path= drive + '/data10/'
files10= findfile(path + '*.fits')
n_files10= n_elements(files10)
cr= cr_start10
  for cs=0,(n_files10 -1L) do begin

; Read in SOHO/MDI
; magnetic field synoptic map data.
;    fitsdata,path+'synop_M_0.'+rotation+'.fits',map2,/byteswap
    fitsdata,files10[cs],map2,/byteswap
    index=where(map2 lt -3000.,count)
    if (count ne 0) then map2(index)=0.
;
; Line-of-sight to radial conversion (Needs B-angle correction)
;
;    los2r=map2
;    for j=0,1079 do los2r(*,j)=1.1*550./sqrt(550.*550. - (j-540.)*(j-540.))
;    map2=los2r*map2

; New data has this conversion done

;
; Blur to KPNO resolution (10 by 6)
;
    kernal=fltarr(15,9)
    kernal(*,*)=1./(15.*9.)
    map2=convol(map2,kernal)
;
; Resize to KPNO standard
;
    map=congrid(map2,360,180,cubic=-0.5)
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr+1
  endfor


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;SOLIS data
; Loop through series of images
;
path= drive + '/data11/'
files11= findfile(path + '*.fits')
n_files11= n_elements(files11)
cr= cr_start11
  for cs=0,(n_files11 -1L) do begin
;
; Read in SOLIS integral Synoptic map data
; magnetic field synoptic map data.
;
    fitsdata, files11[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;GONG data
; Loop through series of images
;
path= drive + '/data12/'
files12= findfile(path + '*.fits')
n_files12= n_elements(files12)
cr= cr_start12
  for cs=0,(n_files12 -1L) do begin
;
; Read in SOLIS integral Synoptic map data
; magnetic field synoptic map data.
;
    fitsdata, files12[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;SOLIS data
; Loop through series of images
;
path= drive + '/data13/'
files13= findfile(path + '*.fits')
n_files13= n_elements(files13)
cr= cr_start13
  for cs=0,(n_files13 -1L) do begin
;
; Read in SOLIS integral Synoptic map data
; magnetic field synoptic map data.
;
    fitsdata, files13[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;GONG data
; Loop through series of images
;
path= drive + '/data14/'
files14= findfile(path + '*.fits')
n_files14= n_elements(files14)
cr= cr_start14
  for cs=0,(n_files14 -1L) do begin
;
; Read in SOLIS integral Synoptic map data
; magnetic field synoptic map data.
;
    fitsdata, files14[cs],map1,/byteswap
    map=float(map1)
    mask(*,*)=1.0
    index=where(map le -3200.,count)
    if (count ne 0) then mask(where(map le -3200.))=0.
    map=mask*map
    ave=total(map,1, /nan)/360.
    bfly(cr-1623,*)=ave
    cr= cr +1
  endfor 


dates=fltarr(615,180)
latitude=fltarr(615,180)
for i =0, 614L do begin
  for j=0, 179L do begin
	  dates(i,j) = 1975.0 + i*(27.27/365.25)
	  lat = -1.0 + j*(2.0/179.0)
          latitude(i,j)= asin(lat)*180/!pi
endfor
 endfor

save, dates, latitude, bfly, filename='butterfly_diagram_data.sav' 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Extract polar fields (average above 70 degrees - top and bottom 5 pixels)
; Extract polar fields (average above 55 degrees - top and bottom 14 pixels)
;
  npix=14
  openw,1,drive + '\sunspots\PolarFields.txt'
  printf,1,'Date  North   South'
  for cr=1623,cr_end14 do begin
    date(cr-1623)=1975.0 + 27.27*(cr-1623)/365.25
    North(cr-1623)=total(bfly(cr-1623,180-npix:179))/npix
    South(cr-1623)=total(bfly(cr-1623,0:npix-1))/npix
    printf,1,date(cr-1623), North(cr-1623),South(cr-1623)
  endfor
  close,1
;
; Plot Polar Fields plot
;
  set_plot,'ps'
    device,filename=drive + '\sunspots\PolarFields.ps'
    device,/TIMES,FONT_SIZE=12
    device,/PORTRAIT
    !p.font=0
    !p.thick=3.0
    plot,date,North,$
      title='Field Strength Poleward of 55 Degrees',$
      xstyle=1,xrange=[1976.,2020.],xtitle='Date',$
      ystyle=1,yrange=[-20.,20.],ytitle='Polar Field (Gauss)'
    oplot,date,South,line=2
    oplot,[1976.,2020.],[0.,0.]
    xyouts,2015.2,17.5,'North'
    xyouts,2015.2,15.5,'South'
  device,/close

  stop
end
