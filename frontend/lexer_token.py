from enum import Enum

class TokenType(Enum):
    EOF = 0
    NUMBER = 1
    PLUS = 2
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    LPAREN = 6
    RPAREN = 7
    ASSIGN = 8
    IDENTIFIER = 9
    VARIABLE = 10
    COMMA = 11
    COLON = 12
    DEF_FUNCTION = 13
    FUNC_REF = 15
    STRING = 16
    LCURLY_BRACE = 17
    RCURLY_BRACE = 18
    FUNCTION = 21
    EOL = 22
    IMPORT_LIB = 23
    CONVERT_INT = 24

class Token:
    def __init__(self, type_: TokenType, value):
        self.type = type_
        self.value = value
    def __repr__(self):
        return "Token(Type: %s, Value: '%s')" % (self.type, self.value)

    def __str__(self):
        return "Token(Type: %s, Value: '%s')" % (self.type, self.value)