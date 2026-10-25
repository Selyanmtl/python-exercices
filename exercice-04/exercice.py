ventes = [
    {"produit": "café", "prix": 2.5, "quantite": 120},
    {"produit": "thé", "prix": 2.0, "quantite": 80},
    {"produit": "jus", "prix": 3.5, "quantite": 45},
]

ca_par_produit = {}
for vente in ventes:
    ca_par_produit[vente["produit"]] = vente["prix"] * vente["quantite"]

print(ca_par_produit)

ca_total = sum(ca_par_produit.values())
print(f"Total : {ca_total:.2f} euros")

meilleur_produit = max(ca_par_produit, key=ca_par_produit.get)
print(f"Meilleur produit : {meilleur_produit}")