# bank-financial-analysis

![In Progress](https://img.shields.io/badge/status-in%20progress-yellow)

## 🔹 Obiettivo del progetto
Questo progetto ha l'obiettivo di effettuare un'analisi comparativa di 10 banche utilizzando dati finanziari pubblici.  

---

## 🔹 Prerequisiti
- Python ≥ 3.9
- Virtual environment (venv) consigliato
- Git
- Librerie Python (installate tramite venv):
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - plotly
  - jupyter 

---

## 🔹 Setup dell'ambiente virtuale (venv)
1. Aprire il terminale nella cartella del progetto

2. Creare il virtual environment:
   ```bash
    python -m venv .venv

3. Attivare il virtual environment:
    Windows (PowerShell)
    ```bash
    .\.venv\Scripts\activate
    ```
    
    Mac/Linux
    ```bash
    source .venv/bin/activate
    ```
4. Installare le librerie necessarie:
    ```bash
    pip install -r requirements.txt
    ```

5. Per disattivare l'ambiente quando finisci:
    ```bash
    deactivate
    ```


## 🔹 Avvio del progetto
Con il virtual environment attivo (venv), avviare Jupyter Notebook
   ```bash
   jupyter notebook
   ```
Aprire il notebook desiderato nella cartella notebooks/ per eseguire l'analisi.


## 🔹 Spegnimento del progetto
### Spegnere Jupyter Notebook
1. Dal terminale dove è avviato, premere Ctrl+C e confermare con Y
2. Oppure dal browser, cliccare su "Quit" nella pagina principale di Jupyter
3. Infine, disattivare il venv:
   deactivate

## 🔹 Dataset

- Per la descrizione completa del dataset, la sua struttura e il contenuto, vedere il file [docs/dataset.md](docs/dataset.md).


## 🔹 Data Cleaning

Il notebook `01_data_cleaning.ipynb` contiene il processo di pulizia del dataset:
- normalizzazione nomi colonne
- gestione valori mancanti
- controllo tipi dati
- rimozione duplicati

Per dettagli completi, vedere [docs/data_cleaning.md](docs/data_cleaning.md)


## 🔹 Struttura della repo
    bank-financial-analysis/
    │
    ├── data/                
    │   ├── raw/             # dataset originali
    │   └── processed/       # dati puliti e pronti per l'analisi
    │
    ├── notebooks/           # Jupyter Notebooks
    │   ├── 01_data_cleaning.ipynb
    │   ├── 02_eda.ipynb
    │   └── 03_kpi_analysis.ipynb
    │
    ├── src/                 # script Python
    │   ├── data_preprocessing.py
    │   ├── kpi_functions.py
    │   └── visualization.py
    │
    ├── reports/             
    │   ├── figures/         # grafici esportati
    │   └── summary.pdf      # report finale
    │
    ├── requirements.txt     
    ├── README.md            
    ├── .gitignore           
    └── LICENSE


## 🔹 Risultati principali
Trend di crescita delle principali banche
Confronto tra KPI finanziari
Cluster di banche simili per profilo finanziario


## 🔹 Note
Tutti i dati utilizzati sono pubblici o simulati a scopo di studio.
Il progetto è pronto per essere esteso con dashboard interattive (Streamlit, Plotly Dash).
La cartella `.venv` è esclusa dal repository; solo `requirements.txt` viene condiviso.
