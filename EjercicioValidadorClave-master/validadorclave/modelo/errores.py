class ValidadorError(Exception):
    pass

class NoCumpleLongitudMinimaError(ValidadorError):
    def __init__(self, mensaje="La clave no cumple con la longitud mínima requerida"):
        super().__init__(mensaje)

class NoTieneLetraMayusculaError(ValidadorError):
    def __init__(self, mensaje="La clave no contiene al menos una letra mayúscula"):
        super().__init__(mensaje)

class NoTieneLetraMinusculaError(ValidadorError):
    def __init__(self, mensaje="La clave no contiene al menos una letra minúscula"):
        super().__init__(mensaje)

class NoTieneNumeroError(ValidadorError):
    def __init__(self, mensaje="La clave no contiene al menos un número"):
        super().__init__(mensaje)

class NoTieneCaracterEspecialError(ValidadorError):
    def __init__(self, mensaje="La clave no contiene al menos un carácter especial (@, _, #, $ o %)"):
        super().__init__(mensaje)

class NoTienePalabraSecretaError(ValidadorError):
    def __init__(self, mensaje="La clave no contiene la palabra secreta requerida"):
        super().__init__(mensaje)
