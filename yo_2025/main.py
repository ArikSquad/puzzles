def euclidean(a: int, b: int) -> int:
    while b != 0:
        temp: int = a % b
        print(f"a:n ja b:n jakojäännös on {temp}")
        a = b
        b = temp
    print("b on 0")
    return a

yksi: int = 121_110_987_654_321
kaksi: int = 123_456_789_101_112
val: int = euclidean(yksi, kaksi)
print(f"Lukujen {yksi} ja {kaksi} suurin yhteinen tekijä on {val}")
