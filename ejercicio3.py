velocidad_asteroide =  25
tamano_asteroide = 40


if velocidad_asteroide > 0 and tamano_asteroide > 25:
    print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_asteroide >= 20 and tamano_asteroide > 0 and tamano_asteroide < 25 :
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif velocidad_asteroide > 0 and tamano_asteroide >= 1000:
    print("Un asteroide gigantesco azotara la tierra")
else:
    print('Nada que ver aquí :)')