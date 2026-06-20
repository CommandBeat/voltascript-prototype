from frontend import lexer_token as lt
import json
import os

with open("syntax.json", "r") as f:
    syntax = json.load(f)
    keywords = syntax["keywords"]

variables = []

def lex(code: str) -> list[lt.Token]:
    """
    Preprocesses code to make a more machine friendly format
    :param code:
    :return:
    """
    lexed_code = []
    num = False

    i = 0
    while i < len(code):
        char = code[i]
        # comment check
        if code[i:i + 2] == "//":
            # skip until newline or EOF
            while i < len(code) and code[i] != '\n':
                i += 1
            continue

        # single char tokens
        if char == '+':
            lexed_code.append(lt.Token(lt.TokenType.PLUS, '+'))
        elif char == '-':
            lexed_code.append(lt.Token(lt.TokenType.MINUS, '-'))
        elif char == '*':
            lexed_code.append(lt.Token(lt.TokenType.MULTIPLY, '*'))
        elif char == '/':
            lexed_code.append(lt.Token(lt.TokenType.DIVIDE, '/'))
        elif char == '=':
            lexed_code.append(lt.Token(lt.TokenType.ASSIGN, '='))
        elif char == ')':
            lexed_code.append(lt.Token(lt.TokenType.RPAREN, ')'))
        elif char == '{':
            lexed_code.append(lt.Token(lt.TokenType.LCURLY_BRACE, '{'))
        elif char == '}':
            lexed_code.append(lt.Token(lt.TokenType.RCURLY_BRACE, '}'))

        # multiple char tokens
        if code[i] == "\n":
            lexed_code.append(lt.Token(lt.TokenType.EOL, '\n'))
            i += 2

        # strings
        if char == "'" or char == '"':
            index = 0
            string = ""
            while index < len(code):
                if code[index] == '"' or code[index] == "'":
                    break
                string += code[index]
                index += 1
            lexed_code.append(lt.Token(lt.TokenType.STRING, string))

        # import
        if code[i:i+len("import")] == "import":
            index = i + len("import")
            library_name = ""
            while index < len(code) and code[index] != '\n':
                library_name += code[index]
                index += 1
            for file in os.scandir("libraries"):
                if file.is_file() and file.name == library_name:
                    lexed_code.append(lt.Token(lt.TokenType.IMPORT_LIB, library_name))
                    break
            i += len("import")

        # function reference
        if char == '(' and code[i-1].isalpha():
            index = i - 1
            while index >= 0:
                index-=1
            func_name = code[index+1:i]
            lexed_code.append(lt.Token(lt.TokenType.FUNC_REF, func_name))
            lexed_code.append(lt.Token(lt.TokenType.LPAREN, '('))

        # variable reference
        if char == '$':
            var_name = ""
            index = i + 1  # skip the '$'

            while index < len(code) and (code[index].isalnum() or code[index] == '_'):
                var_name += code[index]
                index += 1
            lexed_code.append(lt.Token(lt.TokenType.VARIABLE, var_name))

        # integer or float
        if char == '~' and code[i+1].isdigit() and num == False:
            index = i + 1
            num_ = ""
            num = True
            while index < len(code):
                if not code[index].isdigit() and code[index] != '.':
                    break
                num_ += code[index]
                index += 1
            try:
                lexed_code.append(lt.Token(lt.TokenType.NUMBER, int(num_)))
            except Exception as e:
                print(e)
        elif char == '~' and code[i+1].isdigit():
            lexed_code.append(lt.Token(lt.TokenType.CONVERT_INT, "convert_to_integer"))
        elif not char.isdigit() and char != '.':
            num = False

        if char.isdigit() and num == False:
            index = i
            num_ = ""
            num = True
            while index < len(code):
                if not code[index].isdigit() and code[index] != '.':
                    break
                num_ += code[index]
                index += 1
            try:
                lexed_code.append(lt.Token(lt.TokenType.NUMBER, float(num_)))
            except Exception as e:
                print(e)
        elif not char.isdigit() and char != '.':
            num = False

        # if it's a variable statement
        if code[i:i+3] == "var" and i == 0:
            lexed_code.append(lt.Token(lt.TokenType.IDENTIFIER, "var"))
            index = i+3
            # skip whitespace(s)
            while index < len(code):
                if not code[index] == ' ':
                    break
                index+=1
            # get variable name
            var_name = ""
            while index < len(code):
                if code[index] == ' ':
                    break
                var_name += code[index]
                index+=1
            if var_name in keywords:
                raise NameError(f"Variable '{var_name}' is a keyword.")
            lexed_code.append(lt.Token(lt.TokenType.VARIABLE, var_name))
        i+=1

    if lexed_code[-1].type != lt.TokenType.EOL and lexed_code[-1].type != lt.TokenType.EOF:
        lexed_code.append(lt.Token(lt.TokenType.EOF, ''))
    return lexed_code
