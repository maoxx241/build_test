import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mindie_turbo.adapter.vllm_turbo.zip import zip as vl_zip, unzip as vl_unzip
import logging


def test_vllm_zip_roundtrip(caplog):
    with caplog.at_level(logging.INFO):
        a = "baz"
        b = "qux"
        zipped = vl_zip(a, b)
    assert "vllm_turbo" in caplog.text
    assert zipped == a + b
    assert vl_unzip(zipped) == (a, b)
