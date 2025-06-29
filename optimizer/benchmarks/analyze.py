from os import path

# Parses an unoptimized .lprof file, extracts time-percentage data per line, and displays sorted results
def analyze():
    directory = 'benchmarks/results/unoptimized'

    filename = input("Enter filename (e.g. matrix_multiplication.lprof): ").strip()
    filepath = path.join(directory, filename)

    if not path.exists(filepath):
        print(f"Error: The file '{filename}' does not exist in {directory}.")
        return

    values = []
    with open(filepath, 'r') as file:
        for line in file:
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