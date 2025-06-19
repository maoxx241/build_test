from mindie_turbo.logger import get_logger

logger = get_logger("mindie_turbo")


def zip(a, b):
    logger.info(f"Zipping {a} and {b}")
    return a + b


def unzip(a):
    logger.info(f"Unzipping {a}")
    return a[: len(a) // 2], a[len(a) // 2 :]
