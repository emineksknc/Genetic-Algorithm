# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:07:16 2020

@author: Emine
"""

#Kütüphanelerin import edilmesi
from Main import GeneticAlgoritm
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import pyplot as plt
import random
import numpy as np

#Rastgele renk üretmek için fonksiyon
def productColor():
    color = "#"
    for i in range(6):
        color = color + random.choice("ABCDEF0123456789")
    return  color

#Arayüzdeki,sonuçların gösterildiği plot ve tablonun oluşturulması için fonksiyon
def create_charts():
    
    global x1 #kullanıcıdan alınan çalıştırma sayısı
    x1 = int(entry1.get())
    global table1
    global table2
    global table3

    temp_color = []
    temp_iterSphere= []
    temp_maxSphere = []
    temp_iterGriewank = []
    temp_maxGriewank = []
    #Kullanıcıdan alınan değere göre çalıştırma sonuçlarını alma
    for i in range(x1):
        InitialPopulation,iterSphere, maxSphere,iterGriewank, maxGriewank= GeneticAlgoritm()
        temp_iterSphere.append(iterSphere)
        temp_maxSphere.append(maxSphere)
        
        temp_iterGriewank.append(iterGriewank)
        temp_maxGriewank.append(maxGriewank)
        
    #Her çalıştırma için farklı bir renk üretme
    for j in temp_iterSphere:
        color = productColor()
        temp_color.append(color)

    #Çalıştırma sayısına göre sphere tablosunun oluşturulması
    collabel=("Maksimum Değer","iterasyon sayısı")
    column1 = ["{}".format(i+1) for i in range(x1)]
    column2 = ["{}".format(i) for i in temp_maxSphere]
    column3 = ["{}".format(i) for i in temp_iterSphere]

    clust_data = np.array([column2, column3])
    fig1, ax = plt.subplots() 
    ax.set_axis_off() 
    table1 = ax.table( 
    cellText =  clust_data.transpose(),   
    colLabels = collabel, 
    rowLabels = column1,
    rowColours =  [j for j in temp_color],  
    cellLoc ='center',  
    loc ='upper left'
    )         
  

 

    #Çalıştırma sayısına göre griewank tablosunun oluşturulması
    collabel=("Maksimum Değer","iterasyon sayısı")
    column1 = ["{}".format(i+1) for i in range(x1)]
    column2 = ["{}".format(i) for i in temp_maxGriewank]
    column3 = ["{}".format(i) for i in temp_iterGriewank]

    clust_data = np.array([column2, column3])
    fig2, ax2 = plt.subplots() 
    ax2.set_axis_off() 
    table2 = ax2.table( 
    cellText =  clust_data.transpose(),   
    colLabels = collabel, 
    rowLabels = column1,
    rowColours =  [j for j in temp_color],  
    cellLoc ='center',  
    loc ='upper left'
    )         
  

    
    #Başlangıç değerleri tablosunu oluşturma
    temp = 0
    row_name = ['LB','UB','BinaryLB','BinaryUB', 'Chr(#)']

    col_value =['0', '63','000000','111111', '6']

    
    
    val11 = ["Initial Values"] 
    val22 = ["" + i for i in row_name] 
    val33 = [[""+ r for c in range(1)] for r in col_value] 
  

    
    fig3, ax3 = plt.subplots() 
    ax3.set_axis_off() 
    table3 = ax3.table( 
        cellText = val33, 
        rowLabels = val22,  

        cellLoc ='center',  
        rowLoc = 'right',
        loc ='upper left'
        )   
    
    
    
    ax3.set_title('Initial Values ', fontweight ="bold")
    table3 = FigureCanvasTkAgg(fig3, root)
    table3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
     

    ax.set_title('Results of runnning ' + str(x1) + ' times with Sphere Function', fontweight ="bold") 
    table1 = FigureCanvasTkAgg(fig1, root)
    table1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
    

    ax2.set_title('Results of runnning ' + str(x1) + ' times with Griewank Function', fontweight ="bold") 
    table2 = FigureCanvasTkAgg(fig2, root)
    table2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH,expand=1)
     
 


#Oluşturulan tabloların silinmesi için fonksiyon  
def clear_charts():
    table1.get_tk_widget().pack_forget()
    table2.get_tk_widget().pack_forget()
    table3.get_tk_widget().pack_forget()
            
    
root= tk.Tk()
root.title('Genetic Algorithm')
  
canvas1 = tk.Canvas(root, width = 800, height = 300)
canvas1.pack()

label1 = tk.Label(root, text='Genetic Algorithm')
label1.config(font=('Arial', 20))
canvas1.create_window(400, 50, window=label1)



label3 = tk.Label(root, text='Number of run:')  
label3.config(font=('Arial', 10))
canvas1.create_window(240, 100, window=label3)

#Butonların oluşturulması
entry1 = tk.Entry (root)
canvas1.create_window(360, 100, window=entry1) 
button1 = tk.Button (root, text='Create Charts',command=create_charts, bg='palegreen2', font=('Arial', 11, 'bold')) 
canvas1.create_window(360, 180, window=button1)

button2 = tk.Button (root, text='  Clear Charts  ', command=clear_charts, bg='lightskyblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(360, 220, window=button2)

button3 = tk.Button (root, text='Exit Application', command=root.destroy, bg='lightsteelblue2', font=('Arial', 11, 'bold'))
canvas1.create_window(360, 260, window=button3)
 
root.mainloop()