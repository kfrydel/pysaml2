"""This module provides methods for PKI operations."""

import cryptography.x509 as _x509


def load_pem_x509_certificate(data):
    """Load X.509 PEM certificate."""
    return _x509.load_pem_x509_certificate(data)
