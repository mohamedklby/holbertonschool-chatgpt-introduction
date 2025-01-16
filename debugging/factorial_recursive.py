#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Vérification de la validité de l'entrée
if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

try:
    n = int(sys.argv[1])  # Conversion de l'argument en entier
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        sys.exit(1)
    f = factorial(n)  # Calcul de la factorielle
    print(f)
except ValueError:
    print("Please enter a valid integer.")
    sys.exit(1)

