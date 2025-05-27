from os import path

def analyze(profile_type="unoptimized"):
    if profile_type == 'unoptimized':
        directory = 'benchmarks/results/unoptimized'
        filename = input("Enter filename (eg. inefficient_matrix_multiplication.lprof):").strip()
    elif profile_type == 'optimized':
        directory = 'benchmarks/results/optimized'
        filename = input("Enter filename (eg. decorated_test_func.lprof):").strip()
    else:
        raise ValueError(f"Unknown profile_type: {profile_type}")
    
    f = path.join(directory, filename)

    if not path.exists(f):
        print(f"Error: The file '{filename}' does not exist in the specified directory.")
        return

    values = []

    with open(f, 'r') as file:
        lines = file.readlines()

    for line in lines:
        columns = line.split()
        
        if len(columns) > 5:
            try:
                time_percentage = float(columns[4]) 
                line_content = " ".join(columns[5:])  
                values.append((time_percentage, line_content))
            except ValueError:
                continue

    values_sorted = sorted(values, key=lambda x: x[0], reverse=True)

    print("\nResults:")
    for time_percentage, line_content in values_sorted:
        print(f"Time: {time_percentage:.2f}% -> Line: {line_content}")



