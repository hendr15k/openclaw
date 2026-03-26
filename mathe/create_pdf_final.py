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

    def formula_box(self, text):
        """Formula in colored box"""
        self.set_fill_color(245, 245, 255)
        self.set_draw_color(66, 133, 244)
        self.set_font('Courier', '', 10)
        self.multi_cell(180, 5, text, 1, 'L', 1)
        self.set_font('Helvetica', '', 11)
        self.ln(2)

    def tip_box(self, text):
        """Tip in yellow box"""
        self.set_fill_color(255, 250, 230)
        self.set_draw_color(255, 200, 100)
        self.set_font('Helvetica', 'I', 10)
        self.multi_cell(180, 5, text, 1, 'L', 1)
        self.set_font('Helvetica', '', 11)
        self.ln(2)

    def task_box(self, number, text, difficulty=1):
        """Task with difficulty indicator"""
        # Difficulty colors
        colors = {1: (76, 175, 80), 2: (255, 193, 7), 3: (244, 67, 54)}
        labels = {1: 'leicht', 2: 'mittel', 3: 'schwer'}
        color = colors[difficulty]
        label = labels[difficulty]

        # Task number in circle with difficulty
        self.set_fill_color(color[0], color[1], color[2])
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 12)
        self.cell(25, 10, str(number), 0, 0, 'C', 1)

        # Difficulty label
        self.set_font('Helvetica', '', 8)
        self.cell(20, 10, label, 0, 0, 'C', 1)

        self.set_text_color(0, 0, 0)
        self.set_font('Helvetica', '', 11)
        self.multi_cell(155, 6, text)
        self.ln(3)

    def section_header(self, text):
        self.set_font('Helvetica', 'B', 13)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 8, text, 0, 1, 'L', 1)
        self.set_font('Helvetica', '', 11)
        self.ln(2)

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
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection='3d')

    A = np.array([2, 1, 3])
    B = np.array([5, 4, 9])

    ax.scatter(A[0], A[1], A[2], c='red', s=120, label='A(2,1,3)', edgecolors='black')
    ax.scatter(B[0], B[1], B[2], c='blue', s=120, label='B(5,4,9)', edgecolors='black')

    t = np.linspace(-1, 2, 100)
    line = A + np.outer(t, B - A)
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'g-', linewidth=3, label='Gerade g')

    ax.set_xlabel('X', fontsize=10)
    ax.set_ylabel('Y', fontsize=10)
    ax.set_zlabel('Z', fontsize=10)
    ax.set_title('Gerade durch zwei Punkte', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)

    filename = '/tmp/plot_task1.png'
    plt.savefig(filename, dpi=200, bbox_inches='tight')
    plt.close()
    return filename

def create_3d_plot_task3():
    """3D plot for Task 3: Line-Plane intersection"""
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection='3d')

    u_line = np.array([1, 1, 2])
    u_plane1 = np.array([1, 1, 0])
    u_plane2 = np.array([0, 1, 1])

    t = np.linspace(-1, 2, 100)
    P_line = np.array([2, 1, -1])
    line = P_line + np.outer(t, u_line)
    ax.plot(line[:, 0], line[:, 1], line[:, 2], 'r-', linewidth=3, label='Gerade g')

    s, t_plane = np.meshgrid(np.linspace(0, 2, 10), np.linspace(0, 2, 10))
    P_plane = np.array([1, 0, 1])
    plane = P_plane[None, None, :] + s[..., None] * u_plane1 + t_plane[..., None] * u_plane2
    ax.plot_surface(plane[..., 0], plane[..., 1], plane[..., 2], alpha=0.4, color='blue', label='Ebene E')

    S = np.array([3, 2, 1])
    ax.scatter(S[0], S[1], S[2], c='green', s=200, marker='*', label='S(3,2,1)', edgecolors='black')

    ax.set_xlabel('X', fontsize=10)
    ax.set_ylabel('Y', fontsize=10)
    ax.set_zlabel('Z', fontsize=10)
    ax.set_title('Schnittpunkt Gerade-Ebene', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)

    filename = '/tmp/plot_task3.png'
    plt.savefig(filename, dpi=200, bbox_inches='tight')
    plt.close()
    return filename

