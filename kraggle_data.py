import shutil
from pathlib import Path

import kagglehub

DATA_DIR = Path(__file__).parent / "kraggle_data"

# "owner/dataset-name" slugs from the Kaggle URL: kaggle.com/datasets/<owner>/<dataset-name>
DATASETS = [
    "simonzheng12/ctp-project",
]


def main():
    DATA_DIR.mkdir(exist_ok=True)
    for slug in DATASETS:
        path = kagglehub.dataset_download(slug)
        for f in Path(path).glob("*.csv"):
            shutil.copy(f, DATA_DIR / f.name)
            print(f"{slug} -> {DATA_DIR / f.name}")


if __name__ == "__main__":
    main()
