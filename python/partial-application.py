# functions are first-class objects in python (like JS), so we should be able to pass them as arguments to other functions

# from functools import partial
# import inspect

# def partialApplication(func):
#   def partiallyAppliedFunc(*args):
#     # *args lets us pass variable number of arguments to this function
#     arity = len(inspect.getargspec(func).args)
#     if len(args) >= arity:
#       return func(*args)
#     else:
#       return partialApplication(functools.partial(func, *args))
#   return partiallyAppliedFunc

  # need to test still!
