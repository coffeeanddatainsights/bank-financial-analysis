# Data Cleaning - 01_data_cleaning.ipynb

Questo documento descrive tutti i passaggi effettuati nel notebook `01_data_cleaning.ipynb` per pulire il dataset.

## 1. Normalizzazione nomi colonne
- Rimosso spazi iniziali/finali
- Convertiti tutti i caratteri in minuscolo
- Sostituiti spazi interni con underscore
```python
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
```

## 2. Gestione valori mancanti
- Rimozione righe e colonne completamente vuote
```python
df = df.dropna(how='all')      # righe vuote
df = df.dropna(axis=1, how='all')  # colonne vuote
```
- Colonne numeriche
    - Interpolazione dei valori mancanti per mantenere trend
    - Riempimento residuo con 0
```python
numeric_cols = df.select_dtypes(include='number').columns
for col in numeric_cols:
    df[col] = df[col].interpolate().fillna(0)
```

- Colonna date
    - Prima riempimento dei valori mancanti → righe con NaN rimosse
    - Conversione in datetime
```python
df['date'] = pd.to_datetime(df['date'], errors='coerce')
df = df.dropna(subset=['date'])
```

## 3. Controllo tipi dati
- Tutte le colonne numeriche convertite a numerico
```python
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
```

## 4. Rimozione duplicati
- Eliminazione delle righe duplicate per garantire coerenza
```python
df = df.drop_duplicates()
```

## 5. Ordinamento temporale
- Ordinamento del dataset in base alla colonna date
```python
df = df.sort_values('date').reset_index(drop=True)
```

## 6. Salvataggio dataset pulito
```python
df.to_csv('../data/processed/dataset_clean.csv', index=False)
```


Per la trasformazione dei dati, vedere [./data_transforming.md](./data_transforming.md)



## 🔹 Note aggiuntive
Il dataset originale (data/raw/dataset.csv) rimane intatto.
Il notebook include commenti e celle Markdown che spiegano ogni passaggio.
Il dataset pulito sarà utilizzato per la successiva analisi esplorativa.
