<div align=center>
    <img width=200 src='https://user-images.githubusercontent.com/60933617/166180801-b6f8fc4f-37ab-4039-ab40-237cb094f56d.png'/>
    <h1>PONDOC</h1>
    <b>Estágio</b>
</div>

<br>

> ## Sumário
* [Introdução](#Introdução)
* [Sobre](#Sobre)
* [Construído com](#Construído-com)
* [Pré-requisitos](#Pré-requisitos)
* [Instalação](#Instalação)
* [Mais informações](#Mais-informações)

<br>


> ## Introdução
<p>
    Projeto de estágio para a conclusão do curso de Informática na instituição Centro Federal de Educação Tecnológica celso Suckow da Fonseca 
    (CEFET-RJ/MARACANÃ), sob a supervisão do professor Eduardo Bezerra da Silva.
    <div align=right> 
        <b>Dúvidas</b> <br>
        <a href = "https://github.com/araujobtc/pondoc/issues/new"><img src="https://img.shields.io/badge/-Issues-%23333?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>
        <a href="https://www.linkedin.com/in/isabelle-ferreira-de-araujo" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
        <a href = "mailto:isabelletecn@gmail.com"><img src="https://img.shields.io/badge/-Gmail-%23333?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    </div>
</p>

<p align="right"><a href="#PONDOC">Topo ↑</a></p>


> ## Sobre

<p>
    A partir de produções bibliográficas dos docentes do Programa de Pós-graduação em Ciência da Computação (PPCIC) do CEFET-RJ, o projeto gera um relatório em
    excel para analise de potuação destes docentes, dando importância a avaliação Qualis das conferências e das revistas de publicação.
</p>
<div align=center><img width=550 src='https://user-images.githubusercontent.com/60933617/182955105-f64f7bf6-9f0d-4fc9-a08a-a4ee542190e7.png'/></div>

<p align="right"><a href="#PONDOC">Topo ↑</a></p>


> ## Construído com

* <a href='https://pypi.org/project/bs4/'>bs4 (0.0.1)</a>
* <a href='https://pypi.org/project/fuzzywuzzy/'>Fuzzywuzzy (0.18.0)</a>
* <a href='https://pypi.org/project/openpyxl/'>Openpyxl (3.0.9)</a>
* <a href='https://pypi.org/project/pandas/'>Pandas (1.4.2)</a>
* <a href='https://pypi.org/project/psycopg2/'>Psycopg2 (2.9.3)</a>
* <a href='https://pypi.org/project/pyparsing/'>PyParsing (3.0.6)</a>
* <a href='https://www.python.org'>Python (3.10.5)</a>
* <a href='https://pypi.org/project/requests/'>Requests (2.27.1)</a>

<p align="right"><a href="#PONDOC">Topo ↑</a></p>


> ## Pré-requisitos

1. [Python](https://www.python.org/downloads/)
  
3. bs4

        pip install bs4
5. Fuzzywuzzy

        pip install fuzzywuzzy
6. Openpyxl

        pip install openpyxl
8. Psycopg2

        pip install psycopg2
10. PyParsing

        pip install pyparsing
9. Requests

        pip install requests
        
<p align="right"><a href="#PONDOC">Topo ↑</a></p>

> ## Instalação

* Clone o repositório

        git clone https://github.com/araujobtc/pondoc.git
* Banco de dados
<br><div align=center><img width=400 src='https://user-images.githubusercontent.com/60933617/182953618-a2c8ac85-fdb4-4cf3-8bb5-b12ef55f2723.png'/></div>
<br>É necessário que o uso se inicie rodando os arquivos scriptsdb.py que criará toda a estrutura dentro do banco de dados escolhido. Porém antes disso serão               necessárias alterações na função conect_db no arquivo database.py, onde deverão ser inseridas informações para acessar o banco de dados desejado.

<div align=center>
    <img width=245 src='https://user-images.githubusercontent.com/60933617/182961611-c9083d05-5221-4540-9408-dc569f9b4510.png'/>
    <img width=320 src='https://user-images.githubusercontent.com/60933617/182953708-aae118da-0355-403c-a214-6e8649ae6b2d.png'/><br>
</div>

<p align="right"><a href="#PONDOC">Topo ↑</a></p>

> ## Mais informações

### Licença
Distributed under the Apache License. See [`LICENSE.txt`](https://github.com/araujobtc/pondoc/BLOB/main/LICENSE) for more information.

### Relatório
Documentação do projeto PONDOC em [`RelatórioEstágio.docx`](https://github.com/araujobtc/pondoc/blob/main/docs/RelatórioEstágio.docx)

<p align="right"><a href="#PONDOC">Topo ↑</a></p>
