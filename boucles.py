print("--- Boucle for : compter de 1 a 5 ---")
for i in range(1, 6):
    print(f"Tour numero {i}")

print("--- Table de multiplication ---")
nombre = int(input("Quelle table veux-tu voir ? "))
for i in range(1, 11):
    print(f"{nombre} x {i} = {nombre * i}")
