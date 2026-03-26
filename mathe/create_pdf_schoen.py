#!/usr/bin/env python3
from fpdf import FPDF
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import os

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)

    def header(self):
        # Gradient-like header background
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

    def task_box(self, number, text):
        # Task number in circle
        self.set_fill_color(66, 133, 244)
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 12)
        self.cell(20, 10, str(number), 0, 0, 'C', 1)
        self.set_text_color(0, 0, 0)
        self.set_font('Helvetica', '', 11)
        self.multi_cell(0, 6, text)
        self.ln(3)

    def solution_start(self, number):
        self.set_fill_color(200, 220, 255)
        self.set_font('Helvetica', 'B', 11)
        self.cell(0, 8, f'Lösung {number}:', 0, 1, 'L', 1)
        self.set_font('Helvetica', '', 10)

    def solution_text(self, text):
        self.multi_cell(180, 5, text)
        self.ln(2)

    def math(self, text):
        """Format math text"""
        self.set_font('Courier', '', 10)
        self.multi_cell(180, 5, text)
        self.set_font('Helvetica', '', 10)

def create_3d_plot_task1():
    """3D plot for Task 1: Line through two points"""
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111, projection='3d')
    
    # Points A and B
    A = np.array([2, 1, 3])
    B = np.array([5, 4, 9])
    
    # Plot points
    ax.scatter(A[0], A[1], A[2], c='red', s=100, label='A(2,1,3)')
    ax.scatter(B[0], B[1], B[2], c='blue', s=100, label='B(5,4,9)')
    
    # Plot line
    t = np.linspace(-1, 2, 100)
    line = A + np.outer(t, B - A)
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'g-', linewidth=2, label='Gerade g')
    
    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Gerade durch zwei Punkte')
    ax.legend()
    ax.grid(True)
    
    filename = '/tmp/plot_task1.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    return filename

def create_3d_plot_task3():
    """3D plot for Task 3: Line-Plane intersection"""
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111, projection='3d')
    
    # Line g: x = (2,1,-1) + r·(1,1,2)
    # Plane E: x = (1,0,1) + s·(1,1,0) + t·(0,1,1)
    
    # Direction vectors
    u_line = np.array([1, 1, 2])
    u_plane1 = np.array([1, 1, 0])
    u_plane2 = np.array([0, 1, 1])
    
    # Plot line
    t = np.linspace(-1, 2, 100)
    P_line = np.array([2, 1, -1])
    line = P_line + np.outer(t, u_line)
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'r-', linewidth=2, label='Gerade g')
    
    # Plot plane (meshgrid)
    s, t_plane = np.meshgrid(np.linspace(0, 2, 10), np.linspace(0, 2, 10))
    P_plane = np.array([1, 0, 1])
    plane = P_plane[None, None, :] + s[..., None] * u_plane1 + t_plane[..., None] * u_plane2
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.3, color='blue', label='Ebene E')
    
    # Intersection point S = (3,2,1)
    S = np.array([3, 2, 1])
    ax.scatter(S[0], S[1], S[2], c='green', s=150, marker='*', label='S(3,2,1)')
    
    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Schnittpunkt Gerade-Ebene')
    ax.legend()
    ax.grid(True)
    
    filename = '/tmp/plot_task3.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    return filename

