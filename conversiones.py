"""Conversiones de medidas - Práctica U4_9 Agentes en Jenkins."""

CM_POR_PULGADA = 2.54
METROS_POR_PIE = 0.3048
KM_POR_MILLA = 1.609344
LITROS_POR_GALON = 3.785411784
KG_POR_LIBRA = 0.45359237
GRAMOS_POR_ONZA = 28.349523125


# Longitud: cm <-> pulgadas
def cm_a_pulgadas(cm):
    return cm / CM_POR_PULGADA


def pulgadas_a_cm(pulgadas):
    return pulgadas * CM_POR_PULGADA


# Longitud: pies <-> metros
def pies_a_metros(pies):
    return pies * METROS_POR_PIE


def metros_a_pies(metros):
    return metros / METROS_POR_PIE


# Distancia: millas <-> km
def millas_a_km(millas):
    return millas * KM_POR_MILLA


def km_a_millas(km):
    return km / KM_POR_MILLA


# Volumen: galones <-> litros
def galones_a_litros(galones):
    return galones * LITROS_POR_GALON


def litros_a_galones(litros):
    return litros / LITROS_POR_GALON


# Masa: libras <-> kg
def libras_a_kg(libras):
    return libras * KG_POR_LIBRA


def kg_a_libras(kg):
    return kg / KG_POR_LIBRA


# --- Conversiones agregadas por el equipo ---

# Temperatura: Celsius <-> Fahrenheit
def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Masa: onzas <-> gramos
def onzas_a_gramos(onzas):
    return onzas * GRAMOS_POR_ONZA


def gramos_a_onzas(gramos):
    return gramos / GRAMOS_POR_ONZA


if __name__ == "__main__":
    print("=== Conversiones de medidas ===")
    print(f"10 cm        = {cm_a_pulgadas(10):.2f} pulgadas")
    print(f"10 pulgadas  = {pulgadas_a_cm(10):.2f} cm")
    print(f"10 pies      = {pies_a_metros(10):.2f} metros")
    print(f"10 metros    = {metros_a_pies(10):.2f} pies")
    print(f"10 millas    = {millas_a_km(10):.2f} km")
    print(f"10 km        = {km_a_millas(10):.2f} millas")
    print(f"10 galones   = {galones_a_litros(10):.2f} litros")
    print(f"10 litros    = {litros_a_galones(10):.2f} galones")
    print(f"10 libras    = {libras_a_kg(10):.2f} kg")
    print(f"10 kg        = {kg_a_libras(10):.2f} libras")
    print(f"10 °C        = {celsius_a_fahrenheit(10):.2f} °F")
    print(f"10 °F        = {fahrenheit_a_celsius(10):.2f} °C")
    print(f"10 onzas     = {onzas_a_gramos(10):.2f} gramos")
    print(f"10 gramos    = {gramos_a_onzas(10):.2f} onzas")
