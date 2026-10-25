import math


def convertir_note(texte):
    """Convertit "12,5" en 12.5. Renvoie None si le texte n'est pas une note valide."""
    try:
        note = float(texte.replace(",", "."))
    except (ValueError, AttributeError):
        return None

    if not math.isfinite(note):
        return None
    return note


def moyenne(valeurs):
    return sum(valeurs) / len(valeurs)


def mention(note):
    if note >= 16:
        return "Très bien"
    elif note >= 14:
        return "Bien"
    elif note >= 12:
        return "Assez bien"
    else:
        return "Aucune"