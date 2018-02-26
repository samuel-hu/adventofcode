from collections import defaultdict
import operator

OPERATORS = {
    '<': operator.lt,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    '>=': operator.ge,
    '>': operator.gt,
    'inc': operator.add,
    'dec': operator.sub
}

REGISTERS = defaultdict(int)

class Expression(object):
    def __init__(self, register, operator, value):
        self.register = register
        self.operator = operator 
        self.value = value

    def evaluate(self, registers):
        register_value = registers[self.register]
        return OPERATORS[self.operator](register_value, self.value)


def parse_line(line):
    tokens = line.split()
    operation_register = tokens[0]
    operation = tokens[1]
    operation_value = tokens[2]
    condition_register = tokens[4]
    condition = tokens[5]
    condition_value = tokens[6]

    return (
        Expression(operation_register, operation, int(operation_value)),
        Expression(condition_register, condition, int(condition_value)) 
    )


def compute_instructions(file_name):
    with open(file_name, 'r') as fp:
        for line in fp:
            instruction, condition = parse_line(line)
            if condition.evaluate(REGISTERS):
                REGISTERS[instruction.register] = instruction.evaluate(REGISTERS) 

compute_instructions('input.txt')
print max(REGISTERS.values())
