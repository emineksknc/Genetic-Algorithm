# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 12:56:06 2020

@author: Emine
"""
import numpy as np
import random 
import math
import matplotlib.pyplot as plt
import pandas as pd

#Griewank function 
def fitnes_fun(population):
    population = [int(z, 2) for z in population]
    #print(population)
    y = []
    sum = 0
    product = 1
    insideCos = 0
    for k in population: # kromozom sayisi 
        sum = np.divide(1,4000)*(sum + np.power(k-100,2))
        
        insideCos = np.divide(k-100, np.sqrt(population.index(k)+1))
        insideCos = math.cos(insideCos) + 1
        product = product * insideCos
        result = sum - product
        y.append(result)
        
    result = sum - product
    return y,result

 #Aday kromozomları çaprazlama
def CrossingOver(newPopulation):
    tempNew = []  
    #0-3 kromozomlarının çaprazlanması
    crossOverPoint = random.randint(1,4)
    new0 = newPopulation[0][0:crossOverPoint] + newPopulation[3][crossOverPoint:6]
    tempNew.append(new0)
    new1 = newPopulation[3][0:crossOverPoint] + newPopulation[0][crossOverPoint:6]
    tempNew.append(new1)
    
    #1-4 kromozomlarının çaprazlanması
    crossOverPoint = random.randint(1,4)
    
    new2 = newPopulation[1][0:crossOverPoint] + newPopulation[4][crossOverPoint:6]
    tempNew.append(new2)
    new3 = newPopulation[4][0:crossOverPoint] + newPopulation[1][crossOverPoint:6]
    tempNew.append(new3)
    
    #2-5  kromozomlarının çaprazlanması
    crossOverPoint = random.randint(1,4)
    
    new4 = newPopulation[2][0:crossOverPoint] + newPopulation[5][crossOverPoint:6]
    tempNew.append(new4)
    new5 = newPopulation[5][0:crossOverPoint] + newPopulation[2][crossOverPoint:6]
    tempNew.append(new5)
    
    return tempNew
    
def RouletteWheelSelection(fitnessSum,fitnessValues,chromosome):
     #Rulet tekeri yüzdelerinin hesaplanması
     fitnessSum = 0
     for i in fitnessValues:
         fitnessSum = fitnessSum + abs(i)

     fitnessValues = [np.divide(np.multiply(abs(f),100),fitnessSum) for f in fitnessValues]

    #Rulet tekerine yerleştirme
     series = pd.Series(fitnessValues) 
    #kümülatif toplam yardımıyla rulet tekerinde ard arda yerleştirme
     cumsum = series.cumsum()
     

     newCandidate = []
    
    #Rulet tekerini kromozom sayısı kadar döndürme
     for i in range(chromosome):
        #rastgele değer alarak rulet tekerinde karşılığını bulma
        selectedchromosem = random.randint(0,100)
        temp = cumsum.values.tolist()
      
        
        for i in temp:
            if 0 <= selectedchromosem <= temp[0]:
                newCandidate.append(temp.index(i))
        
            elif temp[0] < selectedchromosem <=temp[1]:
                 newCandidate.append(temp.index(i))
                
            elif temp[1] < selectedchromosem <=temp[2]:
                 newCandidate.append(temp.index(i))
                 
                 
            elif temp[2] < selectedchromosem <=temp[3]:
                 newCandidate.append(temp.index(i))
                 
            elif temp[3] < selectedchromosem <=temp[4]:
                 newCandidate.append(temp.index(i))
                 
            elif temp[4] < selectedchromosem <=temp[5]:
                 newCandidate.append(temp.index(i))

     return newCandidate
    

   

def GriewankFunction(InitialPopulation,chromosome):
    #print(InitialPopulation)
    #Başlangıç popülasyonunun uygunluk değerlerinin hesaplanması  
    fitnessValues, fitnessSum = fitnes_fun(InitialPopulation)
    newCandidate = RouletteWheelSelection(fitnessSum,fitnessValues,chromosome)
    
    #Başlangıç popülasyonundan aday kromozomların seçilmesi
    newPopulation = []
    [newPopulation.append(InitialPopulation[n]) for n in newCandidate]
    
    #Seçilen aday kromozomların çaprazlanması
    newPopulation = CrossingOver(newPopulation)


    iterNum  = 0
   
    for i in range(100):
        newfitnessValues, newfitnessSum = fitnes_fun(newPopulation)
  
        newCandidate = RouletteWheelSelection(fitnessSum,fitnessValues,chromosome)
  
        #Yeni popülasyondan aday kromozomların seçilmesi
        [newPopulation.append(newPopulation[n]) for n in newCandidate]
        
        #100 iterasyon içerisinde maksimum değeri bulunca dur!
        if '111111' in newPopulation:
            break
        
        #Maksimum değer bulunamazsa iterasyon sayısını bitir dur!
        else:
            #Seçilen aday kromozomların çaprazlanması
            newPopulation = CrossingOver(newPopulation)
        
            iterNum  +=1
            
    population = [int(z, 2) for z in newPopulation]
    if iterNum  < 100:
        result = "Maksimum değer " + str(iterNum) + ". iterasyonda bulundu."
        return iterNum , max(population)
    elif iterNum >= 100:
        result = "Maksimum değer 100 iterasyonda bulunamadı.Bulunan maksimum değer:" + str(max(population))
        return iterNum , max(population)
