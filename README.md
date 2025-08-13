

# Sobre o projeto e equipe 💻

Somos uma equipe mista de discentes de Inteligência Artificial e Ciência da Computação da Universidade Federal de Pernambuco. Este repositório contém a atividade final da disciplina "Introdução à Programação", oferecida a todos os alunos do primeiro período do Centro de Informática.
O projeto de Introdução à Programação consiste em criar um sistema interativo em 2D. Nele, o usuário controla um objeto para coletar outros itens espalhados pela tela. Tudo o que for coletado será registrado e exibido na tela. O projeto utiliza Python e segue os conceitos de Programação Orientada a Objetos.

----- membros ---

Anysabele de Paula Barbosa Santos
- Cursando Inteligência Artificial

Maria Luiza Cunha de Barros
- Cursando Ciência da Computação

Reilson Batista da Fonseca
- Cursando Inteligência Artificial

Gabriel da Rocha Feitosa
- Cursando Ciência da Computação

Marcus Antônio Cavalcante Oliveira Filho
- Cursando Inteligência Artificial

# Sobre o jogo 🤠🐎

O jogo é ambientado em um cenário 2D onde o jogador controla um personagem principal que deve coletar diferentes tipos de objetos enquanto evita obstáculos e inimigos.O jogo é um jogo do estilo shooter com um tema de faoreste onde o peronagem principal jogavel e um cowboy que precisa atirar nos inimigos que atiram nele e conforme o cowboy for acertando os adversarios surge um bau no qual quando se atira nele vem um item coletavel que o jogador precisa buscar para adicionar na sua coleção. 

- Possui pelo menos 3 tipos de objetos coletáveis.  
- Exibe na tela a contagem de cada objeto coletado.  
- Inclui efeitos sonoros para eventos importantes.  
- Conta com tela inicial e tela de *game over*.  

# Instalação e Execução 📌

**Para executar o jogo é necessário instalar o Python3 e o Pygame.**

Para a instalação do Pygame, pode-se usar o comando:

pip install pygame

# Contribuidores e Funções🖲️



# como jogar o jogo 🎮
Pressione a tecla Enter para iniciar o jogo.

-use as setas do teclado para mover o personagem:

-seta para cima: move o personagem para cima (vertical).

-seta para baixo: move o personagem para baixo (vertical).

-seta para a direita: move o personagem para a direita (horizontal).

-seta para a esquerda: move o personagem para a esquerda (horizontal).

-pressione a tecla Espaço para atirar.

-quando o personagem morre:

-pressione R para reiniciar o jogo.

-pressione Esc para fechar o jogo.

# Arquitetura 💻

main.py: contém o loop principal do jogo e funções para as telas de start e game over.

objetos.py: contém a lógica dos itens coletáveis.

jogador.py: contém a lógica do herói (cowboy).

inimigo.py: contém a lógica do inimigo (bandido).

imagens/: contém as imagens utilizadas para as animações.

sprites.py: contém as animações do jogo.

sons_jogo/: contém os efeitos sonoros utilizados no jogo.

efeitos_sonoros.py: contém a estrutura para salvar e ajustar o volume dos sons.

# Ferramentas, bibliotecas, frameworks 🧲
---- Ferramentas ---
- VScode: ditor de cordigo usado para escrever o codigo para o projeto.
- Github: escolhido por ser mais pratico para compartilhar o codigo com a equipe.
- 

---- Bibliotecas ----
- pygame: usada para cirar o ambiente 2d,gerenciar graficos,eventos e sons.

# Conceitos vistos em aula 👨🏻‍💻

- funções: para modularizar e organizar a logica do jogo.
- listas: para armazenar e manipular objetos e sprites.
- estruturas de controle: loops e condicionais para fluxo do jogo.

# Desafios, erros e lições aprendidas ♥️

- Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
  - maior erro: problemas na detecção de colisões, que causavam coleta incorreta dos objetos.
  - solução: ajustamos a lógica de colisão e implementamos testes para validar.

- Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
- maior desafio: integrar imagens , sons e animações de forma sincrona sem perda de desempenho.
- solução: otimizamos o caregamento de recursos e otimizamos o loop principal do jogo.
  

- Quais as lições aprendidas durante o projeto?
- importância de dividir o trabalho com clareza.  
- necessidade de organizar o código desde o início para evitar retrabalho.  
 - uso de GitHub para colaboração e resolução de conflitos no código.




