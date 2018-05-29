#def zero():
    #try:
        ## The print just to show it works
        #print("zero")
    #except Exception as e:
        #print(e)
    #return "zero"

#def one():
    #print("one")
    #return "one"

#def numbers_to_functions_to_strings(argument):
    #try:
        #switcher = {
            #0: zero,
            #1: one,
            #2: lambda: "two",
        #}
        ## Get the function from switcher dictionary
        #func = switcher.get(argument, lambda: "nothing")
        ## Execute the function
        #return func()
    #except Exception as e:
        #print(e)
#numbers_to_functions_to_strings("tow")


def zero():
    try:
        # The print just to show it works
        print("zero")
    except Exception as e:
        print(e)
    return "zero"

def one():
    print("one")
    return "one"

def numbers_to_functions_to_strings(argument):
    try:
        switcher = {
            0: zero,
            1: one,
            2: lambda: "two",
        }
        # Get the function from switcher dictionary
        func = switcher.get(argument, lambda: numbers_to_functions_to_strings(1))
        # Execute the function
        return func()
    except Exception as e:
        print(e)
numbers_to_functions_to_strings("tow")
