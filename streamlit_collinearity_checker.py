import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import Point3D, Plane, Line3D

# Título y descripción de la aplicación
st.title("Cálculo y Visualización para el Problema 2")
st.write("""
Esta aplicación calcula y representa los elementos geométricos para la construcción de un túnel en el espacio 3D.
Usaremos los puntos dados para calcular los planos, las rectas y los pilares del túnel.
""")

# Coordenadas de los puntos A, B, y C
A = Point3D(1, 2, 3)
B = Point3D(2, 3, 9)
C = Point3D(1, 2, 7)

# 1. Cálculo del vector normal del plano P1 que contiene A, B y C
plane_P1 = Plane(A, B, C)
normal_vector = plane_P1.normal_vector
st.write(f"Vector normal del plano P1: {normal_vector}")

# 2. Ecuación del plano P1
st.write(f"Ecuación del plano P1: {plane_P1.equation()}")

# 3. Distancia entre planos
lambda_value = st.slider("Seleccione la distancia entre los planos P1 y P2 (λ)", 5.0, 6.0, 5.5)

# Plano P2 paralelo a P1 y a una distancia λ de P1
P2_point = A + lambda_value * normal_vector.unit
plane_P2 = Plane(P2_point, normal_vector)
st.write(f"Ecuación del plano P2: {plane_P2.equation()}")

# 4. Recta L1 que contiene los puntos A y C
line_L1 = Line3D(A, C)
st.write(f"Ecuación de la recta L1: {line_L1.equation()}")

# 5. Recta L2 en el plano P2 paralela a L1
L2_point = P2_point
line_L2 = Line3D(L2_point, L2_point + (C - A))
st.write(f"Ecuación de la recta L2: {line_L2.equation()}")

# Visualización 3D
fig = go.Figure()

# Añadir puntos A, B, C en el plano P1
fig.add_trace(go.Scatter3d(x=[A[0], B[0], C[0]], y=[A[1], B[1], C[1]], z=[A[2], B[2], C[2]],
                           mode='markers', marker=dict(size=5, color="blue"), name="Puntos A, B, C"))

# Añadir plano P1
x_vals = np.linspace(-10, 10, 10)
y_vals = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x_vals, y_vals)
Z_P1 = (-plane_P1.coefficients[0]*X - plane_P1.coefficients[1]*Y - plane_P1.coefficients[2])/plane_P1.coefficients[3]
fig.add_trace(go.Surface(x=X, y=Y, z=Z_P1, opacity=0.5, colorscale="Blues", name="Plano P1"))

# Añadir plano P2
Z_P2 = (-plane_P2.coefficients[0]*X - plane_P2.coefficients[1]*Y - plane_P2.coefficients[2])/plane_P2.coefficients[3]
fig.add_trace(go.Surface(x=X, y=Y, z=Z_P2, opacity=0.5, colorscale="Reds", name="Plano P2"))

# Añadir rectas L1 y L2
fig.add_trace(go.Scatter3d(x=[A[0], C[0]], y=[A[1], C[1]], z=[A[2], C[2]], mode='lines', name="Recta L1", line=dict(color="green")))
fig.add_trace(go.Scatter3d(x=[L2_point[0], L2_point[0] + (C[0] - A[0])], 
                           y=[L2_point[1], L2_point[1] + (C[1] - A[1])], 
                           z=[L2_point[2], L2_point[2] + (C[2] - A[2])], 
                           mode='lines', name="Recta L2", line=dict(color="purple")))

# Ajustes de la visualización
fig.update_layout(scene=dict(
    xaxis_title='X',
    yaxis_title='Y',
    zaxis_title='Z'
), title="Visualización 3D de Planos y Rectas del Túnel")

st.plotly_chart(fig)
