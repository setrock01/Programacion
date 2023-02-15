from typeguard import typechecked


class Fraction:

    @typechecked
    def __init__(self, numer: int, deno: int):
        self.__numerador = numer
        self.__denominador = deno
        self.__resultado = 0

    @property
    def numerador(self):
        self.comprobar()
        return self.__numerador

    @property
    def denominador(self):
        return self.__denominador

    def comprobar(self):
        paso = 0
        if self.__denominador <= 0:
            raise RuntimeError("ERROR: No se puede dividir entre 0")
        else:
            while True:
                for i in range(2, self.__numerador):
                    if self.__numerador % i == 0 and self.__denominador % i == 0:
                        self.__numerador = self.__numerador // i
                        self.__denominador = self.__denominador // i
                        paso += 1
                if paso == 0:
                    break
                paso = 0

    def resultado(self):
        self.comprobar()
        self.__resultado = self.__numerador / self.__denominador
        print(self.__resultado)

    def multiplicar_numero(self, value):
        self.comprobar()
        self.__numerador *= value
        print(f"Resultado multiplicacion por numero-> numerador:{self.__numerador}, denominador:{self.__denominador}")
        self.comprobar()
        return print(f"Resultado simplificado -> numerador:{self.__numerador}, denominador:{self.__denominador}")

    def multiplicar_frac(self, num, deno):
        self.comprobar()
        self.__numerador *= num
        self.__denominador *= deno
        print(f"Resultado multiplicacion-> numerador:{self.__numerador}, denominador:{self.__denominador}")
        self.comprobar()
        return print(f"Resultado simplificado -> numerador:{self.__numerador}, denominador:{self.__denominador}")

    def dividir_frac(self, num, deno):
        self.comprobar()
        self.__numerador *= deno
        self.__denominador *= num
        print(f"Resultado division-> numerador:{self.__numerador}, denominador:{self.__denominador}")
        self.comprobar()
        return print(f"Resultado simplificado -> numerador:{self.__numerador}, denominador:{self.__denominador}")

    def sumar_frac(self, num, deno):
        self.comprobar()
        if self.__denominador == deno:
            self.__numerador += num
        else:
            self.__numerador *= deno
            num *= self.__denominador
            self.__denominador *= deno
            self.__numerador += num
        print(f"Resultado suma-> numerador:{self.__numerador}, denominador:{self.__denominador}")
        self.comprobar()
        return print(f"Resultado simplificado -> numerador:{self.__numerador}, denominador:{self.__denominador}")

    def restar_frac(self, num, deno):
        self.comprobar()
        if self.__denominador == deno:
            self.__numerador -= num
        else:
            self.__numerador *= deno
            num *= self.__denominador
            self.__denominador *= deno
            self.__numerador -= num
        print(f"Resultado resta-> numerador:{self.__numerador}, denominador:{self.__denominador}")
        self.comprobar()
        return print(f"Resultado simplificado -> numerador:{self.__numerador}, denominador:{self.__denominador}")

