"""Conversiones de medidas - Práctica U4_9 Agentes en Jenkins."""

CM_POR_PULGADA = 2.54
METROS_POR_PIE = 0.3048
KM_POR_MILLA = 1.609344
LITROS_POR_GALON = 3.785411784
KG_POR_LIBRA = 0.45359237
GRAMOS_POR_ONZA = 28.349523125


# 1. Longitud: cm -> pulgadas
def cm_a_pulgadas(cm):
    return cm / CM_POR_PULGADA


# 2. Longitud: pies -> metros
def pies_a_metros(pies):
    return pies * METROS_POR_PIE


# 3. Distancia: millas -> km
def millas_a_km(millas):
    return millas * KM_POR_MILLA


# 4. Volumen: galones -> litros
def galones_a_litros(galones):
    return galones * LITROS_POR_GALON


# 5. Masa: libras -> kg
def libras_a_kg(libras):
    return libras * KG_POR_LIBRA


# --- Conversiones agregadas por el equipo ---

# 6. Temperatura: Celsius -> Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# 7. Masa: onzas -> gramos
def onzas_a_gramos(onzas):
    return onzas * GRAMOS_POR_ONZA


if __name__ == "__main__":
    print("=== Conversiones de medidas ===")
    print(f"1. 10 cm      = {cm_a_pulgadas(10):.2f} pulgadas")
    print(f"2. 10 pies    = {pies_a_metros(10):.2f} metros")
    print(f"3. 10 millas  = {millas_a_km(10):.2f} km")
    print(f"4. 10 galones = {galones_a_litros(10):.2f} litros")
    print(f"5. 10 libras  = {libras_a_kg(10):.2f} kg")
    print(f"6. 10 °C      = {celsius_a_fahrenheit(10):.2f} °F")
    print(f"7. 10 onzas   = {onzas_a_gramos(10):.2f} gramos")
