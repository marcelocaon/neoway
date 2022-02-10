# Case Técnico Neoway
Serviço de captura/coleta de dados fictícios presentes no endereço (xxxx) e persistência em um banco de dados SQLite.

### Instalação
Utilizada versão python 3.7 no desenvolvimento. Para executar o projeto, será necessário instalar os seguintes extensões:

* Requests:> no prompt de comando digite: pip install requests
  - Biblioteca usada para fazer as requisições HTTP
* BeatifulSoup:> no prompt de comando digite: pip install beautifulsoup4
  - Biblioteca usada para capturar as informações das páginas HTML
* Unidecode:> no prompt de comando digite: pip install Unidecode
  - Biblioteca usada para remover acentos das strings com os nomes dos candidatos
* Regex:> no prompt de comando digite: pip install regex
  - Biblioteca usada no modelo de validação de CPF, serve para procurar por padrões, caracteres em específico em strings
* SQLite:> no prompt de comando digite: pip install db-sqlite3
  - Banco de dados usado para armazenamento dos dados capturados

### Arquivos que compoem o programa
* main.py
  - Arquivo principal, que contrala a interface e chama as funções necessárias dos outros arquivos
* banco.py
  - Arquivo responável pela conexão com o banco, inserindo e apagando dados
* validador.py
  - Arquivo responsável pela validação dos campos 'cpf' (caso válido deixa o campo status do banco como vazio ou caso inválido coloca um texto como cpf inválido no campo status do banco) e 'nome' (remove os acentos da string e ainda coloca letra maiuscula somente nas iniciais de cada palavra)
* neoway.db
  - Arquivo do banco de dados do programa
* neoway_preenchido.db
  - Exemplo de arquivo do banco de dados preenchido pelo sistema

### Funcionamento
Quando o programa é iniciado o usuário informa a página que quer começar a captura dos dados, opção feita devido ao tempo de captura ser longo e poder ocorrer algum problema durante, então o usuário pode continuar de onde parou antes porque o sistema vai informando na tela cada página recem capturada.

### Desenvolvimento
Para iniciar o desenvolvimento, é necessário clonar o projeto do GitHub num diretório de sua preferência:

- cd "diretorio de sua preferencia"
- git clone https://github.com/marcelocaon/neoway
- python main.py

### Melhorias e sugestões
Nos testes feitos o programa leva cerca de 13 horas para fazer todo o processo captura e persistência dos quase 47mil dados fictícios (nome, score, cpf e validação do cpf) no banco de dados. Acredito que se for possível implementar um programa que rode a captura de dados simultâneamente poderia ser diminuido este tempo do processo. Estou pesquisando ainda, não sei se eh possível. Teria de ser avaliado também se é possível fazer multiplas requisições simultâneas ao site que detêm os dados. Outra questão a ser avaliada eh o uso do banco de dados, utilizei o SQLite por ser bem simples, será que um banco mais robusto poderia melhorar a velocidade?

### Contribuições
Contribuições são sempre bem-vindas!

### Licença
Não se aplica.

