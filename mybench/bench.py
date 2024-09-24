import code
from time import time
class CustomREPL(code.InteractiveConsole):
    def raw_input(self, prompt=">>> "):
        return super().raw_input(prompt)
    def runsource(self, source, filename="<input>", symbol="single"):
        start_time = time()
        result = super().runsource(source, filename, symbol)
        execution_time = time() - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        return result
repl = CustomREPL()
repl.interact("Custom Python Interpreter with Execution Time")
