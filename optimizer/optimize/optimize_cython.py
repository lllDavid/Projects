import os
import subprocess
import importlib.util
import sys
import inspect
from random import randint

def extract_function_code(file_path, func_name):
    """Extracts the code of a function from a Python file."""
    try:
        with open(file_path, "r") as file:
            code = file.read()
        
        # Compile the code to extract the function
        compiled = compile(code, file_path, 'exec')
        func_code = None
        
        # Execute the compiled code in a namespace to extract the function
        exec(compiled, globals())
        
        # Check if the function exists in the global namespace
        if func_name in globals():
            # Extract only the function body
            func_code = inspect.getsource(globals()[func_name]).split("\n", 1)[1]
        
        return func_code
    except Exception as e:
        print(f"Error extracting function {func_name}: {e}")
        return None

def generate_cython_code(func_name, func_code, func_dir):
    """Generates the optimized .pyx file in the specified directory."""
    os.makedirs(func_dir, exist_ok=True)  # Ensure the directory exists
    cython_file_path = os.path.join(func_dir, f"optimized_{func_name}.pyx")  # Add 'optimized_' prefix
    
    # Only write the function body without redundant signature
    cython_code = f"""
def {func_name}(A, B):
{func_code}
    """
    
    with open(cython_file_path, "w") as f:
        f.write(cython_code)
    return cython_file_path

def compile_cython_file(func_name, func_dir):
    """Compiles the .pyx file into a Cython extension module."""
    setup_code = f"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("optimized_{func_name}.pyx", compiler_directives={{'language_level': "3"}}),
)
"""
    
    setup_path = os.path.join(func_dir, "setup.py")
    with open(setup_path, "w") as f:
        f.write(setup_code)
    
    try:
        subprocess.check_call([sys.executable, "setup.py", "build_ext", "--inplace"], cwd=func_dir)
        print(f"Compiled optimized_{func_name}.pyx into a Cython module in {func_dir}.")
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")

def load_compiled_function(func_name, func_dir):
    """Loads the compiled function from the specified directory."""
    sys.path.append(func_dir)  # Add function directory to sys.path
    try:
        module = importlib.import_module(f"optimized_{func_name}")  # Load with 'optimized_' prefix
        return getattr(module, func_name)
    except Exception as e:
        print(f"Error loading {func_name}: {e}")
        return None

def dynamic_cython(func_name, func_code, A, B):
    """Generates, compiles, and loads a Cython function dynamically."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../functions/optimized"))
    func_dir = os.path.join(base_dir, func_name)
    generate_cython_code(func_name, func_code, func_dir)
    compile_cython_file(func_name, func_dir)
    cython_func = load_compiled_function(func_name, func_dir)
    
    if cython_func:
        print(f"Running {func_name} with Cython optimization:")
        return cython_func(A, B)
    else:
        print("Error: Function could not be loaded.")
        return None

def main():
    file_path = input("Enter the path to the Python file (e.g., file.py): ")
    func_name = input("Enter the name of the function you want to cythonize: ")
    
    # Extract the function code from the provided file
    func_code = extract_function_code(file_path, func_name)
    
    if func_code is None:
        print(f"Could not extract the code for {func_name} from {file_path}.")
        return
    
    # Setup random matrices A and B
    size = 50
    min_val = 1
    max_val = 10

    A = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]
    B = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]

    # Dynamically generate, compile, and run the function
    result = dynamic_cython(func_name, func_code, A, B)
    if result:
        print(f"Result of {func_name}:")
        print(result)

if __name__ == "__main__":
    main()
