import numpy as np
import matplotlib.pyplot as plt

# define the length and width of the sea floor
length = 2  
width = 4  

# define the depth of the sea floor
depth_center = 110  
slope = 1.5      

# create the coordinate system
x = np.linspace(-width / 2, width / 2, 100)
y = np.linspace(-length / 2, length / 2, 100)
X, Y = np.meshgrid(x, y)

depth = depth_center - X * np.tan(slope * np.pi / 180) * 1852

# plot the sea floor
plt.figure(figsize=(8, 4))
plt.contourf(X, Y, depth, cmap='viridis_r', levels=50)
plt.colorbar(label='Depth (meters)')
plt.xlabel('West-East (nautical miles)')
plt.ylabel('South-North (nautical miles)')
plt.title('Sea Floor Topography for Q3')
plt.savefig('seafloor_map_q3_2d.png', dpi=600)
plt.show()

# plot the sea floor with survey lines
plt.figure(figsize=(8, 4))
plt.contourf(X, Y, depth, cmap='viridis_r', levels=50)
plt.colorbar(label='Depth (meters)')

# location of the survey lines
d_list = [-3345.47820735791, -2728.13863105574, -2161.30231620619, -1640.83769646353, \
            -1162.95120029616, -724.159600336803, -321.264624774522, 48.6703542641958, \
            388.341725259541, 700.225290781423, 986.594313162101, 1249.53608389004, \
            1490.96713749622, 1712.64722082428, 1916.19211950368, 2103.08543511606, \
            2274.68939889608, 2432.25480078606, 2576.93010621533, 2709.76982705501, \
            2831.74220776229, 2943.73628273748, 3046.56835633331, 3140.98795274820, \
            3227.68327917127, 3307.28624199878, 3380.37705268441, 3447.48845679457, \
            3509.10961709348, 3565.68967896123, 3617.64104413237, 3665.34237661684, 3709.14136271275]

# location of the survey lines (analog) by searching
d_list_analog = [-3345.4782073578917, -2728.138631304272, -2161.302317293652, -1640.837697847851, \
                -1162.9512024483759, -724.159602888592, -321.2646279893, 48.670350591174895, \
                388.3417210974615, 700.2252860464971, 986.5943081297796, 1249.536078111164, \
                1490.9671317496222, 1712.647214452259, 1916.1921121039313, 2103.085427037708, \
                2274.689390985004, 2432.2547922530093, 2576.93009781026, 2709.7698183455386, \
                2831.7421986975587, 2943.736273137561, 3046.5683464445983, 3140.987942830554, \
                3227.683269063464, 3307.286232129565, 3380.3770423331175, 3447.4884464659604, \
                3509.1096064963253, 3565.689668408862, 3617.641034070483, 3665.342366162768, 3709.1413519301327]

x_values = list(map(lambda x: x/1852, d_list))
x_values_analog = list(map(lambda x: x/1852, d_list_analog))

# plot the dividing line
plt.plot([-2, 2], [0, 0], color='white', linewidth=2.0)

# plot the survey lines by modeling
for x_val in x_values:
    plt.plot([x_val, x_val], [0.01, 1], color='white', linewidth=1.0)
    
# define the dash style
custom_dash = [10, 4, 6, 4]
# plot the survey lines by searching
for x_val in x_values_analog:
    plt.plot([x_val, x_val], [-1, -0.01], color='white', linewidth=1.0, linestyle=(0, custom_dash), dash_capstyle='round')

plt.xlabel('West-East (nautical miles)')
plt.ylabel('South-North (nautical miles)')
plt.xlim(-2, 2)
plt.title('Sea Floor Topography for Q3 with survey lines')
plt.savefig('seafloor_map_q3_lines.png', dpi=600)
plt.show()