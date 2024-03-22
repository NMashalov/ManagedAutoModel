import typing as tp
import functools 

class Gardener:
    def __init__(self,name:str):
        self.tools: dict[str,tp.Callable]= {}
        self.name = name

    def add(self,tool_func:tp.Callable):
        func_name = tool_func.__name__
        partial_function = functools.partial(tool_func,name=self.name)
        self.tools[func_name] = partial_function
        return partial_function

Robert = Gardener('robert')

def shovel_robert(name):
    return f'{name} shovel'

# Robert.add(shovel_robert)

Robert.shovel = shovel_robert
print(Robert.shovel(Robert.name))