# Biblioteca_digital
Trabalho - Teoria das Estruturas de Dados - 3º Etapa

É um sistema com o objetivo de fazer um gerenciamento básico de uma biblioteca, que permite cadastrar e consultar leitores, controlar reservas, registrar devoluções e organizar as categorias de livros disponiveis na biblioteca.

# Funcionalidades
Ao iniciar o sistema o menu aparece mostrando as funções disponiveis:<br>
**1.Gerenciamento dos leitores<br>**
   ° Cadastrar leitores,<br>
   ° Listar leitores cadastrados,<br>
   ° Pesquisar leitores pelo ID ou nome,<br>
   ° Atualizar informações dos leitores,<br>
   ° Excluir leitores.<br>
   
**2.Gerenciamento de reservas<br>**
   ° Cadastrar reservas,<br>
   ° Listar reservas,<br>
   ° Atender reservas,<br>
   ° Cancelar reservas.<br>

**3. Gerenciamento de devoluções<br>**
   ° Registrar devoluções,<br>
   ° Listar devoluções,<br>
   ° Pesquisar devoluções,<br>
   ° Retirar a última devolução registrada.<br>

**4. Gerenciamento de Categorias<br>**
   ° Cadastrar categorias principais,<br>
   ° Cadastrar subcategorias,<br>
   ° Pesquisar categorias e subcategorias,<br>
   ° Renomear categorias,<br>
   ° Excluir categorias.<br>

# Armazenamento dos dados
 O sistema utiliza um arquivo de texto com o nome: 'dados_sistema.txt' para armazenar as informações, para que isso aconteça o usuário deve selecionar pelo menu a opção 19, depois de inserir ou alterar as informações que queria. 
 O programa também permite carregar as informações já salvos no arquivo.<br>
 Exemplo de funcionamento:
 <p align="center">
  <img src="https://github.com/user-attachments/assets/a473a4fe-6125-43df-ace0-9d2616cb1ed4" width="300" alt="Exemplo de cadastro de leitor">
</p>
 Ao selecionar a opção 1, posso preencher os campos e cadastrar um leitor e ao finalizar o cadastro seleciono a opção 19 para que o leitor fique salvo no arquivo.
 
# Estrutura do Documento
As informações salvas no arquivo de texto são divididas por '|', sendo:<br>
|Estrutura|Informações<br>
exemplo:
LISTA|001|Ana|02211133300|32911115555|R. Luiz Costa. Nº 90. Bairro: Santa Cecília|1

**Lista - A lista foi utilizada para armazenar os leitores cadastrados, permitindo operações de inserir, consultar, atualizar e excluir.**

**Fila - Foi utilizada para organizar as reservas seguindo o princípio FIFO(First In First Out), onde o primeiro elemento a entrar é o primeiro a sair.**

**Pilha - Foi utilizada para organizar as devoluções seguindo o princípio LIFO (*Last In, First Out*), em que o último elemento a entrar é o primeiro a sair.**

**Árvore - Foi utilizada para organizar as categorias e subcategorias dos livros por meio de dicionários aninhados, permitindo representar uma estrutura hierárquica.**

# Como executar o programa
1. Instale o Python 3.
2. Baixe este repositório.
3. Abra a pasta do projeto.
4. Execute o arquivo principal ' main.py '
