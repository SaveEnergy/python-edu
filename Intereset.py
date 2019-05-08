import math
credit = int(input("Bitte geben Sie an wie viel Geld Sie anlegen möchten: "))
interest = float(input("Bitte sagen Sie uns nun mit welchem Zinssatz in Prozent (z.B. 1.6): "))


def calculate_interest(money: int, percent: float):
    return math.log(money * 2 / money) / math.log(1 + percent / 100)


print("\nIhr Anfangskapital wird sich nach {} Jahren verdoppelt habe.".format(calculate_interest(credit, interest)))

