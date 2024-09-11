from sympy.printing.c import C89CodePrinter, C99CodePrinter

reserved = ...
_math_functions = ...

class _CXXCodePrinterBase:
    printmethod = ...
    language = ...
    _ns = ...
    def __init__(self, settings=...) -> None: ...

class CXX98CodePrinter(_CXXCodePrinterBase, C89CodePrinter):
    standard = ...
    reserved_words = ...

class CXX11CodePrinter(_CXXCodePrinterBase, C99CodePrinter):
    standard = ...
    reserved_words = ...
    type_mappings = ...

class CXX17CodePrinter(_CXXCodePrinterBase, C99CodePrinter):
    standard = ...
    reserved_words = ...
    _kf = ...

cxx_code_printers = ...
