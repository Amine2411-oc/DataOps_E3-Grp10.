import pandas as pd

def compress_to_parquet(input_file, output_file):
    df = pd.read_csv(input_file)
    df.to_parquet(output_file, engine='pyarrow')
    print(f"Fichier compressé en {output_file}")

if __name__ == "__main__":
    compress_to_parquet('data/transformed.csv', 'data/compressed.parquet')
