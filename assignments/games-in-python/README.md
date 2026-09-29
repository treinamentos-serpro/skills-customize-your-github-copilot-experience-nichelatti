
# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Construir um jogo da forca em Python para praticar o uso de strings, laços de repetição, condicionais e entrada de dados do usuário, enquanto desenvolve lógica de jogo interativa e dinâmica.

## 📝 Tarefas

### 🛠️ Seleção da Palavra e Estado Inicial

#### Descrição
Crie uma lista de palavras e escolha uma delas aleatoriamente para iniciar a partida.

#### Requisitos
O programa completo deve:

- Armazenar pelo menos 5 palavras em uma lista predefinida.
- Escolher uma palavra aleatória para cada nova partida.
- Iniciar o jogo com a palavra oculta representada por underscores, como `_ _ _ _ _`.
- Exibir ao usuário o progresso atual da palavra em cada tentativa.

### 🛠️ Entrada do Usuário e Validação de Letras

#### Descrição
Permita que o jogador insira letras e atualize o estado do jogo conforme os palpites informados.

#### Requisitos
O programa completo deve:

- Solicitar uma letra do usuário com `input()`.
- Verificar se a letra pertence à palavra secreta.
- Revelar a letra na posição correta quando houver acerto.
- Manter o registro das letras já tentadas para evitar repetição.
- Reduzir o número de tentativas restantes quando o palpite for incorreto.

### 🛠️ Condição de Vitória e Derrota

#### Descrição
Finalize a partida corretamente quando o jogador vencer ou esgotar as tentativas.

#### Requisitos
O programa completo deve:

- Encerrar a partida quando a palavra for completamente revelada.
- Encerrar a partida quando o número de tentativas acabar.
- Exibir uma mensagem de vitória caso o jogador adivinhe a palavra.
- Exibir uma mensagem de derrota e mostrar a palavra correta ao final.

### 🧠 Habilidades Praticadas

- Manipulação de strings
- Loops e controle de fluxo
- Condicionais
- Seleção aleatória
- Interação com o usuário via entrada e saída