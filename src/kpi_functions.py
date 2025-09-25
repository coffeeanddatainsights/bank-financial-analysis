import sys
sys.path.append('./lib/')
from lib.utils import *
import matplotlib.dates as mdates


def summarize_kpis(df):
    """
    Riepilogo statistico dei principali KPI.
    """
    kpis = ['roa', 'roe', 'cost_income_ratio', 'net_interest_margin', 'asset_growth', 'income_growth']
    return df[kpis].describe()

def rolling_mean(df, col, window=30):
    """
    Media mobile su una colonna.
    """
    return df[col].rolling(window=window).mean()


def plot_timeseries_dates(df, col, title=None, save_path=None):
    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(df['date'], df[col])
    ax.set_title(title if title else col)
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    plt.show()
    
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        fig.savefig(save_path, bbox_inches="tight")
        print(f"Grafico salvato in: {save_path}")