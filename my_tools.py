PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT = "71828182845904523536028747135266249775724709369995957496696762772407663035354759451382178525166427"

def pi_real(round: int):
    if round < 0 or round > 100:
        raise ValueError("Casas decimais precisa ser entre 0 e 100!")

    return f"3,{PI_INT[0:round]}"

def e_real(round: int):
    if round < 0 or round > 100:
        raise ValueError("Casas decimais precisa ser entre 0 e 100!")

    return f"2,{E_INT[0:round]}"
