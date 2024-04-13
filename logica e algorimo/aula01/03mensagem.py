#CONDICIONAL SIMPLES
idade = 16

if idade >= 18:
    print("pode obter a CNH")
else:
     print("nao pode obter a cnh")

#condicional aninhada/composta
media = 8.5

if media == 10:
     print ("nota maxima parabens")  

elif media >= 9:
     print ("otimo")

elif media >= 8:
     print("bom") 

elif media >= 7:
     print("na media")   

elif media >= 5:
     print("EM EXAME")

else:
     print("reprovado")


#operadores logicos
valor = 84

if valor >= 0 and valor <= 100: 
   print("o valor esta entre 0 e 100")
else:
     print ("o valor nao esta entre 0 e 100") 

total = 400
formapagamento = "a prazo "


if total >= 100 and formapagamento == "a vista":
     print ("valor a pagar R$" +str(total*0.9))
else:
     print("o valor a pagar R$"+str(total))


      
     