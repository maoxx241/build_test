import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mindie_turbo.adapter.sglang_turbo.zip import zip as sg_zip, unzip as sg_unzip
import logging


def test_sglang_zip_roundtrip(caplog):
    with caplog.at_level(logging.INFO):
        a = "foo"
        b = "bar"
        zipped = sg_zip(a, b)
    assert "sglang_turbo" in caplog.text
    assert zipped == a + b
    assert sg_unzip(zipped) == (a, b)
