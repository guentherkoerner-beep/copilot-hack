"""Beispiel-Bibliothek

Enthält eine kleine Funktion, die als Ausgangspunkt dienen kann.
"""

def hallo(name: str) -> str:
    """Gibt eine Begrüßung zurück."""
    return f"Hallo, {name}!"


if __name__ == '__main__':
    print(hallo('Welt'))
