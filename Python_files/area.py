#Area Calculator
x = input("Which shape of area do you want to work with: ");
x = x.lower()
if (x == "Circle"):
    r = int(input("Enter the Radius: "));
    a = 3.14*r^2
    print("Area of circle is",a);
elif (x == "Rectange"):
    l = int(input("enter the length: "));
    b = int(input("Enter the breath: "));
    a = 2*(l+b);
    print("Area is",a);
elif (x == "square"):
    l = int(input("enter the length: "));
    a = l^2;
    print("Area is",a);
elif (x == "triangle"):
    h = int(input("Enter the Heigth"));
    b = int(input("Enter the base"));
    a = b*h*0.5;
    print("area is ",a);
elif (x == "polygon"){
    
}

    

