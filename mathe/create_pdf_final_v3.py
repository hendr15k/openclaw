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
        # keep ASCII-only in title for Helvetica core font
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

    def task_box(self, number, text, difficulty=1, show_difficulty=False):
        # difficulty: 1=leicht,2=mittel,3=schwer
        colors = {1: (76, 175, 80), 2: (255, 193, 7), 3: (244, 67, 54)}
        color = colors.get(difficulty, colors[1])
        self.set_fill_color(color[0], color[1], color[2])
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 12)
        self.cell(12, 10, '', 0, 0)  # spacer
        # number badge
        self.cell(18, 10, str(number), 0, 1, 'C', 1)
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
        self.multi_cell(180, 5, text, 1, 'L')
        self.set_font('Helvetica', '', 11)
        self.ln(2)

# ---------------- plotting ----------------

def savefig(path):
    plt.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()


def create_plot_task1():
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    A = np.array([2, 1, 3])
    B = np.array([5, 4, 9])

    ax.scatter(A[0], A[1], A[2], c='red', s=60, edgecolors='black')
    ax.scatter(B[0], B[1], B[2], c='blue', s=60, edgecolors='black')

    t = np.linspace(-0.2, 1.2, 200)
    line = A + np.outer(t, B - A)
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'g-', linewidth=3)

    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.set_title('Aufg. 1: Gerade durch zwei Punkte', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.25)

    out = '/tmp/plot_v3_task1.png'
    savefig(out)
    return out


def create_plot_task3():
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    # line g: x=(2,1,-1)+r*(1,1,2)
    P0 = np.array([2, 1, -1])
    u = np.array([1, 1, 2])

    # plane E: x=(1,0,1)+s*(1,1,0)+t*(0,1,1)
    Q0 = np.array([1, 0, 1])
    v1 = np.array([1, 1, 0])
    v2 = np.array([0, 1, 1])

    t = np.linspace(-0.2, 1.8, 200)
    line = P0 + np.outer(t, u)
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'r-', linewidth=3, label='g')

    s, tt = np.meshgrid(np.linspace(-0.2, 1.6, 10), np.linspace(-0.2, 1.6, 10))
    plane = Q0[None, None, :] + s[..., None] * v1 + tt[..., None] * v2
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.35, color='dodgerblue')

    S = np.array([3, 2, 1])
    ax.scatter(S[0], S[1], S[2], c='green', s=110, marker='*', edgecolors='black', label='S')

    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.set_title('Aufg. 3: Schnittpunkt Gerade-Ebene', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.25)

    out = '/tmp/plot_v3_task3.png'
    savefig(out)
    return out


def create_plot_task6():
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    # Plane: x=(1,0,0)+s*(2,0,1)+t*(1,1,0)
    P0 = np.array([1, 0, 0])
    a = np.array([2, 0, 1])
    b = np.array([1, 1, 0])
    n = np.cross(a, b)

    # Point P
    P = np.array([3, 2, -1])

    # Foot F = P - ((n·(P-P0))/|n|^2) n
    F = P - (np.dot(n, P - P0) / np.dot(n, n)) * n

    # plot plane patch
    s, t = np.meshgrid(np.linspace(-0.5, 2.5, 10), np.linspace(-0.5, 2.5, 10))
    plane = P0[None, None, :] + s[..., None] * a + t[..., None] * b
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.35, color='dodgerblue')

    # plot perpendicular segment P-F
    ax.plot([P[0], F[0]], [P[1], F[1]], [P[2], F[2]], 'g-', linewidth=3)
    ax.scatter(P[0], P[1], P[2], c='red', s=60, edgecolors='black', label='P')
    ax.scatter(F[0], F[1], F[2], c='green', s=60, edgecolors='black', label='F (Fusspunkt)')

    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.set_title('Aufg. 6: Abstand Punkt-Ebene (P zum Fusspunkt)', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.25)

    out = '/tmp/plot_v3_task6.png'
    savefig(out)
    return out


