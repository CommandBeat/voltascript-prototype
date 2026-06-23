class Node:
    def __str__(self):
        return "Node()"
    def __repr__(self):
        return "Node()"

class Number(Node):
    def __init__(self, value: float | int):
        self.value = value
    def __str__(self):
        return f"Number({self.value})"
    def __repr__(self):
        return f"Number({self.value})"

class BinaryOperationPlaceholder(Node):
    def __init__(self, operation: str):
        if operation in ["+", "-", "*", "/"]:
            self.operation = operation
    def __str__(self):
        return f"BinaryOperationPlaceholder({self.operation})"
    def __repr__(self):
        return f"BinaryOperationPlaceholder({self.operation})"

class BinaryOperation(Node):
    def __init__(self, left: Node, operation: str, right: Node):
        self.left = left
        if operation in ["+", "-", "*", "/"]:
            self.operation = operation
        self.right = right
    def __str__(self):
        return f"BinaryOperation(Operation: {self.operation}, Left Node: {self.left}, Right Node: {self.right})"
    def __repr__(self):
        return f"BinaryOperation(Operation: {self.operation}, Left Node: {self.left}, Right Node: {self.right})"

class EOF(Node):
    def __str__(self):
        return "EOF()"
    def __repr__(self):
        return "EOF()"

class EOL(EOF):
    def __str__(self):
        return "EOL()"
    def __repr__(self):
        return "EOL()"

class Variable(Node):
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return f"Variable({self.name})"
    def __repr__(self):
        return f"Variable({self.name})"
    def get_name(self):
        return self.name

class Assign(Node):
    def __init__(self, value: Node):
        self.value = value
    def __str__(self):
        return f"Assign({self.value})"
    def __repr__(self):
        return f"Assign({self.value})"

class AssignPlaceholder(Node):
    def __str__(self):
        return "AssignPlaceholder()"
    def __repr__(self):
        return "AssignPlaceholder()"

class Identifier(Node):
    def __init__(self, name: str):
        self.name = name
    def __str__(self):
        return f"Identifier({self.name})"
    def __repr__(self):
        return f"Identifier({self.name})"

class Function(Node):
    def __init__(self, name: str, args=None):
        self.name = name
        self.args = args
    def __str__(self):
        return f"Function(Name: {self.name}, Args: {self.args})"
    def __repr__(self):
        return f"Function(Name: {self.name}, Args: {self.args})"

class String(Node):
    def __init__(self, value: str):
        self.value = value
    def __str__(self):
        return f"String(\"{self.value}\")"
    def __repr__(self):
        return f"String(\"{self.value}\")"

class Start(Node):
    def __init__(self, value: str):
        self.value = value
    def __str__(self):
        return f"Start('{self.value}')"
    def __repr__(self):
        return f"Start('{self.value}')"

class End(Node):
    def __init__(self, value: str):
        self.value = value
    def __str__(self):
        return f"End('{self.value}')"
    def __repr__(self):
        return f"End('{self.value}')"

class Import(Node):
    def __init__(self, file_path: str):
        self.file_path = file_path
    def __str__(self):
        return f"Import('{self.file_path}')"
    def __repr__(self):
        return f"Import('{self.file_path}')"

class Symbol(Node):
    def __init__(self, symbol: str):
        self.symbol = symbol
    def __str__(self):
        return f"Symbol('{self.symbol}')"
    def __repr__(self):
        return f"Symbol('{self.symbol}')"

class ConvertInt(Node):
    def __str__(self):
        return "ConvertInt()"
    def __repr__(self):
        return "ConvertInt()"

class Condition(Node):
    def __init__(self, condition: list[Comparison]):
        self.condition = condition
    def __str__(self):
        return f"Condition({self.condition})"
    def __repr__(self):
        return f"Condition({self.condition})"

class For(Node):
    def __init__(self, condition: Condition, code: list[Node], start_var: Variable):
        self.condition = condition
        self.variable = start_var
        self.code = code
    def __str__(self):
        return f"For(Condition: {self.condition}, Variable: {self.variable}, Code: {self.code})"
    def __repr__(self):
        return f"For(Condition: {self.condition}, Variable: {self.variable}, Code: {self.code})"

class Comparison(Node):
    def __init__(self, left: Node, right: Node, symbol: str):
        self.left = left
        self.right = right
        self.comparator = symbol
    def __str__(self):
        return f"Comparison(Left Node: {self.left}, Right Node: {self.right}, Comparator: '{self.comparator}')"
    def __repr__(self):
        return f"Comparison(Left Node: {self.left}, Right Node: {self.right}, Comparator: '{self.comparator}')"

class ComparisonPlaceholder(Node):
    def __init__(self, symbol: str):
        self.comparator = symbol
    def __str__(self):
        return f"ComparisonPlaceholder({self.comparator})"
    def __repr__(self):
        return f"ComparisonPlaceholder({self.comparator})"

def convertComparisonToString(comparison: Comparison) -> str:
    condition = ""

    # check left value
    if isinstance(comparison.left, Number):
        condition += str(comparison.left.value)
    elif isinstance(comparison.left, Variable):
        return condition

    # check comparator
    condition += str(comparison.comparator)

    # check right value
    if isinstance(comparison.right, Number):
        condition += str(comparison.right.value)
    if isinstance(comparison.right, Variable):
        return condition
    return condition

class Increment(Node):
    def __str__(self):
        return "Increment()"
    def __repr__(self):
        return "Increment()"

class Decrement(Node):
    def __str__(self):
        return "Decrement()"
    def __repr__(self):
        return "Decrement()"