def create_3d_plot_task10():
    """3D plot for Task 10: Distance between skew lines"""
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection='3d')

    u_g = np.array([1, 0, 0])
    u_h = np.array([0, 1, 0])
    P_g = np.array([0, 0, 0])
    P_h = np.array([0, 1, 1])

    r = np.linspace(-1, 2, 100)
    s = np.linspace(-1, 2, 100)
    line_g = P_g + np.outer(r, u_g)
    line_h = P_h + np.outer(s, u_h)
    ax.plot(line_g[:, 0], line_g[:, 1], line_g[:, 2], 'r-', linewidth=3, label='Gerade g')
    ax.plot(line_h[:, 0], line_h[:, 1], line_h[:, 2], 'b-', linewidth=3, label='Gerade h')

    n = np.cross(u_g, u_h)
    n = n / np.linalg.norm(n)
    P_g_closest = P_g
    P_h_closest = P_h
    ax.plot([P_g_closest[0], P_h_closest[0]], [P_g_closest[1], P_h_closest[1]],
            [P_g_closest[2], P_h_closest[2]], 'g--', linewidth=3, label='Abstand=1')

    ax.scatter(P_g_closest[0], P_g_closest[1], P_g_closest[2], c='red', s=120, edgecolors='black')
    ax.scatter(P_h_closest[0], P_h_closest[1], P_h_closest[2], c='blue', s=120, edgecolors='black')

    ax.set_xlabel('X', fontsize=10)
    ax.set_ylabel('Y', fontsize=10)
    ax.set_zlabel('Z', fontsize=10)
    ax.set_title('Windschiefe Geraden - Abstand', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)

    filename = '/tmp/plot_task10.png'
    plt.savefig(filename, dpi=200, bbox_inches='tight')
    plt.close()
    return filename

def create_3d_plot_task15():
    """3D plot for Task 15: Triangle and plane"""
    fig = plt.figure(figsize=(7, 5))
    ax = fig.add_subplot(111, projection='3d')

    A = np.array([1, 0, 0])
    B = np.array([0, 1, 0])
    C = np.array([0, 0, 1])

    triangle = np.array([A, B, C, A])
    ax.plot(triangle[:, 0], triangle[:, 1], triangle[:, 2], 'b-', linewidth=3)

    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    verts = [list(zip([A[0], B[0], C[0]], [A[1], B[1], C[1]], [A[2], B[2], C[2]]))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.4, facecolors='lightblue', edgecolors='blue'))

    ax.scatter(A[0], A[1], A[2], c='red', s=120, label='A(1,0,0)', edgecolors='black')
    ax.scatter(B[0], B[1], B[2], c='green', s=120, label='B(0,1,0)', edgecolors='black')
    ax.scatter(C[0], C[1], C[2], c='blue', s=120, label='C(0,0,1)', edgecolors='black')

    ax.set_xlabel('X', fontsize=10)
    ax.set_ylabel('Y', fontsize=10)
    ax.set_zlabel('Z', fontsize=10)
    ax.set_title('Dreieck ABC in der Ebene', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)

    filename = '/tmp/plot_task15.png'
    plt.savefig(filename, dpi=200, bbox_inches='tight')
    plt.close()
    return filename

