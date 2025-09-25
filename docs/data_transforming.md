# Data Cleaning - 01_data_cleaning.ipynb
## Data Transforming – 02_data_transformation.ipynb

Dopo la fase di pulizia (Notebook 01), i dati sono stati trasformati per includere nuove colonne utili all’analisi delle performance bancarie.  

### Colonne aggiunte
- **roa** = Return on Assets (`net_income / total_assets`)  
- **roe** = Return on Equity (`net_income / shareholder_equity`)  
- **cost_income_ratio** = Rapporto costi/ricavi (`operating_expenses / operating_income`)  
- **net_interest_margin** = Margine di interesse netto (`(interest_income - interest_expense) / average_earning_assets`)  
- **assets_growth** = Crescita percentuale giornaliera degli asset (`pct_change` su `total_assets`)  
- **income_growth** = Crescita percentuale giornaliera dell’utile netto (`pct_change` su `net_income`)  

### Gestione valori anomali
- Conversione di `inf` e `-inf` in `NaN`  
- Sostituzione dei `NaN` con `0` o interpolazione  
- Controllo e limitazione di valori fuori scala (outlier)  
- Salvataggio del dataset trasformato in:  

``` bash
  data/processed/dataset_transformed.csv
```