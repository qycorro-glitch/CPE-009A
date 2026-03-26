import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = f"Two real roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        result = f"One real root: {root}"
    else:
        real = -b / (2*a)
        imag = math.sqrt(-discriminant) / (2*a)
        result = f"Complex roots: {real}+{imag}i, {real}-{imag}i"

    return result


def write_to_file(a, b, c, filename="quadratic_output.txt"):
    result = solve_quadratic(a, b, c)

    with open(filename, "w") as file:
        file.write(f"Equation: {a}x^2 + {b}x + {c} = 0\n")
        file.write(f"Result: {result}\n")

    print("Results written to file.")

write_to_file(1, -3, 2)