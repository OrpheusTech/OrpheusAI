import geopandas as gpd

def integrate_time_location(df: pd.DataFrame) -> gpd.GeoDataFrame:
    """Turn dataframe into GeoDataFrame with timestamps."""
    gdf = gpd.GeoDataFrame(
        df,
        geometry=gpd.points_from_xy(df.longitude, df.latitude),
        crs='EPSG:4326'
    )
    gdf['time'] = pd.to_datetime(gdf['time'])
    return gdf

def detect_yield_drops(gdf: gpd.GeoDataFrame, yield_col='yield'):
    """Identify zones/times of yield drops."""
    # Example: rolling window or spatial clustering
    return gdf[gdf[yield_col] < gdf[yield_col].quantile(0.1)]
