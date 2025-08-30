# Area Calculator
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Area Calculator")
        self.setFixedSize(400, 200)
        self.initUI()

    def initUI(self):
        self.label = QLabel("Enter shape name:", self)
        self.label.setGeometry(10, 10, 150, 30)

        self.button = QPushButton("Enter", self)
        self.button.setGeometry(150, 50, 100, 30)
        
        self.input = QLineEdit(self)
        self.input.setGeometry(10, 10, 200, 30)
        
        self.calculate = QPushButton("Calculate", self)
        self.calculate.setGeometry(150, 50, 100, 30)
        self.calculate.clicked.connect(self.calculate_area)
        
        self.result = QLabel("", self)
        self.result.setGeometry(10, 90, 380, 100)
        self.result.setWordWrap(True)
    def calculate_area(self):
        shape = self.input.text().strip().lower()
        if shape == "circle":
            r = float(input("Enter the radius: "))
            a = 3.14 * (r ** 2)
            self.result.setText(f"Area of circle is {a}")
        elif shape == "rectangle":
            l = float(input("Enter the length: "))
            b = float(input("Enter the breadth: "))
            a = l * b
            self.result.setText(f"Area of rectangle is {a}")
        elif shape == "square":
            l = float(input("Enter the length: "))
            a = l ** 2
            self.result.setText(f"Area of square is {a}")
        elif shape == "triangle":
            h = float(input("Enter the height: "))
            b = float(input("Enter the base: "))
            a = 0.5 * b * h
            self.result.setText(f"Area of triangle is {a}")
        elif shape == "parallelogram":
            h = float(input("Enter the height: "))
            b = float(input("Enter the base: "))
            a = b * h
            self.result.setText(f"Area of parallelogram is {a}")
        elif shape == "trapezium":
            a1 = float(input("Enter the first parallel side: "))
            b1 = float(input("Enter the second parallel side: "))
            h = float(input("Enter the height: "))
            area = 0.5 * (a1 + b1) * h
            self.result.setText(f"Area of trapezium is {area}")
        elif shape == "ellipse":
            a1 = float(input("Enter the semi-major axis: "))
            b1 = float(input("Enter the semi-minor axis: "))
            area = 3.14 * a1 * b1
            self.result.setText(f"Area of ellipse is {area}")
        elif shape == "rhombus":
            d1 = float(input("Enter the length of first diagonal: "))
            d2 = float(input("Enter the length of second diagonal: "))
            area = 0.5 * d1 * d2
            self.result.setText(f"Area of rhombus is {area}")
        elif shape == "kite":
            d1 = float(input("Enter the length of first diagonal: "))
            d2 = float(input("Enter the length of second diagonal: "))
            area = 0.5 * d1 * d2
            self.result.setText(f"Area of kite is {area}")
        elif shape == "sector":
            r = float(input("Enter the radius: "))
            theta = float(input("Enter the angle in degrees: "))
            area = (3.14 * r * r * theta) / 360
            self.result.setText(f"Area of sector is {area}")
        elif shape == "segment":
            r = float(input("Enter the radius: "))
            theta = float(input("Enter the angle in degrees: "))
            area = (3.14 * r * r * (theta - (3.14 / 180) * (theta))) / 360
            self.result.setText(f"Area of segment is {area}")
        elif shape == "annulus":
            R = float(input("Enter the radius of the outer circle: "))
            r = float(input("Enter the radius of the inner circle: "))
            area = 3.14 * (R * R - r * r)
            self.result.setText(f"Area of annulus is {area}")
        elif shape == "frustum":
            r1 = float(input("Enter the radius of the top base: "))
            r2 = float(input("Enter the radius of the bottom base: "))
            h = float(input("Enter the height: "))
            area = 3.14 * (r1 + r2) * ((r1 - r2) ** 2 + h ** 2) ** 0.5 + 3.14 * (r1 ** 2 + r2 ** 2)
            self.result.setText(f"Area of frustum is {area}")
        elif shape == "cylinder":
            r = float(input("Enter the radius: "))
            h = float(input("Enter the height: "))
            area = 2 * 3.14 * r * (r + h)
            self.result.setText(f"Area of cylinder is {area}")
        elif shape == "cone":
            r = float(input("Enter the radius: "))
            h = float(input("Enter the height: "))
            area = 3.14 * r * (r + (h ** 2 + r ** 2) ** 0.5)
            self.result.setText(f"Area of cone is {area}")
        elif shape == "sphere":
            r = float(input("Enter the radius: "))
            area = 4 * 3.14 * r * r
            self.result.setText(f"Area of sphere is {area}")
        elif shape == "hemisphere":
            r = float(input("Enter the radius: "))
            area = 3 * 3.14 * r * r
            self.result.setText(f"Area of hemisphere is {area}")
        elif shape == "cuboida":
            l = float(input("Enter the length: "))
            b = float(input("Enter the breadth: "))
            h = float(input("Enter the height: "))
            area = 2 * (l * b + b * h + h * l)
            self.result.setText(f"Area of cuboida is {area}")
        elif shape == "cube":
            a = float(input("Enter the side length: "))
            area = 6 * a * a
            self.result.setText(f"Area of cube is {area}")
        elif shape == "torus":
            R = float(input("Enter the major radius: "))
            r = float(input("Enter the minor radius: "))
            area = 4 * 3.14 * 3.14 * R * r
            self.result.setText(f"Area of torus is {area}")
        elif shape == "help":
            self.result.setText("Available shapes: circle, rectangle, square, triangle, parallelogram, trapezium, ellipse, rhombus, kite, sector, segment, annulus, frustum, cylinder, cone, sphere, hemisphere, cuboida, cube, torus\nType 'exit' to quit the program.")
        elif shape == "":
            self.result.setText("Please enter a shape name.")
        elif shape == "exit":
            self.close()
        else:
            self.result.setText("Invalid input")
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
if __name__ == "__main__":
    main()