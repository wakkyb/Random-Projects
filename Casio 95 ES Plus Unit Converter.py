def inch_to_cm(ins):
    _cm = ins * 2.54
    return _cm


# 2
def cm_to_inch(_cm):
    inch = _cm / 2.54
    return inch


# 3
def ft_to_m(ft):
    _m = ft / 3.28084
    return _m


# 4
def m_to_ft(_m):
    ft = _m * 3.28084
    return ft


# 5
def yd_to_m(yd):
    _m = yd / 1.09361
    return _m


# 6
def m_to_yd(_m):
    yd = _m * 1.09361
    return yd


# 7
def mile_to_km(mile):
    km = mile * 1.60934
    return km


# 8
def km_to_mile(km):
    mile = km / 1.60934
    return mile


# 9
def F_to_C(_F):
    _C = (_F - 32) * 0.55
    return _C


# 10
def C_to_F(_C):
    _F = (1.8 * _C) + 32
    return _F


# 11
def J_to_cal(J):
    cal = J * 4.184
    return cal


# 12
def cal_to_J(cal):
    J = cal / 4.184
    return J


# 13
def kg_to_lb(kg):
    lb = 0.4535 * kg
    return lb


# 14
def lb_to_kg(lb):
    kg = lb / 0.4535
    return kg


# 15
def kmph_to_mps(kph):
    mps = kph * (1 / 3.6)
    return mps


# 16
def mps_to_kmph(mps):
    kph = mps / 0.2777
    return kph


# 17
def oz_to_g(oz):
    g = 0.035274 * oz
    return g


# # 18
def g_to_oz(g):
    oz = g / 0.035274


# # 19
def gal_UK_to_L(gal_UK):
    L = gal_UK * 4.546
    return L


# 20
def L_to_gal_UK(L):
    gal = L / 4.546
    return gal


# 21
def parsec_to_km(parsec):
    km = parsec * 3.086e+13
    return km


# 22
def km_to_parsec(km):
    parsec = km / 3.086e+13
    return parsec


# 23
def L_to_gal_US(L):
    galUS = L * 0.26417
    return galUS


# 24
def gal_US_to_L(gal_US):
    L = gal_US / 0.26417
    return L


# 25
def atm_to_pa(atm):
    pa = atm * 9.86923e-6
    return pa


# 26
def pa_to_atm(pa):
    atm = pa / 9.86923e-6
    return atm


# 27
def mmHG_to_pa(mmHG):
    pa = mmHG * 133.32
    return pa


# 28
def pa_to_mmHG(pa):
    mmhg = pa / 133.32
    return mmhg


# 29
def hp_to_kW(hp):
    kw = hp * 0.7457
    return kw


# 30
def kW_to_hp(kW):
    hp = kW / 0.7457
    return hp


# 31
def lbfin2_to_kPa(lbfin2):
    kpa = 0.145038 * lbfin2
    return kpa


# 32
def kPa_to_lbfin2(kPa):
    lbfin2 = kPa / 0.145038
    return lbfin2


# 33
def nautical_mile_to_m(n_m):
    mile = n_m / 0.868976
    return mile


# 34
def m_to_nautical_mile(m):
    nautical = m * 0.868976
    return nautical


# 35
def acre_to_m2(acre):
    m2 = acre * 4046.86
    return m2


# 36
def m2_to_acre(m2):
    acre = m2 / 4046.86
    return acre


