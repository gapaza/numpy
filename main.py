
# Simplify a simple expression
import sympy




import sys
import functools

# Global variable to store function call logs
function_calls = []

def trace_calls(frame, event, arg):
    if event == 'call':
        code = frame.f_code
        func_name = code.co_name
        func_filename = code.co_filename
        func_lineno = code.co_firstlineno
        function_calls.append((func_name, func_filename, func_lineno))
    return trace_calls

def start_tracing():
    sys.settrace(trace_calls)

def stop_tracing():
    sys.settrace(None)

def trace_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_tracing()
        try:
            result = func(*args, **kwargs)
        finally:
            stop_tracing()
        return result
    return wrapper





def run():
    print('Simplifying')

    expr_str = "2*x + x"
    expr = sympy.sympify(expr_str, evaluate=False)
    print('Expression:', expr)


    wrapped_simplify = trace_decorator(sympy.simplify)
    simp_expr = wrapped_simplify(expr)
    print('Simplified:', simp_expr)

    # Print the recorded function calls
    for call in function_calls:
        print(f"Function {call[0]} called at {call[1]}:{call[2]}")

    # algebraic ops
    alg_ops = [
        '__add__',
        '__mul__',
        '__pow__',
        '__sub__',
        '__truediv__',
    ]

    # Get set of function calls
    func_names = set([call[0] for call in function_calls])
    print('Function Calls:', func_names)

    alg_ops_calls = [call for call in function_calls if call[0] in alg_ops]
    for call in alg_ops_calls:
        print(f"Algebraic Op {call[0]} called at {call[1]}:{call[2]}")



def edge_ints():
    from sympy.integrals.manualintegrate import integral_steps, manualintegrate

    expr = sympy.sympify("(asinh(x))")
    var_x = sympy.Symbol('x')
    print('Expression:', expr)
    print('Variable:', var_x)
    result = manualintegrate(expr, var_x)
    print('Result:', result)

    print('Rule stack:', sympy.integrals.manualintegrate.global_rule_stack)
    print('Output stack:', sympy.integrals.manualintegrate.global_output_stack)

    # get resultant expression







if __name__ == '__main__':
    edge_ints()
