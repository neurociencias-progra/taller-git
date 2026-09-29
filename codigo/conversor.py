"""Un conversor de temperaturas para el taller.

⚠ Este archivo esconde un bug a propósito: se arregla en la práctica de ramas
(clase de Agile y Linear), en una rama y por pull request — nunca directo en main.
"""


def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    return celsius * 5 / 9 + 32


def fahrenheit_a_celsius(fahrenheit):
    """Convierte grados Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    print("El agua hierve a", celsius_a_fahrenheit(100), "°F  (debería decir 212.0)")
    print("Un día templado de 22 °C son", celsius_a_fahrenheit(22), "°F  (debería decir 71.6)")
    print("98.6 °F son", fahrenheit_a_celsius(98.6), "°C  (esta función sí funciona)")
