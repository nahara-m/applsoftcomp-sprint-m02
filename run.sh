#!/bin/bash
uv sync
uv run python workflow/format_1d_data.py
uv run python workflow/viz_1d_data.py
uv run python workflow/digits_data.py
uv run python workflow/viz_2d_data.py
uv run python workflow/viz_1d_multi_data.py