def create_plot_task8():
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    # line g: through origin, direction u
    u = np.array([2, 1, 2])

    # plane: 3x+4y+5z=0 -> normal n
    n = np.array([3, 4, 5])

    # plane basis vectors: pick two independent vectors in plane
    # Find v such that n·v = 0
    # e.g. choose v1 = (4,-3,0) (dot with n: 12-12+0=0)
    v1 = np.array([4, -3, 0])
    v2 = np.cross(n, v1)

    # plot plane patch around origin
    s, t = np.meshgrid(np.linspace(-1.5, 1.5, 10), np.linspace(-1.5, 1.5, 10))
    P0 = np.array([0, 0, 0])
    plane = P0[None, None, :] + s[..., None] * v1 + t[..., None] * v2
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.25, color='dodgerblue')

    # plot line
    tt = np.linspace(-1.2, 1.2, 200)
    line = tt[:, None] * u
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'r-', linewidth=3, label='g')

    # plot normal vector at origin
    n_unit = n / np.linalg.norm(n)
    ax.plot([0, n_unit[0]], [0, n_unit[1]], [0, n_unit[2]], 'g--', linewidth=3, label='Normalenrichtung')

    ax.scatter([0], [0], [0], c='k', s=20)

    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.set_title('Aufg. 8: Winkel Gerade zu Ebene (u vs. Normalenvektor)', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.25)

    out = '/tmp/plot_v3_task8.png'
    savefig(out)
    return out


def create_plot_task10():
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    # g: x=(0,0,0)+r*(1,0,0)
    # h: x=(0,1,1)+s*(0,1,0)
    P_g = np.array([0, 0, 0])
    u_g = np.array([1, 0, 0])
    P_h = np.array([0, 1, 1])
    u_h = np.array([0, 1, 0])

    r = np.linspace(-0.3, 1.8, 200)
    s = np.linspace(-0.3, 1.8, 200)
    g_line = P_g + np.outer(r, u_g)
    h_line = P_h + np.outer(s, u_h)

    ax.plot(g_line[:, 0], g_line[:, 1], g_line[:, 2], 'r-', linewidth=3, label='g')
    ax.plot(h_line[:, 0], h_line[:, 1], h_line[:, 2], 'b-', linewidth=3, label='h')

    # normal for skew distance (not exact closest, but visually ok)
    n = np.cross(u_g, u_h)
    # use fixed closest points for this specific configuration (works well here)
    A = np.array([0, 0, 0])  # on g
    B = np.array([0, 1, 0])  # on h (same x,z); distance is 1

    ax.plot([A[0], B[0]], [A[1], B[1]], [A[2], B[2]], 'g--', linewidth=3, label='Abstand')
    ax.scatter([A[0]], [A[1]], [A[2]], c='red', s=50, edgecolors='black')
    ax.scatter([B[0]], [B[1]], [B[2]], c='blue', s=50, edgecolors='black')

    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.set_title('Aufg. 10: Windschiefe Geraden - Abstand', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=9)

    out = '/tmp/plot_v3_task10.png'
    savefig(out)
    return out


def create_plot_task15():
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    A = np.array([1, 0, 0])
    B = np.array([0, 1, 0])
    C = np.array([0, 0, 1])

    tri = np.array([A, B, C, A])
    ax.plot(tri[:, 0], tri[:, 1], tri[:, 2], 'b-', linewidth=3)

    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    verts = [[(A[0], A[1], A[2]), (B[0], B[1], B[2]), (C[0], C[1], C[2])]]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.35, facecolors='lightblue', edgecolors='blue'))

    ax.scatter([A[0]], [A[1]], [A[2]], c='red', s=60, edgecolors='black', label='A')
    ax.scatter([B[0]], [B[1]], [B[2]], c='green', s=60, edgecolors='black', label='B')
    ax.scatter([C[0]], [C[1]], [C[2]], c='blue', s=60, edgecolors='black', label='C')

    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.set_title('Aufg. 15: Dreieck ABC', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=9)

    out = '/tmp/plot_v3_task15.png'
    savefig(out)
    return out


