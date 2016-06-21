import pytest

from anoncreds.protocol.credential_definition import CredentialDefinition
from anoncreds.protocol.types import GVT, XYZCorp
from anoncreds.protocol.verifier import Verifier
from anoncreds.test.helper import getProver


@pytest.fixture(scope="module")
def issuers(issuer1, issuer2):
    # Return issuer's public key
    return {GVT.name: issuer1, "xyz": issuer2}


@pytest.fixture(scope="module")
def issuersPk(issuers):
    pk_i = {}
    for k, v in issuers.items():
        pk_i[k] = v.PK
    return pk_i


@pytest.fixture(scope="module")
def attrNames1():
    return GVT.getNames()


@pytest.fixture(scope="module")
def attrNames2():
    return XYZCorp.getNames()


@pytest.fixture(scope="module")
def issuer1(attrNames1):
    return CredentialDefinition(attrNames1)


@pytest.fixture(scope="module")
def issuerPk(issuer1):
    # Return issuer's public key
    return {GVT.name: issuer1.PK}


@pytest.fixture(scope="module")
def issuer2(attrNames2):
    return CredentialDefinition(attrNames2)


@pytest.fixture(scope="module")
def proverAndAttrs1(issuerPk):
    attribs = GVT.attribs(name='Aditya Pratap Singh',
                          age=25,
                          sex='male')

    prover, attrs = getProver(attribs, issuerPk)

    return prover, attrs


@pytest.fixture(scope="module")
def proverAndAttrs2(issuerPk):
    attribs = GVT.attribs(name='Jason Law',
                          age=42,
                          sex='male')

    prover, attrs = getProver(attribs, issuerPk)

    return prover, attrs


@pytest.fixture(scope="module")
def proverAndAttrsForMultiple1(issuersPk):
    attribs = GVT.attribs(name='Aditya Pratap Singh',
                          age=25,
                          sex='male')

    prover, attrs = getProver(attribs, issuersPk)

    return prover, attrs


@pytest.fixture(scope="module")
def proverAndAttrsForMultiple2(issuersPk):
    attribs = XYZCorp.attribs(status='ACTIVE')

    prover, attrs = getProver(attribs, issuersPk)

    return prover, attrs


@pytest.fixture(scope="module")
def verifier1(issuerPk):
    return Verifier(issuerPk)


@pytest.fixture(scope="module")
def verifierMulti1(issuersPk):
    return Verifier(issuersPk)


@pytest.fixture(scope="module")
def verifierMulti2(issuersPk):
    return Verifier(issuersPk)