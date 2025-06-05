import pandas as pd

def clean_soil_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and standardize soil data."""
    df = df.dropna(subset=['latitude', 'longitude', 'time'])
    df = df.fillna(df.median(numeric_only=True))
    # Standardize column names, units etc.
    df.columns = [c.strip().lower() for c in df.columns]
    # Example: convert units if needed
    # df['n'] = convert_nitrogen_units(df['n'])
    return df

def structure_soil_data(df: pd.DataFrame) -> pd.DataFrame:
    """Feature engineering for soil data."""
    # Example: calculate NPK ratios, organic matter index
    df['npk_ratio'] = df['n'] / (df['p'] + df['k'] + 1e-6)
    return df
