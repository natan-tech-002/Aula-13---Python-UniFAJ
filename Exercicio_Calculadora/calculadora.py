"""Calculadora de terminal para praticar operações básicas com Python."""

from decimal import Decimal, InvalidOperation
from typing import Callable

Operacao = Callable[[Decimal, Decimal], Decimal]


def somar(a: Decimal, b: Decimal) -> Decimal:
    return a + b


def subtrair(a: Decimal, b: Decimal) -> Decimal:
    return a - b


def multiplicar(a: Decimal, b: Decimal) -> Decimal:
    return a * b


def dividir(a: Decimal, b: Decimal) -> Decimal:
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


OPERACOES: dict[str, tuple[str, Operacao]] = {
    "1": ("Adição (+)", somar),
    "2": ("Subtração (-)", subtrair),
    "3": ("Multiplicação (*)", multiplicar),
    "4": ("Divisão (/)", dividir),
}


def ler_numero(mensagem: str) -> Decimal:
    """Lê um decimal e aceita tanto vírgula quanto ponto."""
    while True:
        entrada = input(mensagem).strip().replace(",", ".")
        try:
            numero = Decimal(entrada)
        except InvalidOperation:
            print("Entrada inválida. Digite um número, por exemplo: 12,5.")
            continue

        if not numero.is_finite():
            print("Digite um número finito.")
            continue

        return numero


def formatar_numero(numero: Decimal) -> str:
    """Evita zeros decimais desnecessários na exibição."""
    return format(numero.normalize(), "f")


def main() -> None:
    print("=" * 42)
    print("          CALCULADORA PYTHON")
    print("=" * 42)

    while True:
        print("\nEscolha uma operação:")
        for opcao, (nome, _) in OPERACOES.items():
            print(f"  {opcao} - {nome}")
        print("  0 - Sair")

        escolha = input("Opção: ").strip()

        if escolha == "0":
            print("Até mais! Obrigado por usar a calculadora.")
            break

        if escolha not in OPERACOES:
            print("Opção inválida. Escolha de 0 a 4.")
            continue

        nome, funcao = OPERACOES[escolha]
        primeiro = ler_numero("Digite o primeiro número: ")
        segundo = ler_numero("Digite o segundo número: ")

        try:
            resultado = funcao(primeiro, segundo)
        except ZeroDivisionError as erro:
            print(f"Erro: {erro}")
            continue

        print(f"\n{nome}: {formatar_numero(primeiro)} e "
              f"{formatar_numero(segundo)}")
        print(f"Resultado: {formatar_numero(resultado)}")


if __name__ == "__main__":
    main()
