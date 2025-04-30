import matplotlib
matplotlib.use('Agg')  # Use Agg backend for non-GUI plotting
import matplotlib.pyplot as plt
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv("suicide_data.csv")
    yearly_data = df.groupby('year')['suicides_no'].sum()

    plt.figure(figsize=(8,4))
    yearly_data.plot(kind='line', color='red', marker='o')
    plt.title("Suicides in India Over Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Suicides")
    plt.grid(True)
    plt.tight_layout()
    
    # Save the plot to a file (without showing the GUI)
    plt.savefig("static/graph.png")
    plt.close()  # Close the plot to release resources

    total = df['suicides_no'].sum()
    return render_template("index.html", total=total)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
