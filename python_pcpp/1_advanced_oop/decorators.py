"""
As you and your team have been working on your internal applications, you've found yourself wanting to be able to quickly benchmark and add logging to a function to help in your debugging. Your team has decided that they'd like to have a library of decorators that they can easily pull in to add logging and benchmarking to a function temporarily without needing to actually modify the function. You've been tasked with building these decorators.

Here are the decorators that you need to build and their requirements.

benchmark - Will note the start time and completion time of the wrapped function and print (or write to a file) the following line when the function is called:
benchmark: [wrapped_function_name] duration: [total_runtime_in_seconds]
log - Simply prints (or writes to a file) the message when the function is called.
running: [wrapped_function_name], args: [positional_arguments], kwargs: [keyword_arguments]
For both of these decorators, you should be able to provide file_name as an optional keyword argument to state the file that the benchmark or log lines should be written.

"""
import math
def benchmark():
    pass

def log(func=None, *, file_name=None):
    def log_decorator(func):
        def _wrapper_func(*args, **kwargs):
            result = func(*args, **kwargs)
        return _wrapper_func 
    if func:
        return log_decorator
    else:
        return log 