def create_diagram_parameter():
    """2D diagram showing parameter concept"""
    fig, ax = plt.subplots(figsize=(7, 4))

    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.3)

    x = np.linspace(-1, 4, 100)
    y = x + 1
    ax.plot(x, y, 'b-', linewidth=3, label='g')

    points = [(0, 1), (1, 2), (2, 3)]
    labels = ['r=0', 'r=1', 'r=2']
    for (px, py), label in zip(points, labels):
        ax.scatter(px, py, c='red', s=100, edgecolors='black')
        ax.text(px+0.1, py+0.1, label, fontsize=11, fontweight='bold')

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title('Parameterdarstellung: x = P + r*u', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.set_aspect('equal')

    filename = '/tmp/diagram_parameter.png'
    plt.savefig(filename, dpi=200, bbox_inches='tight')
    plt.close()
    return filename

def create_diagram_abstand():
    """2D diagram showing distance concept"""
    fig, ax = plt.subplots(figsize=(7, 4))

    ax.axhline(y=0, color='k', linewidth=1)
    ax.axvline(x=0, color='k', linewidth=1)
    ax.grid(True, alpha=0.3)

    x = np.linspace(-1, 4, 100)
    y = 2*x + 1
    ax.plot(x, y, 'b-', linewidth=3, label='Ebene')

    P = [1, 3]
    ax.scatter(P[0], P[1], c='red', s=200, label='P(1,3)', zorder=5, edgecolors='black')

    x_perp = np.linspace(0.5, 1.5, 100)
    y_perp = -0.5*(x_perp - 1) + 3
    ax.plot(x_perp, y_perp, 'g--', linewidth=3, label='Abstand')

    F = [1, 3]
    ax.scatter(F[0], F[1], c='green', s=150, marker='x', label='Fusspunkt', zorder=5)

    ax.set_xlabel('x', fontsize=11)
    ax.set_ylabel('y', fontsize=11)
    ax.set_title('Abstand Punkt-Ebene (vereinfacht 2D)', fontsize=12, fontweight='bold')
    ax.legend(fontsize=10)
    ax.set_aspect('equal')

    filename = '/tmp/diagram_abstand.png'
    plt.savefig(filename, dpi=200, bbox_inches='tight')
    plt.close()
    return filename

def create_formula_card(title, formula, description):
    """Create a card with formula and description"""
    fig, ax = plt.subplots(figsize=(8, 3))

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')

    # Title
    ax.text(5, 4.2, title, fontsize=14, fontweight='bold', ha='center', va='center')
    ax.plot([0.5, 9.5], [3.8, 3.8], 'k-', linewidth=2)

    # Formula
    ax.text(5, 2.8, formula, fontsize=12, ha='center', va='center', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

    # Description
    ax.text(5, 1.5, description, fontsize=10, ha='center', va='center', wrap=True)

    # Border
    ax.plot([0.5, 0.5, 9.5, 9.5, 0.5], [0.5, 4.5, 4.5, 0.5, 0.5], 'k-', linewidth=2)

    return fig

def save_formula_card(filename, fig):
    fig.savefig(filename, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close()

def create_pdf():
    pdf = PDF()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_top_margin(20)
    pdf.add_page()

    print("Erstelle Abbildungen...")
    plot_task1 = create_3d_plot_task1()
    plot_task3 = create_3d_plot_task3()
    plot_task10 = create_3d_plot_task10()
    plot_task15 = create_3d_plot_task15()
    diagram_param = create_diagram_parameter()
    diagram_abstand = create_diagram_abstand()

    # Formula cards
    print("Erstelle Formelkarten...")
    fig1 = create_formula_card("Richtungsvektor (Gerade)", "u = B - A", "Differenz der Ortsvektoren zweier Punkte")
    save_formula_card('/tmp/formel1.png', fig1)

    fig2 = create_formula_card("Normalenvektor (Ebene)", "n = u1 x u2", "Kreuzprodukt zweier Richtungsvektoren")
    save_formula_card('/tmp/formel2.png', fig2)

    fig3 = create_formula_card("Schnittpunkt Gerade-Ebene", "Pg + r*ug = Pe + s*u1 + t*u2", "Gleichsetzen und nach r, s, t aufloesen")
    save_formula_card('/tmp/formel3.png', fig3)

    # Title page
    pdf.chapter_title('Aufgaben - Geraden und Ebenen im R3')
    pdf.set_font('Helvetica', 'I', 10)
    pdf.cell(0, 6, 'Loesungsweg und Platz fuer Rechnungen', 0, 1, 'C')
    pdf.ln(5)

    # Formula cards section
    pdf.section_header('WICHTIGE FORMELN')
    pdf.ln(2)

    # Formula cards in 2x2 layout
    pdf.image('/tmp/formel1.png', x=15, y=55, w=85)
    pdf.image('/tmp/formel2.png', x=110, y=55, w=85)
    pdf.image('/tmp/formel3.png', x=62, y=115, w=85)
    pdf.ln(85)

    # Concept diagrams
    pdf.section_header('GRUNDKONZEPTE')
    pdf.ln(2)
    pdf.image(diagram_param, x=15, y=None, w=90)
    pdf.set_font('Helvetica', '', 9)
    pdf.cell(100, 6, 'Parameterdarstellung', 0, 0)
    pdf.image(diagram_abstand, x=105, y=None, w=90)
    pdf.cell(0, 6, 'Abstandsberechnung', 0, 1)
    pdf.ln(10)

    # Tasks
    pdf.section_header('AUFGABEN')
    pdf.ln(2)

    pdf.task_box(1, "Bestimmen Sie die Parameterdarstellung der Geraden g durch die Punkte A(2|1|3) und B(5|4|9).", difficulty=1)
    pdf.tip_box("Tipp: Der Richtungsvektor ist die Differenz der Ortsvektoren: u = B - A")
    pdf.image(plot_task1, x=15, y=None, w=85)
    pdf.ln(5)

    pdf.task_box(2, "Bestimmen Sie die Parameterdarstellung der Ebene E durch die Punkte P(1|0|2), Q(3|1|4) und R(2|2|1).", difficulty=1)
    pdf.task_box(3, "Gegeben sind die Gerade g: x = (2,1,-1) + r·(1,1,2) und die Ebene E: x = (1,0,1) + s·(1,1,0) + t·(0,1,1). Bestimmen Sie den Schnittpunkt S.", difficulty=2)
    pdf.tip_box("Tipp: Gleichsetzen und das lineare Gleichungssystem nach r, s, t aufloesen")
    pdf.image(plot_task3, x=15, y=None, w=85)
    pdf.ln(5)

    pdf.task_box(4, "Pruefen Sie die Lagenbeziehung der beiden Geraden: g: x = (1,0,1) + r·(1,2,3), h: x = (2,1,3) + s·(2,4,6).", difficulty=1)
    pdf.task_box(5, "Wandeln Sie die Ebenengleichung in Parameterform um: E: 2x - y + 3z = 6.", difficulty=1)
    pdf.task_box(6, "Berechnen Sie den Abstand des Punktes P(3|2|-1) von der Ebene E: x = (1,0,0) + s·(2,0,1) + t·(1,1,0).", difficulty=2)
    pdf.tip_box("Tipp: Erst Normalenvektor berechnen: n = u1 x u2, dann Abstandsformel verwenden")
    pdf.task_box(7, "Bestimmen Sie die Schnittgerade der beiden Ebenen: E1: x = (0,1,2) + r·(1,0,0) + s·(0,1,1) und E2: x - 2y + z = 3.", difficulty=2)
    pdf.task_box(8, "Berechnen Sie den Winkel zwischen der Geraden g: x = (0,0,0) + r·(2,1,2) und der Ebene E: 3x + 4y + 5z = 0.", difficulty=2)
    pdf.tip_box("Tipp: Winkel zwischen Richtungsvektor und Normalenvektor berechnen")
    pdf.task_box(9, "Bestimmen Sie eine Parameterdarstellung der Ebene E, die die Gerade g: x = (1,2,1) + r·(1,1,0) enthaelt und durch den Punkt P(2|0|1) geht.", difficulty=2)
    pdf.task_box(10, "Gegeben sind zwei windschiefe Geraden: g: x = (0,0,0) + r·(1,0,0), h: x = (0,1,1) + s·(0,1,0). Bestimmen Sie den kuerzesten Abstand.", difficulty=3)
    pdf.tip_box("Tipp: Abstand = |(P2-P1) · (u1 x u2)| / |u1 x u2|")
    pdf.image(plot_task10, x=15, y=None, w=85)
    pdf.ln(5)

    pdf.add_page()
    pdf.task_box(11, "Gegeben ist die Ebene E: x + y + z = 6 und der Punkt P(1|2|3). Bestimmen Sie den Fusspunkt des Lotes von P auf die Ebene E.", difficulty=2)
    pdf.task_box(12, "Geben Sie eine Parameterdarstellung der Ebene E: 2x - 3y + z = 4 an.", difficulty=1)
    pdf.task_box(13, "Bestimmen Sie die Parameterdarstellung der Geraden g, die orthogonal zur Ebene E: x - 2y + 2z = 5 ist und durch den Punkt P(1|0|1) geht.", difficulty=2)
    pdf.tip_box("Tipp: Orthogonal zur Ebene heisst: Richtungsvektor = Normalenvektor")
    pdf.task_box(14, "Bestimmen Sie alle Ebenen, die parallel zur Ebene E: 2x - y + 2z = 8 sind und den Abstand 2 zum Ursprung haben.", difficulty=3)
    pdf.task_box(15, "Gegeben sind die drei Punkte A(1|0|0), B(0|1|0) und C(0|0|1). (a) Bestimmen Sie die Parameterdarstellung der Ebene durch A, B und C. (b) Berechnen Sie die Flaeche des Dreiecks ABC.", difficulty=3)
    pdf.tip_box("Tipp: Flaeche = 0.5 * |u x v| (Kreuzprodukt der Seitenvektoren)")
    pdf.image(plot_task15, x=15, y=None, w=85)
    pdf.ln(5)

    pdf.task_box(16, "Gegeben sind die Gerade g: x = (2,1,0) + r·(1,-1,1) und die Ebene E: x = (0,0,1) + s·(2,0,-1) + t·(0,1,1). Bestimmen Sie die Parameter r, s, t im Schnittpunkt.", difficulty=2)
    pdf.task_box(17, "Bestimmen Sie die Parameterdarstellung einer Geraden g durch den Punkt P(1|2|3), die parallel zur Ebene E: x + y + z = 0 und parallel zur Geraden h: x = (0,0,0) + r·(1,1,0) verlaeuft.", difficulty=3)
    pdf.task_box(18, "Bestimmen Sie die Parameterdarstellung der Ebene, die die beiden parallelen Geraden enthaelt: g: x = (1,0,1) + r·(1,1,2), h: x = (3,1,4) + s·(1,1,2).", difficulty=2)
    pdf.task_box(19, "Berechnen Sie den Winkel zwischen den Ebenen: E1: x - y + 2z = 4, E2: 2x + y - z = 1.", difficulty=2)
    pdf.tip_box("Tipp: Winkel zwischen Normalenvektoren berechnen: cos(alpha) = (n1·n2) / (|n1|*|n2|)")
    pdf.task_box(20, "Bestimmen Sie die Parameterdarstellung der Schnittgeraden der drei Ebenen: E1: x + y + z = 6, E2: x - y + z = 2, E3: x + y - z = 0. Pruefen Sie, ob die Ebenen einen gemeinsamen Schnittpunkt haben.", difficulty=3)
    pdf.tip_box("Tipp: Lineares Gleichungssystem loesen - gibt es eine eindeutige Loesung?")

    # Solutions page
    pdf.add_page()
    pdf.chapter_title('Loesungen', color=(66, 180, 100))

    pdf.solution_start(1)
    pdf.formula_box("Schritt 1: Richtungsvektor berechnen")
    pdf.solution_text("u = B - A = (5-2, 4-1, 9-3) = (3, 3, 6)")
    pdf.formula_box("Schritt 2: Parameterdarstellung aufstellen")
    pdf.math("g: x = (2,1,3) + r·(3,3,6)")
    pdf.ln(5)

    pdf.solution_start(2)
    pdf.formula_box("Schritt 1: Richtungsvektoren berechnen")
    pdf.solution_text("u1 = Q - P = (2, 1, 2)")
    pdf.solution_text("u2 = R - P = (1, 2, -1)")
    pdf.formula_box("Schritt 2: Parameterdarstellung aufstellen")
    pdf.math("E: x = (1,0,2) + s·(2,1,2) + t·(1,2,-1)")
    pdf.ln(5)

    pdf.solution_start(3)
    pdf.formula_box("Schritt 1: Gleichsetzen")
    pdf.math("(2+r, 1+r, -1+2r) = (1+s, s+t, 1+t)")
    pdf.formula_box("Schritt 2: Lineares System aufloesen")
    pdf.solution_text("Aus 2. Komponente: 1+r = s+t -> t = 1+r-s")
    pdf.solution_text("Aus 3. Komponente: -1+2r = 1+t = 2+r-s -> r = 3-s")
    pdf.solution_text("Aus 1. Komponente: 2+r = 1+s -> 2+3-s = 1+s -> 5-s = 1+s -> 4 = 2s -> s = 2")
    pdf.formula_box("Schritt 3: Ergebnisse")
    pdf.solution_text("s = 2, r = 1, t = 0")
    pdf.solution_text("Schnittpunkt: S = (3, 2, 1)")
    pdf.ln(5)

    pdf.solution_start(4)
    pdf.formula_box("Schritt 1: Richtungsvektoren vergleichen")
    pdf.solution_text("ug = (1,2,3)")
    pdf.solution_text("uh = (2,4,6) = 2·(1,2,3)")
    pdf.formula_box("Ergebnis")
    pdf.solution_text("uh ist ein Vielfaches von ug -> g und h sind PARALLEL")
    pdf.solution_text("Ph - Pg = (1,1,2) ist kein Vielfaches von (1,2,3)")
    pdf.solution_text("-> g und h sind NICHT IDENTISCH")
    pdf.ln(5)

    pdf.solution_start(5)
    pdf.formula_box("Normalenvektor auslesen")
    pdf.solution_text("Aus der Koordinatengleichung 2x - y + 3z = 6:")
    pdf.math("n = (2, -1, 3)")
    pdf.formula_box("Parameterform")
    pdf.math("E: x = (3,0,0) + s·(1,2,0) + t·(0,3,1)")
    pdf.ln(5)

    pdf.solution_start(6)
    pdf.formula_box("Schritt 1: Normalenvektor berechnen")
    pdf.solution_text("u1 = (2,0,1), u2 = (1,1,0)")
    pdf.solution_text("n = u1 x u2 = (-1, 1, 2)")
    pdf.formula_box("Schritt 2: Abstandsformel")
    pdf.solution_text("Koordinatengleichung: x - y - 2z = 1")
    pdf.solution_text("Abstand: d = |3 - 2 - 2(-1)| / sqrt(1+1+4)")
    pdf.math("d = 3 / sqrt(6)")
    pdf.ln(5)

    pdf.solution_start(7)
    pdf.formula_box("Schritt 1: E1 in Koordinatenform")
    pdf.solution_text("E1: x + y + z = 3")
    pdf.formula_box("Schritt 2: Schnitt berechnen")
    pdf.solution_text("x + y + z = 3")
    pdf.solution_text("x - 2y + z = 3")
    pdf.solution_text("Subtrahiere: 3y = 0 -> y = 0")
    pdf.solution_text("Einsetzen: x + z = 3 -> z = 3 - x")
    pdf.formula_box("Schnittgerade")
    pdf.math("g: x = (0,0,3) + r·(1,0,-1)")
    pdf.ln(5)

    pdf.solution_start(8)
    pdf.formula_box("Schritt 1: Vektoren berechnen")
    pdf.solution_text("u = (2,1,2), n = (3,4,5)")
    pdf.formula_box("Schritt 2: Winkel berechnen")
    pdf.solution_text("u · n = 20")
    pdf.solution_text("|u| = 3, |n| = 5*sqrt(2)")
    pdf.solution_text("cos(alpha) = 20 / (3 * 5*sqrt(2)) = 4 / (3*sqrt(2))")
    pdf.solution_text("Winkel Gerade-Ebene: beta = 90° - alpha")
    pdf.ln(5)

    pdf.solution_start(9)
    pdf.formula_box("Schritt 1: Richtungsvektoren bestimmen")
    pdf.solution_text("u1 = (1,1,0) (aus Gerade g)")
    pdf.solution_text("u2 = P - A = (1, -2, 0)")
    pdf.formula_box("Schritt 2: Parameterdarstellung")
    pdf.math("E: x = (1,2,1) + s·(1,1,0) + t·(1,-2,0)")
    pdf.ln(5)

    pdf.solution_start(10)
    pdf.formula_box("Schritt 1: Vektoren berechnen")
    pdf.solution_text("ug = (1,0,0), uh = (0,1,0)")
    pdf.solution_text("n = ug x uh = (0,0,1)")
    pdf.formula_box("Schritt 2: Abstandsformel")
    pdf.solution_text("P2 - P1 = (0,1,1)")
    pdf.solution_text("d = |(P2-P1) · n| / |n| = |0*0 + 1*0 + 1*1| / 1 = 1")
    pdf.ln(5)

    pdf.add_page()
    pdf.solution_start(11)
    pdf.formula_box("Schritt 1: Normalenvektor")
    pdf.solution_text("n = (1,1,1)")
    pdf.formula_box("Schritt 2: Lot aufstellen")
    pdf.math("g: x = (1,2,3) + r·(1,1,1)")
    pdf.formula_box("Schritt 3: Schnittpunkt berechnen")
    pdf.solution_text("(1+r) + (2+r) + (3+r) = 6 -> 6 + 3r = 6 -> r = 0")
    pdf.solution_text("Fusspunkt: F = (1, 2, 3)")
    pdf.solution_text("(Kontrolle: P liegt auf der Ebene!)")
    pdf.ln(5)

    pdf.solution_start(12)
    pdf.formula_box("Normalenvektor auslesen")
    pdf.solution_text("n = (2, -3, 1)")
    pdf.formula_box("Parameterform")
    pdf.math("E: x = (2,0,0) + s·(3,2,0) + t·(0,1,3)")
    pdf.ln(5)

    pdf.solution_start(13)
    pdf.formula_box("Schritt 1: Normalenvektor auslesen")
    pdf.solution_text("n = (1, -2, 2)")
    pdf.formula_box("Schritt 2: Parameterdarstellung")
    pdf.solution_text("Richtungsvektor = Normalenvektor")
    pdf.math("g: x = (1,0,1) + r·(1,-2,2)")
    pdf.ln(5)

    pdf.solution_start(14)
    pdf.formula_box("Schritt 1: Normalenvektor")
    pdf.solution_text("n = (2, -1, 2)")
    pdf.formula_box("Schritt 2: Parallele Ebenen")
    pdf.solution_text("2x - y + 2z = d")
    pdf.solution_text("Abstand: |d| / 3 = 2 -> d = ±6")
    pdf.formula_box("Ergebnis")
    pdf.solution_text("Zwei Ebenen:")
    pdf.math("E1: 2x - y + 2z = 6")
    pdf.math("E2: 2x - y + 2z = -6")
    pdf.ln(5)

    pdf.solution_start(15)
    pdf.formula_box("Schritt 1: Richtungsvektoren (Teil a)")
    pdf.solution_text("u = B - A = (-1, 1, 0)")
    pdf.solution_text("v = C - A = (-1, 0, 1)")
    pdf.math("E: x = (1,0,0) + s·(-1,1,0) + t·(-1,0,1)")
    pdf.formula_box("Schritt 2: Flaeche berechnen (Teil b)")
    pdf.solution_text("u x v = (1, 1, 1)")
    pdf.solution_text("|u x v| = sqrt(3)")
    pdf.solution_text("Flaeche = 0.5 * sqrt(3) = sqrt(3)/2")
    pdf.ln(5)

    pdf.solution_start(16)
    pdf.formula_box("Schritt 1: Gleichsetzen")
    pdf.math("(2+r, 1-r, r) = (2s, t, 1-s+t)")
    pdf.formula_box("Schritt 2: System aufloesen")
    pdf.solution_text("1: 2+r = 2s")
    pdf.solution_text("2: 1-r = t")
    pdf.solution_text("3: r = 1-s+t")
    pdf.formula_box("Ergebnis")
    pdf.solution_text("s = 6/5, r = 2/5, t = 3/5")
    pdf.solution_text("Schnittpunkt: S = (12/5, 3/5, 2/5)")
    pdf.ln(5)

    pdf.solution_start(17)
    pdf.formula_box("Schritt 1: Bedingungen analysieren")
    pdf.solution_text("nE = (1,1,1), uh = (1,1,0)")
    pdf.solution_text("g parallel zu E -> u orthogonal zu nE")
    pdf.solution_text("g parallel zu h -> u parallel zu uh")
    pdf.formula_box("Schritt 2: Richtungsvektor berechnen")
    pdf.solution_text("u = nE x uh = (-1, 1, 0)")
    pdf.formula_box("Schritt 3: Parameterdarstellung")
    pdf.math("g: x = (1,2,3) + r·(-1,1,0)")
    pdf.ln(5)

    pdf.solution_start(18)
    pdf.formula_box("Schritt 1: Richtungsvektoren")
    pdf.solution_text("u = (1,1,2) (gemeinsamer Richtungsvektor)")
    pdf.solution_text("v = Ph - Pg = (2,1,3)")
    pdf.formula_box("Schritt 2: Parameterdarstellung")
    pdf.math("E: x = (1,0,1) + s·(1,1,2) + t·(2,1,3)")
    pdf.ln(5)

    pdf.solution_start(19)
    pdf.formula_box("Schritt 1: Normalenvektoren")
    pdf.solution_text("n1 = (1, -1, 2)")
    pdf.solution_text("n2 = (2, 1, -1)")
    pdf.formula_box("Schritt 2: Winkel berechnen")
    pdf.solution_text("n1 · n2 = -1")
    pdf.solution_text("|n1| = sqrt(6), |n2| = sqrt(6)")
    pdf.solution_text("cos(alpha) = |-1| / 6 = 1/6")
    pdf.solution_text("alpha = arccos(1/6)")
    pdf.ln(5)

    pdf.solution_start(20)
    pdf.formula_box("Schritt 1: Lineares System aufstellen")
    pdf.solution_text("x + y + z = 6")
    pdf.solution_text("x - y + z = 2")
    pdf.solution_text("x + y - z = 0")
    pdf.formula_box("Schritt 2: Aufloesen")
    pdf.solution_text("E1 - E2: 2y = 4 -> y = 2")
    pdf.solution_text("E1 - E3: 2z = 6 -> z = 3")
    pdf.solution_text("Einsetzen in E3: x + 2 - 3 = 0 -> x = 1")
    pdf.formula_box("Ergebnis")
    pdf.solution_text("Schnittpunkt: S(1, 2, 3)")
    pdf.solution_text("Die drei Ebenen schneiden sich im Punkt S, NICHT in einer Geraden!")

    # Clean up temporary files
    for f in [plot_task1, plot_task3, plot_task10, plot_task15, diagram_param, diagram_abstand,
              '/tmp/formel1.png', '/tmp/formel2.png', '/tmp/formel3.png']:
        if os.path.exists(f):
            os.remove(f)

    return pdf

if __name__ == '__main__':
    pdf = create_pdf()
    output_file = '/home/openclaw/.openclaw/workspace/mathe/geraden-ebenen-uebung-final.pdf'
    pdf.output(output_file)
    print(f"PDF erstellt: {output_file}")
    print(f"Dateigroesse: {os.path.getsize(output_file)} Bytes")
