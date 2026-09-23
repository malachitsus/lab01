import argparse
import sys

from toolkit.calculator import calculate
from toolkit.converter import convert


def main():
    parser = argparse.ArgumentParser(prog='toolkit', description='Калькулятор и конвертер')
    subparsers = parser.add_subparsers(dest='command')
    
    calc_parser = subparsers.add_parser('calc', help='Вычислить выражение')
    calc_parser.add_argument('expression', type=str, help='Выражение')
    
    conv_parser = subparsers.add_parser('convert', help='Конвертировать единицы')
    conv_parser.add_argument('value', type=float, help='Значение')
    conv_parser.add_argument('--from', dest='from_unit', required=True)
    conv_parser.add_argument('--to', dest='to_unit', required=True)
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help(sys.stderr)
        sys.exit(2)
    
    try:
        if args.command == 'calc':
            print(calculate(args.expression))
        elif args.command == 'convert':
            print(convert(args.value, args.from_unit, args.to_unit))
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(2)


if __name__ == '__main__':
    main()