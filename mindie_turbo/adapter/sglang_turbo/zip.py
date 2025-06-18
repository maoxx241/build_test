from mindie_turbo.multimodal import zip as mm_zip, unzip as mm_unzip


def zip(a, b):
    print(f'Zipping {a} and {b} in sglang_turbo')
    return mm_zip(a, b)


def unzip(a):
    print(f'Unzipping {a} in sglang_turbo')
    return mm_unzip(a)
