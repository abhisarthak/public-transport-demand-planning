"""
Synthetic Public Transport Demand Generator
Kharagpur -> Kolkata Corridor

Generates a reproducible 90-day multimodal passenger-demand dataset
for rail and bus services across the corridor.
"""

from pathlib import Path

import numpy as np
import pandas as pd


# ============================================================
# 1. CONFIGURATION
# ============================================================

RANDOM_SEED = 42
N_DAYS = 90

np.random.seed(RANDOM_SEED)

START_DATE = "2025-08-01"

# Corridor structure
OD_SEGMENTS = [
    ("Kharagpur", "Midnapore"),
    ("Midnapore", "Uluberia"),
    ("Uluberia", "Howrah"),
    ("Howrah", "Kolkata"),
]

# Base daily passenger demand by OD segment and mode
BASE_DEMAND = {
    ("Kharagpur", "Midnapore", "Rail"): 12000,
    ("Kharagpur", "Midnapore", "Bus"): 8000,

    ("Midnapore", "Uluberia", "Rail"): 14000,
    ("Midnapore", "Uluberia", "Bus"): 6500,

    ("Uluberia", "Howrah", "Rail"): 13000,
    ("Uluberia", "Howrah", "Bus"): 8000,

    ("Howrah", "Kolkata", "Rail"): 15000,
    ("Howrah", "Kolkata", "Bus"): 6500,
}

# Random variability by mode
NOISE_STD = {
    "Rail": 0.05,
    "Bus": 0.12,
}

# Weekend demand reduction
WEEKEND_FACTOR = 0.85

# Stress/festival demand increase
FESTIVAL_FACTOR = 1.80

# Explicit synthetic stress/festival dates
FESTIVAL_DATES = [
    "2025-08-02",
    "2025-08-15",
    "2025-09-05",
    "2025-09-15",
    "2025-10-02",
    "2025-10-05",
    "2025-10-20",
]


# ============================================================
# 2. DATA GENERATION
# ============================================================

def generate_synthetic_data():
    """
    Generate synthetic multimodal passenger demand.
    """

    dates = pd.date_range(
        start=START_DATE,
        periods=N_DAYS,
        freq="D"
    )

    records = []

    for date in dates:

        date_string = date.strftime("%Y-%m-%d")

        # Weekend indicator
        is_weekend = date.dayofweek >= 5

        # Festival/stress indicator
        is_festival = date_string in FESTIVAL_DATES

        # Calendar multiplier
        if is_festival:
            calendar_factor = FESTIVAL_FACTOR
        elif is_weekend:
            calendar_factor = WEEKEND_FACTOR
        else:
            calendar_factor = 1.0

        for origin, destination in OD_SEGMENTS:

            for mode in ["Rail", "Bus"]:

                base_demand = BASE_DEMAND[
                    (origin, destination, mode)
                ]

                # Random stochastic variation
                noise = np.random.normal(
                    loc=0,
                    scale=NOISE_STD[mode]
                )

                passengers = (
                    base_demand
                    * calendar_factor
                    * (1 + noise)
                )

                # Passenger count cannot be negative
                passengers = max(0, passengers)

                records.append(
                    {
                        "date": date,
                        "origin": origin,
                        "destination": destination,
                        "mode": mode,
                        "passengers": round(passengers),
                        "festival": int(is_festival),
                        "weekend": int(is_weekend),
                    }
                )

    return pd.DataFrame(records)


# ============================================================
# 3. DATA VALIDATION
# ============================================================

def validate_dataset(df):
    """
    Perform basic quality checks on the generated dataset.
    """

    expected_rows = N_DAYS * len(OD_SEGMENTS) * 2

    assert len(df) == expected_rows, (
        f"Expected {expected_rows} rows, "
        f"but generated {len(df)} rows."
    )

    assert df["passengers"].notna().all(), (
        "Passenger demand contains missing values."
    )

    assert (df["passengers"] >= 0).all(), (
        "Passenger demand contains negative values."
    )

    assert df["mode"].isin(["Rail", "Bus"]).all(), (
        "Unexpected transport mode detected."
    )

    print("\nDataset validation passed.")


# ============================================================
# 4. SAVE DATASET
# ============================================================

def save_dataset(df):

    project_root = Path(__file__).resolve().parents[2]

    output_directory = project_root / "data" / "synthetic"

    output_directory.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = (
        output_directory
        / "transport_demand_90days.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(f"\nDataset saved to:")
    print(output_file)


# ============================================================
# 5. SUMMARY
# ============================================================

def print_summary(df):

    print("\n" + "=" * 60)
    print("SYNTHETIC TRANSPORT DEMAND DATASET")
    print("=" * 60)

    print(f"Number of observations : {len(df):,}")
    print(
        f"Date range             : "
        f"{df['date'].min().date()} "
        f"to "
        f"{df['date'].max().date()}"
    )

    print(
        f"OD segments            : "
        f"{df[['origin', 'destination']].drop_duplicates().shape[0]}"
    )

    print(
        f"Transport modes        : "
        f"{', '.join(df['mode'].unique())}"
    )

    print(
        f"Festival observations  : "
        f"{df['festival'].sum():,}"
    )

    print(
        f"Total passengers       : "
        f"{df['passengers'].sum():,}"
    )

    print("\nAverage demand by mode:")

    mode_summary = (
        df.groupby("mode")["passengers"]
        .agg(["mean", "std", "min", "max"])
        .round(2)
    )

    print(mode_summary)

    print("\nFirst 10 observations:")
    print(df.head(10).to_string(index=False))

    print("=" * 60)


# ============================================================
# 6. MAIN PROGRAM
# ============================================================

if __name__ == "__main__":

    print("Generating synthetic transport demand...")

    data = generate_synthetic_data()

    validate_dataset(data)

    print_summary(data)

    save_dataset(data)

    print("\nData generation completed successfully.")