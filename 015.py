dias = int(input("Quantos dias foi alugado? "))
km = float(input("Quantos kilometros foram percorridos? "))
dia = dias * 60
km_rodado = km * 0.15       
print(f"O valor da diaria foi de: {dia:5.2f}, e o valor por km rodado foi de: {km_rodado:5.2f}. O total a ser pago é de: {dia + km_rodado:5.2f}")