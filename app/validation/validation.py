#
ARGS = 1
KWARGS = 2


def validate(argsCount=1, paramType=1):
    def wapper(func):
        def inner_fun(*args, **kwargs):
            if paramType == ARGS:
                if argsCount <= 0:
                    return print("Parameter Error: can not validate 0 args")
                elif len(kwargs) > 0 and len(args) <= 0:
                    return print(f"Validation Error: Function parameters requird as args ex: (val1,val2)")
                else:
                    param = args[1:]
                    if(len(param) != argsCount):
                        return print(
                            f"Validation Error: Required {argsCount} but only found {len(param)}")
            elif paramType == KWARGS:
                if argsCount <= 0:
                    return print("Parameter Error: can not validate 0 args")
                elif len(args) > 0 and len(kwargs) <= 0:
                    return print(f"Validation Error: Function parameters requird as kwargs ex: (val1='value1',val2=10)")
                else:
                    if(len(kwargs) != argsCount):
                        return print(
                            f"Validation Error: Required {argsCount} but only found {len(kwargs)}")
            return func(*args, **kwargs)
        return inner_fun
    return wapper


def get_inputs(params):
    def wapper(func):
        def innder_fun(*args, **kwargs):
            new_params = {}
            for x in range(0, len(params)):
                i = input(f"Enter {params[x]}: ")
                new_params[params[x]] = i
            return func(*args, **new_params)
        return innder_fun
    return wapper