#fuçoes 
def suvalor (valogr,qtdtotal):
    return(subvalor - qtdtotal)

def advalor (nvalorg,qtdtotal):
    return  (addvalor - qtdtotal)

def valorf (qtdtotal,svalor,valorg):
    return(qtdtotal + svalor - valorg)

qtdtotal = float(input("Qual a quantia que voce tem"));

cats = ["Valor.t","valor.g","valor.a","valor.f"]
vals = [qtdtotal]

a = input("houve algum gasto? s/n")

#subtrair ou adicionar valor
while a == "s":
    valorg = float(input("qual o valor do gasto?")) 
    subvalor = valorg + qtdtotal 
    nvalor = suvalor (valorg,qtdtotal)
    vals.append(nvalor)
    a = input("houve mais gasto? s/n")

    if a == 'n':
        nvalor = 0
        vals.append(nvalor)



somarv = input("deseja somar algum valor?")


while somarv == 's':
    if somarv == 's':
        svalor = float(input("qual o valor deseja somar?"))
        addvalor = svalor + qtdtotal   
        nvalor = advalor (addvalor,qtdtotal)
        vals.append(nvalor)
        somarv= input("deseja mais somar algum valor ? s/n")

    if somarv == 'n':
        nvalor = 0
        vals.append(nvalor)
        b = input ("deseja adicionar mais algum valor s/n")

    if b == 'n':
        nvalor = valorf (qtdtotal,svalor,valorg)
        vals.append(nvalor)
        

print (cats)
print (vals)
#fim 