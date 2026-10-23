"""Testes básicos da calculadora usando apenas unittest."""

import unittest
from decimal import Decimal
from unittest.mock import patch

from calculadora import (
    dividir,
    formatar_numero,
    ler_numero,
    multiplicar,
    somar,
    subtrair,
)


class TestOperacoes(unittest.TestCase):
    def test_somar(self):
        self.assertEqual(somar(Decimal("2"), Decimal("3")), Decimal("5"))

    def test_subtrair(self):
        self.assertEqual(subtrair(Decimal("10"), Decimal("4")), Decimal("6"))

    def test_multiplicar(self):
        self.assertEqual(
            multiplicar(Decimal("2.5"), Decimal("4")),
            Decimal("10.0"),
        )

    def test_dividir(self):
        self.assertEqual(dividir(Decimal("9"), Decimal("3")), Decimal("3"))

    def test_dividir_por_zero_gera_erro(self):
        with self.assertRaises(ZeroDivisionError):
            dividir(Decimal("10"), Decimal("0"))

    def test_formatar_numero_remove_zeros_desnecessarios(self):
        self.assertEqual(formatar_numero(Decimal("12.500")), "12.5")

    def test_entrada_aceita_virgula_decimal(self):
        with patch("builtins.input", return_value="12,5"):
            self.assertEqual(ler_numero("Número: "), Decimal("12.5"))


if __name__ == "__main__":
    unittest.main()
