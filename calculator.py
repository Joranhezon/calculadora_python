class Calculator:

    def __init__(self, variable_x, variable_y, desired_operation):
        self.variable_x = variable_x
        self.variable_y = variable_y
        self.desired_operation = desired_operation

    def sum(self):
        result = self.variable_x + self.variable_y
        print("Seu resultado eh:" + str(result))

    def subtraction(self):
        result = self.variable_x - self.variable_y
        print("Seu resultado eh:" + str(result))

    def multiply(self):
        result = self.variable_x * self.variable_y
        print("Seu resultado eh:" + str(result))

    def divide(self):
        result = self.variable_x / self.variable_y
        print("Seu resultado eh:" + str(result))

    ## Reads user's input and chooses the desired operation, if it exists
    def choose_operation(self):
        if(self.desired_operation == '+'):
            self.sum()
        elif(self.desired_operation == '-'):
            self.subtraction()
        elif(self.desired_operation == '*'):
            self.multiply()
        elif(self.desired_operation == '/'):
            self.divide()
        else:
            print('The desired operation is not supported. Please try again and choose between sum, subtraction, divide and multiply.')
