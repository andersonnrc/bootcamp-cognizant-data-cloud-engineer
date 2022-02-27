import sys

segundos = int(input())
horas = int(segundos) / 3600
resto = int(segundos) % 3600
minutos = int(resto) / 60
segundos = int(resto) % 60

print("{}:{}:{}".format(int(horas), int(minutos), int(segundos)))