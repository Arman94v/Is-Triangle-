print("Will you be able to create a triangle or not?!")
print("One way to find out!!")

a = float(input("Size of the First  Edge:"))
b = float(input("Size of the Second Edge:"))
c = float(input("Size of the Third  Edge:"))

d = a + b
e = b + c
f = a + c

if (d > c) and (e > a) and (f > b):
    print("That would be a triangle")
else:
    print("Nah you got it all wrong!!")
    print("To determine if 3 side lengths are a triangle, use the triangle inequality theorem, which states that the sum of 2 sides of a triangle must be greater than the third side.")
    print("Wanna try again?! Run again!!")