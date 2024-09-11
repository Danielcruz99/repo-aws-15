from typing_extensions import Self

from sympy.core.function import Function

class SingularityFunction(Function):
    is_real = ...
    def fdiff(self, argindex=...) -> Self | None: ...
    @classmethod
    def eval(cls, variable, offset, exponent) -> None: ...

    _eval_rewrite_as_DiracDelta = ...
    _eval_rewrite_as_HeavisideDiracDelta = ...
