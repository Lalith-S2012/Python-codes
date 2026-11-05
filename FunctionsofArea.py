def area_of_square(L):
    area = L * L
    return area
    
def area_of_rectangle(l, H):
    area_2 = l * H
    return area_2

def area_of_triangle(h, b):
    area_3 = (h * b) / 2
    return area_3

square = float(input("Enter the side of a square: "))
print("Area of a Square is:", area_of_square(square))

rect_1 = float(input("Enter the Lenght of a Rectangle: "))

rect_2 = float(input("Enter the Height of a Rectangle: ")) 
print("Area of a Ractangle is:", area_of_rectangle(rect_1, rect_2))

triangle_1 = float(input("Enter the Height of the Triangle: "))

triangle_2 = float(input("Enter the Lenght of the base of the Triangle: "))
print("Area of a Triangle is:", area_of_triangle(triangle_1, triangle_2))


