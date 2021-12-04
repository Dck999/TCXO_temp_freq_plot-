import pandas as pd
from test_find_path import *
import matplotlib.pyplot as plt
import numpy as np

def collect_tcxo_temp_vs_freq():
    dict = {}
    index = 0
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
        
        dict[str(index)] = arrary1
        index = index + 1
        dict[str(index)] = arrary2
        index = index + 1
        dict[str(index)] = arrary3
        index = index + 1
        
    df = pd.DataFrame(dict)
    df.to_csv('tcxo_temp/result.csv')


def plot_tcxo_temp_ppm():
    index=0
    brandname=['Rackon8','TXC8','TXC7','TXC6','TXC4','TXC3','TXC2','TXC1']
    brandname_index = 0
    
    plt.figure(figsize=(20,10)) #控制視窗大小
    for i in range(8):

        arrary1 = []
        arrary2 = []
        
        df = pd.read_csv('tcxo_temp/result.csv')
        df.drop(['Unnamed: 0'],axis=1,inplace=True)
        df.drop([0,1,2],axis=0,inplace=True)
        
        for Temp in df[str(index+1)]:
            arrary1.append(float(Temp))
        for ppm in df[str(index+2)]:
            arrary2.append(float(ppm))
            
        plt.plot(arrary1,arrary2,label=brandname[brandname_index]) #將每一組plot
        plt.legend(loc=2, bbox_to_anchor=(1.01,0.7),borderaxespad = 0.) #將每一組的lable 放到外面
        index = index +3
        brandname_index = brandname_index + 1
    
    plt.xlim(-40, 100) #設定x軸範圍
    plt.ylim(-0.5, 0.5)#設定y軸範圍
    
    my_x_ticks = np.arange(-40, 100, 5) #設定x軸刻度
    my_y_ticks = np.arange(-0.5, 0.5,0.1)  #設定y軸刻度
    plt.xticks(my_x_ticks)
    plt.yticks(my_y_ticks)
    
    plt.grid(b=True, which='major', color='#666666', linestyle='-.') # 格線
    
    plt.title("Temperature - Frequency Deviation",fontsize=20) #lable
    plt.xlabel("Temperature (Degree C)",fontsize=20)
    plt.ylabel("Temperature Deviation (ppm)",fontsize=20)
    
    plt.show()



plot_tcxo_temp_ppm()
