def multiplier_par_2(nombre):
    """fonction qui multiplie par 2"""
    if isinstance(nombre,int):
        return 2 * nombre
    else:
        return None
print(multiplier_par_2(5))
