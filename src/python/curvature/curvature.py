import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SeaFloorAnalysis:
    def __init__(self, data):
        self.data = data
        self.x_coords = data.columns.to_numpy(dtype=float)
        self.y_coords = data.index.to_numpy(dtype=float)
        self.X, self.Y = np.meshgrid(self.x_coords, self.y_coords)
        self.Z = data.values
    
    def find_min_curvature(self, vertices):
        x_contour, y_contour = vertices[:, 0], vertices[:, 1]

        # calculate the curvature
        dx = np.gradient(x_contour)
        dy = np.gradient(y_contour)
        ddx = np.gradient(dx)
        ddy = np.gradient(dy)

        curvature = np.abs(ddx * dy - ddy * dx) / (dx**2 + dy**2)**1.5
        
        # set the first and last 5 points to inf
        curvature[:5] = np.inf
        curvature[-5:] = np.inf
        
        # set too small curvature to inf
        curvature[curvature < 1e-5] = np.inf
        
        # find the point with the minimum curvature
        min_curvature_index = np.argmin(curvature)        
        min_curvature_point = vertices[min_curvature_index]
        
        return min_curvature_point

    def plot_contour_and_3d(self, depth):
        
        # 2D Contour plot
        fig1 = plt.figure(figsize=(7, 7))
    
        contour = plt.contourf(self.x_coords, self.y_coords, self.Z, cmap='viridis_r')
        plt.colorbar(contour)

        contour_set = plt.contour(self.x_coords, self.y_coords, self.Z, levels=[depth], colors='red')
        contour_path = contour_set.get_paths()[0]
        vertices = contour_path.vertices
        
        min_curvature_x, min_curvature_y = self.find_min_curvature(vertices)
        plt.scatter(min_curvature_x, min_curvature_y, marker='x', color='red', label='Min Curvature Point')
        
        plt.legend()
        plt.title(f'2D Contour Plot at Depth {depth}')
        
        # save the plot
        plt.savefig('contour_plot_2D.png', dpi=600)
        
        # 3D plot
        fig2= plt.figure(figsize=(10, 7))
        ax2 = fig2.add_subplot(projection='3d')
        
        surf = ax2.plot_surface(self.X, self.Y, -self.Z, cmap='viridis', alpha=0.8)
        fig2.colorbar(surf)
        
        ax2.contour(self.X, self.Y, -self.Z, levels=[-depth], colors='red', linestyles='dashed')
        ax2.scatter(min_curvature_x, min_curvature_y, -depth, marker='x', color='red', label='Min Curvature Point')
        
        ax2.set_xlabel('X Coordinate')
        ax2.set_ylabel('Y Coordinate')
        ax2.set_zlabel('Depth')
        ax2.set_title(f'3D Plot of the Sea Floor Depth with Depth {depth} Contour')
        
        # rotate the default view 90 degrees in clockwise direction
        ax2.view_init(azim=45)
        
        plt.legend()
        plt.savefig('contour_plot_3D.png', dpi=600)
        
        plt.show()


# Load the data
file_path = 'data_b_interpolated.csv'
data = pd.read_csv(file_path, index_col=0)

# Initialize the SeaFloorAnalysis class
sea_floor_analysis = SeaFloorAnalysis(data)

# Example usage
depth = 50  # Replace this with the desired depth value
sea_floor_analysis.plot_contour_and_3d(depth)
