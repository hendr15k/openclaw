#!/usr/bin/env python3
from fpdf import FPDF
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------- PDF helpers ----------------
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        self.set_fill_color(66, 133, 244)
        self.rect(0, 0, 210, 15, 'F')
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 10)
        self.cell(60, 10, 'Lineare Algebra', 0, 0, 'L')
        self.cell(80, 10, 'Uebung: Geraden & Ebenen', 0, 0, 'C')
        self.cell(60, 10, f'Seite {self.page_no()}', 0, 0, 'R')
        self.set_text_color(0, 0, 0)
        self.ln(10)

    def chapter_title(self, title, color=(66, 133, 244)):
        self.set_font('Helvetica', 'B', 16)
        self.set_fill_color(color[0], color[1], color[2])
        self.set_text_color(255, 255, 255)
        self.cell(0, 12, title, 0, 1, 'L', 1)
        self.set_text_color(0, 0, 0)
        self.ln(5)

    def section_header(self, text):
        self.set_font('Helvetica', 'B', 13)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 8, text, 0, 1, 'L', 1)
        self.set_font('Helvetica', '', 11)
        self.ln(2)

    def tip_box(self, text):
        self.set_fill_color(255, 250, 230)
        self.set_draw_color(255, 200, 100)
        self.set_font('Helvetica', 'I', 10)
        self.multi_cell(180, 5, text, 1, 'L')
        self.set_font('Helvetica', '', 11)
        self.ln(2)

    def task_box(self, number, text, difficulty=1):
        colors = {1: (76, 175, 80), 2: (255, 193, 7), 3: (244, 67, 54)}
        color = colors.get(difficulty, colors[1])

        self.set_fill_color(color[0], color[1], color[2])
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 12)
        self.cell(18, 10, str(number), 0, 1, 'C', 1)

        # keep task text ASCII-only
        self.set_text_color(0, 0, 0)
        self.set_font('Helvetica', '', 11)
        self.multi_cell(180, 6, text)
        self.ln(4)

    def solution_start(self, number):
        self.set_fill_color(200, 220, 255)
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 8, f'Loesung {number}:', 0, 1, 'L', 1)
        self.set_font('Helvetica', '', 10)

    def solution_text(self, text):
        self.multi_cell(180, 5, text)
        self.ln(1)

    def formula_box(self, text):
        self.set_fill_color(245, 245, 255)
        self.set_draw_color(66, 133, 244)
        self.set_font('Courier', '', 10)
        self.multi_cell(180, 5, text, 1, 'L', 1)
        self.set_font('Helvetica', '', 11)
        self.ln(2)

# ------------- plotting utility -------------

def savefig(path):
    plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()


def plot_task1():
    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    A = np.array([2, 1, 3])
    B = np.array([5, 4, 9])

    ax.scatter(A[0], A[1], A[2], c='red', s=60, edgecolors='black')
    ax.scatter(B[0], B[1], B[2], c='blue', s=60, edgecolors='black')

    t = np.linspace(-0.2, 1.2, 200)
    line = A + np.outer(t, B - A)
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'g-', linewidth=3)

    ax.set_title('Aufg. 1: Gerade durch zwei Punkte', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)

    out = '/tmp/v4_plot_task1.png'
    savefig(out)
    return out


