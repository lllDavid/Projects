from os import path

def analyze():
    directory = 'benchmarks/results/unoptimized'
    filename = input("Enter filename (eg. inefficient_matrix_multiplication.lprof):").strip()
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



