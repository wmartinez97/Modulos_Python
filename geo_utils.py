import geopandas as gpd

def load_vector_data(file_path):
    """Carga un archivo vectorial y devuelve un GeoDataFrame."""
    return gpd.read_file(file_path)

def get_basic_info(gdf):
    """Devuelve información básica del GeoDataFrame."""
    return {
        "Número de elementos": len(gdf),
        "Sistema de coordenadas": gdf.crs,
        "Columnas": gdf.columns.tolist()
    }

def filter_by_attribute(gdf, column, value):
    """Filtra el GeoDataFrame según un valor en una columna específica."""
    return gdf[gdf[column] > value]