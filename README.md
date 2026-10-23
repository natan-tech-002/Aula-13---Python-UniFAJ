# Aula 13 — Python UniFAJ

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em%20desenvolvimento-0F766E?style=for-the-badge)

Repositório de práticas acadêmicas da disciplina de Introdução à Programação — UniFAJ. O objetivo é consolidar a lógica de programação por meio de exercícios pequenos e executáveis.

## 🧮 Projeto em destaque: Calculadora

A pasta [**Exercicio_Calculadora**](https://github.com/natan-tech-002/Aula-13---Python-UniFAJ/tree/main/Exercicio_Calculadora) contém uma calculadora de terminal para operações matemáticas básicas.

**O que ela faz:**
- Soma, subtrai, multiplica e divide.
- Aceita números decimais com vírgula ou ponto.
- Valida entradas e trata divisão por zero.
- Inclui testes automatizados para as operações e casos importantes.
- Usa apenas a biblioteca padrão do Python.

### ▶️ Executar

Com Python 3.10 ou superior instalado, rode a partir da raiz do repositório:

```bash
python Exercicio_Calculadora/calculadora.py
```

No Windows, também pode funcionar com:

```powershell
py Exercicio_Calculadora/calculadora.py
```

### 🧪 Executar os testes

```bash
python -m unittest discover -s Exercicio_Calculadora -p "test_*.py"
```

Os testes usam o `unittest` que já vem com Python. Não é necessário instalar dependências extras.

Confira o [guia da calculadora](https://github.com/natan-tech-002/Aula-13---Python-UniFAJ/blob/main/Exercicio_Calculadora/README.md) para ver os detalhes e um exemplo de uso.

## 📁 Estrutura

```text
Aula-13---Python-UniFAJ/
├── Exercicio_Calculadora/
│   ├── calculadora.py
│   ├── test_calculadora.py
│   └── README.md
├── teste.py
└── README.md
```

O arquivo `teste.py` é mantido como parte dos materiais já existentes do repositório.

## 🎯 Objetivos de aprendizagem

- Praticar funções, condicionais e estruturas de repetição.
- Ler e validar valores informados pelo usuário.
- Organizar um programa em partes menores.
- Documentar como executar o código.
- Verificar resultados com testes automatizados.

Este repositório está em evolução conforme os estudos avançam.
