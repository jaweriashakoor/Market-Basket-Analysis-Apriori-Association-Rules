import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# 1. Dataset
dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'Ice cream', 'Eggs']]

# 2. Encoding
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# 3. Apriori
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

# 4. Association Rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# --- DECIMAL TO PERCENT CONVERSION ---
# Hum columns ko 100 se multiply karke % sign add kar rahe hain readability ke liye
frequent_itemsets_pct = frequent_itemsets.copy()
frequent_itemsets_pct['support'] = (frequent_itemsets_pct['support'] * 100).astype(str) + '%'

rules_pct = rules[['antecedents', 'consequents', 'support', 'confidence']].copy()
rules_pct['support'] = (rules_pct['support'] * 100).astype(str) + '%'
rules_pct['confidence'] = (rules_pct['confidence'] * 100).astype(str) + '%'

# Print Results
print("--- Frequent Itemsets (Percent Form) ---")
print(frequent_itemsets_pct)
print("\n--- Association Rules (Percent Form) ---")
print(rules_pct)

# --- 5. VISUALIZATION ---
plt.figure(figsize=(10, 6))
plt.scatter(rules['support'], rules['confidence'], alpha=0.5, s=100, color='red')
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.title('Association Rules: Support vs Confidence')

# Har point ke saath uska text label add karna (Optional but helpful)
for i, txt in enumerate(rules.index):
    plt.annotate(f"Rule {txt}", (rules['support'][i], rules['confidence'][i]))

plt.grid(True, linestyle='--')
plt.show()