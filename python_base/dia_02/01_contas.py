# %%
print("Ola, mundo!")

print("Ola você!")

# %%
print("Meu nome eh teo")

# %%

# soma
print("1 + 1 =", 1+1)

# subtracao
print("10 - 5 =", 10-5)

# multiplicacao
print("2 * 5 =", 2*5)

# exponeniacao
print("2 ** 63 =", 2 ** 63)

# divisao
print("10 / 2 =", 10/2)

# divisao inteira
print("101 / 2 =", 101 / 2)
print("101 // 2 =", 101 // 2)

# resto da divisao
print("101 % 2 =", 101 % 2)

print("4 ** (1/2) = ", 4 ** (1/2) )

# %%

meu_int = int(-4.32)
print("Meu int:", meu_int)

meu_float = float(4)
print("Meu float:", meu_float)

# %%

original = -100
divisor = 3

valor_int = original // divisor
resto = original % divisor

novo_original = (valor_int * divisor) + resto

if novo_original == original:
    print("Sucesso!")
else:
    print("Fracasso!")