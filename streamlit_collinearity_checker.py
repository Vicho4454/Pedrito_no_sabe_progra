
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Title and description
st.title("3D Visualization of Planes, Lines, and Vectors")
st.write("This visualization includes two planes, two lines, a beam, and a 'sky' plane at z = 11.5.")

# Define points and vector normal
N1 = np.array([4, -4, 0])  # Normal vector for planes
point_on_plane1 = np.array([1, 1, -1])  # Point on P1
point_on_plane2 = np.array([1, 1, 7.778174593052024])  # Point on P2

# Define t parameter range for lines and beam
t_values = np.linspace(-5, 5, 100)

# Line L1: starting point and direction
L1_origin = np.array([1, 2, 3])
L1_direction = np.array([0, 0, 4])
L1_points = L1_origin + np.outer(t_values, L1_direction)

# Line L2: starting point and direction
L2_origin = np.array([4.8890873, -1.8890873, 3])
L2_direction = np.array([0, 0, 4])
L2_points = L2_origin + np.outer(t_values, L2_direction)

# Beam V: starting point and direction
V_origin = np.array([1, 2, 6])
V_direction = np.array([1, 0, 0])
V_points = V_origin + np.outer(t_values, V_direction)

# Define grid for planes P1 and P2
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z1 = (-N1[0] * X - N1[1] * Y - 4) / N1[2] if N1[2] != 0 else np.zeros_like(X)
Z2 = (-N1[0] * X - N1[1] * Y - 35.112698372208094) / N1[2] if N1[2] != 0 else np.zeros_like(X)

# Define the sky plane at z = 11.5
Z_sky = np.full_like(X, 11.5)

# Plotting all elements in 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot planes
ax.plot_surface(X, Y, Z1, color='cyan', alpha=0.5, rstride=100, cstride=100, edgecolor='none', label="Plane P1")
ax.plot_surface(X, Y, Z2, color='orange', alpha=0.5, rstride=100, cstride=100, edgecolor='none', label="Plane P2")
ax.plot_surface(X, Y, Z_sky, color='skyblue', alpha=0.3, rstride=100, cstride=100, edgecolor='none', label="Sky Plane")

# Plot lines L1 and L2
ax.plot(L1_points[:,0], L1_points[:,1], L1_points[:,2], color="blue", label="Line L1")
ax.plot(L2_points[:,0], L2_points[:,1], L2_points[:,2], color="purple", label="Line L2")

# Plot beam V
ax.plot(V_points[:,0], V_points[:,1], V_points[:,2], color="green", linestyle="--", label="Beam V")

# Vector normal N1
ax.quiver(0, 0, 0, N1[0], N1[1], N1[2], color="red", length=5, normalize=True, label="Normal Vector N1")

# Setting labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])
ax.set_zlim([-10, 15])

# Display legend and plot
ax.legend()
st.pyplot(fig)
