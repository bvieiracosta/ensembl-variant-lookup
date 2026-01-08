# Consulta de Variantes Genéticas – Ensembl API

🇺🇸 [Read this README in English](README.md)

Este projeto é uma aplicação web simples desenvolvida em Python para consulta de variantes genéticas humanas (rsIDs), utilizando dados públicos da **Ensembl REST API**.

A aplicação permite que o usuário informe um rsID (por exemplo, `rs1333049`) e visualize informações genômicas relevantes de forma clara e organizada.

---

## 🧬 Funcionalidades

- Consulta de variantes genéticas humanas via Ensembl REST API
- Exibição de:
  - Cromossomo
  - Posição genômica
  - Alelos
  - Frequência do alelo menor (quando disponível)
  - Genes associados
  - Consequências funcionais
- Interface web simples utilizando Flask
- Tratamento de erros para variantes inexistentes
- Testes unitários com pytest

---

## 🛠️ Tecnologias utilizadas

- Python 3.14
- Flask
- Requests
- Pytest
- Ensembl REST API

---

## 📁 Estrutura do projeto

```text
.
├── app.py
├── ensembl_api.py
├── requirements.txt
├── README.md
├── README_pt.md
├── templates/
│   └── index.html
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_ensembl_api.py
└── Dockerfile
