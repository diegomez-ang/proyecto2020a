import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import pyplot as plt
import numpy as np

##worbook1= "grafica temperatura.xlsx"

df = pd.read_excel("grafica temperatura.xlsx")

valores = df[["HORA","TEMPERATURA"]]
ax = np.arange(0,24,1)
ax = valores.plot(x="HORA",y="TEMPERATURA",linewidth = 2,color = 'blue')
plt.title('Historial de temperatura')
plt.grid()
plt.show()