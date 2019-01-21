import inspect

def __Title__(title) :
    print("\n")
    print("###################################")
    print("## ", title)
    print("###################################")

def __print__(var) :
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    name = [var_name for var_name, var_val in callers_local_vars if var_val is var]
    if len(name) == 0 :
        print(var)
    else :
        print("%s = %s" % (name[0], str(var)))