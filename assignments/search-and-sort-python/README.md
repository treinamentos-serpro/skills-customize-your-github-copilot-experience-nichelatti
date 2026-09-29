# 📘 Assignment: Busca e Ordenação em Python

## 🎯 Objective

Pratique o uso de listas, loops e funções implementando algoritmos simples de busca e ordenação em Python. Ao final, você conseguirá localizar valores e organizar uma lista sem usar bibliotecas externas.

## 📝 Tasks

### 🛠️ Implementar uma Busca Linear

#### Descrição

Complete a função `linear_search(numbers, target)` para procurar um número em uma lista. A função deve examinar os elementos na ordem em que aparecem e retornar o índice da primeira ocorrência encontrada.

#### Requisitos

O programa concluído deve:

- Retornar o índice do primeiro elemento igual a `target`
- Retornar `-1` quando o valor não estiver na lista
- Funcionar com listas vazias e listas que contenham valores repetidos

Exemplo:

```python
linear_search([12, 4, 9, 4], 4)  # Retorna 1
linear_search([12, 4, 9, 4], 7)  # Retorna -1
```

### 🛠️ Implementar uma Ordenação por Seleção

#### Descrição

Complete a função `selection_sort(numbers)` para ordenar uma lista de números em ordem crescente usando o algoritmo de ordenação por seleção. O algoritmo deve encontrar o menor elemento da parte ainda não ordenada e colocá-lo na posição correta.

#### Requisitos

O programa concluído deve:

- Retornar uma nova lista ordenada em ordem crescente
- Não usar `sort()` ou `sorted()`
- Preservar a lista original recebida como argumento
- Funcionar com listas vazias, números repetidos e números negativos

Exemplo:

```python
selection_sort([5, 2, 8, 1])  # Retorna [1, 2, 5, 8]
```

### 🛠️ Criar um Relatório de Resultados

#### Descrição

Use as duas funções para analisar a lista `scores` fornecida no arquivo inicial. Encontre a posição de uma nota informada pelo usuário e exiba a lista de notas em ordem crescente.

#### Requisitos

O programa concluído deve:

- Solicitar ao usuário uma nota para pesquisar
- Informar o índice retornado por `linear_search`
- Exibir as notas ordenadas usando `selection_sort`
- Continuar funcionando quando a nota pesquisada não for encontrada
