# Human Genetic Variant Lookup (Ensembl API)

🇧🇷 [Leia este README em português](README_pt.md)

## Overview

This project is a simple web application that allows fast lookup of **human genetic variants (rsIDs)** using the **Ensembl REST API**. The application retrieves public genomic data and displays key information about a given variant in a clear and organized way.

The project was developed as a **technical challenge for a Bioinformatics Analyst position**, with a focus on clean structure, API integration, testing, and reproducibility.

---

## 🧬 Motivation

This project was developed with a focus on **bioinformatics**, **molecular genetics**, and **pharmacogenomics**, serving as a foundation for:
- Genetic variant analysis
- Integration with genomic databases
- Reproducible scientific software development

---

## Features

* Query human genetic variants using **rsID** (e.g. `rs1333049`)
* Fetch data from the **Ensembl REST API**
* Display relevant variant information:

  * Chromosome
  * Genomic position
  * Alleles
  * Minor allele frequency (when available)
  * Associated genes
  * Molecular consequences
* Simple **Flask web interface**
* JSON-formatted backend response
* Unit tests using **pytest**

---

## Tech Stack

* **Python 3.14**
* **Flask** – web framework
* **Requests** – HTTP requests to Ensembl API
* **Pytest** – unit testing
* **HTML (Jinja2 templates)** – frontend rendering

----

## 🗂 Project Structure

```text
.
├── app.py                 # Flask application
├── ensembl_api.py         # Ensembl API access logic
├── requirements.txt       # Project dependencies
├── README.md              # English documentation
├── README_pt.md           # Portuguese documentation
├── templates/
│   └── index.html         # HTML template
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   └── test_ensembl_api.py
└── Dockerfile             # Docker configuration

```
---

## How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/bvieiracosta/ensembl-variant-lookup.git
cd ensembl-variant-lookup
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

Access the application at:

```
http://127.0.0.1:5000
```

---

## How to Run Tests

From the project root directory, run:

```bash
pytest
```

All tests should pass successfully.

---

## Example Usage

1. Open the web application in your browser
2. Enter a valid rsID (e.g. `rs1333049`)
3. Submit the query
4. View the variant information displayed on the page

---

## API Data Source

This project uses the **Ensembl REST API**:

* [https://rest.ensembl.org](https://rest.ensembl.org)

Specifically, the endpoint:

```
/variation/human/{rsID}
```

All data retrieved is publicly available and provided by Ensembl.

---

## Error Handling

* If a variant is not found, the application returns a clear error message
* Missing fields from the API response are handled gracefully and returned as `null` or empty values

---
## 🐳 Running the application with Docker
🔹 What is Docker?

Docker allows the application to run in an isolated, reproducible environment, ensuring consistent behavior across different systems.

This project can be easily run using Docker, without the need to manually install Python dependencies.

### 🔧 Requirements
- Docker Desktop installed and running  
  👉 https://www.docker.com/products/docker-desktop/

---


### 📦 Build the Docker image

From the root of the project, run:

```bash
docker build -t ensembl-variant-app .
```
### 📦 Run the container
```bash
docker run -p 5000:5000 ensembl-variant-app
```
Then access:
http://127.0.0.1:5000

### 📦 List running containers
```bash
docker ps
```

### 📦 Stop a container
```bash
docker stop <CONTAINER_ID>
```



# Author

Developed by Brenda Vieira

Graduated in Pharmacy and Biochemistry. Bioinformatics and Genomics enthusiastic.