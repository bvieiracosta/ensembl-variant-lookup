# Consulta de Variantes Genéticas – Ensembl API

🇺🇸 [Read this README in English](README.md)

Este projeto é uma aplicação web simples desenvolvida em Python para consulta de variantes genéticas humanas (rsIDs), utilizando dados públicos da **Ensembl REST API**.

A aplicação permite que o usuário informe um rsID (por exemplo, `rs1333049`) e visualize informações genômicas relevantes de forma clara e organizada.

O projeto foi desenvolvido como um desafio técnico para uma vaga de Analista de Bioinformática, com foco em boa organização de código, integração com APIs, testes e reprodutibilidade.

--- 

## Motivação

Este projeto foi desenvolvido com foco em bioinformática, genética molecular e farmacogenômica, servindo como base para:

* Análise de variantes genéticas 
* Integração com bancos de dados genômicos 
* Desenvolvimento de software científico reprodutível

--- 
## Funcionalidades

* Consulta de variantes genéticas humanas utilizando rsID (ex.: rs1333049)
* Consumo de dados da API REST do Ensembl 
* Exibição das seguintes informações da variante:
  * Cromossomo 
  * Posição genômica 
  * Alelos 
  * Frequência do alelo menor (quando disponível)
  * Genes associados 
  * Consequências moleculares

* Interface web simples desenvolvida com Flask 
* Backend com resposta estruturada em JSON 
* Testes unitários utilizando pytest

---
# Tecnologias Utilizadas

* Python 3.10+ 
* Flask – framework web 
* Requests – requisições HTTP para a API do Ensembl 
* Pytest – testes unitários 
* HTML (templates Jinja2) – renderização do frontend
---
# Estrutura do Projeto
```text
.
├── app.py                 # Aplicação Flask
├── ensembl_api.py         # Lógica de acesso à API do Ensembl
├── requirements.txt       # Dependências do projeto
├── README.md              # Documentação em inglês
├── README_pt.md           # Documentação em português
├── templates/
│   └── index.html         # Template HTML
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_ensembl_api.py
└── Dockerfile             # Configuração do Docker
```

# Como Executar Localmente
### 1. Clonar o repositório
```bash
git clone https://github.com/bvieiracosta/ensembl-variant-lookup.git
cd ensembl-variant-lookup
```

### 2. Criar e ativar um ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```
### 4. Executar a aplicação Flask
```bash
python app.py
```

Acesse no navegador:
```text
http://127.0.0.1:5000
```
---
# Como Executar os Testes

Na raiz do projeto, execute:
```bash
pytest
```

* Testes unitários validam a integração com a API e o processamento dos dados 
* Todos os testes devem passar com sucesso

---
## Exemplo de Uso

1. Abra a aplicação web no navegador 
2. Insira um rsID válido (ex.: rs1333049)
3. Envie a consulta 
4. Visualize as informações da variante genética na tela
---

## Fonte dos Dados

Este projeto utiliza a API REST do Ensembl:

https://rest.ensembl.org

Endpoint utilizado:
```text
/variation/human/{rsID}
```

Todos os dados são públicos e fornecidos pelo Ensembl.

## Tratamento de Erros

* Caso uma variante não seja encontrada, a aplicação retorna uma mensagem de erro clara 
* Campos ausentes na resposta da API são tratados de forma segura, retornando valores nulos ou listas vazias 
* O tratamento de erros é feito por meio de exceções na camada de dados e respostas controladas na aplicação Flask

# Executando a Aplicação com Docker
### O que é Docker?

Docker permite executar a aplicação em um ambiente isolado e reprodutível, garantindo comportamento consistente em diferentes sistemas, sem a necessidade de instalar dependências manualmente.

## Requisitos

Docker Desktop instalado e em execução
https://www.docker.com/products/docker-desktop/

### Construir a imagem Docker

Na raiz do projeto, execute:
```bash
docker build -t ensembl-variant .
```
### Executar o container
```bash
docker run -p 5000:5000 ensembl-variant
```

Acesse:
```text
http://127.0.0.1:5000
```
### Listar containers em execução
```bash
docker ps
```
### Parar um container
```bash
docker stop <CONTAINER_ID>
```

# Observação importante
Nem todas as variantes retornam consequência funcional ou minor_allele_freq usando o endpoint /variation/human/{rsID}. Quando a informação não está disponível, o sistema retorna listas vazias ou null, mantendo robustez e transparência.
# Autora

Desenvolvido por **Brenda Vieira**

Graduada em Farmácia e Bioquímica

Entusiasta em Bioinformática e Genômica