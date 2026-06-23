from frontend import node
from frontend import AST

variables = {}

numNodes = (
    node.BinaryOperation,
    node.Number
)

# recursive function for binary operations inside binary operations
def calculateBinaryOperation(node_):
    if isinstance(node_, float):
        return node_
    if isinstance(node_, node.Number):
        return node_.value
    if isinstance(node_, node.EOF):
        raise ValueError("Unexpected EOF in expression")
    if isinstance(node_, node.Variable):
        name = node_.get_name()
        if name not in variables:
            raise NameError(f"Variable '{name}' is not defined")
        return variables[name]

    if isinstance(node_, node.BinaryOperation):
        left = calculateBinaryOperation(node_.left)
        right = calculateBinaryOperation(node_.right)

        if node_.operation == '+':
            return left + right
        if node_.operation == '-':
            return left - right
        if node_.operation == '*':
            return left * right
        if node_.operation == '/':
            if right == 0 or left == 0:
                raise ZeroDivisionError("Division by zero")
            return left / right

    raise TypeError(f"Cannot evaluate node type: {type(node_).__name__}")

def interpret(ast: AST.AST):
    """
    Interprets an AST node
    :param ast:
    :return:
    """
    code = ast.get_code()
    for i, token in enumerate(code):
        if isinstance(token, node.Assign):
            target = code[i - 1]
            expr = token.value
            value = calculateBinaryOperation(expr)
            variables[target.get_name()] = value
        if isinstance(token, node.Function) and token.name == "log":
            for arg in token.args:
                if isinstance(arg, node.Variable):
                    name = arg.get_name()
                    if name not in variables:
                        raise NameError(f"Variable \"{name}\" is not defined")
                    print(variables[name])

                elif isinstance(arg, node.BinaryOperation):
                    print(calculateBinaryOperation(arg))

                elif isinstance(arg, node.Number):
                    print(arg.value)

                elif isinstance(arg, node.String):
                    print(arg.value)

                else:
                    raise TypeError(f"Unsupported argument type in log(): {type(arg).__name__}")
