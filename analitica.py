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
Ure=[0.6,1.5]
Cre=[70,110]
LDL=[0,130]

rest=[]

now=datetime.datetime.now()

categories=['Hem','Bio']







for k in range(1,3):
    file=open('analitica%s.txt'%k,'r')
    
    info=file.readlines()
    pacient=info[0].split(',')[0]
#Defenim el diccionari amb el nom del/de la pacient  
    exec('%s={}'%pacient)
    
    for cat in categories:
        exec('%s_%s={}'%(cat,pacient))
        

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

        
        
        

#Leu=[4000,12000]




    for test in categories:
        for j in eval('%s_%s'%(test,pacient)):
            res=estimacio(eval(j),eval('%s_%s'%(test,pacient))['%s'%j])
            if res<=np.exp(1):
                res=0
            else:
                res=res-np.exp(1)
            rest.append(res)
            
    
#eval(i)['%s'%j],j,eval(j)
#%%
        
        
