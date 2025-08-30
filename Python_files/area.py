#Area Calculator
while True:
    x = input("Which shape of area do you want to work with: ").strip().lower()
    if x == "circle":
        r = float(input("Enter the radius: "))
        a = 3.14 * (r ** 2)
        print("Area of circle is", a)
        break
    elif x == "rectangle":
        l = float(input("Enter the length: "))
        b = float(input("Enter the breadth: "))
        a = l * b
        print("Area of rectangle is", a)
        break
    elif x == "square":
        l = float(input("Enter the length: "))
        a = l ** 2
        print("Area of square is", a)
        break
    elif x == "triangle":
        h = float(input("Enter the height: "))
        b = float(input("Enter the base: "))
        a = 0.5 * b * h
        print("Area of triangle is", a)
        break
    elif x == "parallelogram":
        h = float(input("Enter the height: "))
        b = float(input("Enter the base: "))
        a = b * h
        print("Area of parallelogram is", a)
        break
    elif x == "trapezium":
        a = float(input("Enter the first parallel side: "))
        b = float(input("Enter the second parallel side: "))
        h = float(input("Enter the height: "))
        area = 0.5 * (a + b) * h
        print("Area of trapezium is", area)
        break
    elif x == "ellipse":
        a = float(input("Enter the semi-major axis: "))
        b = float(input("Enter the semi-minor axis: "))
        area = 3.14 * a * b
        print("Area of ellipse is", area)
        break
    elif x == "rhombus":
        d1 = float(input("Enter the length of first diagonal: "))
        d2 = float(input("Enter the length of second diagonal: "))
        area = 0.5 * d1 * d2
        print("Area of rhombus is", area)
        break
    elif x == "kite":
        d1 = float(input("Enter the length of first diagonal: "))
        d2 = float(input("Enter the length of second diagonal: "))
        area = 0.5 * d1 * d2
        print("Area of kite is", area)
        break
    elif x == "sector":
        r = float(input("Enter the radius: "))
        theta = float(input("Enter the angle in degrees: "))
        area = (3.14 * r * r * theta) / 360
        print("Area of sector is", area)
        break
    elif x == "segment":
        r = float(input("Enter the radius: "))
        theta = float(input("Enter the angle in degrees: "))
        area = (3.14 * r * r * (theta - (3.14 / 180) * (theta))) / 360
        print("Area of segment is", area)
        break
    elif x == "annulus":
        R = float(input("Enter the radius of the outer circle: "))
        r = float(input("Enter the radius of the inner circle: "))
        area = 3.14 * (R * R - r * r)
        print("Area of annulus is", area)
        break
    elif x == "frustum":
        r1 = float(input("Enter the radius of the top base: "))
        r2 = float(input("Enter the radius of the bottom base: "))
        h = float(input("Enter the height: "))
        area = 3.14 * (r1 + r2) * ((r1 - r2) ** 2 + h ** 2) ** 0.5 + 3.14 * (r1 ** 2 + r2 ** 2)
        print("Area of frustum is", area)
        break
    elif x == "cylinder":
        r = float(input("Enter the radius: "))
        h = float(input("Enter the height: "))
        area = 2 * 3.14 * r * (r + h)
        print("Area of cylinder is", area)
        break
    elif x == "cone":
        r = float(input("Enter the radius: "))
        h = float(input("Enter the height: "))
        area = 3.14 * r * (r + (h ** 2 + r ** 2) ** 0.5)
        print("Area of cone is", area)
        break
    elif x == "sphere":
        r = float(input("Enter the radius: "))
        area = 4 * 3.14 * r * r
        print("Area of sphere is", area)
        break
    elif x == "hemisphere":
        r = float(input("Enter the radius: "))
        area = 3 * 3.14 * r * r
        print("Area of hemisphere is", area)
        break
    elif x == "cuboida":
        l = float(input("Enter the length: "))
        b = float(input("Enter the breadth: "))
        h = float(input("Enter the height: "))
        area = 2 * (l * b + b * h + h * l)
        print("Area of cuboida is", area)
        break
    elif x == "cube":
        a = float(input("Enter the side length: "))
        area = 6 * a * a
        print("Area of cube is", area)
        break
    elif x == "torus":
        R = float(input("Enter the major radius: "))
        r = float(input("Enter the minor radius: "))
        area = 4 * 3.14 * 3.14 * R * r
        print("Area of torus is", area)
        break
    elif x == "exit":
        print("Exiting the program.")
        break
    elif x == "help":
        print("Available shapes: circle, rectangle, square, triangle, parallelogram, trapezium, ellipse, rhombus, kite, sector, segment, annulus, frustum, cylinder, cone, sphere, hemisphere, cuboida, cube, torus")
        print("Type 'exit' to quit the program.")
        continue
    elif x == "":
        print("Please enter a shape name.")
        continue
    else:
        print("Invalid input")

    

