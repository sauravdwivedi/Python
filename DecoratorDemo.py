"""A demo for decorator method that filters string values passed to a method that takes
   kwarg as input.

   Example: Let test_fun be a method that takes kwags as input. A decorator filter_string
   modifies behavior of method test_fun, and returns only kwargs with string values:

   for

   input_pars = (a=1, b="Saurav", c=[1,2,3])

   test_fun(input_pars) returns {'b': 'Saurav'}.
"""

def filter_string(func):
    def wrapper(*args, **kwargs):
        dict_empt = {}
        for key in kwargs:
            if type(kwargs[key]) == str:
                dict_empt[key] = kwargs[key]
        return dict_empt
    return wrapper
    
@filter_string
def test_fun(*args, **kwargs):
    return kwargs
    
def main():
    pass
    
if __name__ == '__main__':
    main()
