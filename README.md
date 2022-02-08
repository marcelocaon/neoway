# Neoway
Serviço de captura/coleta de dados fictícios presentes no endereço (xxxx) e persistência em um banco de dados SQLite.

### Instalação
Utilizada versão python 3.7 no desenvolvimento. Para executar o projeto, será necessário instalar os seguintes extensões:

Requests:> no prompt de comando digite: pip install requests
BeatifulSoup:> no prompt de comando digite: pip install beautifulsoup4
Unidecode:> no prompt de comando digite: pip install Unidecode
Regex:> no prompt de comando digite: pip install regex
SQLite:> no prompt de comando digite: pip install db-sqlite3


### Desenvolvimento
Para iniciar o desenvolvimento, é necessário clonar o projeto do GitHub num diretório de sua preferência:

cd "diretorio de sua preferencia"
git clone https://github.com/marcelocaon/neoway
python main.py

### Melhorias e sugestões
Nos testes feitos o programa leva cerca de 13 horas para fazer todo o processo captura e persistência dos quase 47mil dados fictícios (nome, score, cpf e validação do cpf) no banco de dados. Acredito que se for possível implementar um programa que rode a captura de dados simultâneamente poderia ser diminuido este tempo do processo. Estou pesquisando ainda, não sei se eh possível. Teria de ser avaliado também se é possível fazer multiplas requisições simultâneas ao site que detêm os dados.

### Contribuições
Contribuições são sempre bem-vindas!

### Licença
Não se aplica.

