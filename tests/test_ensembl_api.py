from ensembl_api import build_variant_response


def test_valid_rsid():
    result = build_variant_response("rs1333049")

    assert result["chromosome"] is not None
    assert result["position"] is not None
    assert isinstance(result["genes"], list)
    assert isinstance(result["consequence"], list)

import pytest


def test_invalid_rsid():
    with pytest.raises(Exception):
        build_variant_response("rsINVALID123")
