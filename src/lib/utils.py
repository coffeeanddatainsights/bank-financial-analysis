# libs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# funzioni comuni
def check_df_info(df, n_rows=5):
    """
    Stampa un riepilogo veloce di un DataFrame pandas.

    Parametri
    ----------
    df : pandas.DataFrame
        Il DataFrame da analizzare.
    n_rows : int, default=5
        Numero di righe da mostrare in anteprima.

    Output
    ------
    - Info generale del DataFrame
    - Statistiche descrittive di base
    - Prime n righe
    """
    print("\n=== Shape (righe, colonne) ===")
    print(df.shape)

    print("\n=== Nomi colonne ===")
    print(df.columns.tolist())

    print("\n=== Tipi di dato ===")
    print(df.dtypes)

    print("\n=== Info DataFrame ===")
    df.info()

    print("\n=== Statistiche descrittive (numeriche) ===")
    print(df.describe().transpose())

    print(f"\n=== Prime {n_rows} righe ===")
    print(df.head(n_rows))

    print(f"\n=== Ultime {n_rows} righe ===")
    print(df.tail(n_rows))