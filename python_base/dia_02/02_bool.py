# %%
nome = "Teo"
print(type(nome))

# %%
print(True)
print(False)

print(type(True))
print(type(1))
print(type(1.))

# %%
print(int(False))
print(int(True))

print(bool(10))
print(bool(-1))

# %%

print(10 > 5)       # verdade
print(10 < 5)       # falso
print(10 == 10)     # verdadeiro
print(10 != 10)     # false
print(not 10 != 10) # verdadeiro

print("teo" in "teo calvo")
print("ana" in "teo calvo")
print("ana" not in "teo calvo")

# %%

print(10 > 5 and 5 > 4)
print(True and True)

print(10 > 5 or 5 <= 4)
print(True or False)

# %%

print("True and True:", True and True)
print("True and False:", True and False)
print("False and False:", False and False)
print("False and True:", False and True)

print("True and True:", 1 * 1)
print("True and False:", 1 * 0)
print("False and False:", 0 * 0)
print("False and True:", 0 * 1)

# %%

print("True or True:", True or True)
print("True or False:", True or False)
print("False or False:", False or False)
print("False or True:", False or True)

print("True or True:", 1 + 1)
print("True or False:", 1 + 0)
print("False or False:", 0 + 0)
print("False or True:", 0 + 1)