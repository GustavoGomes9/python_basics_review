def calc_gas(cash_value, gas_value):
    result = cash_value / gas_value
    return f'Voce terá {result:.2f}L de gasolina' #Formatted string literals

arg1 = float(input('tell me how much are you buying: '))
arg2 = float(input('And how much the gas cost: '))
print('---------------------------------')
print(calc_gas(arg1, arg2))
