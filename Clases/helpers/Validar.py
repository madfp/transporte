from re import search

REG_NUMBER = '^[1-9]{1}[0-9]*$'
REG_FLOAT = '^([0-9])+(\\.{1}[0-9]+)*$'

def lectura(reg_ex:str) -> str:
    var = ''
    while(not search(reg_ex, var)): var = input('-> ')
    return var