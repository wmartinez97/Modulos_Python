import matplotlib.pyplot as plt

def plot_vector_data(gdf, title):
    """Dibuja un mapa del archivo vectorial."""
    fig, ax = plt.subplots(figsize=(10, 6))
    gdf.plot(ax=ax, edgecolor='black', color='purple')

    ax.set_aspect('equal')

    ax.set_title(title)

    ax.axis("off")

    plt.show()