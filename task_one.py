import pandas as pd
import matplotlib.pyplot as plt

def get_file():

file_name = ("x_y_coordinates")
try:
  file_obj = open(file_name,"r")
  return file_obj

except FileNotFoundError:
      print("File not found.Please try again.")
      return get_file

def plot_data(file_obj):

    data = []
    for line in file_obj:
        values = line.strip().split()
        if len(values)==2:
            x,y = float(values[0]),float(values[1])
            data.append((x,y))

if data:
 x_values, y_values = zip(*data)
 plt.figure(figsize=(8,6))
 plt.scatter(x_values,y_values,c="blue")
 plt.xlabel("X")
 plt.ylabel("Y")
 plt.title("scatterplot of data")
 plt.grid(True)
 plt.legend()
 plt.show()

else:
    print("no data found in the file.)
