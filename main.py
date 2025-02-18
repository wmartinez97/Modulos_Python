from geo_utils import load_vector_data, get_basic_info, filter_by_attribute
from visualization import plot_vector_data

file_path = "data/municipios.shp"

# Cargar datos
gdf = load_vector_data(file_path)

# Visualización inicial sin filtro
plot_vector_data(gdf, title="Municipios de Colombia - Visualización Inicial")

info = get_basic_info(gdf)
print("Información del archivo:", info)

# Asegurar que 'Area_ha' es numérico
gdf["Area_ha"] = gdf["Area_ha"].astype(float)

# Filtrar polígonos con más de 500.000 ha
filtered_gdf = filter_by_attribute(gdf, 'Area_ha', 500000)
print("Elementos filtrados:", len(filtered_gdf))

# Verificar si hay elementos filtrados antes de graficar
if filtered_gdf.empty:
    print("No hay elementos que cumplan con el filtro. Ajusta el valor.")
else:
    plot_vector_data(filtered_gdf, title="Municipios de Colombia con un área mayor a 500.000 ha")