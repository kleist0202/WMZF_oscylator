# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 22:01:13 2020

@author: Michal
"""
import numpy as np
def Amplitudy(l):
    t=np.arrange(0,1,10)
    A0=20
    print('wpisz promień kuli R')
    R=float(input())
    print('wpisz masę kuli m ')
    m=float(input())
    A=A0*np.e**(-3*np.pi*R*l*t/m)
    return A 
def Energia(l):
    t=np.arrange(0,1,10)
    A0=20
    print('wpisz promień kuli R')
    R=float(input())
    print('wpisz masę kuli m ')
    m=float(input())
    print('wpis współczynnik sprężystosci k')
    k=float(input())
    E=0.5*k*A0**2*np.e**(-6*np.pi*R*l*t/m)
    return E
print(Amplitudy(7))
print(Energia(7))
   
    