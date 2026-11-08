from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).parent / "kraggle_data"
OUT_DIR = Path(__file__).parent / "filtered_data"  # small enough to commit

YEARS_BACK = 5
MAX_AGE = 18  # keep people younger than this (change to 21 if needed)

CUTOFF = pd.Timestamp.today().normalize() - pd.DateOffset(years=YEARS_BACK)
CHUNK = 500_000  # rows per read, so the 1.2 GB file doesn't need to fit in memory


def filter_people():
    src = RAW_DIR / "Motor_Vehicle_Collisions_-_Person_20261028.csv"
    parts = []
    for chunk in pd.read_csv(src, chunksize=CHUNK, low_memory=False):
        chunk["CRASH_DATE"] = pd.to_datetime(chunk["CRASH_DATE"], format="%m/%d/%Y", errors="coerce")
        chunk["PERSON_AGE"] = pd.to_numeric(chunk["PERSON_AGE"], errors="coerce")
        keep = (
            (chunk["CRASH_DATE"] >= CUTOFF)
            & (chunk["PERSON_AGE"] >= 0)
            & (chunk["PERSON_AGE"] < MAX_AGE)
        )
        parts.append(chunk[keep])
    people = pd.concat(parts, ignore_index=True)
    people.to_csv(OUT_DIR / f"collisions_person_under{MAX_AGE}.csv", index=False)
    print(f"people under {MAX_AGE}: {len(people):,} rows")
    return people


def filter_crashes(collision_ids):
    src = RAW_DIR / "Motor_Vehicle_Collisions_-_Crashes_20261028.csv"
    parts = []
    for chunk in pd.read_csv(src, chunksize=CHUNK, low_memory=False):
        parts.append(chunk[chunk["COLLISION_ID"].isin(collision_ids)])
    crashes = pd.concat(parts, ignore_index=True)
    crashes.to_csv(OUT_DIR / f"collisions_crashes_under{MAX_AGE}.csv", index=False)
    print(f"crashes involving someone under {MAX_AGE}: {len(crashes):,} rows")


def filter_cafeteria():
    src = RAW_DIR / "DOHMH_School_Cafeteria_Inspections_(2020-Present)_20261104.csv"
    df = pd.read_csv(src, low_memory=False)
    dates = pd.to_datetime(df["InspectionDate"], format="%m/%d/%Y", errors="coerce")
    df = df[dates >= CUTOFF]
    df.to_csv(OUT_DIR / "cafeteria_inspections.csv", index=False)
    print(f"cafeteria inspections: {len(df):,} rows")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"keeping data from {CUTOFF.date()} onward")
    people = filter_people()
    filter_crashes(set(people["COLLISION_ID"]))
    filter_cafeteria()


if __name__ == "__main__":
    main()