def create_plot_task16_intersection():
    from mpl_toolkits.mplot3d import Axes3D  # noqa
    fig = plt.figure(figsize=(6.5, 4.2))
    ax = fig.add_subplot(111, projection='3d')

    # g: (2,1,0)+r*(1,-1,1)
    P0 = np.array([2, 1, 0])
    u = np.array([1, -1, 1])

    # E: (0,0,1)+s*(2,0,-1)+t*(0,1,1)
    Q0 = np.array([0, 0, 1])
    v1 = np.array([2, 0, -1])
    v2 = np.array([0, 1, 1])

    # Solve P0 + r u = Q0 + s v1 + t v2
    # Rearr: r u - s v1 - t v2 = Q0 - P0
    A = np.column_stack([u, -v1, -v2])  # 3x3
    b = Q0 - P0
    r, s, t = np.linalg.solve(A, b)
    X = P0 + r * u

    # plot line segment
    rr = np.linspace(float(r)-1.0, float(r)+1.0, 200)
    line = P0 + rr[:, None] * u
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'r-', linewidth=3, label='g')

    # plot plane patch around intersection
    # sample s,t around found values
    ss, tt = np.meshgrid(np.linspace(float(s)-1.0, float(s)+1.0, 10), np.linspace(float(t)-1.0, float(t)+1.0, 10))
    plane = Q0[None, None, :] + ss[..., None] * v1 + tt[..., None] * v2
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.3, color='dodgerblue')

    ax.scatter([X[0]], [X[1]], [X[2]], c='green', s=100, marker='*', edgecolors='black', label='S')

    ax.set_xlabel('X', fontsize=9)
    ax.set_ylabel('Y', fontsize=9)
    ax.set_zlabel('Z', fontsize=9)
    ax.set_title('Aufg. 16: Schnittpunkt Gerade-Ebene', fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.25)
    ax.legend(loc='upper left', fontsize=9)

    out = '/tmp/plot_v3_task16.png'
    savefig(out)
    return out


def create_diagram_parameter_ascii():
    fig, ax = plt.subplots(figsize=(6.5, 2.9))
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.25)

    x = np.linspace(-1, 4, 100)
    y = x + 1
    ax.plot(x, y, 'b-', linewidth=3)

    points = [(0, 1), (1, 2), (2, 3)]
    labs = ['r=0', 'r=1', 'r=2']
    for (px, py), lab in zip(points, labs):
        ax.scatter(px, py, c='red', s=90, edgecolors='black', zorder=5)
        ax.text(px + 0.08, py + 0.08, lab, fontsize=10, fontweight='bold')

    ax.set_xlabel('x', fontsize=10)
    ax.set_ylabel('y', fontsize=10)
    ax.set_title('Parameterdarstellung: x = P + r*u', fontsize=11, fontweight='bold')
    ax.set_aspect('equal')

    out = '/tmp/diagram_v3_param.png'
    savefig(out)
    return out


