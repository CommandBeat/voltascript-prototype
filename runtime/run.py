from runtime import interpreter
from frontend import parser
from frontend import lexer

def run(code):
    lex = lexer.lex(code)
    parse = parser.parse(lex)
    interpreter.interpret(parse)

def runFile(filepath):
    with open(filepath, 'r') as f:
        for line in f:
            run(line)