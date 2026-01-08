import requests

ENSEMBL_URL = "https://rest.ensembl.org/variation/human/{}"
HEADERS = {"Content-Type": "application/json"}


def fetch_variant(rsid: str) -> dict:
    """
    Consulta a API do Ensembl e retorna o JSON bruto.
    """
    if not rsid:
        raise ValueError("RSID cannot be empty")

    response = requests.get(
        ENSEMBL_URL.format(rsid),
        headers=HEADERS,
        timeout=10
    )

    if response.status_code != 200:
        raise ValueError("Variant not found")

    return response.json()



def extract_mapping(data: dict) -> dict:
    """
    Extrai cromossomo e posição genômica.
    """
    mapping = data.get("mappings", [{}])[0]

    return {
        "chromosome": mapping.get("seq_region_name"),
        "position": mapping.get("start")
    }


def extract_genes_and_consequences(data: dict) -> tuple[list, list]:
    """
    Extrai genes e consequências funcionais sem duplicação.
    """
    genes = set()
    consequences = set()

    for feature in data.get("variation_feature", []):
        gene = feature.get("gene_name")
        if gene:
            genes.add(gene)

        for consequence in feature.get("consequence_types", []):
            consequences.add(consequence)

    return list(genes), list(consequences)


def build_variant_response(rsid: str) -> dict:
    """
    Função principal que organiza toda a resposta.
    """
    data = fetch_variant(rsid)

    mapping = extract_mapping(data)
    genes, consequences = extract_genes_and_consequences(data)

    return {
        "rsid": rsid,
        "chromosome": mapping["chromosome"],
        "position": mapping["position"],
        "alleles": data.get("alleles"),
        "minor_allele_freq": data.get("minor_allele_freq"),
        "genes": genes,
        "consequence": consequences
    }
