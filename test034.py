# -*- coding: utf-8 -*-
import types

def fn():
    pass

aa = type(fn) == types.FunctionType
bb = type(abs) == types.BuiltinFunctionType
cc = type(lambda x: x) == types.LambdaType
dd = type((x for x in range(10))) == types.GeneratorType

print(aa, bb, cc, dd)
