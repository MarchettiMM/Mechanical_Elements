import math
ratio = 3.14159
e = 0.001/100
eps_ref = ratio*e
eps = eps_ref
Nmin = 15
Nmax = 100
s = 1
c = 0
R_high = (ratio + eps)
R_low = (ratio - eps)
Nh3 = math.floor((Nmax * Nmax) / R_high)
Nh4 = math.floor(Nmax / math.sqrt(R_high))
print("N2", " N3", " Ratio1", " N4", " N5", " Ratio2",
      "error")
while (s == 1):
    for pinion1 in range(Nmin, Nh4+1, 1):
        Nhh = min(Nmax, math.floor(Nh3/pinion1))
        for pinion2 in range(pinion1, Nhh+1, 1):
            P = math.floor(pinion1 * pinion2 * R_high)
            Q = math.floor(pinion1 * pinion2 * R_low)+1
            if (P < Q):
                pass
            else:
                Nm = max(Nmin, math.floor((Q+Nmax-1) / Nmax))
                Np = math.sqrt(P)
                for K in range(Q, P+1, 1):
                    for gear_1 in range(Nm, int(Np+1), 1):
                        if ((K % gear_1) != 0):
                            pass
                        else:
                            gear_2 = (K/gear_1)
                            error = ((ratio-K)/(pinion1*pinion2))
                            if (error > eps):
                                pass
                            else:
                                pin1 = pinion1
                                pin2 = pinion2
                                gear1 = gear_1
                                gear2 = gear_2
                                error = round(abs(error), 5)
                                ratio1 = round((gear_1 / pinion1), 4)
                                ratio2 = round((gear_2 / pinion2), 4)
                                ratio = (ratio1 * ratio2)
                                s = s + 1
                                print(pin1, " ", gear_1, " ", "%.4f" % ratio1, " ",
                                      pin2, " ", gear2, " ", "%.4f" % ratio2, " ", "%.5f" % error)
                                s != 1
eps = eps*2
c = c + 1

# From here, the calculation of the geometric characteristics of the composite set begins
print("\nEnter the number of teeth for each gear with values ​​from 15 to 100\n")
n2 = int(input("Enter the number of teeth on pinion N2: "))
n3 = int(input("Enter the number of N3 sprocket teeth: "))
n4 = int(input("Enter the number of teeth on pinion N4: "))
n5 = int(input("Enter the number of N3 sprocket teeth: "))
if (n2 and n3 and n4 and n5) >= 15 and (n2 and n3 and n4 and n5) <= 100:
    m = int(input("Enter modulus value 'm': "))
    angle = int(input("Enter the pressure angle value: "))
    cosangle = math.cos(math.radians(angle))
    senangle = math.sin(math.radians(angle))
    print("\nGeometric characteristics of the composite set\n")

    # Gear Ratio
    mg = (n3*n5)/(n2*n4)
    print("Gear Ratio:", "%.4f" % mg)

    # Circular Step
    pc = math.pi * m
    print("Circular Step:", "%.4f" % pc)

    # Base Step
    pb = pc * (cosangle)
    print("Base Step:", "%.4f" % pb)

    # Diameter of Pinion
    dp1 = n2*m
    dp2 = n4*m
    print("N2 pinion pitch diameter:", dp1)
    print("N4 pinion pitch diameter:", dp2)

    # Sprocket wheel diameter
    dg1 = n3*m
    dg2 = n5*m
    print("N3 sprocket pitch diameter:", dg1)
    print("N5 sprocket pitch diameter:", dg2)

    # Pinion primitive radius
    rp1 = (dp1/2)
    rp2 = (dp2/2)
    print("N2 pinion radius:", rp1)
    print("N4 pinion radius:", rp2)

    # Primitive radius of sprockets
    rg1 = (dg1/2)
    rg2 = (dg2/2)
    print("N3 sprockets radius:", rg1)
    print("N5 sprockets radius:", rg2)

    # Distance between nominal center C
    cn2n3 = rp1 + rg1
    cn4n5 = rp2 + rg2
    print("Nominal Center N2-N3:", cn2n3)
    print("Nominal Center N4-N5:", cn4n5)

    # Addendum and dedentum values ​​according to the table in the book by R. L. Norton
    if (m > 1.25):
        a = 1.00 * m
        b = 1.25 * m
    else:
        a = 1.00 * m
        b = 1.40 * m
        print("A (Addendum):", a)
        print("B (Dedentum):", b)

    # Tooth Depth
    ht = a + b
    print("Dept:", ht)

    # Gap
    c = b - a
    print("Gap:", "%.4f" % c)

    # Outside diameter of pinions
    dop1 = (dp1 + (2*a))
    dop2 = (dp2 + (2*a))
    print("Pinion outside diameter N2:", dop1)
    print("Pinion outside diameter N4:", dop2)

    # Outside diameter of sprockets
    dog1 = (dg1 + (2*a))
    dog2 = (dg2 + (2*a))
    print("Sprockets outside diameter N3:", dog1)
    print("Sprockets outside diameter N5:", dog2)

    # Covering degree between N2 and N3
    zN2N3 = (math.sqrt(((rp1+a)**2) - ((rp1*cosangle)**2)) + math.sqrt(((rg1+a)**2) -
                                                                       ((rg1*cosangle)**2))) - (cn2n3*senangle)
    mpN2N3 = zN2N3/pb
    print("Covering degree between N2 and N3:", "%.4f" % mpN2N3)

    # Covering degree between N4 and N5
    zN4N5 = (math.sqrt(((rp2+a)**2) - ((rp2*cosangle)**2)) + math.sqrt(((rg2+a)**2) -
                                                                       ((rg2*cosangle)**2))) - (cn4n5*senangle)
    mpN4N5 = zN4N5/pb
    print("Covering degree between N4 and N5:", "%.4f" % mpN4N5)

    # Engine calculations
    print("\nEngine calculations\n")
    f = 1800 / 60
    P = 2.206

    # Input speed (pinion N2)
    Vent = 2 * math.pi * f
    print("Input speed:", "%.4f" % Vent)

    # Input torque
    te = (P * 1000) / Vent
    print("Input torque:", "%.4f" % te)
    # Output torque
    ts = P / Vent * ((rp1 / rg1) * (rp2 / rg2))
    print("Output torque:", "%.4f" % ts)
else:
    print("\nEnter value for the number of teeth from 15 to 100!")
