
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Title and description
st.title("Collinearity Checker for 3D Points")
st.write("Enter coordinates for three points in 3D space to check if they are collinear and visualize them.")

# Input fields for point coordinates
A_x = st.number_input("A_x", value=1.0)
A_y = st.number_input("A_y", value=2.0)
A_z = st.number_input("A_z", value=3.0)
B_x = st.number_input("B_x", value=2.0)
B_y = st.number_input("B_y", value=3.0)
B_z = st.number_input("B_z", value=9.0)
C_x = st.number_input("C_x", value=1.0)
C_y = st.number_input("C_y", value=2.0)
C_z = st.number_input("C_z", value=7.0)

# Defining the points as numpy arrays
A = np.array([A_x, A_y, A_z])
B = np.array([B_x, B_y, B_z])
C = np.array([C_x, C_y, C_z])

# Function to check if points are collinear
def son_colineales(A, B, C):
    AB = B - A
    AC = C - A
    # Use cross product to check collinearity
    return np.all(np.cross(AB, AC) == 0)

# Checking collinearity and displaying result
if son_colineales(A, B, C):
    st.write("The points are collinear.")
else:
    st.write("The points are not collinear.")

# Plotting the points in 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(*A, color='r', label="Point A")
ax.scatter(*B, color='g', label="Point B")
ax.scatter(*C, color='b', label="Point C")
ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], color='gray', linestyle='--')
ax.plot([A[0], C[0]], [A[1], C[1]], [A[2], C[2]], color='gray', linestyle='--')

# Setting labels
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
st.pyplot(fig)
