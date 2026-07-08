#Charger et explorer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger
df = pd.read_csv("data.csv")

# Explorer
print(df.shape)
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Étape 2 — Nettoyer
# Supprimer ou remplir les valeurs manquantes
df = df.dropna()  # ou df.fillna(...)

# Supprimer les doublons
df = df.drop_duplicates()

# Gérer les outliers si nécessaire

Scores : [0.51857219 0.70523043 0.74248174 0.63227819 0.68205721]
Moyenne : 0.66
Écart-type : 0.08Intéressant ! 🎯
Ce que ça nous dit :
Les scores varient beaucoup selon le découpage :

Minimum : 0.51
Maximum : 0.74
Moyenne : 0.66
Écart-type : 0.08


Pourquoi la moyenne est 0.66 ici alors qu'on avait 0.81 avant ?
Avant on testait sur 20% des données choisies aléatoirement — on avait eu de la chance avec ce découpage !
Ici on teste sur 100% des données en 5 fois — c'est beaucoup plus représentatif de la vraie performance du modèle.

💡 C'est pour ça que la cross-validation est essentielle avant de déployer un modèle en production — elle évite de se faire avoir par un bon découpage chanceux !


Tableau final complet et honnête :
ModèleRMSER² (test simple)R² (cross-val)KNN sans normalisation1.060.15-Régression linéaire0.750.58-KNN avec normalisation0.660.67-Random Forest0.510.810.66XGBoost0.460.84-
On s'arrête là sur le ML ou tu veux tester la cross-validation sur XGBoost aussi ? 😄on fait aussi sur xgboost. Mais avant, pourquoi ne pas commencer par une cross validation et se baser dessus?Excellente question ! 🎯
Tu as tout à fait raison — en pratique, un bon workflow ML c'est :
1. Charger et explorer les données
2. Préparer (X, y)
3. Cross-validation pour comparer les modèles
4. GridSearchCV sur le meilleur modèle
5. Évaluation finale sur le test set
Le train/test split simple qu'on a fait d'abord c'est bien pour apprendre et comprendre rapidement — mais en vrai projet, on commence directement par la cross-validation pour avoir des scores fiables dès le départ.

💡 Le train/test simple c'est comme noter un élève sur un seul examen — la cross-validation c'est comme le noter sur 5 examens différents et faire la moyenne. Beaucoup plus juste !


On teste la cross-validation sur XGBoost :
pythonscores_xgb = cross_val_score(
    XGBRegressor(n_estimators=100, random_state=42),
    X, y, cv=5, scoring="r2"
)

print(f"Scores XGBoost : {scores_xgb}")
print(f"Moyenne : {scores_xgb.mean():.2f}")
print(f"Écart-type : {scores_xgb.std():.2f}")
Lance — ça devrait être plus rapide que Random Forest ! ⏳Scores XGBoost : [0.54932537 0.70386605 0.72793222 0.66010998 0.64280305]
Moyenne : 0.66
Écart-type : 0.06Intéressant ! Les deux modèles sont à égalité en cross-validation :
ModèleR² cross-valÉcart-typeRandom Forest0.660.08XGBoost0.660.06
XGBoost a un écart-type légèrement plus faible (0.06 vs 0.08) — ça veut dire qu'il est plus stable et régulier sur les différents découpages. C'est un avantage !

Ce qu'on retient de tout ce projet ML :

Le R² de 0.84 qu'on avait avec XGBoost était un peu optimiste — la vraie performance c'est 0.66
XGBoost et Random Forest sont équivalents sur ce dataset
La cross-validation donne une image honnête du modèle


On a fait le tour du ML de base ! 🚀
Ce qu'on pourrait encore explorer :

GridSearchCV sur XGBoost pour optimiser ses paramètres
Feature engineering — créer de nouvelles colonnes pour améliorer le score
Classification — prédire une catégorie au lieu d'un nombre

On continue ou on s'arrête là sur le ML ? 😄on va continuer mais avant je veux un processus complet, étapes par étapes, avec la cross-validation pour avoir des scores fiables dès le départ pour un projet en production🚀 Workflow ML complet en production
Voilà le processus standard, étape par étape :

Étape 1 — Charger et explorer
pythonimport pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger
df = pd.read_csv("data.csv")

# Explorer
print(df.shape)
print(df.head())
print(df.describe())
print(df.isnull().sum())

Étape 2 — Nettoyer
python# Supprimer ou remplir les valeurs manquantes
df = df.dropna()  # ou df.fillna(...)

# Supprimer les doublons
df = df.drop_duplicates()

# Gérer les outliers si nécessaire

#Étape 3 — Préparer X et y
X = df.drop(columns=["target"])
y = df["target"]

#Étape 4 — Comparer les modèles avec cross-validation
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

modeles = {
    "Régression linéaire": LinearRegression(),
    "Random Forest": RandomForestRegressor(random_state=42),
    "XGBoost": XGBRegressor(random_state=42),
    "KNN": Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsRegressor())
    ])
}

for nom, modele in modeles.items():
    scores = cross_val_score(modele, X, y, cv=5, scoring="r2")
    print(f"{nom} → R² moyen : {scores.mean():.2f} | Écart-type : {scores.std():.2f}")
    
#Étape 5 — Optimiser le meilleur modèle avec GridSearchCV
from sklearn.model_selection import GridSearchCV

param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [5, 10, None],
    "min_samples_split": [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestRegressor(random_state=42),
    param_grid,
    cv=5,
    scoring="r2",
    n_jobs=-1  # utilise tous les CPU disponibles → plus rapide !
)

grid_search.fit(X, y)
print(f"Meilleurs paramètres : {grid_search.best_params_}")
print(f"Meilleur R² : {grid_search.best_score_:.2f}")

#Étape 6 — Évaluation finale sur le test set
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Découper en train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entraîner le meilleur modèle
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# Évaluer
y_pred = best_model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"RMSE final : {rmse:.2f}")
print(f"R² final : {r2:.2f}")

#Étape 7 — Sauvegarder le modèle
import joblib

joblib.dump(best_model, "model.pkl")

# Pour recharger plus tard
model = joblib.load("model.pkl")