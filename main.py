import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv('countries of the world.csv')

df.info()

fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")

ax.scatter3D(df.index, df['Area (sq. mi.)'], df['Population'])
#threedee.set_xlabel('GDP')
#threedee.set_ylabel('Area')
#threedee.set_zlabel('Pop.Density')
plt.show()