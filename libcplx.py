import numpy as np
#Cristian David Naranjo


# 1 .Suma complejos representados como una tupla (real, imaginaria)
def sumacplx(a, b):
    real = a[0] + b[0]
    img = a[1] + b[1]
    return (real, img)


# 3 resta complejos representados como una tupla
def restcplx(a, b):
    real = (a[0]) - (b[0])
    img = (a[1]) - (b[1])
    return (real, img)


# 3 Multiplica complejos representados como una tupla
def multcplx(a, b):
    real = (a[0] * b[0]) - (a[1] * b[1])
    img = (a[0] * b[1]) + (b[0] * a[1])
    return (real, img)


# 4 divide complejos representados como una tupla
def divcplx(a, b):
    real = ((a[0] * b[0]) + (a[1] * b[1])) // (((b[0]) ** 2) + ((b[1]) ** 2))
    img = ((b[0] * a[1]) - (a[0] * b[1])) // (((b[0]) ** 2) + ((b[1]) ** 2))
    return (real, img)


# 5 calcula el modulo de  complejos representados como una tupla
def modulo(a):
    a = ((a[0]) ** 2) + ((a[1]) ** 2)
    real = np.sqrt(a)
    return (real)

# 6 calcula el conjugado de complejos representados como una tupla
def conjugado(a):
    real = a[0]
    img = a[1]
    if img > 0:
        img = img * -1
    else:
        img = img * -1
    return(real,img)
# 7a pasa  de cartesianas a polares
def toPolar(c):
    theta = np.arctan2(c[1], c[0])
    rho = np.sqrt((c[0] * c[0]) + (c[1] * c[1]))
    return (rho, theta)
# 7b pasa  de polares a cartesianas
def toCartesian(c):
    real = c[0] * np.cos(c[1])
    img =  c[0] * np.sin(c[1])
    return(real,img)

# 8 halla la fase
def Phase(c):
    theta = np.arctan2(c[1], c[0])
    if 0 <= theta < 360:
        return theta



def prettyprinting(c):
    # Para cartesianos
    if c[1] > 0:
        print(str(c[0]) + "+" + str(c[1]) + "i")
    else:
        print(str(c[0]) + str(c[1]) + "i")

def polprettyprinting(c):
    # Para polares
    print(str(c[0]) + " e^(i " + str(c[1]) + ")")


if __name__ == '__main__':
    prettyprinting(sumacplx((2, 3), (4, 7)))
    prettyprinting(restcplx((2, 3), (4, 7)))
    prettyprinting(multcplx((2, 3), (4, 7)))
    prettyprinting(divcplx((-2, 1), (1, 2)))
    print(modulo((10, 4)))
    prettyprinting(conjugado((3,3)))
    print(Phase((4,2)))
    print(toCartesian((90,4)))

    # Prueba polares
    polprettyprinting(toPolar((-3, -2)))




