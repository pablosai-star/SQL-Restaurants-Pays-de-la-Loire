# 🍽️ Analyse SQL — Restaurants Pays de la Loire

Exploration de l'offre touristique restauration en Pays de la Loire
à partir des données publiques de Nantes Métropole.

## 🎯 Objectif

Analyser la répartition et les caractéristiques des restaurants
touristiques en Pays de la Loire via des requêtes SQL avancées.

## 📦 Dataset

- **Source** : [Nantes Métropole Open Data](https://data.nantesmetropole.fr)
- **Volume** : 3 359 restaurants, 49 variables
- **Couverture** : Loire-Atlantique, Maine-et-Loire, Sarthe, Mayenne

## 🛠️ Stack

- **Python** : Pandas, SQLite3
- **SQL** : SQLite (window functions, CTEs, agrégations)
- **Environnement** : Jupyter Notebook, VS Code

## 📁 Structure du repo

├── offre_touristique_paysdelaloire.ipynb  # Notebook principal
├── offre-touristique-restaurants.csv      # Dataset
└── README.md

## 📊 Requêtes SQL couvertes

- `COUNT + GROUP BY` — répartition des restaurants par département
- `TOP 10 + WHERE + LIMIT` — communes les plus actives
- `RANK() OVER PARTITION BY` — rang des communes par département
- `CTE + RANK()` — top 3 catégories par département
- `NTILE()` — classement des communes en quartiles
- `LAG()` — écart entre communes consécutives

## 🔍 Key Insights

- **Loire-Atlantique** concentre 46% des restaurants (1 547 sur 3 359)
- **Saint-Nazaire devant Nantes** en Loire-Atlantique — effet tourisme
  côtier sur le dataset
- **Cuisine traditionnelle** domine dans les 4 départements
- **Maine-et-Loire** se distingue avec la gastronomie en #2 — effet
  vignoble Anjou
- **Mayenne** profil plus rural — bistrot/bar à vin en #2