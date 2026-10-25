from outils import convertir_note, mention, moyenne

notes_brutes = ["12,5", "15", "abc", "9", "18,25"]

notes_valides = []
nb_ignorees = 0

for texte in notes_brutes:
    note = convertir_note(texte)
    if note is None:
        nb_ignorees += 1
    else:
        notes_valides.append(note)

moyenne_notes = moyenne(notes_valides)

print(f"Notes ignorées : {nb_ignorees}")
print(f"Moyenne : {moyenne_notes:.2f}")
print(f"Mention : {mention(moyenne_notes)}")
