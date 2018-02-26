signals = {}
operator_values = ['AND', 'OR', 'LSHIFT', 'RSHIFT', 'NOT']

def get_value(signals, key):
    try:
        return int(key)
    except ValueError:
        return signals.get(key, 0)

index = 0
with open('input.txt', 'r') as f:
    for operation in f:
        index += 1
        operators = []
        operands = []
        rvalue, lvalue = operation.strip().split(' -> ')
        for token in rvalue.split(' '):
            if token in operator_values:
                operators.append(token.strip())
            else:
                operands.append(token.strip())

        while len(operators):
            operator = operators.pop(0)
            if operator == 'AND':
                value = get_value(signals, operands.pop(0)) & \
                        get_value(signals, operands.pop(0))
            elif operator == 'OR':
                value = get_value(signals, operands.pop(0)) | \
                        get_value(signals, operands.pop(0))
            elif operator == 'LSHIFT':
                value = get_value(signals, operands.pop(0)) << \
                        int(operands.pop(0)) & 0xffff
            elif operator == 'RSHIFT':
                value = get_value(signals, operands.pop(0)) >> \
                        int(operands.pop(0)) & 0xffff
            elif operator == 'NOT':
                value = ~get_value(signals, operands.pop(0))
            operands.insert(0, value)

        
        result = get_value(signals, operands.pop(0))
        if result < 0:
            result += 2 ** 16
        signals[lvalue] = result
        if index < 10:
            print operation
            print signals
            
print '!!!'
print signals['a']
