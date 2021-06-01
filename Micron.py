import sys
import re

class MicronLexer():
    tokens = {
        ("Identif",  r"[_a-zA-Z][_a-zA-Z0-9]*"),
        ("FloatLit", r"[+-]?([0-9]*[.])?[0-9]+"),
        ("Lbracket", r"\["),
        ("Rbracket", r"\]"),
        ("QuoteLit", r"([\"'])(?:(?=(\\?))\2.)*?\1"),
        ("Colon",    r"\:"),
        ("Equals",   r"=="),
        ("NotEquals",r"!="),
        ("GreatEqls",r">="),
        ("LessEqual",r"<="),
        ("Let",      r"/(^|\s+)let(?=\s+|$)/"),
        ("If",       r"/(^|\s+)if(?=\s+|$)/"),
        ("Set",      r"/(^|\s+)set(?=\s+|$)/"),
        ("GreatThan",r">"),
        ("LessThan", r"<"),
        ("LCurlyBr", r"{"),
        ("RCurlyBr", r"}"),
        ("Tilda",    r"~"),
        ("While",    r"(^|\s+)while(?=\s+|$)"),
        ("Backtick", r"`"),
        ("Comment",  r";"),
        ("Newline",  r"[\n\t]+"),
        ("Space",    r"#[^\m")
    }

    def Tokenize(self, data):
        pos = 0
        tokens = []
        while pos < len(data):
            match = None
            for token_exprs in self.tokens:
                token_expr = token_exprs[1]
                pattern = token_expr
                tag = token_expr
                regex = re.compile(pattern)
                match = regex.match(data, pos)
                if match:
                    text = match.group(0)
                    if tag:
                        token = (text, tag)
                        tokens.append(token)
                    break
            if not match:
               sys.stderr.write('Invalid: %s\\n' % data[pos])
               sys.exit(1)
            else:
                pos = match.end(0)
        return tokens


if __name__ == '__main__':
    file = open(sys.argv[1])
    data = file.read()
    file.close()
    lexer = MicronLexer()
    lexer.Tokenize(data)
    for tok in lexer.Tokenize(data):
        print(tok)
