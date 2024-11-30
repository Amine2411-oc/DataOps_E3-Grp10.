import pandas as pd

def transform_data(df):
    df = df.dropna()  # Suppression des lignes vides
    df['double_score'] = df['score'] * 2  # Exemple de transformation
    return df

if __name__ == "__main__":
    df = pd.read_csv('data/input.csv')
    transformed_df = transform_data(df)
    transformed_df.to_csv('data/transformed.csv', index=False)
    print("Data transformed and saved to data/transformed.csv")
