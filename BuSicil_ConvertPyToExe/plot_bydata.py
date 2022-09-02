# importing the required module 
import matplotlib.pyplot as plt 
import pandas as pd

nama_file = input("Masukkan nama file: ")
data = pd.read_excel(nama_file)

x_label = input("Nama Sumbu X: ")
y_label = input("Nama Sumbu Y: ")

judul_grafik = input("Nama grafik: ")
    
# plotting the points  
plt.plot(data['x'], data['y']) 
    
# naming the x axis 
plt.xlabel(x_label) 
# naming the y axis 
plt.ylabel(y_label) 
    
# giving a title to my graph 
plt.title(judul_grafik) 
    
# function to show the plot 
plt.show() 