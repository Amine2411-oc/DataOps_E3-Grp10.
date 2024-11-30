import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
    return data

if __name__ == "__main__":
    df = load_data('data/input.csv')
    print(df.head())
