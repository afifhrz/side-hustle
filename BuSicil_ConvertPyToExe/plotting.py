# importing the required module 
import matplotlib.pyplot as plt 

panjang_data = int(input("Silahkan input banyak data yang akan disimpan: "))
x = [] #type data list
y = [] #type data list

for data in range(panjang_data):
    x.append(int(input("Masukkan nilai x: ")))
    y.append(int(input("Masukkan nilai y: ")))

x_label = input("Nama Sumbu X: ")
y_label = input("Nama Sumbu Y: ")

judul_grafik = input("Nama grafik: ")
    
# plotting the points  
plt.plot(x, y) 
    
# naming the x axis 
plt.xlabel(x_label) 
# naming the y axis 
plt.ylabel(y_label) 
    
# giving a title to my graph 
plt.title(judul_grafik) 
    
# function to show the plot 
plt.show() 