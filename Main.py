# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 16:28:20 2020

@author: Emine
"""
import random
from SphereFunction import *
from GriewankFunction import *

#Ondalık tabandaki sayıyı ikili tabana dönüştürme (Parametre Kodlama)
def DecimalToBinary(n):  
    return bin(n).replace("0b", "")

def GeneticAlgoritm():
    LB = 0
    UB = 63
    chromosome = 6


    # Parametre kodlama
    pUB = DecimalToBinary(63)
    gene = len(pUB)
    pLB = DecimalToBinary(0).zfill(gene)
   
    
    #Başlangıç popülasyonu oluşturma
    InitialPopulation = []
    for i in range(chromosome):
        tempGene = ""
        for j in range(gene):
            geneRandom = str(random.randint(0,1))
            tempGene += geneRandom
   

        InitialPopulation.append(tempGene)
    
    iterSphere, maxSphere= SphereFunction(InitialPopulation,chromosome)
    iterGriewank, maxGriewank = GriewankFunction(InitialPopulation, chromosome)
    

    return InitialPopulation,iterSphere, maxSphere,iterGriewank, maxGriewank


