documento = int(input('''Digite seu documento: 
  1 - para RG
  2 - para titulo de eleitor                      
 '''))

if documento == 1:
    rg = int(input("Digite seu RG: "))
    if rg == 1223333:
        print("Nome do eleitor: João do Carmo")
        print("Pode Votar!")
    else:
        print("Eleitor não encontrado")
    
if documento == 2:
    titulo = int(input("Digite seu titulo: "))
    if titulo == 12345678:
        print("Nome do eleitor: João do Carmo")
        print("Pode Votar!")
    else:
        print("Eleitor não encontrado")
