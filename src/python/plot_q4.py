import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.ticker as ticker
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# Read in the data
df = pd.read_csv('data_b.csv', header=None)
print(df.shape)
transposed = df.T
y_values = df.iloc[1:, 0].astype(float)
x_values = df.iloc[0, 1:].astype(float)
depth_data = df.iloc[1:, 1:].astype(float)

# draw 2d map
plt.figure(figsize=(2.51*4, 2.01*4)) 
ax = plt.axes()
# use plt.contourf to filling contours
contour = plt.contourf(x_values, y_values, depth_data, cmap='viridis_r', levels=20)

# add labels and title
plt.colorbar(label='Depth (meters)')
plt.xlabel('West-East (nautical miles)')
#ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
#plt.grid(which='both', alpha=0.9)
plt.ylabel('South-North (nautical miles)')
plt.title('Seafloor Map for Q4')
plt.savefig('seafloor_map_q4.png', dpi=600)
plt.show()

# draw 3d map
fig = plt.figure(figsize=(2.51*4, 2.01*4))
ax = fig.add_subplot(projection='3d')

# Make data.
X, Y = np.meshgrid(x_values, y_values)
Z = -depth_data

# Plot the 3d surface.
# cmap = coolwarm, viridis, magma, inferno, plasma, etc.
surf = ax.plot_surface(X, Y, Z, cmap=cm.viridis,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-200, 0)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# add color bar
cbar = fig.colorbar(surf, shrink=0.5, aspect=5)
cbar.set_label('depth (meters)')

# add labels and title
plt.xlabel('West-East (nautical miles)')
plt.ylabel('South-North (nautical miles)')
plt.clabel('Depth (meters)')
plt.title('3D Seafloor Map for Q4')
plt.savefig('seafloor_map_q4_3d.png', dpi=600)
plt.show()

# draw 2d map with survey lines
plt.figure(figsize=(2.51*4, 2.01*4)) 

# use plt.contourf to filling contours
contour = plt.contourf(y_values, x_values, depth_data, cmap='viridis_r', levels=20)

# read in the area_all.txt file that stores all survey lines
with open('area_all.txt', 'r') as f:
    lines = f.readlines()

# use regular expression to extract coordinates
coordinates = []
for line in lines:
    matches = re.findall(r'\((.*?), (.*?)\)', line)
    if matches:
        from_coords = (float(matches[0][0])/1852, float(matches[0][1])/1852)
        to_coords = (float(matches[1][0])/1852, float(matches[1][1])/1852)
        coordinates.append((from_coords, to_coords))

# plot the survey lines
for segment in coordinates:
    from_coords, to_coords = segment
    plt.plot([from_coords[0], to_coords[0]], [from_coords[1], to_coords[1]], color="white", linewidth=1.5)

# add labels and title
plt.colorbar(label='Depth (meters)')
plt.xlabel('West-East (nautical miles)')
plt.ylabel('South-North (nautical miles)')
plt.ylim(0, 5)
plt.xlim(0, 4)
plt.title('Seafloor Map for Q4')
plt.savefig('seafloor_map_q4_lines_A.png', dpi=600)
plt.show()