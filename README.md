# 🏠 California Housing — Prédiction des Prix Immobiliers

Comparaison de modèles de Machine Learning pour prédire les prix
immobiliers en Californie à partir du dataset sklearn.

## 🎯 Objectif

Construire et comparer plusieurs modèles de régression pour prédire
le prix médian des logements par district en Californie, et identifier
le modèle le plus performant via GridSearchCV.

## 📦 Dataset

- **Source** : Scikit-learn (fetch_california_housing)
- **Volume** : 20 640 districts, 8 variables
- **Cible** : Prix médian des logements (en centaines de milliers $)

## 🛠️ Stack

- **Python** : Pandas, Scikit-learn, XGBoost
- **Machine Learning** : Régression Linéaire, Random Forest,
  XGBoost, KNN
- **Optimisation** : GridSearchCV + Cross-validation 5 folds
- **Environnement** : Jupyter Notebook, VS Code

## 📁 Structure du repo

├── ML_california_housing1.ipynb  # Notebook principal
├── model_california.pkl          # Modèle XGBoost sauvegardé
└── README.md

## 🤖 Comparaison des Modèles (Cross-validation 5 folds)

| Modèle | R² moyen | Écart-type |
|--------|----------|------------|
| Régression Linéaire | 0.61 | ± 0.05 |
| Random Forest | 0.65 | ± 0.09 |
| XGBoost | 0.65 | ± 0.04 |
| KNN | 0.59 | ± 0.06 |

## 🏆 Modèle Final — XGBoost optimisé

- **Meilleurs paramètres** : learning_rate=0.1, max_depth=3,
  n_estimators=300
- **Meilleur R² CV** : 0.69
- **RMSE final** : 0.49
- **R² final** : 0.82

## 🔍 Key Insights

- XGBoost légèrement meilleur que Random Forest avec un écart-type
  plus faible (0.04 vs 0.09) — plus stable en production
- GridSearchCV améliore le R² de 0.65 → 0.82 après optimisation
- KNN moins adapté aux données géographiques de ce dataset