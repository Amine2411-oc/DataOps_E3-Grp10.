import time
import pandas as pd

def benchmark_function(func, *args):
    start_time = time.time()
    func(*args)
    end_time = time.time()
    return end_time - start_time

if __name__ == "__main__":
    results = []

    # Benchmark Extraction
    from extract import load_data
    extraction_time = benchmark_function(load_data, 'data/input.csv')
    results.append(['Extraction', extraction_time, 'Load data from input.csv'])

    # Benchmark Transformation
    from transform import transform_data
    df = pd.read_csv('data/input.csv')
    transformation_time = benchmark_function(transform_data, df)
    results.append(['Transformation', transformation_time, 'Clean and transform the data'])

    # Save Results
    results_df = pd.DataFrame(results, columns=['test', 'execution_time', 'description'])
    results_df.to_csv('data/benchmark_results.csv', index=False)
    print("Benchmark results saved to data/benchmark_results.csv")
