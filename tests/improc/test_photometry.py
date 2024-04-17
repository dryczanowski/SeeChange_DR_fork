import pytest
from improc.photometry import iterative_photometry


def test_sigma_clip(ptf_datastore):
    import pdb; pdb.set_trace()
    result = iterative_photometry(ptf_datastore.image, ptf_datastore.weight, ptf_datastore.flags, ptf_datastore.psf)
    pass