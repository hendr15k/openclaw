#!/usr/bin/env python3
from fpdf import FPDF
import os

class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        self.set_font('Arial', 'B', 10)
        self.cell(60, 6, 'Lineare Algebra', 0, 0, 'L')
        self.cell(80, 6, 'Uebung: Geraden & Ebenen', 0, 0, 'C')
        self.cell(60, 6, f'Seite {self.page_no()}', 0, 0, 'R')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(2)

    def task(self, number, text):
        self.set_font('Arial', '', 11)
        self.cell(10, 6, f'{number}.', 0, 0)
        self.multi_cell(0, 6, text)
        self.ln(3)

    def solution_start(self, number):
        self.set_font('Arial', 'B', 11)
        self.set_fill_color(230, 240, 255)
        self.cell(0, 6, f'Lösung {number}:', 0, 1, 'L', 1)
        self.set_font('Arial', '', 10)

    def solution_text(self, text):
        self.multi_cell(170, 5, text)
        self.ln(2)

    def math(self, text):
        """Format math text"""
        self.set_font('Courier', '', 10)
        self.multi_cell(170, 5, text)
        self.set_font('Arial', '', 10)

def create_pdf():
    pdf = PDF()
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.set_top_margin(15)
    pdf.add_page()

    # Titelseite Aufgaben
    pdf.chapter_title('Aufgaben - Geraden und Ebenen im R³')
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 6, 'Loesungsweg und Platz fuer Rechnungen', 0, 1, 'C')
    pdf.ln(5)

    # Aufgaben
    pdf.task(1, "Bestimmen Sie die Parameterdarstellung der Geraden g durch die Punkte A(2|1|3) und B(5|4|9).")
    pdf.task(2, "Bestimmen Sie die Parameterdarstellung der Ebene E durch die Punkte P(1|0|2), Q(3|1|4) und R(2|2|1).")
    pdf.task(3, "Gegeben sind die Gerade g: x = (2,1,-1) + r·(1,1,2) und die Ebene E: x = (1,0,1) + s·(1,1,0) + t·(0,1,1). Bestimmen Sie den Schnittpunkt S.")
    pdf.task(4, "Pruefen Sie die Lagenbeziehung der beiden Geraden: g: x = (1,0,1) + r·(1,2,3), h: x = (2,1,3) + s·(2,4,6). Sind sie parallel, windschief oder schneiden sie sich?")
    pdf.task(5, "Wandeln Sie die Ebenengleichung in Parameterform um: E: 2x - y + 3z = 6.")
    pdf.task(6, "Berechnen Sie den Abstand des Punktes P(3|2|-1) von der Ebene E: x = (1,0,0) + s·(2,0,1) + t·(1,1,0).")
    pdf.task(7, "Bestimmen Sie die Schnittgerade der beiden Ebenen: E1: x = (0,1,2) + r·(1,0,0) + s·(0,1,1) und E2: x - 2y + z = 3.")
    pdf.task(8, "Berechnen Sie den Winkel zwischen der Geraden g: x = (0,0,0) + r·(2,1,2) und der Ebene E: 3x + 4y + 5z = 0.")
    pdf.task(9, "Bestimmen Sie eine Parameterdarstellung der Ebene E, die die Gerade g: x = (1,2,1) + r·(1,1,0) enthaelt und durch den Punkt P(2|0|1) geht.")
    pdf.task(10, "Gegeben sind zwei windschiefe Geraden: g: x = (0,0,0) + r·(1,0,0), h: x = (0,1,1) + s·(0,1,0). Bestimmen Sie den kuerzesten Abstand.")

    pdf.add_page()
    pdf.task(11, "Gegeben ist die Ebene E: x + y + z = 6 und der Punkt P(1|2|3). Bestimmen Sie den Fusspunkt des Lotes von P auf die Ebene E.")
    pdf.task(12, "Geben Sie eine Parameterdarstellung der Ebene E: 2x - 3y + z = 4 an.")
    pdf.task(13, "Bestimmen Sie die Parameterdarstellung der Geraden g, die orthogonal zur Ebene E: x - 2y + 2z = 5 ist und durch den Punkt P(1|0|1) geht.")
    pdf.task(14, "Bestimmen Sie alle Ebenen, die parallel zur Ebene E: 2x - y + 2z = 8 sind und den Abstand 2 zum Ursprung haben.")
    pdf.task(15, "Gegeben sind die drei Punkte A(1|0|0), B(0|1|0) und C(0|0|1). (a) Bestimmen Sie die Parameterdarstellung der Ebene durch A, B und C. (b) Berechnen Sie die Flaeche des Dreiecks ABC.")
    pdf.task(16, "Gegeben sind die Gerade g: x = (2,1,0) + r·(1,-1,1) und die Ebene E: x = (0,0,1) + s·(2,0,-1) + t·(0,1,1). Bestimmen Sie die Parameter r, s, t im Schnittpunkt.")
    pdf.task(17, "Bestimmen Sie die Parameterdarstellung einer Geraden g durch den Punkt P(1|2|3), die parallel zur Ebene E: x + y + z = 0 und parallel zur Geraden h: x = (0,0,0) + r·(1,1,0) verlaeuft.")
    pdf.task(18, "Bestimmen Sie die Parameterdarstellung der Ebene, die die beiden parallelen Geraden enthaelt: g: x = (1,0,1) + r·(1,1,2), h: x = (3,1,4) + s·(1,1,2).")
    pdf.task(19, "Berechnen Sie den Winkel zwischen den Ebenen: E1: x - y + 2z = 4, E2: 2x + y - z = 1.")
    pdf.task(20, "Bestimmen Sie die Parameterdarstellung der Schnittgeraden der drei Ebenen: E1: x + y + z = 6, E2: x - y + z = 2, E3: x + y - z = 0. Pruefen Sie, ob die Ebenen einen gemeinsamen Schnittpunkt haben.")

    # Neue Seite für Lösungen
    pdf.add_page()
    pdf.chapter_title('Loesungen')

    # Lösungen
    pdf.ln(5)
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
    pdf.ln(5)

    return pdf

if __name__ == '__main__':
    pdf = create_pdf()
    output_file = '/home/openclaw/.openclaw/workspace/mathe/geraden-ebenen-uebung.pdf'
    pdf.output(output_file)
    print(f"PDF erstellt: {output_file}")
    print(f"Dateigroesse: {os.path.getsize(output_file)} Bytes")