def plot_task2_plane_through_points():
    # P(1,0,2), Q(3,1,4), R(2,2,1)
    P = np.array([1, 0, 2])
    Q = np.array([3, 1, 4])
    R = np.array([2, 2, 1])
    v1 = Q - P
    v2 = R - P

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    # plane patch
    a = np.linspace(-0.3, 1.3, 12)
    b = np.linspace(-0.3, 1.3, 12)
    Agrid, Bgrid = np.meshgrid(a, b)
    pts = P[None, None, :] + Agrid[..., None] * v1[None, None, :] + Bgrid[..., None] * v2[None, None, :]

    ax.plot_surface(pts[..., 0], pts[..., 1], pts[..., 2], alpha=0.35, color='dodgerblue')

    ax.scatter(P[0], P[1], P[2], c='red', s=60, edgecolors='black', label='P')
    ax.scatter(Q[0], Q[1], Q[2], c='green', s=60, edgecolors='black', label='Q')
    ax.scatter(R[0], R[1], R[2], c='blue', s=60, edgecolors='black', label='R')

    ax.set_title('Aufg. 2: Ebene durch 3 Punkte', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task2.png'
    savefig(out)
    return out


def plot_task3_line_plane_intersection():
    P0 = np.array([2, 1, -1])
    u = np.array([1, 1, 2])

    Q0 = np.array([1, 0, 1])
    v1 = np.array([1, 1, 0])
    v2 = np.array([0, 1, 1])

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(-0.2, 1.8, 200)
    line = P0 + np.outer(t, u)
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'r-', linewidth=3)

    s, tt = np.meshgrid(np.linspace(-0.2, 1.6, 10), np.linspace(-0.2, 1.6, 10))
    plane = Q0[None, None, :] + s[..., None] * v1 + tt[..., None] * v2
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.35, color='dodgerblue')

    S = np.array([3, 2, 1])
    ax.scatter(S[0], S[1], S[2], c='green', s=90, marker='*', edgecolors='black', label='S')

    ax.set_title('Aufg. 3: Schnittpunkt Gerade-Ebene', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task3.png'
    savefig(out)
    return out


def plot_task6_distance_point_to_plane():
    P0 = np.array([1, 0, 0])
    a = np.array([2, 0, 1])
    b = np.array([1, 1, 0])
    n = np.cross(a, b)

    # point P(3,2,-1)
    P = np.array([3, 2, -1])
    F = P - (np.dot(n, P - P0) / np.dot(n, n)) * n

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    s, t = np.meshgrid(np.linspace(-0.5, 2.5, 10), np.linspace(-0.5, 2.5, 10))
    plane = P0[None, None, :] + s[..., None] * a + t[..., None] * b
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.35, color='dodgerblue')

    ax.plot([P[0], F[0]], [P[1], F[1]], [P[2], F[2]], 'g-', linewidth=3)
    ax.scatter(P[0], P[1], P[2], c='red', s=60, edgecolors='black', label='P')
    ax.scatter(F[0], F[1], F[2], c='green', s=60, edgecolors='black', label='F')

    ax.set_title('Aufg. 6: Abstand Punkt-Ebene', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task6.png'
    savefig(out)
    return out


def plot_task7_intersection_two_planes():
    # Derived intersection line: x=3+t, y=1+t, z=2+t
    # E1: x = (0,1,2) + r*(1,0,0) + s*(0,1,1) => x=r, y=1+s, z=2+s
    # E2: x - 2y + z = 3
    # shows both planes and intersection line

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    t = np.linspace(-0.5, 1.5, 200)
    line = np.vstack([3 + t, 1 + t, 2 + t]).T
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'g-', linewidth=3, label='Schnittgerade')

    # Plane E1: set parameters r and s
    r = np.linspace(-0.5, 2.5, 10)
    s = np.linspace(-0.5, 2.5, 10)
    Rgrid, Sgrid = np.meshgrid(r, s)
    # x=r, y=1+s, z=2+s
    X = Rgrid
    Y = 1 + Sgrid
    Z = 2 + Sgrid
    ax.plot_surface(X, Y, Z, alpha=0.25, color='dodgerblue')

    # Plane E2: choose grid for x and y, compute z = 3 - x + 2y
    xx = np.linspace(-0.5, 3.5, 10)
    yy = np.linspace(-0.5, 3.5, 10)
    XX, YY = np.meshgrid(xx, yy)
    ZZ = 3 - XX + 2 * YY
    ax.plot_surface(XX, YY, ZZ, alpha=0.18, color='orange')

    ax.set_title('Aufg. 7: Schnitt zweier Ebenen', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task7.png'
    savefig(out)
    return out


def plot_task8_angle_line_plane():
    # line direction u=(2,1,2); plane normal n=(3,4,5)
    u = np.array([2, 1, 2])
    n = np.array([3, 4, 5])

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    # plane patch near origin: x,v1,v2 with n dot=0
    v1 = np.array([4, -3, 0])
    v2 = np.cross(n, v1)
    s, t = np.meshgrid(np.linspace(-1.5, 1.5, 10), np.linspace(-1.5, 1.5, 10))
    plane = np.array([0, 0, 0])[None, None, :] + s[..., None] * v1 + t[..., None] * v2
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.25, color='dodgerblue')

    # line
    tt = np.linspace(-1.2, 1.2, 200)
    line = tt[:, None] * u
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'r-', linewidth=3, label='g')

    # normal vector
    n_unit = n / np.linalg.norm(n)
    ax.plot([0, n_unit[0]], [0, n_unit[1]], [0, n_unit[2]], 'g--', linewidth=3, label='Normalenrichtung')

    ax.scatter([0], [0], [0], c='k', s=20)

    ax.set_title('Aufg. 8: Winkel zwischen Gerade und Ebene', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task8.png'
    savefig(out)
    return out


def plot_task10_skew_distance():
    P_g = np.array([0, 0, 0])
    u_g = np.array([1, 0, 0])
    P_h = np.array([0, 1, 1])
    u_h = np.array([0, 1, 0])

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    r = np.linspace(-0.3, 1.8, 200)
    s = np.linspace(-0.3, 1.8, 200)
    g_line = P_g + np.outer(r, u_g)
    h_line = P_h + np.outer(s, u_h)

    ax.plot(g_line[:, 0], g_line[:, 1], g_line[:, 2], 'r-', linewidth=3, label='g')
    ax.plot(h_line[:, 0], h_line[:, 1], h_line[:, 2], 'b-', linewidth=3, label='h')

    # closest points for this configuration: A=(0,0,0) on g, B=(0,1,0) on h
    A = np.array([0, 0, 0])
    B = np.array([0, 1, 0])
    ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'g--', linewidth=3, label='Abstand')
    ax.scatter([A[0]], [A[1]], [A[2]], c='red', s=50, edgecolors='black')
    ax.scatter([B[0]], [B[1]], [B[2]], c='blue', s=50, edgecolors='black')

    ax.set_title('Aufg. 10: Windschiefe Geraden - Abstand', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task10.png'
    savefig(out)
    return out


def plot_task14_parallel_planes():
    # Planes parallel to 2x - y + 2z = 8 with distance 2 => d=6 and d=-6
    # We'll plot both planes and show origin

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    # Parameterize plane using x and y: solve for z from 2x - y + 2z = d => z = (d -2x + y)/2
    xx = np.linspace(-0.5, 3.5, 12)
    yy = np.linspace(-0.5, 3.5, 12)
    XX, YY = np.meshgrid(xx, yy)

    for d, color, alpha in [(6, 'dodgerblue', 0.22), (-6, 'orange', 0.22)]:
        ZZ = (d - 2 * XX + YY) / 2
        ax.plot_surface(XX, YY, ZZ, alpha=alpha, color=color)

    # origin
    ax.scatter([0], [0], [0], c='k', s=30, edgecolors='black', label='Ursprung')

    ax.set_title('Aufg. 14: Parallel-Ebenen im Abstand 2', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task14.png'
    savefig(out)
    return out


def plot_task15_triangle():
    A = np.array([1, 0, 0])
    B = np.array([0, 1, 0])
    C = np.array([0, 0, 1])

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    tri = np.array([A, B, C, A])
    ax.plot(tri[:, 0], tri[:, 1], tri[:, 2], 'b-', linewidth=3)

    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    verts = [[(A[0], A[1], A[2]), (B[0], B[1], B[2]), (C[0], C[1], C[2])]]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.35, facecolors='lightblue', edgecolors='blue'))

    ax.scatter([A[0]], [A[1]], [A[2]], c='red', s=55, edgecolors='black', label='A')
    ax.scatter([B[0]], [B[1]], [B[2]], c='green', s=55, edgecolors='black', label='B')
    ax.scatter([C[0]], [C[1]], [C[2]], c='blue', s=55, edgecolors='black', label='C')

    ax.set_title('Aufg. 15: Dreieck ABC', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task15.png'
    savefig(out)
    return out


def plot_task16_intersection():
    # g: x=(2,1,0)+r*(1,-1,1)
    P0 = np.array([2, 1, 0])
    u = np.array([1, -1, 1])

    # E: x=(0,0,1)+s*(2,0,-1)+t*(0,1,1)
    Q0 = np.array([0, 0, 1])
    v1 = np.array([2, 0, -1])
    v2 = np.array([0, 1, 1])

    A = np.column_stack([u, -v1, -v2])
    b = Q0 - P0
    r, s, t = np.linalg.solve(A, b)
    X = P0 + r * u

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    rr = np.linspace(float(r) - 1.0, float(r) + 1.0, 200)
    line = P0 + rr[:, None] * u
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'r-', linewidth=3, label='g')

    ss, tt = np.meshgrid(np.linspace(float(s) - 1.0, float(s) + 1.0, 10), np.linspace(float(t) - 1.0, float(t) + 1.0, 10))
    plane = Q0[None, None, :] + ss[..., None] * v1 + tt[..., None] * v2
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.3, color='dodgerblue')

    ax.scatter([X[0]], [X[1]], [X[2]], c='green', s=100, marker='*', edgecolors='black', label='S')

    ax.set_title('Aufg. 16: Schnittpunkt Gerade-Ebene', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task16.png'
    savefig(out)
    return out


def plot_task19_angle_between_planes():
    # E1: x - y + 2z = 4, E2: 2x + y - z = 1
    # plot both planes and their intersection line

    n1 = np.array([1, -1, 2])
    n2 = np.array([2, 1, -1])

    # intersection line param derived in analysis
    # z=t, x=(5-t)/3, y=(-7+5t)/3, direction (-1,5,3)
    t = np.linspace(-1.0, 2.0, 200)
    line = np.vstack([(5 - t) / 3, (-7 + 5 * t) / 3, t]).T

    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'g-', linewidth=3, label='Schnittlinie')

    # Plane E1: parameterize using x and z => y = x + 2z - 4
    xx = np.linspace(-0.5, 4.0, 12)
    zz = np.linspace(-0.5, 4.0, 12)
    XX, ZZ = np.meshgrid(xx, zz)
    YY = XX + 2 * ZZ - 4
    ax.plot_surface(XX, YY, ZZ, alpha=0.2, color='dodgerblue')

    # Plane E2: parameterize using x and z => from 2x + y - z = 1 => y = 1 - 2x + z
    XX2, ZZ2 = np.meshgrid(xx, zz)
    YY2 = 1 - 2 * XX2 + ZZ2
    ax.plot_surface(XX2, YY2, ZZ2, alpha=0.15, color='orange')

    # Show normal vectors at origin for intuition (not necessarily perpendicular at origin but direction is fine)
    n1u = n1 / np.linalg.norm(n1)
    n2u = n2 / np.linalg.norm(n2)
    ax.quiver([0, 0], [0, 0], [0, 0], [n1u[0], n2u[0]], [n1u[1], n2u[1]], [n1u[2], n2u[2]],
              length=1.5, colors=['green', 'red'], linewidths=2)

    ax.set_title('Aufg. 19: Winkel zwischen zwei Ebenen', fontsize=11, fontweight='bold')
    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=8)

    out = '/tmp/v4_plot_task19.png'
    savefig(out)
    return out


