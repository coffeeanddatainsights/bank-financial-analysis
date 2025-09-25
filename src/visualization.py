import sys
sys.path.append('./lib/')
from lib.utils import *

def plot_timeseries(df, col, title=None, save_path=None):
    plt.figure(figsize=(10,5))
    plt.plot(df['date'], df[col], label=col)
    plt.title(title if title else col)
    plt.xlabel("Data")
    plt.ylabel(col)
    plt.legend()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.show()

def plot_histogram(df, col, bins=20, save_path=None):
    plt.figure(figsize=(8,5))
    plt.hist(df[col].dropna(), bins=bins, alpha=0.7)
    plt.title(f"Distribuzione di {col}")
    if save_path:
        plt.savefig(save_path, bbox_inches="tight")
    plt.show()
