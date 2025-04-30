from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import os  # Import os module to handle directory operations

app = Flask(__name__)

@app.route("/")
def home():
    # Ensure that the 'static' directory exists
    if not os.path.exists('static'):
        os.makedirs('static')  # Create 'static' directory if it doesn't exist

    df = pd.read_csv("suicide_data.csv")
    yearly_data = df.groupby('year')['suicides_no'].sum()

    plt.figure(figsize=(8, 4))
    yearly_data.plot(kind='line', color='red', marker='o')
    plt.title("Suicides in India Over Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Suicides")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("static/graph.png")  # Save plot in the 'static' directory
    plt.close()

    total = df['suicides_no'].sum()
    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

