"""Pruebas unitarias de conversiones.py (una por cada método)."""
import pytest
import conversiones as c


def test_cm_a_pulgadas():
    assert c.cm_a_pulgadas(2.54) == pytest.approx(1)
    assert c.cm_a_pulgadas(100) == pytest.approx(39.3701, rel=1e-4)


def test_pies_a_metros():
    assert c.pies_a_metros(1) == pytest.approx(0.3048)
    assert c.pies_a_metros(10) == pytest.approx(3.048)


def test_millas_a_km():
    assert c.millas_a_km(1) == pytest.approx(1.609344)
    assert c.millas_a_km(10) == pytest.approx(16.09344)


def test_galones_a_litros():
    assert c.galones_a_litros(1) == pytest.approx(3.785411784)
    assert c.galones_a_litros(5) == pytest.approx(18.92705892)


def test_libras_a_kg():
    assert c.libras_a_kg(1) == pytest.approx(0.45359237)
    assert c.libras_a_kg(100) == pytest.approx(45.359237)


def test_celsius_a_fahrenheit():
    assert c.celsius_a_fahrenheit(0) == pytest.approx(32)
    assert c.celsius_a_fahrenheit(100) == pytest.approx(212)


def test_onzas_a_gramos():
    assert c.onzas_a_gramos(1) == pytest.approx(28.349523125)
    assert c.onzas_a_gramos(16) == pytest.approx(453.59237)
