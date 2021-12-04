import pandas as pd
from test_find_path import *
import csv

def collect_tcxo_temp_vs_freq():
    dict = {}
    index = 1
    for file in show_csv_file_nam(target_path):

        arrary1 = []
        arrary2 = []
        arrary3 = []
     
        df = pd.read_csv('tcxo_temp/' + file,names=['column1','column2','column3'])
        for freq in df['column1']:
            arrary1.append(freq)
        for temp in df['column2']:
            arrary2.append(temp)
        for ppm in df['column3']:
            arrary3.append(ppm)  
        
        dict[file+'freq'] = arrary1
        dict[file+'Temp'] = arrary2
        dict[file+'ppm'] = arrary3
        
    df = pd.DataFrame(dict)
    df.to_csv('tcxo_temp/result.csv')


v = open('tcxo_temp/result.csv')
r = csv.reader(v)
row0 = next(r)
row0.append(' ')
print(row0)
v.close()