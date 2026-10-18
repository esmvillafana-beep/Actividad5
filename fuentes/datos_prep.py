"""Preparación reproducible de comentarios sintéticos (Actividad 5)."""
from pathlib import Path
import unicodedata
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
ORIGEN = RAIZ / "datos" / "datos_ini" / "comentarios_originales_v1.csv"
DESTINO = RAIZ / "datos" / "datos_limp" / "comentarios_limpios_v1.csv"

def limpiar_texto(valor: str) -> str:
    # No eliminar acentos ni signos: pueden aportar señal semántica al PLN.
    texto = unicodedata.normalize("NFC", str(valor))
    return " ".join(texto.strip().split())

def preparar(origen=ORIGEN, destino=DESTINO):
    df = pd.read_csv(origen, encoding="utf-8-sig")
    if not {"texto", "etiqueta_real"}.issubset(df.columns):
        raise ValueError("El CSV debe incluir texto y etiqueta_real")
    inicial = len(df)
    df = df[["texto", "etiqueta_real"]].dropna().copy()
    df["texto"] = df["texto"].map(limpiar_texto)
    df["etiqueta_real"] = df["etiqueta_real"].astype(str).str.strip().str.upper()
    df = df[df["texto"].ne("")]
    no_validas = set(df["etiqueta_real"]) - {"POS", "NEG", "NEU"}
    if no_validas:
        raise ValueError(f"Etiquetas no validas: {sorted(no_validas)}")
    df = df.drop_duplicates(subset=["texto", "etiqueta_real"]).reset_index(drop=True)
    destino = Path(destino)
    destino.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(destino, index=False, encoding="utf-8-sig")
    print(f"Registros originales: {inicial}; registros limpios: {len(df)}")
    print(f"Eliminados por nulos, vacíos o duplicados: {inicial - len(df)}")
    print("Distribución:", df["etiqueta_real"].value_counts().to_dict())
    print("Archivo:", destino)
    return df

if __name__ == "__main__":
    preparar()
