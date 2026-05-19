import math


def cbrt(x):
    # kompleksiluvun luomisen ohittamiseksi
    return math.copysign(abs(x) ** (1/3), x)


# class analyysille. Tämä voisi hyvin olla vain funktio,
# mutta alunperin mietin Lexerin kirjoittamista, jonka vuoksi tästä tuli class.
class Analysis:
    def __init__(self, equation: str):
        self.equation = equation

    def evaluate(self, x: float) -> float:
        return eval(
            self.equation,
            {"x": x, "e": math.e, "sin": math.sin, "cos": math.cos,
                "cbrt": cbrt, "sqrt": math.sqrt}
        )


text: str = input('Syötä yhtälö: ')
x_0: float = float(input('Syötä x0: '))
parser = Analysis(text)


def fixed_point(g: Analysis, x0: float,
                tol=1e-8, max_iter=100) -> (float, int):
    # toleranssi ja maksimi iteraatiot näyttääpi toimivan parhaiten näillä
    # luvuilla kaikissa tehtävissä.

    x: float = x0

    for i in range(max_iter):
        x_next: float = g.evaluate(x)

        print(f"Iteraatio {i + 1}: x = {x_next}")

        if abs(x_next - x) < tol:
            return x_next, i + 1

        x = x_next

    # ei ollut mahdollista saada tulosta
    raise ValueError("Luku ei konvergoitunut")


root, iterations = fixed_point(parser, x_0)
print(f"Ratkaisu: {root}")
print(f"Iteraatioita: {iterations}")
