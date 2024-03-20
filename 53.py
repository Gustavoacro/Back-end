txt = str(input('Insira uma palavra: ')).strip().lower()
alter = txt.split()
inverter = "".join(alter)
vr = inverter[::-1]
if vr == inverter:
    print('palindromo')