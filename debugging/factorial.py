#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n  # Multiplie 'result' par 'n' à chaque itération
        n -= 1  # Décrémente 'n' pour réduire la valeur jusqu'à 1
    return result

# Récupère l'argument de la ligne de commande, convertit en entier, et calcule sa factorielle
f = factorial(int(sys.argv[1]))
print(f)  # Affiche le résultat de la factorielle

