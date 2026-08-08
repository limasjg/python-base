# Python Base

Coleção de anotações, exemplos e pequenos projetos para estudo de Python.

O repositório está organizado em dois grupos principais:

- `notes/`: exemplos isolados de sintaxe, estruturas de dados, funções, orientação a objetos, arquivos, exceções e recursos da biblioteca padrão;
- `projects/`: programas de linha de comando e interfaces gráficas simples para praticar os conceitos.

## Requisitos

- Python 3
- Dependências opcionais conforme o exemplo executado

A maior parte dos scripts usa apenas a biblioteca padrão. Alguns exemplos de interface gráfica usam Tkinter, normalmente distribuído junto com o Python.

## Como executar

Clone o repositório e execute um arquivo individual:

```bash
git clone https://github.com/limasjg/python-base.git
cd python-base
python projects/calculator.py
```

No Windows, se necessário:

```powershell
py projects\calculator.py
```

## Conteúdos estudados

A pasta `notes/` abrange, entre outros:

- Variáveis, strings, operadores e conversão de tipos;
- Condicionais, laços, listas, dicionários e compreensões;
- Funções, argumentos posicionais e arbitrários, escopo e decoradores;
- Módulos, datas, matemática, coleções e aleatoriedade;
- Tratamento de exceções e leitura/escrita de arquivos;
- Classes, herança, polimorfismo, propriedades, métodos estáticos e mágicos;
- Interfaces gráficas com Tkinter;
- Requisições HTTP, manipulação de JSON e multithreading.

## Projetos de prática

Alguns dos programas disponíveis em `projects/`:

| Arquivo | Exercício |
| --- | --- |
| `calculator.py` | Calculadora no terminal. |
| `guessing_game.py` | Jogo de adivinhação. |
| `hangman.py` | Jogo da forca. |
| `jokenpo.py` | Jogo de pedra, papel e tesoura. |
| `dice_game.py` | Jogo de dados. |
| `banking.py` | Simulação simples de operações bancárias. |
| `shopping-car.py` e `shopping-car-v2.py` | Exercícios de carrinho de compras. |
| `digital-clock.py`, `stopwatch.py` e `alarm-clock.py` | Relógio, cronômetro e alarme. |
| `gui-weather.py` | Aplicação gráfica de clima; requer configuração de acesso à API usada pelo script. |
| `download-organizator.py` | Organizador de arquivos baixados. |

## Observações

- Os arquivos são exercícios independentes; não há uma aplicação única a ser executada.
- Alguns scripts interagem com arquivos locais, rede ou interface gráfica. Leia o código antes de executá-los e ajuste caminhos, chaves e valores de exemplo.
- Este repositório ainda não possui uma licença definida.