def diagram_parameter_2d():
    fig, ax = plt.subplots(figsize=(6.5, 2.9))
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.25)

    x = np.linspace(-1, 4, 100)
    y = x + 1
    ax.plot(x, y, 'b-', linewidth=3)

    pts = [(0, 1), (1, 2), (2, 3)]
    for px, py in pts:
        ax.scatter(px, py, c='red', s=90, edgecolors='black', zorder=5)

    ax.set_title('Idee: Gerade als P + r*u', fontsize=11, fontweight='bold')
    ax.set_xlabel('x', fontsize=10)
    ax.set_ylabel('y', fontsize=10)
    ax.set_aspect('equal')

    out = '/tmp/v4_diagram_param.png'
    savefig(out)
    return out


def diagram_distance_2d():
    fig, ax = plt.subplots(figsize=(6.5, 2.9))
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.25)

    x = np.linspace(-1, 4, 100)
    y = 2 * x + 1
    ax.plot(x, y, 'b-', linewidth=3)

    P = (1, 3)
    ax.scatter([P[0]], [P[1]], c='red', s=120, edgecolors='black', zorder=6)

    x_perp = np.linspace(0.5, 1.5, 50)
    y_perp = -0.5 * (x_perp - 1) + 3
    ax.plot(x_perp, y_perp, 'g--', linewidth=3)

    ax.scatter([P[0]], [P[1]], c='green', s=70, marker='x', zorder=7)

    ax.set_title('Idee: Abstand Punkt-Ebene (2D-Skizze)', fontsize=11, fontweight='bold')
    ax.set_xlabel('x', fontsize=10)
    ax.set_ylabel('y', fontsize=10)
    ax.set_aspect('equal')

    out = '/tmp/v4_diagram_dist.png'
    savefig(out)
    return out