def create_3d_plot_task10():
    """3D plot for Task 10: Distance between skew lines"""
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111, projection='3d')
    
    # Line g: x = (0,0,0) + r·(1,0,0)
    # Line h: x = (0,1,1) + s·(0,1,0)
    
    u_g = np.array([1, 0, 0])
    u_h = np.array([0, 1, 0])
    P_g = np.array([0, 0, 0])
    P_h = np.array([0, 1, 1])
    
    # Plot lines
    r = np.linspace(-1, 2, 100)
    s = np.linspace(-1, 2, 100)
    line_g = P_g + np.outer(r, u_g)
    line_h = P_h + np.outer(s, u_h)
    ax.plot(line_g[:, 0], line_g[:, 1], line_g[:, 2], 'r-', linewidth=2, label='Gerade g')
    ax.plot(line_h[:, 0], line_h[:, 1], line_h[:, 2], 'b-', linewidth=2, label='Gerade h')
    
    # Distance line (normal vector)
    n = np.cross(u_g, u_h)
    n = n / np.linalg.norm(n)
    distance = 1
    # Find closest points (approximately)
    P_g_closest = P_g
    P_h_closest = P_h
    ax.plot([P_g_closest[0], P_h_closest[0]], [P_g_closest[1], P_h_closest[1]], 
            [P_g_closest[2], P_h_closest[2]], 'g--', linewidth=2, label=f'Abstand={distance}')
    
    ax.scatter(P_g_closest[0], P_g_closest[1], P_g_closest[2], c='red', s=100)
    ax.scatter(P_h_closest[0], P_h_closest[1], P_h_closest[2], c='blue', s=100)
    
    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Windschiefe Geraden - Abstand')
    ax.legend()
    ax.grid(True)
    
    filename = '/tmp/plot_task10.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    return filename

def create_3d_plot_task15():
    """3D plot for Task 15: Triangle and plane"""
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot(111, projection='3d')
    
    # Triangle points
    A = np.array([1, 0, 0])
    B = np.array([0, 1, 0])
    C = np.array([0, 0, 1])
    
    # Plot triangle
    triangle = np.array([A, B, C, A])
    ax.plot(triangle[:, 0], triangle[:, 1], triangle[:, 2], 'b-', linewidth=2)
    
    # Fill triangle
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    verts = [list(zip([A[0], B[0], C[0]], [A[1], B[1], C[1]], [A[2], B[2], C[2]]))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, facecolors='blue'))
    
    # Plot points
    ax.scatter(A[0], A[1], A[2], c='red', s=100, label='A(1,0,0)')
    ax.scatter(B[0], B[1], B[2], c='green', s=100, label='B(0,1,0)')
    ax.scatter(C[0], C[1], C[2], c='blue', s=100, label='C(0,0,1)')
    
    # Set labels
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Dreieck ABC in der Ebene')
    ax.legend()
    ax.grid(True)
    
    filename = '/tmp/plot_task15.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    return filename

def create_diagram_parameter():
    """2D diagram showing parameter concept"""
    fig, ax = plt.subplots(figsize=(6, 3))
    
    # Draw coordinate system
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.3)
    
    # Draw line
    x = np.linspace(-1, 4, 100)
    y = x + 1  # y = x + 1
    ax.plot(x, y, 'b-', linewidth=2, label='g')
    
    # Mark points
    ax.scatter([0, 1, 2], [1, 2, 3], c='red', s=80)
    ax.text(0.1, 1.1, 'r=0', fontsize=10)
    ax.text(1.1, 2.1, 'r=1', fontsize=10)
    ax.text(2.1, 3.1, 'r=2', fontsize=10)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Parameterdarstellung: x = P + r·u')
    ax.legend()
    ax.set_aspect('equal')
    
    filename = '/tmp/diagram_parameter.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    return filename

def create_diagram_abstand():
    """2D diagram showing distance concept"""
    fig, ax = plt.subplots(figsize=(6, 3))
    
    # Draw coordinate system
    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.3)
    
    # Draw plane (line in 2D)
    x = np.linspace(-1, 4, 100)
    y = 2*x + 1
    ax.plot(x, y, 'b-', linewidth=2, label='Ebene')
    
    # Draw point
    P = [1, 3]
    ax.scatter(P[0], P[1], c='red', s=150, label='P(1,3)', zorder=5)
    
    # Draw perpendicular (distance)
    # For line y = 2x + 1, perpendicular slope is -1/2
    x_perp = np.linspace(0.5, 1.5, 100)
    y_perp = -0.5*(x_perp - 1) + 3
    ax.plot(x_perp, y_perp, 'g--', linewidth=2, label='Abstand')
    
    # Mark foot point
    F = [1, 3]
    ax.scatter(F[0], F[1], c='green', s=100, marker='x', label='Fusspunkt', zorder=5)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Abstand Punkt-Ebene (vereinfacht 2D)')
    ax.legend()
    ax.set_aspect('equal')
    
    filename = '/tmp/diagram_abstand.png'
    plt.savefig(filename, dpi=150, bbox_inches='tight')
    plt.close()
    return filename

