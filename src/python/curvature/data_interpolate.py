import numpy as np
import pandas as pd
from scipy.interpolate import griddata

# read the data
file_path = 'data_b.csv'
data = pd.read_csv(file_path, header=None)

# get the x and y coordinates
x_coords = data.iloc[0, 1:].values
y_coords = data.iloc[1:, 0].values
# get the depth data
Z = data.iloc[1:, 1:].values

# create the meshgrid
X, Y = np.meshgrid(x_coords, y_coords)

# create a more dense new grid
x_new = np.linspace(x_coords.min(), x_coords.max(), len(x_coords) * 10)
y_new = np.linspace(y_coords.min(), y_coords.max(), len(y_coords) * 10)
X_new, Y_new = np.meshgrid(x_new, y_new)

# interpolate the data to increase the density
Z_new = griddata((X.flatten(), Y.flatten()), Z.flatten(), (X_new, Y_new), method='cubic')

# save the new data
new_data = pd.DataFrame(Z_new, index=y_new, columns=x_new)
new_data.to_csv('data_b_interpolated.csv')