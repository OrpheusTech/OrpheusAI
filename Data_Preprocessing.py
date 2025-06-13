import pandas as pd
import numpy as np

def pivot_and_clean_analyte_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset:
    - Parse dates
    - Clean '<' values
    - Pivot analytes into columns
    - Extract date features
    - Fill missing values
    """

    # Validate required columns
    required_columns = ['Result_Final_Txt', 'Samp_No', 'Location', 'Analyte', 'SampleDate_txt']
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Convert date column
    df['SampleDate'] = pd.to_datetime(df['SampleDate_txt'], errors='coerce')

    # Extract date features
    df['Year'] = df['SampleDate'].dt.year
    df['Month'] = df['SampleDate'].dt.month
    
    df['Day'] = df['SampleDate'].dt.day
    df['Quarter'] = df['SampleDate'].dt.quarter
    df['DayOfYear'] = df['SampleDate'].dt.dayofyear

    # Clean Result_Final_Txt values
    def clean_result(value):
        if isinstance(value, str) and value.startswith("<"):
            try:
                return float(value[1:])
            except ValueError:
                return np.nan
        try:
            return float(value)
        except:
            return np.nan

    df['clean_result'] = df['Result_Final_Txt'].apply(clean_result)

    # pivot analytes into columns
    pivot_df = df.pivot_table(
        index=['Samp_No', 'Location', 'Year', 'Month', 'Day', 'Quarter', 'DayOfYear'],
        columns='Analyte',
        values='clean_result',
        aggfunc='first'
    ).reset_index()

    # Fill missing analyte values using column median
    pivot_df = pivot_df.fillna(pivot_df.median(numeric_only=True))

    # Add NPK ratio if present
    if all(col in pivot_df.columns for col in ['N', 'P', 'K']):
        pivot_df['NPK_ratio'] = pivot_df['N'] / (pivot_df['P'] + pivot_df['K'] + 1e-6)

    return pivot_df


