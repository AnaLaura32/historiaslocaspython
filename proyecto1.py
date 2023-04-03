# Supongamos que queremos crear una cadena que diga:
# Aprende a programar con ____________________.

# organizacion = "freeCodeCamp"

# print("Aprende a programar con " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}")

# Mad Libs (Historias locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("verbo: ")
sustantivo_plural = input("sustantivo (plural): ")
 
madlib = f"¡Programar es tan {adj}! Siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madlib)
