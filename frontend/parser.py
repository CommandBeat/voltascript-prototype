from frontend import lexer_token as lt
from frontend import node
from frontend import AST

# test exception
class TestException(Exception):
    pass

binaryOperatorsTypes = [
    lt.TokenType.PLUS,
    lt.TokenType.MINUS,
    lt.TokenType.MULTIPLY,
    lt.TokenType.DIVIDE
]


def calculateNode(token: lt.Token):
    if token.type == lt.TokenType.EOF: return node.EOF()
    elif token.type == lt.TokenType.EOL: return node.EOL()
    elif token.type == lt.TokenType.NUMBER: return node.Number(token.value)
    elif token.type == lt.TokenType.INCREMENT: return node.Increment()
    elif token.type == lt.TokenType.DECREMENT: return node.Decrement()
    elif token.type in binaryOperatorsTypes: return node.BinaryOperationPlaceholder(token.value)
    elif token.type == lt.TokenType.IDENTIFIER: return node.Identifier(token.value)
    elif token.type == lt.TokenType.VARIABLE: return node.Variable(token.value)
    elif token.type == lt.TokenType.ASSIGN: return node.AssignPlaceholder()
    elif token.type == lt.TokenType.FUNC_REF: return node.Function(token.value)
    elif token.type == lt.TokenType.STRING: return node.String(token.value)
    elif token.type == lt.TokenType.START: return node.Start(token.value)
    elif token.type == lt.TokenType.END: return node.End(token.value)
    elif token.type == lt.TokenType.IMPORT_LIB: return node.Import(token.value)
    elif token.type == lt.TokenType.SYMBOL: return node.Symbol(token.value)
    elif token.type == lt.TokenType.COMPARISON: return node.ComparisonPlaceholder(token.value)
    elif token.type == lt.TokenType.CONVERT_INT: return node.ConvertInt()
    elif token.type == lt.TokenType.CONDITION: return node.Condition(token.value)
    return node.Node()


def parse_expression(tokens: list):
    """
    Parses binary operations respecting standard mathematical precedence.

    :param tokens: list of tokens:
    :return: processed code
    """
    temp = tokens[:]
    i = 0
    while i < len(temp):
        if isinstance(temp[i], node.BinaryOperationPlaceholder) and temp[i].operation in ['*', '/']:
            left = temp[i - 1]
            right = temp[i + 1]
            new_node = node.BinaryOperation(left, temp[i].operation, right)
            temp[i - 1:i + 2] = [new_node]
            i = max(i - 1, 0)
        else:
            i += 1

    i = 0
    while i < len(temp):
        if isinstance(temp[i], node.BinaryOperationPlaceholder) and temp[i].operation in ['+', '-']:
            left = temp[i - 1]
            right = temp[i + 1]
            new_node = node.BinaryOperation(left, temp[i].operation, right)
            temp[i - 1:i + 2] = [new_node]
            i = max(i - 1, 0)
        else:
            i += 1
    return temp[0] if temp else None

def parse_for_block(parsed_code: list[node.Node]) -> list[node.Node]:
    i = 0
    while i < len(parsed_code):
        token = parsed_code[i]
        if isinstance(token, node.Identifier) and token.name == "for":
            var = None
            code = []
            condition = node.Condition([])
            start_func = i

            index = i + 1
            start_i = 1000
            while index < len(parsed_code):
                current_token = parsed_code[index]
                # get variable
                if isinstance(current_token, node.Identifier) and current_token.name == "var": var = parsed_code[index + 1]
                elif isinstance(current_token, node.Comparison): condition.condition.append(current_token)
                elif isinstance(current_token, node.Start) and current_token.value == '{': start_i = index + 1

                elif isinstance(current_token, node.End) and current_token.value == '}':
                    break
                if index > start_i: code.append(current_token)
                index += 1

            # set for loop
            new_node = node.For(condition, code, var)
            parsed_code[start_func:index] = [new_node]
        i += 1

    return parsed_code


def parse_blocks(parsed_code: list) -> list:
    i = 0
    while i < len(parsed_code):
        token = parsed_code[i]

        if isinstance(token, node.Function):
            n = i
            index = i + 1
            args: list[node.Node] = []

            while index < len(parsed_code):
                current_token = parsed_code[index]
                if (isinstance(current_token, node.End) and current_token.value == ')') or \
                        isinstance(current_token, node.EOL) or \
                        isinstance(current_token, node.EOF):
                    index += 1
                    break

                if not isinstance(current_token, node.Start):
                    args.append(current_token)

                index += 1

            token.args = args

            parsed_code[n:index] = [token]

            i = n + 1

        elif isinstance(token, node.AssignPlaceholder):
            if i + 1 >= len(parsed_code):
                return parsed_code
            right = parsed_code[i + 1]
            parsed_code[i:i + 2] = [node.Assign(right)]
            i += 1

        elif isinstance(token, node.ComparisonPlaceholder):
            if i + 1 > len(parsed_code): return parsed_code

            left = parsed_code[i - 1]
            right = parsed_code[i + 1]

            parsed_code[i - 1:i + 1] = [node.Comparison(left, right, token.comparator)]

        else:
            i += 1
    return parsed_code


def parse(lexed_code: list) -> AST.AST:
    """
    Creates an AST from a list of tokens.
    :param lexed_code:
    :return:
    """
    parsed_code = [calculateNode(token) for token in lexed_code]
    parsed_code = parse_blocks(parsed_code)
    parsed_code = parse_for_block(parsed_code)

    i = 0
    while i < len(parsed_code):
        current_node = parsed_code[i]
        if isinstance(current_node, node.BinaryOperationPlaceholder):
            if i == 0 or i + 1 >= len(parsed_code):
                raise SyntaxError("Malformed binary expression: missing operand")

            left = parsed_code[i - 1]
            right = parsed_code[i + 1]

            if isinstance(right, (node.EOF, node.EOL)):
                raise SyntaxError(f"Unexpected end of line/file in expression")

            new_node = node.BinaryOperation(left, current_node.operation, right)
            parsed_code[i - 1:i + 2] = [new_node]
            i = max(i - 1, 0)
        else:
            i += 1

    return AST.generateAST(parsed_code)
