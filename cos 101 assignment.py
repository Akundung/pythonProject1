print(" PROGRAM TO CALCULATE MAHTEMATICAL AND PHYSICS EQUATION")
def calculate_linear_equation(M, X, B):
    linear_equation = M * X + B
    #formula for linear_equation is Y = MX + B
    return linear_equation

print("select either a,b,c or d to continue")
print('a. linear_equation')
print('b. weight')
print('d. area of rectangle')
print('c. potential_energy')
select_letter = (input())

if select_letter == 'a':
    print("the formula of linear_equation is Y = MX + B")
    print("input the value of M")
    M = float(input())
    print("input the value of X")
    X = float(input())
    print("input the value of B")
    B = float(input())
    linear_equation = calculate_linear_equation(M, X, B)
    print("linear equation (y):", linear_equation, )

def calculate_area_of_rectangle(lenght, width):
    area = lenght * width
    #formula for area is A = lb
    return area

if select_letter == 'd':
    print("the formular for area_of_rectangle is A = lb")
    print("input the value of l:,")
    length = float(input())
    print("input the value of b:,")
    width = float(input())
    area = calculate_area_of_rectangle(length, width)
    print("area (A):", area, )

def calculate_weight(mass, gravity):
    weight = mass * gravity
    #formula for weight is W = mg
    return weight

if select_letter == 'b':
    print("the formular for weight is W = mg")
    print("input the value of m:,")
    mass = float(input())
    print("input the value of g:,")
    gravity = float(input())
    weight = calculate_weight(mass, gravity)
    print("weight (W):", weight, )

def calculate_energy(mass, speed_of_light,):
    energy = mass * speed_of_light**2
    #formula for energy is E = mc^2
    return energy

if select_letter == 'e':
    print('the formula for energy is E = mc^2')
    print("input the value of m")
    mass = float(input())
    print("input the value of c")
    speed_of_light = float(input())
    energy = calculate_energy(mass, speed_of_light,)
    print("energy (E):", energy, )

def calculate_potential_energy(mass, velocity,):
    potential_energy = mass * velocity**2
    #formular for potential_energy is P.E = mv^2
    return potential_energy

if select_letter == 'c':
    print('the formula for potential_energy is P.E = mv^2')
    print('input the value of m')
    mass = float(input())
    print('input the value of v')
    velocity = float(input())
    potential_energy = calculate_potential_energy(mass, velocity,)
    print("Potential_energy (P.E):", potential_energy, )