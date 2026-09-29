
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construa um jogo da forca em Python para praticar strings, listas, laços de repetição, condicionais e entrada de dados. O jogo deve revelar as letras corretas e terminar quando o jogador vencer ou ficar sem tentativas.

## 📝 Tarefas

### 🛠️ Selecionar a palavra secreta e preparar a partida

#### Descrição
Crie uma lista de palavras e escolha uma delas aleatoriamente para iniciar cada partida.

#### Requisitos
O programa completo deve:

- Armazenar pelo menos 5 palavras em uma lista predefinida.
- Escolher aleatoriamente uma palavra da lista no início da partida.
- Exibir a palavra oculta por underscores, com um espaço entre cada posição, como `_ _ _ _ _`.
- Atualizar e exibir o progresso da palavra após cada palpite.

### 🛠️ Receber e validar os palpites

#### Descrição
Solicite letras ao jogador e atualize o estado do jogo de acordo com cada palpite.

#### Requisitos
O programa completo deve:

- Solicitar um palpite usando `input()` e aceitar apenas uma letra por vez.
- Comparar palpites sem diferenciar letras maiúsculas de minúsculas.
- Revelar todas as posições correspondentes quando a letra estiver na palavra secreta.
- Registrar as letras já tentadas e avisar quando o jogador repetir uma letra, sem descontar uma tentativa.
- Descontar uma tentativa quando a letra não estiver na palavra secreta.

### 🛠️ Encerrar a partida com vitória ou derrota

#### Descrição
Finalize a partida quando o jogador descobrir a palavra ou esgotar as tentativas disponíveis.

#### Requisitos
O programa completo deve:

- Encerrar a partida quando a palavra for completamente revelada.
- Encerrar a partida quando não restarem tentativas.
- Exibir uma mensagem de vitória quando o jogador descobrir a palavra.
- Em caso de derrota, exibir uma mensagem e revelar a palavra secreta.
