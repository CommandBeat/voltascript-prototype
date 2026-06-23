from enum import Enum

class TokenType(Enum):
    EOF = 0
    NUMBER = 1
    PLUS = 2
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    ASSIGN = 6
    IDENTIFIER = 7
    VARIABLE = 8
    COMMA = 9
    COLON = 10
    DEF_FUNCTION = 11
    FUNC_REF = 12
    STRING = 13
    START = 14
    END = 15
    FUNCTION = 16
    EOL = 17
    IMPORT_LIB = 18
    CONVERT_INT = 19
    CONDITION = 20
    SYMBOL = 21
    COMPARISON = 22
    INCREMENT = 23
    DECREMENT = 24
    OVERRIDE_FUNC = 25

class Token:
    def __init__(self, type_: TokenType, value):
        self.type = type_
        self.value = value
    def __repr__(self):
        return "Token(Type: %s, Value: '%s')" % (self.type, self.value)

    def __str__(self):
        return "Token(Type: %s, Value: '%s')" % (self.type, self.value)