nom = input("Quel est ton nom ? ")
age = int(input("Quel est ton age ? "))

if age >= 18:
    print(f"Bonjour {nom}, tu es majeur.")
else:
    print(f"Bonjour {nom}, tu es mineur.")
