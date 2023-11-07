from modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, NoTieneLetraMinusculaError, NoTieneNumeroError, NoTieneCaracterEspecialError, NoTienePalabraSecretaError


class ReglaValidacion:
    def __init__(self, longitud_esperada):
        self._longitud_esperada = longitud_esperada

    def _validar_longitud(self, clave):
        if len(clave) <= self._longitud_esperada:
            raise NoCumpleLongitudMinimaError()

    def _contiene_mayuscula(self, clave):
        if not any(char.isupper() for char in clave):
            raise NoTieneLetraMayusculaError()

    def _contiene_minuscula(self, clave):
        if not any(char.islower() for char in clave):
            raise NoTieneLetraMinusculaError()

    def _contiene_numero(self, clave):
        if not any(char.isdigit() for char in clave):
            raise NoTieneNumeroError()

class ReglaValidacionGanimedes(ReglaValidacion):
    def contiene_caracter_especial(self, clave):
        if not any(char in "@_#$%" for char in clave):
            raise NoTieneCaracterEspecialError()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_mayuscula(clave)
        self._contiene_minuscula(clave)
        self._contiene_numero(clave)
        self.contiene_caracter_especial(clave)
        return True

class ReglaValidacionCalisto(ReglaValidacion):
    def contiene_calisto(self, clave):
        if "calisto" not in clave.lower():
            raise NoTienePalabraSecretaError()

    def es_valida(self, clave):
        self._validar_longitud(clave)
        self._contiene_numero(clave)
        self.contiene_calisto(clave)
        return True

class Validador:
    def __init__(self, regla):
        self._regla = regla

    def es_valida(self, clave):
        return self._regla.es_valida(clave)
