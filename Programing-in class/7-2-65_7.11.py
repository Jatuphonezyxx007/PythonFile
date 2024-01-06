def TriangleArea(w,h):
    area = w*h/2
    return area
width = float(input("Enter Width:"))
height = int(input("Enter Height:"))
TotalArea = TriangleArea(width,height)
print("The area of triangle is {0:,.2f}".format(TotalArea))