def create_diagram_abstand_ascii():
    fig, ax = plt.subplots(figsize=(6.5, 2.9))
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.25)

    x = np.linspace(-1, 4, 100)
    y = 2 * x + 1
    ax.plot(x, y, 'b-', linewidth=3)

    P = (1, 3)
    ax.scatter([P[0]], [P[1]], c='red', s=120, edgecolors='black', zorder=6)

    # perpendicular-ish helper line
    x_perp = np.linspace(0.5, 1.5, 50)
    y_perp = -0.5 * (x_perp - 1) + 3
    ax.plot(x_perp, y_perp, 'g--', linewidth=3)

    ax.scatter([P[0]], [P[1]], c='green', s=70, marker='x', zorder=7)

    ax.set_xlabel('x', fontsize=10)
    ax.set_ylabel('y', fontsize=10)
    ax.set_title('Abstand Punkt-Ebene (Idee, 2D-Skizze)', fontsize=11, fontweight='bold')
    ax.set_aspect('equal')

    out = '/tmp/diagram_v3_abstand.png'
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

    # Visual assets
    plot1 = create_plot_task1()
    plot3 = create_plot_task3()
    plot6 = create_plot_task6()
    plot8 = create_plot_task8()
    plot10 = create_plot_task10()
    plot15 = create_plot_task15()
    plot16 = create_plot_task16_intersection()

    diagram_param = create_diagram_parameter_ascii()
    diagram_abstand = create_diagram_abstand_ascii()

    # Title
    pdf.chapter_title('Aufgaben - Geraden und Ebenen im R3')
    pdf.set_font('Helvetica', 'I', 10)
    pdf.cell(0, 6, 'Mit Skizzen zur schnellen Orientierung (Loesungen am Ende).', 0, 1, 'C')
    pdf.ln(4)

    # Concept diagrams
    pdf.section_header('GRUNDKONZEPTE')
    pdf.ln(2)
    pdf.image(diagram_param, x=15, y=None, w=90)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(90, 6, 'Parameterdarstellung', 0, 0)
    pdf.image(diagram_abstand, x=105, y=None, w=90)
    pdf.cell(0, 6, 'Abstand (Idee)', 0, 1)
    pdf.ln(10)

    # Skizzen section
    pdf.section_header('SKIZZEN (zu ausgewahlten Aufgaben)')
    pdf.ln(2)

    images = [
        (plot1, 'Aufg. 1'),
        (plot3, 'Aufg. 3'),
        (plot6, 'Aufg. 6'),
        (plot8, 'Aufg. 8'),
        (plot10, 'Aufg. 10'),
        (plot15, 'Aufg. 15'),
        (plot16, 'Aufg. 16'),
    ]

    # 2-column layout, 3 rows per page approx
    x_left = 15
    w_img = 90
    x_right = 105
    y = None

    row = 0
    for i, (img, cap) in enumerate(images):
        if i % 2 == 0:
            x = x_left
        else:
            x = x_right

        if i % 2 == 0:
            y = pdf.get_y()

        pdf.image(img, x=x, y=y, w=w_img)
        pdf.set_y(y + 64)
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(w_img, 6, cap, 0, 1, 'C')
        pdf.set_font('Helvetica', '', 11)

        if i % 2 == 1:
            pdf.ln(2)

    pdf.ln(8)

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
        (15, 'Gegeben sind die Punkte A(1|0|0), B(0|1|0) und C(0|0|1). (a) Parameterdarstellung der Ebene durch A,B,C. (b) Flaeche des Dreiecks ABC.', 3),
        (16, 'Gegeben sind die Gerade g: x = (2,1,0) + r*(1,-1,1) und die Ebene E: x = (0,0,1) + s*(2,0,-1) + t*(0,1,1). Bestimmen Sie r, s, t im Schnittpunkt.', 2),
        (17, 'Bestimmen Sie eine Gerade g durch den Punkt P(1|2|3), die parallel zur Ebene E: x + y + z = 0 und parallel zur Geraden h: x = (0,0,0) + r*(1,1,0) verlaeuft.', 3),
        (18, 'Bestimmen Sie die Parameterdarstellung der Ebene, die die parallelen Geraden enthaelt: g: x = (1,0,1) + r*(1,1,2), h: x = (3,1,4) + s*(1,1,2).', 2),
        (19, 'Berechnen Sie den Winkel zwischen den Ebenen: E1: x - y + 2z = 4, E2: 2x + y - z = 1.', 2),
        (20, 'Bestimmen Sie die Schnittgerade der drei Ebenen: E1: x + y + z = 6, E2: x - y + z = 2, E3: x + y - z = 0. Pruefen Sie, ob es einen gemeinsamen Schnittpunkt gibt.', 3),
    ]

    tips = {
        1: 'Tipp: Der Richtungsvektor ist u = B - A.',
        3: 'Tipp: Gleichsetzen und dann das lineare Gleichungssystem nach r, s, t loesen.',
        6: 'Tipp: Erst Normalenvektor n = a x b bestimmen und dann Abstandsformel verwenden.',
        8: 'Tipp: Winkel Gerade zu Ebene aus Winkel zwischen Richtungsvektor u und Normalenvektor n.',
        10: 'Tipp: Abstand windschiefer Geraden ueber Normalenrichtung/Skalarprodukt.',
        15: 'Tipp: Flaeche = 0.5 * |u x v| fuer zwei Seitenvektoren u, v.',
        16: 'Tipp: Gleichsetzen (line vs. Ebene) => 3x3 System fuer r,s,t.',
    }

    for num, txt, diff in tasks:
        pdf.task_box(num, txt, difficulty=diff)
        if num in tips:
            pdf.tip_box(tips[num])

        # occasional page break
        if num in (6, 12):
            pdf.add_page()

    # Solutions
    pdf.add_page()
    pdf.chapter_title('Loesungen', color=(66, 180, 100))

    # Same solutions as v2 (ASCII-only). Kept concise.
    sol = {
        1: [
            'u = B - A = (3,3,6)',
            'g: x = (2,1,3) + r*(3,3,6)'
        ],
        2: [
            'Ebene durch P,Q,R: u = Q-P, v = R-P',
            'E: x = (1,0,2) + s*(2,1,2) + t*(1,2,-1)'
        ],
        3: [
            'Gleichsetzen und loesen:',
            'S = (3,2,1)'
        ],
        4: [
            'Richtungsvektor h ist Vielfaches von g => parallel',
            'Verschiebungsvektor ist kein Vielfaches davon => nicht identisch'
        ],
        5: [
            'Normalenvektor n = (2,-1,3)',
            'Parameterform (eine Moeglichkeit):',
            'E: x = (3,0,0) + s*(1,2,0) + t*(0,3,1)'
        ],
        6: [
            'Normalenvektor n = a x b = (-1,1,2)',
            'Abstand: d = 3 / sqrt(6)'
        ],
        7: [
            'E1: x + y + z = 3, E2: x - 2y + z = 3',
            'Schnitt: y=0, z=3-x',
            'g: x = (0,0,3) + r*(1,0,-1)'
        ],
        8: [
            'cos(alpha) = |u·n|/(|u||n|) mit u=(2,1,2), n=(3,4,5)',
            'u·n=20, |u|=3, |n|=5*sqrt(2)',
            'alpha = arccos(4/(3*sqrt(2)))',
            'Winkel Gerade-Ebene: beta = 90deg - alpha'
        ],
        9: [
            'Eine Ebenenaufstellung (Beispiel):',
            'E: x = (1,2,1) + s*(1,1,0) + t*(1,-2,0)'
        ],
        10: [
            'Abstand ergibt sich zu d = 1 (in dieser Konfiguration)'
        ],
        11: [
            'Normalenvektor n=(1,1,1)',
            'Lot schneidet bei r=0 => Fusspunkt F=(1,2,3)'
        ],
        12: [
            'Normalenvektor n=(2,-3,1)',
            'Parameterform (Beispiel):',
            'E: x = (2,0,0) + s*(3,2,0) + t*(0,1,3)'
        ],
        13: [
            'Orthogonal zur Ebene => Richtungsvektor = Normalenvektor',
            'n=(1,-2,2)',
            'g: x = (1,0,1) + r*(1,-2,2)'
        ],
        14: [
            'Abstand zur Form: |d|/||n|| = 2 => d = +/- 6',
            'E: 2x - y + 2z = 6 und E: 2x - y + 2z = -6'
        ],
        15: [
            'a) u=B-A=(-1,1,0), v=C-A=(-1,0,1)',
            'E: x = (1,0,0) + s*u + t*v',
            'b) Flaeche = 0.5*|u x v| = sqrt(3)/2'
        ],
        16: [
            'Gleichsetzen und loesen => r=2/5, s=6/5, t=3/5',
            'Schnittpunkt S=(12/5, 3/5, 2/5)'
        ],
        17: [
            'Bedingungen: parallel zu Ebene => u orthogonal zu nE; parallel zu h => u parallel zu uh',
            'Ein Richtungsvektor ist u = (-1,1,0)',
            'g: x = (1,2,3) + r*(-1,1,0)'
        ],
        18: [
            'E enthaelt beide parallele Geraden => Ebene wird durch einen Richtungsvektor u=(1,1,2) und Verbindungsvektor v=(2,1,3) aufgespannt',
            'E: x = (1,0,1) + s*(1,1,2) + t*(2,1,3)'
        ],
        19: [
            'Winkel ueber Normalenvektoren n1=(1,-1,2), n2=(2,1,-1)',
            'cos(alpha)=|n1·n2|/(|n1||n2|)=1/6',
            'alpha=arccos(1/6)'
        ],
        20: [
            'Drei Ebenen liefern eindeutigen Schnittpunkt:',
            'S = (1,2,3) (kein Schnitt in einer Geraden, sondern Punkt)'
        ],
    }

    for num in range(1, 21):
        pdf.solution_start(num)
        for line in sol[num]:
            pdf.solution_text(line)

    # Cleanup temporary plots
    for f in [plot1, plot3, plot6, plot8, plot10, plot15, plot16, diagram_param, diagram_abstand]:
        try:
            os.remove(f)
        except Exception:
            pass

    return pdf


if __name__ == '__main__':
    pdf = create_pdf()
    out = '/home/openclaw/.openclaw/workspace/mathe/geraden-ebenen-uebung-final-v3.pdf'
    pdf.output(out)
    print('PDF erstellt:', out)
    print('Bytes:', os.path.getsize(out))
