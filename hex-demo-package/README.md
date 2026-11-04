# hex-demo

A tiny sample package for testing Hex's **Git package import**.

## Contents

- `hex_demo/orders.py`: three helper functions (`load_sample_orders`, `clean_orders`, `summarize_by_region`)
- `hex_demo/data/sample_orders.csv`: a small bundled dataset

## Use it in a Hex project

After importing the package from the Environments sidebar, a folder named
`{git user}-{repo name}` appears in the project's files. Add it to the path:

```python
!ls   # confirm the folder name

import sys, os
PKG_DIR = os.path.abspath("your-github-user-hex-demo-package")  # adjust
sys.path.append(PKG_DIR)

from hex_demo import load_sample_orders, clean_orders, summarize_by_region

df = clean_orders(load_sample_orders())
summarize_by_region(df)
```

Read the raw file directly instead:

```python
import pandas as pd
raw = pd.read_csv(os.path.join(PKG_DIR, "hex_demo", "data", "sample_orders.csv"))
```

## Optional: install with pip

If you add an install command in Hex's package settings, you can run:

```
pip install ./
```

(adjust to your repo layout)
