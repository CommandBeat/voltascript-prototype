class AST:
    def __init__(self, parsedcode: list):
        self.code = parsedcode
    def __str__(self):
        return f"AST({self.code})"
    def __repr__(self):
        return f"AST({self.code})"

def generateAST(parsedcode: list):
    return AST(parsedcode)