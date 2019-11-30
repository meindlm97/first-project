#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Berechnen der Quadratwurzel
"""

a = float(input("Zu berechnende Quadratwurzel: ")) 
x = 1
# float bedeutet, dass mit Kommazahlen gerechnet werden soll!  
print ("Iteration  Näherungswert") 
print ("_________________________")    
for i in range(1,6): 
  x = 0.5*(x+a/x) 
  print ('   ',i,'    ',x)
