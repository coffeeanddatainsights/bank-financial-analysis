# Notebook 03 – Analisi KPI

## 🔹 Obiettivo
Il notebook `03_kpi_analysis.ipynb` si concentra sull’analisi dei principali KPI (Key Performance Indicators) delle banche presenti nel dataset trasformato.  
L’obiettivo è:
- Calcolare indicatori di redditività, efficienza, margine di interesse e crescita.
- Visualizzare i KPI attraverso grafici leggibili.
- Annotare osservazioni e insight per eventuali anomalie, trend o outlier.

---

## 🔹 Dataset
- File utilizzato: `../data/processed/dataset_transformed.csv`
- Contiene la colonna `date` (convertita in datetime) e tutte le colonne numeriche derivate dai notebook precedenti.
- Include KPI già calcolati come ROA, ROE, Cost/Income Ratio, Net Interest Margin, crescita asset e crescita utile netto.

---

## 🔹 Librerie utilizzate
- `pandas`: gestione e manipolazione dati.
- `matplotlib.pyplot` e `matplotlib.dates`: visualizzazione serie temporali.
- Funzioni di utilità e KPI importate dai file:
  - `src/lib/utils.py`
  - `src/kpi_functions.py`
  - `src/visualization.py`

---

## 🔹 Workflow e passi principali

### 1. Setup iniziale
- Import delle librerie e delle funzioni.
- Caricamento del dataset trasformato.
- Conversione della colonna `date` in formato datetime.
- Controllo veloce della struttura del DataFrame (colonne, tipi dati, eventuali valori mancanti).

### 2. Calcolo e riepilogo KPI
- KPI Redditività: ROA, ROE
- KPI Efficienza: Cost/Income Ratio
- KPI Margine di Interesse: Net Interest Margin
- KPI Crescita: crescita asset e utile netto

### 3. Visualizzazione KPI
- Serie temporali per ROA, ROE, NIM, crescita asset/utile.
- Istogrammi per Cost/Income Ratio.
- Tutti i grafici salvati in [../reports/figures](../reports/figures).

### 4. Insight e analisi
- Annotare le osservazioni principali dai grafici e dai KPI in celle Markdown.
- Alcuni spunti:
    - Quali KPI mostrano tendenze positive o negative?
    - Ci sono anomalie o outlier evidenti?
    - Eventuali pattern stagionali o variazioni improvvise da approfondire.
