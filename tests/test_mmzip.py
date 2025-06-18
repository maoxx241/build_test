import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mindie_turbo.multimodal import zip as mm_zip, unzip as mm_unzip


def test_mmzip_roundtrip():
    a = "hello"
    b = "world"
    zipped = mm_zip(a, b)
    assert zipped == a + b
    assert mm_unzip(zipped) == (a, b)