def create_pdf():
    pdf = PDF()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_top_margin(20)
    pdf.add_page()

    # Create plots
    print("Erstelle Abbildungen...")
    plot_task1 = create_3d_plot_task1()
    plot_task3 = create_3d_plot_task3()
    plot_task10 = create_3d_plot_task10()
    plot_task15 = create_3d_plot_task15()
    diagram_param = create_diagram_parameter()
    diagram_abstand = create_diagram_abstand()

    # Title page
    pdf.chapter_title('Aufgaben - Geraden und Ebenen im R3')
    pdf.set_font('Helvetica', 'I', 10)
    pdf.cell(0, 6, 'Loesungsweg und Platz fuer Rechnungen', 0, 1, 'C')
    pdf.ln(5)

    # Concept diagrams
    pdf.set_font('Helvetica', 'B', 12)
    pdf.cell(0, 8, 'Grundkonzepte:', 0, 1, 'L')
    pdf.ln(2)
    
    # Parameter diagram
    pdf.image(diagram_param, x=15, y=75, w=90)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(100, 6, 'Parameterdarstellung', 0, 0)
    
    # Distance diagram
    pdf.image(diagram_abstand, x=105, y=75, w=90)
    pdf.cell(0, 6, 'Abstandsberechnung', 0, 1)
    pdf.ln(10)

    # Tasks
    pdf.set_font('Helvetica', 'B', 11)
    pdf.cell(0, 8, 'Aufgaben:', 0, 1, 'L')
    pdf.ln(2)

    pdf.task_box(1, "Bestimmen Sie die Parameterdarstellung der Geraden g durch die Punkte A(2|1|3) und B(5|4|9).")
    pdf.image(plot_task1, x=15, y=None, w=80)
    pdf.ln(5)

    pdf.task_box(2, "Bestimmen Sie die Parameterdarstellung der Ebene E durch die Punkte P(1|0|2), Q(3|1|4) und R(2|2|1).")
    pdf.task_box(3, "Gegeben sind die Gerade g: x = (2,1,-1) + r·(1,1,2) und die Ebene E: x = (1,0,1) + s·(1,1,0) + t·(0,1,1). Bestimmen Sie den Schnittpunkt S.")
    pdf.image(plot_task3, x=15, y=None, w=80)
    pdf.ln(5)

    pdf.task_box(4, "Pruefen Sie die Lagenbeziehung der beiden Geraden: g: x = (1,0,1) + r·(1,2,3), h: x = (2,1,3) + s·(2,4,6).")
    pdf.task_box(5, "Wandeln Sie die Ebenengleichung in Parameterform um: E: 2x - y + 3z = 6.")
    pdf.task_box(6, "Berechnen Sie den Abstand des Punktes P(3|2|-1) von der Ebene E: x = (1,0,0) + s·(2,0,1) + t·(1,1,0).")
    pdf.task_box(7, "Bestimmen Sie die Schnittgerade der beiden Ebenen: E1: x = (0,1,2) + r·(1,0,0) + s·(0,1,1) und E2: x - 2y + z = 3.")
    pdf.task_box(8, "Berechnen Sie den Winkel zwischen der Geraden g: x = (0,0,0) + r·(2,1,2) und der Ebene E: 3x + 4y + 5z = 0.")
    pdf.task_box(9, "Bestimmen Sie eine Parameterdarstellung der Ebene E, die die Gerade g: x = (1,2,1) + r·(1,1,0) enthaelt und durch den Punkt P(2|0|1) geht.")
    pdf.task_box(10, "Gegeben sind zwei windschiefe Geraden: g: x = (0,0,0) + r·(1,0,0), h: x = (0,1,1) + s·(0,1,0). Bestimmen Sie den kuerzesten Abstand.")
    pdf.image(plot_task10, x=15, y=None, w=80)
    pdf.ln(5)

    pdf.add_page()
    pdf.task_box(11, "Gegeben ist die Ebene E: x + y + z = 6 und der Punkt P(1|2|3). Bestimmen Sie den Fusspunkt des Lotes von P auf die Ebene E.")
    pdf.task_box(12, "Geben Sie eine Parameterdarstellung der Ebene E: 2x - 3y + z = 4 an.")
    pdf.task_box(13, "Bestimmen Sie die Parameterdarstellung der Geraden g, die orthogonal zur Ebene E: x - 2y + 2z = 5 ist und durch den Punkt P(1|0|1) geht.")
    pdf.task_box(14, "Bestimmen Sie alle Ebenen, die parallel zur Ebene E: 2x - y + 2z = 8 sind und den Abstand 2 zum Ursprung haben.")
    pdf.task_box(15, "Gegeben sind die drei Punkte A(1|0|0), B(0|1|0) und C(0|0|1). (a) Bestimmen Sie die Parameterdarstellung der Ebene durch A, B und C. (b) Berechnen Sie die Flaeche des Dreiecks ABC.")
    pdf.image(plot_task15, x=15, y=None, w=80)
    pdf.ln(5)

    pdf.task_box(16, "Gegeben sind die Gerade g: x = (2,1,0) + r·(1,-1,1) und die Ebene E: x = (0,0,1) + s·(2,0,-1) + t·(0,1,1). Bestimmen Sie die Parameter r, s, t im Schnittpunkt.")
    pdf.task_box(17, "Bestimmen Sie die Parameterdarstellung einer Geraden g durch den Punkt P(1|2|3), die parallel zur Ebene E: x + y + z = 0 und parallel zur Geraden h: x = (0,0,0) + r·(1,1,0) verlaeuft.")
    pdf.task_box(18, "Bestimmen Sie die Parameterdarstellung der Ebene, die die beiden parallelen Geraden enthaelt: g: x = (1,0,1) + r·(1,1,2), h: x = (3,1,4) + s·(1,1,2).")
    pdf.task_box(19, "Berechnen Sie den Winkel zwischen den Ebenen: E1: x - y + 2z = 4, E2: 2x + y - z = 1.")
    pdf.task_box(20, "Bestimmen Sie die Parameterdarstellung der Schnittgeraden der drei Ebenen: E1: x + y + z = 6, E2: x - y + z = 2, E3: x + y - z = 0. Pruefen Sie, ob die Ebenen einen gemeinsamen Schnittpunkt haben.")

    # Solutions page
    pdf.add_page()
    pdf.chapter_title('Loesungen', color=(66, 180, 100))

    pdf.solution_start(1)
    pdf.solution_text("Richtungsvektor: u = B - A = (3,3,6)")
    pdf.math("g: x = (2,1,3) + r·(3,3,6)")
    pdf.ln(5)

    pdf.solution_start(2)
    pdf.solution_text("Richtungsvektoren: u = Q - P = (2,1,2), v = R - P = (1,2,-1)")
    pdf.math("E: x = (1,0,2) + s·(2,1,2) + t·(1,2,-1)")
    pdf.ln(5)

    pdf.solution_start(3)
    pdf.solution_text("Gleichsetzen und loesen:")
    pdf.math("(2+r, 1+r, -1+2r) = (1+s, s+t, 1+t)")
    pdf.solution_text("Aus 2. Komponente: 1+r = s+t -> t = 1+r-s")
    pdf.solution_text("Aus 3. Komponente: -1+2r = 1+t = 2+r-s -> r = 3-s")
    pdf.solution_text("Aus 1. Komponente: 2+r = 1+s -> 2+3-s = 1+s -> 5-s = 1+s -> 4 = 2s -> s = 2")
    pdf.solution_text("Damit: r = 3-2 = 1, t = 1+1-2 = 0")
    pdf.solution_text("Schnittpunkt: S = (3,2,1)")
    pdf.ln(5)

    pdf.solution_start(4)
    pdf.solution_text("Richtungsvektoren: ug = (1,2,3), uh = (2,4,6) = 2·(1,2,3)")
    pdf.solution_text("uh ist ein Vielfaches von ug, also parallel.")
    pdf.solution_text("Ph - Pg = (1,1,2) ist kein Vielfaches von (1,2,3).")
    pdf.solution_text("=> g und h sind PARALLEL, ABER NICHT IDENTISCH.")
    pdf.ln(5)

    pdf.solution_start(5)
    pdf.solution_text("Koordinatengleichung: 2x - y + 3z = 6")
    pdf.solution_text("Normalenvektor: n = (2,-1,3)")
    pdf.math("E: x = (3,0,0) + s·(1,2,0) + t·(0,3,1)")
    pdf.ln(5)

    pdf.solution_start(6)
    pdf.solution_text("Normalenvektor: n = u x v = (-1,1,2)")
    pdf.solution_text("Koordinatengleichung: -x + y + 2z = -1 oder x - y - 2z = 1")
    pdf.solution_text("Abstand: d = |3-2-2(-1)| / sqrt(1+1+4) = 3/sqrt(6)")
    pdf.ln(5)

    pdf.solution_start(7)
    pdf.solution_text("E1 in Koordinatenform: x + y + z = 3")
    pdf.solution_text("Schnitt: x + y + z = 3, x - 2y + z = 3")
    pdf.solution_text("Subtrahiere: 3y = 0 -> y = 0")
    pdf.solution_text("Einsetzen: x + z = 3 -> z = 3 - x")
    pdf.math("g: x = (0,0,3) + r·(1,0,-1)")
    pdf.ln(5)

    pdf.solution_start(8)
    pdf.solution_text("u = (2,1,2), n = (3,4,5)")
    pdf.solution_text("u · n = 20, |u| = 3, |n| = 5*sqrt(2)")
    pdf.solution_text("cos(alpha) = 20 / (3 * 5*sqrt(2)) = 4 / (3*sqrt(2))")
    pdf.solution_text("Winkel Gerade-Ebene: beta = 90° - alpha")
    pdf.ln(5)

    pdf.solution_start(9)
    pdf.solution_text("u1 = (1,1,0) (aus Gerade g)")
    pdf.solution_text("u2 = P - A = (1,-2,0)")
    pdf.math("E: x = (1,2,1) + s·(1,1,0) + t·(1,-2,0)")
    pdf.ln(5)

    pdf.solution_start(10)
    pdf.solution_text("ug = (1,0,0), uh = (0,1,0)")
    pdf.solution_text("n = ug x uh = (0,0,1)")
    pdf.solution_text("Ph - Pg = (0,1,1)")
    pdf.solution_text("Abstand: d = |n · (Ph - Pg)| / |n| = |1| / 1 = 1")
    pdf.ln(5)

    pdf.add_page()
    pdf.solution_start(11)
    pdf.solution_text("Normalenvektor: n = (1,1,1)")
    pdf.math("Lot: g: x = (1,2,3) + r·(1,1,1)")
    pdf.solution_text("Schnitt: (1+r) + (2+r) + (3+r) = 6 -> 6 + 3r = 6 -> r = 0")
    pdf.solution_text("Fusspunkt: F = (1,2,3)")
    pdf.solution_text("(Kontrolle: P liegt auf der Ebene!)")
    pdf.ln(5)

    pdf.solution_start(12)
    pdf.solution_text("Normalenvektor: n = (2,-3,1)")
    pdf.math("E: x = (2,0,0) + s·(3,2,0) + t·(0,1,3)")
    pdf.ln(5)

    pdf.solution_start(13)
    pdf.solution_text("Normalenvektor der Ebene: n = (1,-2,2)")
    pdf.solution_text("Gerade orthogonal -> Richtungsvektor = n")
    pdf.math("g: x = (1,0,1) + r·(1,-2,2)")
    pdf.ln(5)

    pdf.solution_start(14)
    pdf.solution_text("Normalenvektor: n = (2,-1,2)")
    pdf.solution_text("Parallele Ebenen: 2x - y + 2z = d")
    pdf.solution_text("Abstand: |d| / 3 = 2 -> d = ±6")
    pdf.solution_text("Zwei Ebenen: 2x - y + 2z = 6 und 2x - y + 2z = -6")
    pdf.ln(5)

    pdf.solution_start(15)
    pdf.solution_text("(a) u = B - A = (-1,1,0), v = C - A = (-1,0,1)")
    pdf.math("E: x = (1,0,0) + s·(-1,1,0) + t·(-1,0,1)")
    pdf.solution_text("(b) u x v = (1,1,1)")
    pdf.solution_text("Flaeche = 1/2 * |u x v| = sqrt(3)/2")
    pdf.ln(5)

    pdf.solution_start(16)
    pdf.solution_text("Gleichsetzen:")
    pdf.math("(2+r, 1-r, r) = (2s, t, 1-s+t)")
    pdf.solution_text("Aus den Gleichungen: s = 6/5, r = 2/5, t = 3/5")
    pdf.solution_text("Schnittpunkt: S = (12/5, 3/5, 2/5)")
    pdf.ln(5)

    pdf.solution_start(17)
    pdf.solution_text("nE = (1,1,1), uh = (1,1,0)")
    pdf.solution_text("u = nE x uh = (-1,1,0)")
    pdf.math("g: x = (1,2,3) + r·(-1,1,0)")
    pdf.ln(5)

    pdf.solution_start(18)
    pdf.solution_text("Richtungsvektor: u = (1,1,2)")
    pdf.solution_text("Verbindungsvektor: Ph - Pg = (2,1,3)")
    pdf.math("E: x = (1,0,1) + s·(1,1,2) + t·(2,1,3)")
    pdf.ln(5)

    pdf.solution_start(19)
    pdf.solution_text("n1 = (1,-1,2), n2 = (2,1,-1)")
    pdf.solution_text("n1 · n2 = -1, |n1| = sqrt(6), |n2| = sqrt(6)")
    pdf.solution_text("cos(alpha) = 1/6 -> alpha = arccos(1/6)")
    pdf.ln(5)

    pdf.solution_start(20)
    pdf.solution_text("Lineares System:")
    pdf.math("x + y + z = 6")
    pdf.math("x - y + z = 2")
    pdf.math("x + y - z = 0")
    pdf.solution_text("Loesung: x = 1, y = 2, z = 3")
    pdf.solution_text("Die drei Ebenen schneiden sich im Punkt S(1|2|3), NICHT in einer Geraden.")

    # Clean up temporary files
    for f in [plot_task1, plot_task3, plot_task10, plot_task15, diagram_param, diagram_abstand]:
        if os.path.exists(f):
            os.remove(f)

    return pdf

if __name__ == '__main__':
    pdf = create_pdf()
    output_file = '/home/openclaw/.openclaw/workspace/mathe/geraden-ebenen-uebung-schoen.pdf'
    pdf.output(output_file)
    print(f"PDF erstellt: {output_file}")
    print(f"Dateigroesse: {os.path.getsize(output_file)} Bytes")
