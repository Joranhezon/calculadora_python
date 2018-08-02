from calculator import Calculator

def main():
    variable_x = int(input("Digite o valor do primeiro número:"))
    variable_y = int(input("Digite o valor do segundo número:"))
    desired_operation = input("Digite a operação que deseja realizar. Suas opções são: +, -, * e /:")

    calculator = Calculator(variable_x, variable_y, desired_operation)
    calculator.choose_operation()

## Line used to run the main function when the file is read
if __name__ == "__main__":
    main()
