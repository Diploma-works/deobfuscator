def check_triangle(a,b,c):
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
              return "Isosceles"

a = int(input())
b = int(input())
c = int(input())

print(check_triangle(a,b,c))
input()
