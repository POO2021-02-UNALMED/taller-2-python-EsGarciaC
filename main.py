class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "negro" or color == "blanco":
            self.color = color


class Motor:
    def __init__(self, numeroCilidros, tipo, registro):
        self.numeroCilindros = numeroCilidros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo = tipo


class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        x = 0
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                x += 1
        return x

    def verificarIntegridad(self):
        result = "Auto original"
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                if self.registro != asiento.registro or self.registro != self.motor.registro:
                    result = "Las piezas no son originales"
                    break
        return result