# ---------------- main ----------------

def create_pdf():
    pdf = PDF()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_top_margin(20)
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font('Helvetica', '', 11)

    # Assets
    plot1 = plot_task1()
    plot2 = plot_task2_plane_through_points()
    plot3 = plot_task3_line_plane_intersection()
    plot6 = plot_task6_distance_point_to_plane()
    plot7 = plot_task7_intersection_two_planes()
    plot8 = plot_task8_angle_line_plane()
    plot10 = plot_task10_skew_distance()
    plot14 = plot_task14_parallel_planes()
    plot15 = plot_task15_triangle()
    plot16 = plot_task16_intersection()
    plot19 = plot_task19_angle_between_planes()

    diagram_param = diagram_parameter_2d()
    diagram_dist = diagram_distance_2d()

    # Title
    pdf.chapter_title('Aufgaben - Geraden und Ebenen im R3')
    pdf.set_font('Helvetica', 'I', 10)
    pdf.cell(0, 6, 'Mit mehr Skizzen zur schnellen Orientierung (Loesungen am Ende).', 0, 1, 'C')
    pdf.ln(4)

    # Concepts
    pdf.section_header('GRUNDKONZEPTE')
    pdf.ln(2)
    pdf.image(diagram_param, x=15, y=None, w=90)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(90, 6, 'Parameterdarstellung', 0, 0)
    pdf.image(diagram_dist, x=105, y=None, w=90)
    pdf.cell(0, 6, 'Abstand (Idee)', 0, 1)
    pdf.ln(10)

    # Skizzen: put a bunch of images (2 columns)
    pdf.section_header('SKIZZEN (zu ausgewahlten Aufgaben)')
    pdf.ln(2)

    images = [
        (plot1, 'Aufg. 1'),
        (plot2, 'Aufg. 2'),
        (plot3, 'Aufg. 3'),
        (plot6, 'Aufg. 6'),
        (plot7, 'Aufg. 7'),
        (plot8, 'Aufg. 8'),
        (plot10, 'Aufg. 10'),
        (plot14, 'Aufg. 14'),
        (plot15, 'Aufg. 15'),
        (plot16, 'Aufg. 16'),
        (plot19, 'Aufg. 19'),
    ]

    x_left, w_img = 15, 90
    x_right = 105
    # each block ~ 70 mm high
    block_h = 72

    # place first block
    for i, (img, cap) in enumerate(images):
        if i == 0:
            pdf.set_y(pdf.get_y() + 0)
        if i % 2 == 0:
            x = x_left
            y = pdf.get_y()
        else:
            x = x_right
            y = pdf.get_y() - 0  # same row

        if i > 0 and i % 2 == 0:
            # new row
            pdf.set_y(y + block_h)

        pdf.image(img, x=x, y=y, w=w_img)
        pdf.set_y(y + 52)
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(w_img, 6, cap, 0, 0, 'C')
        pdf.set_font('Helvetica', '', 11)

        if i % 2 == 1:
            pdf.set_y(y + block_h)

        # page safety
        if pdf.get_y() > 260:
            pdf.add_page()
            pdf.set_y(25)

    pdf.ln(10)

    # Tasks
    pdf.section_header('AUFGABEN')
    pdf.ln(2)

    tasks = [
        (1, 'Bestimmen Sie die Parameterdarstellung der Geraden g durch die Punkte A(2|1|3) und B(5|4|9).', 1),
        (2, 'Bestimmen Sie die Parameterdarstellung der Ebene E durch die Punkte P(1|0|2), Q(3|1|4) und R(2|2|1).', 1),
        (3, 'Gegeben sind die Gerade g: x = (2,1,-1) + r*(1,1,2) und die Ebene E: x = (1,0,1) + s*(1,1,0) + t*(0,1,1). Bestimmen Sie den Schnittpunkt S.', 2),
        (4, 'Pruefen Sie die Lagenbeziehung der beiden Geraden: g: x = (1,0,1) + r*(1,2,3), h: x = (2,1,3) + s*(2,4,6).', 1),
        (5, 'Wandeln Sie die Ebenengleichung in Parameterform um: E: 2x - y + 3z = 6.', 1),
        (6, 'Berechnen Sie den Abstand des Punktes P(3|2|-1) von der Ebene E: x = (1,0,0) + s*(2,0,1) + t*(1,1,0).', 2),
        (7, 'Bestimmen Sie die Schnittgerade der beiden Ebenen: E1: x = (0,1,2) + r*(1,0,0) + s*(0,1,1) und E2: x - 2y + z = 3.', 2),
        (8, 'Berechnen Sie den Winkel zwischen der Geraden g: x = (0,0,0) + r*(2,1,2) und der Ebene E: 3x + 4y + 5z = 0.', 2),
        (9, 'Bestimmen Sie eine Parameterdarstellung der Ebene E, die die Gerade g: x = (1,2,1) + r*(1,1,0) enthaelt und durch den Punkt P(2|0|1) geht.', 2),
        (10, 'Gegeben sind zwei windschiefe Geraden: g: x = (0,0,0) + r*(1,0,0), h: x = (0,1,1) + s*(0,1,0). Bestimmen Sie den kuerzesten Abstand.', 3),
        (11, 'Gegeben ist die Ebene E: x + y + z = 6 und der Punkt P(1|2|3). Bestimmen Sie den Fusspunkt des Lotes von P auf die Ebene E.', 2),
        (12, 'Geben Sie eine Parameterdarstellung der Ebene E: 2x - 3y + z = 4 an.', 1),
        (13, 'Bestimmen Sie die Parameterdarstellung der Geraden g, die orthogonal zur Ebene E: x - 2y + 2z = 5 ist und durch den Punkt P(1|0|1) geht.', 2),
        (14, 'Bestimmen Sie alle Ebenen, die parallel zur Ebene E: 2x - y + 2z = 8 sind und den Abstand 2 zum Ursprung haben.', 3),
        (15, 'Gegeben sind die Punkte A(1|0|0), B(0|1|0) und C(0|0|1). (a) Bestimmen Sie die Parameterdarstellung der Ebene durch A,B,C. (b) Flaeche des Dreiecks ABC.', 3),
        (16, 'Gegeben sind die Gerade g: x = (2,1,0) + r*(1,-1,1) und die Ebene E: x = (0,0,1) + s*(2,0,-1) + t*(0,1,1). Bestimmen Sie r,s,t im Schnittpunkt.', 2),
        (17, 'Bestimmen Sie eine Gerade g durch den Punkt P(1|2|3), die parallel zur Ebene E: x + y + z = 0 und parallel zur Geraden h: x = (0,0,0) + r*(1,1,0) verlaeuft.', 3),
        (18, 'Bestimmen Sie die Parameterdarstellung der Ebene, die die parallelen Geraden enthaelt: g: x = (1,0,1) + r*(1,1,2), h: x = (3,1,4) + s*(1,1,2).', 2),
        (19, 'Berechnen Sie den Winkel zwischen den Ebenen: E1: x - y + 2z = 4, E2: 2x + y - z = 1.', 2),
        (20, 'Bestimmen Sie die Schnittgerade der drei Ebenen: E1: x + y + z = 6, E2: x - y + z = 2, E3: x + y - z = 0. Pruefen Sie, ob es einen gemeinsamen Schnittpunkt gibt.', 3),
    ]

    tips = {
        1: 'Tipp: Richtungsvektor u = B - A.',
        3: 'Tipp: Gleichsetzen und lineares System nach r,s,t loesen.',
        6: 'Tipp: Normalenvektor n = a x b; dann Abstandsformel.',
        7: 'Tipp: E1 in Koordinatenform bringen und mit E2 kombinieren.',
        8: 'Tipp: Winkel Gerade-Ebene ueber |u·n| / (|u||n|).',
        10: 'Tipp: Abstand windschief: d = |(P2-P1)·(u1 x u2)| / |u1 x u2|.',
        14: 'Tipp: d bestimmt ueber Parallel-Ebenen-Abstand zum Ursprung.',
        15: 'Tipp: Flaeche = 0.5 * |u x v|.',
        16: 'Tipp: Schnitt line/ebene => 3x3 Gleichungssystem.',
        19: 'Tipp: cos(alpha) = |n1·n2|/(|n1||n2|).',
    }

    for num, txt, diff in tasks:
        pdf.task_box(num, txt, difficulty=diff)
        if num in tips:
            pdf.tip_box(tips[num])

    # Solutions at end (concise)
    pdf.add_page()
    pdf.chapter_title('Loesungen', color=(66, 180, 100))

    sol = {
        1: ['u = B - A = (3,3,6)', 'g: x = (2,1,3) + r*(3,3,6)'],
        2: ['u = Q-P, v = R-P', 'Ebene z.B.: x = P + s*u + t*v'],
        3: ['Gleichsetzen und System loesen', 'S = (3,2,1)'],
        4: ['u_h ist Vielfaches von u_g => parallel', 'Verschiebungsvektor ist kein Vielfaches => nicht identisch'],
        5: ['Koordinatenform 2x - y + 3z = 6; daraus Parameterform.',],
        6: ['n = a x b', 'Abstand d = 3/sqrt(6)'],
        7: ['Schnittgerade: x = 3+t, y = 1+t, z = 2+t', 'g: x = (3,1,2) + t*(1,1,1)'],
        8: ['cos(alpha)=4/(3*sqrt(2)) und beta = 90deg - alpha'],
        9: ['Ebene durch g und Punkt P aufspannen (u,v aus g + Verbindungsvektor)'],
        10: ['Abstand = 1 in der gegebenen Konfiguration'],
        11: ['Fusspunkt: F = (1,2,3)'],
        12: ['Normalenvektor n = (2,-3,1); Parameterform erstellen'],
        13: ['orthogonal => Richtungsvektor = n; g: x = P + r*n'],
        14: ['d = +/-6 => zwei Ebenen: 2x - y + 2z = 6 und -6'],
        15: ['a) Ebene: x = A + s*(B-A) + t*(C-A)', 'b) Flaeche = sqrt(3)/2'],
        16: ['r=2/5, s=6/5, t=3/5', 'Schnittpunkt S=(12/5,3/5,2/5)'],
        17: ['u = (nE x uh); daraus Gerade'],
        18: ['Ebene wird durch u=(1,1,2) und Verbindungsvektor v=(2,1,3) aufgespannt'],
        19: ['cos(alpha)=1/6 => alpha = arccos(1/6)'],
        20: ['Schnittpunkt S=(1,2,3) (Punkt), kein Schnitt in einer Geraden'],
    }

    for num in range(1, 21):
        pdf.solution_start(num)
        for line in sol[num]:
            pdf.solution_text(line)

    # cleanup plots
    for f in [plot1, plot2, plot3, plot6, plot7, plot8, plot10, plot14, plot15, plot16, plot19, diagram_param, diagram_dist]:
        try:
            os.remove(f)
        except Exception:
            pass

    return pdf


if __name__ == '__main__':
    pdf = create_pdf()
    out = '/home/openclaw/.openclaw/workspace/mathe/geraden-ebenen-uebung-final-v4.pdf'
    pdf.output(out)
    print('PDF erstellt:', out)
    print('Bytes:', os.path.getsize(out))
