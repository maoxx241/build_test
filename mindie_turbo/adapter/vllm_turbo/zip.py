from mindie_turbo.multimodal import zip as mm_zip, unzip as mm_unzip
from mindie_turbo.logger import get_logger

logger = get_logger("vllm_turbo")


def zip(a, b):
    logger.info(f"Zipping {a} and {b} in vllm_turbo")
    return mm_zip(a, b)


def unzip(a):
    logger.info(f"Unzipping {a} in vllm_turbo")
    return mm_unzip(a)
