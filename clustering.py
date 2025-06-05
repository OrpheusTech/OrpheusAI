from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def cluster_soil(df: pd.DataFrame, n_clusters: int = 5) -> pd.DataFrame:
    """Apply unsupervised clustering to soil features."""
    features = ['n', 'p', 'k', 'organic_matter', 'ph', 'cadmium', 'nickel', 'chromium']
    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])
    km = KMeans(n_clusters=n_clusters, random_state=0)
    df['cluster'] = km.fit_predict(X)
    return df

def reduce_dimensionality(df: pd.DataFrame, n_components=2):
    features = ['n', 'p', 'k', 'organic_matter', 'ph', 'cadmium', 'nickel', 'chromium']
    scaler = StandardScaler()
    X = scaler.fit_transform(df[features])
    pca = PCA(n_components=n_components)
    coords = pca.fit_transform(X)
    df['pc1'] = coords[:, 0]
    df['pc2'] = coords[:, 1]
    return df
