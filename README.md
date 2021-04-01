# 21

Jogo de Cartas 21


# Projeto

- [35%] Cartas
- [40%] Baralho
- [30%] Mão
- [40%] Jogador
- [30%] Rodadas
- [10%] Menu

# Log

Formatei meu PC e perdi os arquivos do curso de python. Vou tentar replicar o projeto final, agora com uso do tkinter.
Não sei se é assim que se documenta um projeto, mas tudo tem sua primeira vez certo?

Fiz ontem as cartas e o baralho. Preciso dar uma carta do baralho para a mão de um jogador.
Quantos jogadores vão ser afinal? Pra um projeto simples, um ta bom eu acho.

Preciso arrumar a questão do valor do Ás. Um jeito automático de ver o melhor valor possível da mão.
Arrumei um pouco a função que lê o valor da mão, mas ainda preciso arrumar a questão de como modificar o valor de um Ás que saiu como
a primeira carta da mão, mas que depois de comprar 1 ou duas cartas, o valor dele precisaria ser alterado para 1 ou invés de 11, devido
o problema de estourar o valor da mão acima de 21.

Tenho que acertar a questão da codição de vitória. Qual devem ser os passos lógicos a serem seguidos? O objetivo do jogo, é 
vencer a banca. Qual é o primeiro passo, verificar quem perdeu? A banca ou o jogador? ou ambos? Ou verificar quem tem o insta 21?

Fui ler a regras do jogo e lembrei que existem várias ações que podem ser tomadas. Mas vamos implementar o jogo uma coisa de cada vez.

Tenho que ver como eu vou fazer com a questão de renovar as cartas do baralho conforme elas vão sendo compradas

Logo vou precisar de um menu interativo, e não sei se vale a pena fazer um pelo terminal. O ideal era usar o tkinter
Por enquanto vai o terminal mesmo. Aprendendo coisas de linux agora que comecei a trabalhar, mostrou que pode ser interessante uma versão de terminal.
Mas se eu quiser transformar numa versão com GUI, vou precisar adaptar todas as funções.
Provavelmente desmembrar a função jogo atual também.

Será que um dia isso aqui fica bonito igual os dos sites?

