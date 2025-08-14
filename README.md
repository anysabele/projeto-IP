

# Sobre o projeto e equipe 💻

Somos uma equipe mista de discentes de Inteligência Artificial e Ciência da Computação da Universidade Federal de Pernambuco. Este repositório contém a atividade final da disciplina "Introdução à Programação", oferecida a todos os alunos do primeiro período do Centro de Informática.
O projeto de Introdução à Programação consiste em criar um sistema interativo em 2D. Nele, o usuário controla um objeto para coletar outros itens espalhados pela tela. Tudo o que for coletado será registrado e exibido na tela. O projeto utiliza Python e segue os conceitos de Programação Orientada a Objetos.

----- membros ---

Anysabele de Paula Barbosa Santos
- Cursando Inteligência Artificial
- Eventos
- Sprites e sons
  
Maria Luiza Cunha de Barros
- Cursando Ciência da Computação
- Main
- Eventos

Reilson Batista da Fonseca
- Cursando Inteligência Artificial
- Criativo
- Eventos

Gabriel da Rocha Feitosa
- Cursando Ciência da Computação
- Criativo
- Eventos

Marcus Antônio Cavalcante Oliveira Filho
- Cursando Inteligência Artificial
- Eventos
- Correção final do código.

# Sobre o jogo 🤠🐎

Nosso jogo é um "Shooter" no qual o protagonista, um cowboy, pode se mover em todas as direções (frente, trás, cima e lados) e atirar horizontalmente para eliminar os inimigos (bandidos). Os bandidos avançam em direção ao cowboy enquanto também disparam.
Cada inimigo leva 3 tiros para ser derrotado e, ao morrer, solta um baú com itens aleatórios. Para abrir o baú, é necessário atirar nele duas vezes e, em seguida, se aproximar para coletar o item. Os itens coletados são exibidos no canto superior esquerdo da tela, abaixo dos corações que representam a vida do cowboy.

----- Como jogar? ---
- Pressione ENTER para começar o jogo
- Use as teclas de seta (↑ ↓ ← →) para mover o cowboy em todas as direções.
- Pressione ESPAÇO para atirar.
- Aproxime-se do objeto dropado para coletar.
- Em caso de game over, pressione R para reiniciar o jogo ou ESC para fechar a janela.
 

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
- VScode: escolhido por ser o editor de código que a equipe possui mais familiarização ate agora.  
- Github: escolhido por ser mais pratico para compartilhar o codigo com a equipe.

---- Bibliotecas ----
- Pygame: escolhida por ser a biblioteca mais simples e focada no desenvolvimento de jogos 2D, sendo a melhor opção para nossa equipe, que está iniciando na programação de jogos..
- Sys: escolhida para eventos como "fechar o jogo".
- Random: escolhida para gerar numeros aleátorios de coordenadas em que os cowboys aparecem na tela.

---- Frameworks ---
- Não foram ultilizadas.

# Conceitos vistos em aula 👨🏻‍💻

- Funções: ultilizadas para organizar a dinamica de cada personagem e objetos.
- Listas: usamos listas dentro das funções para salvar tiros, itens coletados e vida dos personagens.
- Laços de repetição: ultilizamos para o loop principal do jogo e para implementar algo de acordo com as ações feitas e sofridas pelos personagens.
- Comandos condicionais: usamos para monitorar as ações dos personagens e ações sofridas.

# Desafios, erros e lições aprendidas ♥️

- Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
  - Começar algo sem entender completamente como funciona. Recomeçamos quase do zero.

- Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
  - O maior desafio foi a separação do código em pastas, pois cada membro desenvolvia uma parte do jogo separadamente, causando confusão na integração. Para resolver, consolidamos tudo em uma única pasta, organizamos o código de forma clara e só então o dividimos novamente em módulos, garantindo que todas as partes funcionassem juntas corretamente. Além disso, o curto prazo para desenvolvimento e os compromissos com outras disciplinas nos impediram de implementar todos os recursos planejados inicialmente para o jogo, mas pretendemos adicioná-los e aprimorá-lo no futuro.

  
- Quais as lições aprendidas durante o projeto?
  - Entender por completo algo para depois reproduzi-lo. 

# Galeria de Imagens 📷



<img width="793" height="624" alt="tela_inicio" src="https://github.com/user-attachments/assets/1629e30f-7e36-48ab-96b2-74216af2e513" />
<img width="462" height="309" alt="img3" src="https://github.com/user-attachments/assets/907bd188-9b05-46ce-8a20-4e36530526e5" />
<img width="630" height="334" alt="img4" src="https://github.com/user-attachments/assets/f49cb275-de1e-4f90-a004-22bd5009d579" />
<img width="446" height="282" alt="img11" src="https://github.com/user-attachments/assets/8b12f6b6-5c51-4bbd-88c8-3c32fe527840" />
<img width="<img width="797" height="624" alt="tela_game_over" src="https://github.com/user-attachments/assets/8852a27d-741e-432b-8c77-066f9498c8e8" />
