class AST:
    def __init__(self, parsed_code: list):
        self.code = parsed_code
    def __str__(self):
        return f"AST({self.code})"
    def __repr__(self):
        return f"AST({self.code})"
    def get_code(self):
        return self.code

def generateAST(parsed_code: list):
    return AST(parsed_code)