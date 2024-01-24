def soma (a:float, b:float):
    return a+b
def subtracao (a:float, b:float):
    return a-b
def multiplicacao (a:float, b:float):
    return a*b
def divisao (a:float,b:float):
    if b!= 0:   
        return a/b

var1 = float(input("entre com um numero:"))
var2 = float(input("entre com o segundo numero:"))

print(f"a soma é {soma(var1,var2)}")
print(f"a subtracao é {subtracao(var1,var2)}")
print(f"a multiplicacao é {multiplicacao(var1,var2)}")
print(f"a divisao é {divisao(var1,var2)}")

