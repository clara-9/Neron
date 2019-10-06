#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 16:36:41 2019

@author: raulf clarar
"""

import numpy as np
import datetime as datetime



def estimacio(l,num):      
    return np.exp(abs(num-((min(l)+max(l))/2))/((max(l)-min(l))/2))


WCC=[3500,11000]
RBC=[4300000,5900000]
Hmo=[12.5,17]
VCM=[70,100]
Glu=[70,110]
Cre=[70,110]
Ure=[0.6,1.5]
LDL=[0,130]
Leu=[4000,12000]
Cet=[0,5]
Nit=[0,0.05]
Pro=[0,20]
Leu=[30,40]
Bac=[0,5]
Sat=[95,100]
RPM=[60,170]

now=datetime.datetime.now()

categories=['Hem','Bio','Ori','Car']




pacients=[]

for k in range(1,7):
    file=open('analitica%s.txt'%k,'r')
    
    info=file.readlines()
    pacient=info[0].split(',')[0]
#Defenim el diccionari amb el nom del/de la pacient  
    exec('%s={}'%pacient)
    
    for cat in categories:
        exec('%s_%s={}'%(cat,pacient))
    pacients.append(pacient)
        

    persona=info[0][0:(len(info[0])-1)]
    eval(pacient)['data']=datetime.datetime(int(persona.split(',')[1]),int(persona.split(',')[2]),
                           int(persona.split(',')[3]),int(persona.split(',')[4]),
                           int(persona.split(',')[5]))
    
    for i in info[1::]:
        i=i[0:len(i)-1]
        if i in categories:
            cate=i
        else:
            eval('%s_%s'%(cate,pacient))['%s'%i.split(',')[0]]=float(i.split(',')[1])

        
        
        





    rest=[0]
    for cat in categories:
        for test in eval('%s_%s'%(cat,pacient)):
            res=estimacio(eval(test),eval('%s_%s'%(cat,pacient))['%s'%test])
            if res<=(np.exp(1)+0.0001):
                res=0.0
            else:
                res=res-np.exp(1)
            if res>max(rest):
                testmax=test
            rest.append(res)
    totaldolents=0
    for i in rest:
        if i>0:
            totaldolents+=1
    eval(pacient)['suma']=sum(rest)
    eval(pacient)['pitjor']=testmax
    eval(pacient)['valorpitjor']=max(rest)
    eval(pacient)['testdolents']=totaldolents
    eval(pacient)['testtotals']=totaldolents/len(rest)

def prioritat(pacient):
    percent=pacient['testtotals']
    suma=pacient['suma']
    if percent>0.8 and suma>20:
        prioritat='ALTA'
    elif percent>50:
        if suma<5:
            prioritat='BAIX'
        elif suma<15:
            prioritat='MIG'
        else:
            prioritat='ALT'
    elif percent<20:
        if suma<10:
            prioritat='BAIX'
        elif suma<25:
            prioritat='MIG'
        else:
            prioritat='ALT'
    else:
        prioritat='BAIX'
    return prioritat
        
for i in pacients:
    eval(i)['prioritat']=prioritat(eval(i))
            
            
    
#eval(i)['%s'%j],j,eval(j)
#%%
        
        
