def basic_print():
    print("Hello World!")

def basic_print_float(fnum):
    print(f"Float Format => {fnum:.2f}")
    print(f"Float Format => |{fnum:>12,.2f}|")


if __name__ == '__main__':
    basic_print()
    basic_print_float(283563.456778)
    basic_print_float(0.125)
