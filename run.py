class Interpreter:
    def __init__(self):
        self.vars = {}

    def find_var(self, var_name):
        if var_name in self.vars:
            return self.vars[var_name]
        else:
            return "NULL"

    def interpret(self, expr):
        parts = expr.split(" ")
        if parts[0] == "set":
            if not all(c.isalpha() or c.isspace() for c in parts[1]):
                print("Variable name must be a string")
            else:
                self.vars[parts[1]] = parts[2]
        elif parts[0] == "print":
            if parts[1] in self.vars:
                print(self.vars[parts[1]])
            else:
                print(parts[1])
        elif parts[0] == "add":
            if parts[1] in self.vars and parts[2] in self.vars:
                self.vars[parts[1]] += self.vars[parts[2]]
            elif parts[1] in self.vars and parts[2] not in self.vars:
                self.vars[parts[1]] += int(parts[2])
            elif parts[1] not in self.vars and parts[2] in self.vars:
                self.vars[parts[1]] = int(parts[2]) + self.vars[parts[2]]
            elif parts[1] not in self.vars and parts[2] not in self.vars:
                self.vars[parts[1]] = int(parts[2]) + int(parts[3])
            else:
                print("Variable not found")

    def start(self):
        while True:
            expr = input(">>>")
            if expr == "exit()":
                break
            self.interpret(expr)

interpreter = Interpreter()
interpreter.start()
