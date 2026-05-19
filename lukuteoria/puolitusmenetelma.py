import math

# pythonissa kuutiojuuresta tulee kompleksiluku.
# tämä funktio kopio saman etumerkin aina.


def cbrt(x):
    return math.copysign(abs(x) ** (1/3), x)


class Analysis:
    def __init__(self, equation: str):
        self.equation = equation

    def evaluate(self, x: float) -> float:
        return eval(
            self.equation,
            {"x": x, "sin": math.sin, "cos": math.cos,
                "cbrt": cbrt, "sqrt": math.sqrt}
        )


text = input('Syötä yhtälö: ')
parser = Analysis(text)

bot, top = map(float, input('Syötä yläraja ja alaraja: ').split())
b, t, = bot, top
print(f"Rajat ovat {bot}, {top}")

if parser.evaluate(bot) * parser.evaluate(top) >= 0:
    print("Virhe: välillä ei ole nollakohtaa tai niitä on parillinen määrä.")
    exit()

mid = (bot + top) / 2
length = abs(bot - top)

while length >= 1e-5:
    botVal = parser.evaluate(bot)
    midVal = parser.evaluate(mid)

    if botVal * midVal < 0:
        top = mid
    else:
        bot = mid

    mid = (top + bot) / 2
    length = abs(bot - top)

print(f'Yhtälön ratkaisu on noin {mid:.6f} välillä [{b:.0f}, {t:.0f}]')
