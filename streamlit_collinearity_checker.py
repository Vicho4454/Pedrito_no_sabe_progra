from sympy.abc import x, y, z
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from sympy import Point3D, Plane, Line3D, Matrix

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

# Calcular la magnitud del vector normal
normal_vector_magnitude = Matrix(normal_vector).norm()
normal_vector_unit = Matrix(normal_vector) / normal_vector_magnitude  # Vector normal unitario

# Determinar un punto en el plano P2 usando la distancia λ
P2_point = A + lambda_value * normal_vector_unit  # Punto en el plano P2
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
fig.add_trace(go.Scatter3d(x=[float(A[0]), float(B[0]), float(C[0])],
                           y=[float(A[1]), float(B[1]), float(C[1])],
                           z=[float(A[2]), float(B[2]), float(C[2])],
                           mode='markers', marker=dict(size=5, color="blue"), name="Puntos A, B, C en P1"))

# Añadir el plano P1
x_vals = np.linspace(-10, 10, 10)
y_vals = np.linspace(-10, 10, 10)
X, Y = np.meshgrid(x_vals, y_vals)
# Convertir los coeficientes del plano P1 a valores flotantes
a1, b1, c1, d1 = float(plane_P1.equation().coeff(x)), float(plane_P1.equation().coeff(y)), float(
    plane_P1.equation().coeff(z)), float(plane_P1.equation().coeff(1))
if c1 != 0:
    Z_P1 = (-a1 * X - b1 * Y - d1) / c1
else:
    Z_P1 = np.zeros_like(X)
fig.add_trace(go.Surface(x=X, y=Y, z=Z_P1, opacity=0.5, colorscale="Blues", name="Plano P1"))

# Añadir el plano P2 paralelo a P1
a2, b2, c2, d2 = float(plane_P2.equation().coeff(x)), float(plane_P2.equation().coeff(y)), float(
    plane_P2.equation().coeff(z)), float(plane_P2.equation().coeff(1))
if c2 != 0:
    Z_P2 = (-a2 * X - b2 * Y - d2) / c2
else:
    Z_P2 = np.zeros_like(X)
fig.add_trace(go.Surface(x=X, y=Y, z=Z_P2, opacity=0.5, colorscale="Reds", name="Plano P2"))

# Añadir la recta L1 entre los puntos A y C en el plano P1
fig.add_trace(go.Scatter3d(x=[float(A[0]), float(C[0])],
                           y=[float(A[1]), float(C[1])],
                           z=[float(A[2]), float(C[2])],
                           mode='lines', line=dict(color="green", width=3), name="Recta L1 en P1"))

# Añadir la recta L2 en el plano P2, paralela a L1
fig.add_trace(go.Scatter3d(x=[float(L2_point[0]), float(L2_point[0] + (C[0] - A[0]))],
                           y=[float(L2_point[1]), float(L2_point[1] + (C[1] - A[1]))],
                           z=[float(L2_point[2]), float(L2_point[2] + (C[2] - A[2]))],
                           mode='lines', line=dict(color="purple", width=3), name="Recta L2 en P2"))

# Ajustes de la visualización
fig.update_layout(scene=dict(
    xaxis_title='X',
    yaxis_title='Y',
    zaxis_title='Z',
    xaxis=dict(nticks=10, range=[-10, 10]),
    yaxis=dict(nticks=10, range=[-10, 10]),
    zaxis=dict(nticks=10, range=[-10, 10])
), title="Visualización 3D de Planos y Rectas del Túnel")

st.plotly_chart(fig)
