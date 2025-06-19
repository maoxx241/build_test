# build_test

This repository contains three Python packages:

- `mindie_turbo`: the core utilities.
- `sglang_turbo`: an adapter depending on `mindie_turbo`.
- `vllm_turbo`: another adapter depending on `mindie_turbo`.

Each package now includes a `pyproject.toml` so you can build wheels with
[Poetry](https://python-poetry.org/).

## Building the packages

1. Install Poetry if you don't have it:
   ```bash
   pip install poetry
   ```
2. From the repository root, run the following commands to build each
   package individually:
   ```bash
   poetry build
   (cd mindie_turbo/adapter/sglang_turbo && poetry build)
   (cd mindie_turbo/adapter/vllm_turbo && poetry build)
   ```
   The generated wheels will be placed in each package's `dist/` directory.
