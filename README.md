# Human Genetic Variant Lookup (Ensembl API)

🇧🇷 [Leia este README em português](README_pt.md)

## Overview

This project is a simple web application that allows fast lookup of **human genetic variants (rsIDs)** using the **Ensembl REST API**. The application retrieves public genomic data and displays key information about a given variant in a clear and organized way.

The project was developed as a **technical challenge for a Bioinformatics Analyst position**, with a focus on clean structure, API integration, testing, and reproducibility.

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

---

## Project Structure

```
PythonProject/
│
├── app.py                  # Flask application entry point
├── ensembl_api.py          # Ensembl API integration and data processing
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
│
├── templates/
│   └── index.html          # Web interface template
│
├── tests/
│   └── test_ensembl_api.py # Unit tests
│
└── .venv/                  # Virtual environment (not committed)
```

---

## How to Run Locally

### 1. Clone the repository

```bash
git clone <repository_url>
cd PythonProject
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask application

```bash
python app.py
```

The application will be available at:

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

## Future Improvements

* Add caching to reduce repeated API calls
* Improve frontend styling
* Add support for batch rsID queries
* Extend annotations with clinical or pharmacogenomic data
* Dockerize the application for easier deployment

---

## Author

Developed by **Brenda Vieira**

Background in **Pharmacy and Biochemistry**, transitioning into **Bioinformatics and Data Analysis**.
