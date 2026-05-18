<div align="center">

# <span style="color:#ef4444">Market Basket Analysis (Apriori & Association Rules)</span>

![Python](https://img.shields.io/badge/Python-3.10%2B-1e293b?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Dataframe-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Mlxtend](https://img.shields.io/badge/Mlxtend-Machine_Learning-41b883?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-059669?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-ef4444?style=for-the-badge)

<br/>

<h3>
  <em>"Uncovering Hidden Consumer Purchase Patterns Using Unsupervised Data Mining"</em><br/>
</h3>

<br/>

[📌 Overview](#-overview) • [✨ Features](#-features) • [🚀 Pipeline Flow](#-pipeline-flow) • [⚙️ Installation](#%EF%B8%8F-installation) • [📊 Data Dictionary](#-transactional-dataset-dictionary) • [🧠 Technical Deep Dive](#-technical-deep-dive) • [🤝 Contributing](#-contributing)

</div>

---

## 📌 Overview

**Market Basket Analysis** is a data-mining and affinity-analysis project focused on identifying strong relationships between products in consumer transaction histories. Using the **Apriori Algorithm** alongside statistical metrics for generating **Association Rules**, this system processes transactional groupings to discover items that are frequently bought together. 

The engine converts complex decimal probabilities into clean, localized percentages and creates a dual-metric scatter dashboard. This gives retail analysts mathematical confirmation on item bundling, shelf placement, and promotional strategies.

---

## ✨ Features

### 🎯 Core Capabilities
| Feature | Description |
|---|---|
| 🛒 **Transaction Matrix Encoding** | Converts arbitrary categorical purchase matrices into dense, machine-readable binary Boolean truth tables. |
| 🔍 **Apriori Support Pruning** | Prunes infrequent itemsets using parameterized item frequency controls (`min_support=0.6`). |
| 📈 **Association Constraints** | Computes antecedent-to-consequent metrics using threshold bounds (`min_threshold=0.7`). |
| 🧮 **Percent Transformation Engine**| Formats decimal values into readable percentage representations (`80.0%`) for easy reporting. |
| 📊 **Relationship Visualization** | Generates an annotated scatter dashboard mapping rule support against overall confidence. |

### 🌟 Design Highlights
- 🧠 **Unsupervised Mining Architecture** — Uncovers organic purchasing behavior without needing target labels.
- 💬 **Code Commentary Integration** — Includes clear bilingual (Hinglish/Urdu) comments to make data transformation steps easy to follow.
- 🎨 **Point Annotation Maps** — Pairs interactive scatter points directly with their mathematical lookup indices.

---

## 🚀 Pipeline Flow

┌─────────────────────────────────────────────────────────┐│                RAW TRANSACTION MATRIX INPUT             ││          (Multi-Item Lists Tracking Store Baskets)       │└─────────────────────────────────────────────────────────┘│▼[ TransactionEncoder Fit & Transform ]│▼[ Binary Boolean Feature DataFrame Mapping ]│▼┌───────────────────────────────────────────────────────┐│               APRIORI ALGORITHM MINING                ││    Prune Infrequent Itemsets via Minimum Support Score │└───────────────────────────┬───────────────────────────┘│▼┌───────────────────────────────────────────────────────┐│              ASSOCIATION RULE EXTRACTION              ││    Evaluate Metric Thresholds (Support & Confidence)   │└───────────────────────────┬───────────────────────────┘│▼[ Percentage Conversions Parser ]│▼┌─────────────────────────────────────────────────────────┐│              ANALYTICS & VISUALIZATION                  ││                                                         ││   Render: Terminal Performance Summary DataFrames       ││   Metric: Matplotlib Support vs Confidence Scatter     ││   Labels: Dynamic Anchor Identifiers (Rule 0, 1...)     │└─────────────────────────────────────────────────────────┘
---

## ⚙️ Installation

### Prerequisites

Ensure you have the following software ready on your local system:
- Python 3.10+
- Git

---

### 🔧 Step-by-Step Setup

**1. Clone the Repository**
```bash
git clone [https://github.com/jaweriashakoor/Market-Basket-Analysis-Apriori-Association-Rules.git](https://github.com/jaweriashakoor/Market-Basket-Analysis-Apriori-Association-Rules.git)
cd Market-Basket-Analysis-Apriori-Association-Rules
2. Create a Virtual EnvironmentBashpython -m venv myenv

# Windows (PowerShell)
.\myenv\Scripts\Activate.ps1

# Linux / macOS
source myenv/bin/activate
3. Install DependenciesBashpip install pandas matplotlib mlxtend
4. Execute the Script PipelineBashpython apriori.py
📊 Transactional Dataset DictionaryThe pipeline processes a custom multi-basket retail sample to model real-world grocery dependencies:  Transaction IDItems Contained in BasketT1Milk, Onion, Nutmeg, Kidney Beans, Eggs, YogurtT2Dill, Onion, Nutmeg, Kidney Beans, Eggs, YogurtT3Milk, Apple, Kidney Beans, EggsT4Milk, Unicorn, Corn, Kidney Beans, YogurtT5Corn, Onion, Onion, Kidney Beans, Ice cream, Eggs🧠 Technical Deep DiveRule Generation Evaluation MatrixThe data framework relies on two critical statistical equations to score the strength of its transactional relationships:Support Metrics: Determines how frequently an itemset appears across the whole dataset:$$Support(A \rightarrow B) = \frac{\text{Transactions containing } A \text{ and } B}{\text{Total Transactions}}$$Confidence Metrics: Measures how often the items in $B$ are bought given that item $A$ is already in the basket:$$Confidence(A \rightarrow B) = \frac{Support(A \cup B)}{Support(A)}$$If a generated rule falls below min_support=0.6 or min_threshold=0.7, the system automatically filters it out. This ensures that retail decisions are built only on reliable, high-volume buying patterns.🤝 ContributingContributions are welcome and appreciated! Here's how you can submit updates:Bash# 1. Fork the Project Repository
# 2. Setup your feature branch
git checkout -b feature/enhanced-rule-metrics

# 3. Commit changes
git commit -m "Add: Added Lift and Conviction metric columns"

# 4. Push branch updates
git push origin feature/enhanced-rule-metrics

# 5. Open a Pull Request
📄 LicenseThis project is open-source software licensed under the MIT License.
