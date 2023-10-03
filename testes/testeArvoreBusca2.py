import sys;
sys.path.append("..");

from logic.tabuleiro import *;
from logic.node import *;
from logic.arvoreDeBusca import *;

head = Node();
arvore = ArvoreDeBusca(head);

solucao = arvore.buscar(10, "PRIORITY");
i = 0;
print(solucao);
# for each in solucao:
#     i += 1;
#     print("---------------------PASSO " + str(i));
#     each.visualize();