import matplotlib.pyplot as plt
import pandas as pd

def create_visualizations(df):
    plt.figure(figsize=(10, 6))
    df['score'].plot(kind='bar', color='skyblue')
    plt.title("Scores des utilisateurs")
    plt.xlabel("Index")
    plt.ylabel("Score")
    plt.savefig('data/visualization.png')
    print("Visualization saved to data/visualization.png")

if __name__ == "__main__":
    df = pd.read_csv('data/transformed.csv')
    create_visualizations(df)

