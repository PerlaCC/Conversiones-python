"""Pruebas unitarias de conversiones.py (una o más por cada método)."""
import pytest
import conversiones as c


def test_cm_a_pulgadas():
    assert c.cm_a_pulgadas(2.54) == pytest.approx(1)
    assert c.cm_a_pulgadas(100) == pytest.approx(39.3701, rel=1e-4)


def test_pulgadas_a_cm():
    assert c.pulgadas_a_cm(1) == pytest.approx(2.54)
    assert c.pulgadas_a_cm(12) == pytest.approx(30.48)


def test_pies_a_metros():
    assert c.pies_a_metros(1) == pytest.approx(0.3048)
    assert c.pies_a_metros(10) == pytest.approx(3.048)


def test_metros_a_pies():
    assert c.metros_a_pies(0.3048) == pytest.approx(1)
    assert c.metros_a_pies(1) == pytest.approx(3.28084, rel=1e-5)


def test_millas_a_km():
    assert c.millas_a_km(1) == pytest.approx(1.609344)
    assert c.millas_a_km(10) == pytest.approx(16.09344)


def test_km_a_millas():
    assert c.km_a_millas(1.609344) == pytest.approx(1)
    assert c.km_a_millas(100) == pytest.approx(62.1371, rel=1e-5)


def test_galones_a_litros():
    assert c.galones_a_litros(1) == pytest.approx(3.785411784)
    assert c.galones_a_litros(5) == pytest.approx(18.92705892)


def test_litros_a_galones():
    assert c.litros_a_galones(3.785411784) == pytest.approx(1)
    assert c.litros_a_galones(10) == pytest.approx(2.64172, rel=1e-5)


def test_libras_a_kg():
    assert c.libras_a_kg(1) == pytest.approx(0.45359237)
    assert c.libras_a_kg(100) == pytest.approx(45.359237)


def test_kg_a_libras():
    assert c.kg_a_libras(0.45359237) == pytest.approx(1)
    assert c.kg_a_libras(1) == pytest.approx(2.20462, rel=1e-5)


def test_cero_en_todas():
    for f in (c.cm_a_pulgadas, c.pulgadas_a_cm, c.pies_a_metros,
              c.metros_a_pies, c.millas_a_km, c.km_a_millas,
              c.galones_a_litros, c.litros_a_galones,
              c.libras_a_kg, c.kg_a_libras):
        assert f(0) == 0
