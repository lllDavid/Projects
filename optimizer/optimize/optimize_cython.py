import os
import sys
import subprocess
import importlib.util
from inspect import getsource, signature

# Extract full source code and signature of a function from a Python module
# TODO: Handle functions with decorators
# TODO: Validate file path existence before reading
def extract_function_code(file_path, func_name):
    try:
        with open(file_path, "r") as file:
            code = file.read()
        
        compiled = compile(code, file_path, 'exec')
        env = {}
        exec(compiled, env)
        
        if func_name in env:
            func_obj = env[func_name]
            source = getsource(func_obj)
            func_code = source.split("\n", 1)[1] if "\n" in source else ""
            func_params = str(signature(func_obj))
            return func_code, func_params
        else:
            print(f"Function {func_name} not found in {file_path}.")
            return None, None
    except Exception as e:
        print(f"Error extracting function {func_name}: {e}")
        return None, None
    
# Generates a Cython .pyx file for the specified function
def generate_cython_code(func_name, func_params, func_code, func_dir):
    os.makedirs(func_dir, exist_ok=True)
    cython_file_path = os.path.join(func_dir, f"{func_name}.pyx")
    
    cython_code = f"def optimized_{func_name}{func_params}:\n{func_code}"
    
    with open(cython_file_path, "w") as f:
        f.write(cython_code)
    return cython_file_path

# Compiles the Cython .pyx file into a shared library
# TODO: Clean up temporary build files after compilation
def compile_cython_file(func_name, func_dir):
    setup_code = (
        "from setuptools import setup\n"
        "from Cython.Build import cythonize\n\n"
        "setup(\n"
        f"    ext_modules=cythonize('{func_name}.pyx', compiler_directives={{'language_level': '3'}}),\n"
        ")\n"
    )
    setup_path = os.path.join(func_dir, "setup.py")
    with open(setup_path, "w") as f:
        f.write(setup_code)
    
    try:
        subprocess.check_call([sys.executable, "setup.py", "build_ext", "--inplace"], cwd=func_dir)
        print(f"Compiled {func_name}.pyx into a Cython module in {func_dir}.")
    except subprocess.CalledProcessError as e:
        print(f"Error during compilation: {e}")

# Returns the platform-specific shared library extension
def get_shared_lib_extension():
    return ".pyd" if sys.platform.startswith("win") else ".so"

# Loads the compiled Cython function from the shared library
def load_compiled_function(func_name, func_dir):
    module_name = f"{func_name}"
    module_path = os.path.join(func_dir, f"{module_name}{get_shared_lib_extension()}")
    try:
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return getattr(module, func_name)
    except Exception as e:
        print(f"Error loading {func_name}: {e}")
        return None

# Generates a run.py file to benchmark the compiled function
def generate_run_file(func_name, func_dir):
    run_file_path = os.path.join(func_dir, "run.py")
    run_code = (
f"from functions.optimized.{func_name}.{func_name} import optimized_{func_name}\n"
"from benchmarks.time import time_function\n"
"from benchmarks.profiler import profile_function\n"
"from random import randint\n\n"
"@time_function(repetitions=10)\n"
"@profile_function(profile_type=\"optimized\")\n"
"def " + func_name + "(*args, **kwargs):\n"
"    return " "optimized_"+ func_name + "(*args, **kwargs)\n\n"
"def main():\n"
"    size = 50\n"
"    min_val = 1\n"
"    max_val = 10\n"
"    A = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]\n"
"    B = [[randint(min_val, max_val) for _ in range(size)] for _ in range(size)]\n"
"    " + func_name + "(A, B)\n\n"
"if __name__ == \"__main__\":\n"
"    main()\n"
    )
    with open(run_file_path, "w") as f:
        f.write(run_code)
    print(f"Generated run.py in {func_dir}.")

# Orchestrates the Cython optimization process
def dynamic_cython(func_name, func_params, func_code):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../functions/optimized"))
    
    if not os.path.exists(base_dir):
        print(f"Creating base directory {base_dir}.")
        os.makedirs(base_dir)

    func_dir = os.path.join(base_dir, func_name)
    if not os.path.exists(func_dir):
        print(f"Creating directory for function {func_name} at {func_dir}.")
        os.makedirs(func_dir)

    generate_cython_code(func_name, func_params, func_code, func_dir)
    compile_cython_file(func_name, func_dir)
    generate_run_file(func_name, func_dir)

def main():
    file_path = input("Enter the file path (e.g., optimize/function.py): ")
    file_path = os.path.normpath(file_path)  

    func_name = input("Enter the function to cythonize (e.g., matrix_multiplication): ")

    print(f"File path: {file_path}")
    print(f"Function name: {func_name}")
    
    func_code, func_params = extract_function_code(file_path, func_name)
    if func_code is None:
        print(f"Could not extract the code for {func_name} from {file_path}.")
        return
    
    dynamic_cython(func_name, func_params, func_code)

if __name__ == "__main__":
    main()