# Computação Gráfica

Trabalho para matéria INE5420 onde se é criado um Sistema Gráfico Interativo que vai sendo expandido suas funções a cada duas semanas.

## Utilização

Ao executar a main.py ou o makefile o Sistema ira aparecer, nele são apresentados os botões para mover a window, de zoom in e zoom out, para inserir ponto, linha ou wireframe (polígono) basta clicar no seu respectivo botão de inserção. Para a criação de Ponto e Linha basta inserir as coordenadas nos campos de entradas de texto o valor desejado, para o Wireframe utilize da seguinte formatação "x,y;x1,y1;x2,y2; ...". Para diferente cor de cada objeto inserir cor no seu campo utilizando da logica rgb (entre 0 e 255) separando r g e b com ",". Exemplo: "255,255,0" 

Após criados esses objetos são inseridos na lista presente no canto esquerdo da janela principal do sistema. Para realizar transformações sobre esses objetos basta clicar duas vezes sobre o objeto desejado, uma nova janela sera aberta. 

Para realizar rotação é sempre necessário indicar o valor desejado do ângulo de rotação, para rodar ao redor de um ponto ancora basta inserir o valor desejado nos respectivos campos, para rotação no centro e ao redor da origem não é necessário inserir valores da ancora x e y. 

Para transladar e escalonar o objeto basta inserir os valores nas suas respectivas entradas.

Para importar objetos basta clicar no botao "import" e selecionar o .obj desejado. Para exportar basta clicar no objeto na lista que se deseja exportar, clicar no botão "export" e salvar o documento no local desejado com o nome desejado.

## Contribuintes
Este trabalho é realizado pelos alunos:

João Pedro Santana - 15204129

Stefano Bergamini Poletto - 16100745
