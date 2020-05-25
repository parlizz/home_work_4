from sys import argv
import argparse

parser = argparse.ArgumentParser(description='Calculate')
parser.add_argument('--rate', type=float)
parser.add_argument('--hours', type=float)
parser.add_argument('--prize', default=None, type=float)

args = parser.parse_args(argv[1:])


def salary(rate: float, hours: float, prize: float):
    return rate * hours + prize


print(f'Зарплата: {salary(rate=args.rate, hours=args.hours, prize=args.prize)} руб')
