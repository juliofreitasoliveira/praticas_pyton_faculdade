# Calculadora de Média com Duas Notas

> Programa desenvolvido em Python para calcular a média de um aluno a partir de duas notas.

## 📌 Sobre o projeto

Este projeto foi desenvolvido com o objetivo de facilitar o cálculo da média de um aluno utilizando apenas duas informações: **a primeira nota e a segunda nota**.

O programa realiza a soma das duas notas e divide o resultado pela quantidade de notas informadas, apresentando a média final no terminal.

É um projeto simples, desenvolvido para praticar conceitos básicos da linguagem Python.

## ⚙️ Como funciona

O programa solicita ao usuário:

1. A primeira nota;
2. A segunda nota.

Em seguida, as duas notas são somadas e o resultado é dividido por `2`, obtendo a média.

```python
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2
```

Após o cálculo, o programa apresenta a média final e informa o status do aluno de acordo com a média obtida.

## 🛠️ Conceitos utilizados

Durante o desenvolvimento foram utilizados conceitos básicos de Python, como:

* `print()` — exibição de informações;
* `input()` — entrada de dados;
* `float()` — conversão das notas para números decimais;
* Variáveis — armazenamento das informações;
* Funções — organização do cálculo da média;
* `if`, `elif` e `else` — estruturas condicionais;
* Operadores aritméticos — realização do cálculo da média;
* F-strings — formatação do resultado.

## ▶️ Como executar

É necessário ter o **Python** instalado no computador.

No terminal, execute:

```bash
python nome_do_arquivo.py
```

Substitua `nome_do_arquivo.py` pelo nome do arquivo Python presente no projeto.

## 💻 Exemplo

```text
==Sistema de Notas do Aluno==

Digite a primeira nota: 8

Digite a segunda nota: 6

A media final é: 7.00

Status: Aprovado
```

## 📚 Objetivo de aprendizagem

Este projeto faz parte do processo de aprendizagem de programação e tem como foco a prática de:

* Entrada e saída de dados;
* Funções;
* Variáveis;
* Operações matemáticas;
* Estruturas condicionais.

## 🚀 Possíveis melhorias

Algumas melhorias que podem ser implementadas futuramente:

* Permitir o cálculo de mais de duas notas;
* Adicionar uma validação para notas inválidas;
* Permitir o cadastro de vários alunos;
* Criar uma interface gráfica;
* Armazenar os resultados.

## 👨‍💻 Autor

**Julio**

Estudante de Ciência da Computação.

🔗 [LinkedIn](https://www.linkedin.com/in/juliof-tech/)
