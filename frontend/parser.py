from frontend import lexer_token as lt
from frontend import node
from frontend import AST

binaryOperatorsTypes = [
    lt.TokenType.PLUS,
    lt.TokenType.MINUS,
    lt.TokenType.MULTIPLY,
    lt.TokenType.DIVIDE
]


def calculateNode(token: lt.Token):
    if token.type == lt.TokenType.EOF:
        return node.EOF()
    if token.type == lt.TokenType.EOL:
        return node.EOL()
    if token.type == lt.TokenType.NUMBER:
        return node.Number(token.value)
    if token.type in binaryOperatorsTypes:
        return node.BinaryOperationPlaceholder(token.value)
    if token.type == lt.TokenType.IDENTIFIER:
        return node.Identifier()
    if token.type == lt.TokenType.VARIABLE:
        return node.Variable(token.value)
    if token.type == lt.TokenType.ASSIGN:
        return node.Assign()
    if token.type == lt.TokenType.FUNC_REF:
        return node.Function(token.value)
    if token.type == lt.TokenType.STRING:
        return node.String(token.value)
    if token.type == lt.TokenType.LPAREN or token.type == lt.TokenType.LCURLY_BRACE:
        return node.Start(token.value)
    if token.type == lt.TokenType.RPAREN or token.type == lt.TokenType.RCURLY_BRACE:
        return node.End(token.value)
    if token.type == lt.TokenType.IMPORT_LIB:
        return node.Import(token.value)
    return node.Node()


def parse_expression(tokens):
    temp = tokens[:]
    i = 0
    while i < len(temp):
        if isinstance(temp[i], node.BinaryOperationPlaceholder):
            left = temp[i - 1]
            right = temp[i + 1]
            new_node = node.BinaryOperation(left, temp[i].operation, right)
            temp[i - 1:i + 2] = [new_node]
            i = max(i - 1, 0)
        else:
            i += 1
    return temp[0]


def parse_blocks(parsed_code: list) -> list:
    i = 0
    while i < len(parsed_code):
        token = parsed_code[i]

        if isinstance(token, node.Function):
            # Expect '('
            if not isinstance(parsed_code[i+1], node.Start):
                raise SyntaxError("Expected '(' after function name")

            j = i + 2  # skip '('
            arg_tokens = []
            args = []

            while j < len(parsed_code):
                t = parsed_code[j]

                if isinstance(t, node.End):
                    # End of argument list
                    if arg_tokens:
                        args.append(parse_expression(arg_tokens))
                    break

                # Support commas later if needed
                arg_tokens.append(t)
                j += 1

            # Assign parsed arguments
            token.args = args

            # Remove everything from '(' to ')'
            del parsed_code[i+1:j+1]

        i += 1

    return parsed_code



def parse(lexedcode: list) -> AST.AST:
    """
    Parses through preprocessed code to make an AST node
    :param lexedcode:
    :return:
    """
    parsed_code = []

    for i, token in enumerate(lexedcode):
        parsed_code.append(calculateNode(token))

    parsed_code = parse_blocks(parsed_code)

    i = 0
    while i < len(parsed_code):
        current_node = parsed_code[i]

        if isinstance(current_node, node.BinaryOperationPlaceholder):
            if i == 0 or i + 1 >= len(parsed_code):
                raise SyntaxError("Malformed binary expression: missing operand")

            left = parsed_code[i - 1]
            right = parsed_code[i + 1]

            if isinstance(right, node.EOF):
                raise SyntaxError("Unexpected EOF in expression")
            elif isinstance(right, node.EOL):
                raise SyntaxError("Unexpected EOL in expression")

            new_node = node.BinaryOperation(left, current_node.operation, right)

            parsed_code[i - 1:i + 2] = [new_node]

            i = max(i - 1, 0)
        else:
            i += 1

    if not isinstance(parsed_code[-1], node.EOL) and not isinstance(parsed_code[-1], node.EOF):
        parsed_code.append(node.EOF())

    return AST.generateAST(parsed_code)
