import pandas as pd
import numpy as np

# 1. Carica i dati
dati = pd.read_csv("Dati/Tabella.csv")

Ta = 77
Tf = 293


dati_filtrati = dati[(dati["T"] >= Ta) & (dati["T"] <= Tf)]


T_filtrato = dati_filtrati["T"].values
C_grafite_filtrato = dati_filtrati["C"].values
C_piombo_filtrato = dati_filtrati["Pb"].values

# 4. Calcola l'integrale (l'area totale sotto la curva) con np.trapz
integrale_grafite = np.trapezoid(C_grafite_filtrato, T_filtrato)
integrale_piombo = np.trapezoid(C_piombo_filtrato, T_filtrato)

# 5. Calcola il calore specifico medio dividendo per il delta T totale
cp_medio_grafite = integrale_grafite / (Tf - Ta)    
cp_medio_piombo = integrale_piombo / (Tf - Ta)

print(f"Calore specifico medio Grafite (np.trapz): {cp_medio_grafite:.4f}")
print(f"Calore specifico medio Piombo (np.trapz): {cp_medio_piombo:.4f}")


###CALCOLO VALORI MEDI I VALORI DEI CALORI A 77 E 293 SONO CALCOLATI PER INTERPOLAZIONE LINEARE