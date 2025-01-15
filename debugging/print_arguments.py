#!/usr/bin/python3
import sys

# Afficher tous les arguments à partir de sys.argv[1], en ignorant le nom du script
for i in range(1, len(sys.argv)):  # Commence à 1 pour ignorer le nom du script
    print(sys.argv[i])