if __name__ == '__main__':

    converter = ['1. inch --> cm', '2. cm --> inch', '3. ft --> m', '4. m --> ft', '5. yd --> m', '6. m --> yd',
                 '7. mile --> km', '8. km --> mile', '9. F --> C', '10. C --> F', '11. J --> cal', '12. cal --> J',
                 '13. Kg --> lb', '14. lb --> kg', '15. km/h --> m/s ', '16. m/s --> km/h', '17. oz --> g',
                 '18. g --> oz', '19. gal(UK) --> L', '20. L --> gal(UK)', '21. parsec --> km', '22. Km --> parsec',
                 '23. L --> gal(US)', '24. gal(US) --> L', '25. atm --> Pa', '26. Pa --> atm', '27. mmHg --> Pa',
                 '28. Pa --> mmHg', '29. hp --> kW', '30. kW --> hp', '31. lbf/in^2 --> kPa', '32. kPa --> lbf/in^2',
                 '33. nautical mile --> m', '34. m --> nautical mile', '35. acre --> m^2', '36. m^2 --> acre']

    print("Look at the following")
    for con in converter:
        print(con)
    conv_type = int(input("Enter number corresponding to conversion: "))

    if conv_type == 1:
        inches = float(input("value in inches: "))
        # inch_to_cm(inches)
        print(inch_to_cm(inches), "cm")
    elif conv_type == 2:
        cm = float(input("value in cm: "))
        # cm_to_inch(cm)
        print(cm_to_inch(cm), "inch")
    elif conv_type == 3:
        ft = float(input("value in feet: "))
        print(ft_to_m(ft), "m")
    elif conv_type == 4:
        _m = float(input('Value in meters: '))
        print(m_to_ft(_m), 'feet')
    elif conv_type == 5:
        yd = float(input('Value in Yards: '))
        print(yd_to_m(yd), 'm')
    elif conv_type == 6:
        _m = float(input('Value in meters: '))
        if (m_to_yd(_m)) == 1:
            print(m_to_yd(_m), 'Yard')
        else:
            print(m_to_yd(_m), 'yards')

    elif conv_type == 7:
        mile = float(input('Value in miles: '))
        print(mile_to_km(mile), 'km')

    elif conv_type == 8:
        km = float(input('Value in km: '))
        if km_to_mile(km) == 1:
            print(km_to_mile(km), 'mile')
        else:
            print(km_to_mile(km), 'miles')
    elif conv_type == 9:
        F = float(input('Value in F: '))
        print(F_to_C(F), 'C')
    elif conv_type == 10:
        C = float(input('Value in C: '))
        print(C_to_F(C), 'F')
    elif conv_type == 11:
        J = float(input('Value in J: '))
        print(J_to_cal(J), 'cal')

    elif conv_type == 12:
        cal = float(input('Value in cal: '))
        print(cal_to_J(cal), 'J')

    elif conv_type == 13:
        kg = float(input('Value in kg: '))
        print(kg_to_lb(kg), 'lb')

    elif conv_type == 14:
        lb = float(input('Value in lb: '))
        print(lb_to_kg(lb), 'kg')
    elif conv_type == 15:
        kmph = float(input('Value in kmph: '))
        print(kmph_to_mps(kmph), 'm/s')

    elif conv_type == 16:
        mps = float(input('Value in m/s: '))
        print(mps_to_kmph(mps), 'Km/h')

    elif conv_type == 17:
        oz = float(input('Value in cal: '))
        print(oz_to_g(oz))

    elif conv_type == 18:
        g = float(input('Value in cal: '))
        print(g_to_oz(g), 'g')

    elif conv_type == 19:
        galUK = float(input('Value in gal (UK): '))
        print(gal_UK_to_L(galUK), 'L')

    elif conv_type == 20:
        L = float(input('Value in L: '))
        print(L_to_gal_UK(L), 'gal')

    elif conv_type == 21:
        parsec = float(input('Value in parsec: '))
        print(parsec_to_km(parsec), 'km')

    elif conv_type == 22:
        km = float(input('Value in km: '))
        print(km_to_parsec(km), 'parsec')

    elif conv_type == 23:
        L = float(input('Value in L: '))
        print(L_to_gal_US(L), 'gal')

    elif conv_type == 24:
        galUS = float(input('Value in gal (US): '))
        print(gal_US_to_L(galUS), 'L')

    elif conv_type == 25:
        atm = float(input('Value in atm: '))
        print(atm_to_pa(atm), 'Pa')

    elif conv_type == 26:
        pa = float(input('Value in Pa: '))
        print(pa_to_atm(pa), 'atm')

    elif conv_type == 27:
        mmhg = float(input('Value in mmHg: '))
        print(mmHG_to_pa(mmhg), 'Pa')

    elif conv_type == 28:
        pa = float(input('Value in Pa: '))
        print(pa_to_mmHG(pa), 'mmHg')

    elif conv_type == 29:
        hp = float(input('Value in hp: '))
        print(hp_to_kW(hp), 'kW')

    elif conv_type == 30:
        kw = float(input('Value in kW: '))
        print(kW_to_hp(kw), 'hp')

    elif conv_type == 31:
        lbfin2 = float(input('Value in lbf/in^2: '))
        print(lbfin2_to_kPa(lbfin2), 'kPa')

    elif conv_type == 32:
        kpa = float(input('Value in kPa: '))
        print(kPa_to_lbfin2(kpa), 'lbf/in2')

    elif conv_type == 33:
        nm = float(input('Value in nautical mile: '))
        print(nautical_mile_to_m(nm), 'mile')

    elif conv_type == 34:
        m = float(input('Value in mile: '))
        print(m_to_nautical_mile(m), 'nautical mile')

    elif conv_type == 35:
        acre = float(input('Value in acres: '))
        print(acre_to_m2(acre), 'm^2')

    elif conv_type == 36:
        m2 = float(input('Value in m^2: '))
        if print(m2_to_acre(m2)) == 1:
            print(m2_to_acre(m2), 'acre')
        else:
            print(m2_to_acre(m2), 'acres')
    #
    #
    #
    else:
        print("You did not choose a valid conversion! \n Please start the process again")

