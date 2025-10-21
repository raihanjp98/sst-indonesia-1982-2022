import ssl
import pandas as pd
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib
matplotlib.use('Agg')

# ---------------------------
# 0) SSL bypass (optional)
# ---------------------------
ssl._create_default_https_context = ssl._create_unverified_context

# ---------------------------
# 1) Load data
# ---------------------------
df = pd.read_excel("sst_climatology_indonesia_monthly.xlsx")

# Pastikan kolom 'time' ada dan bisa di-parse ke datetime
df['time'] = pd.to_datetime(df['time'])
df['year'] = df['time'].dt.year

print("Tahun unik dalam data:", sorted(df['year'].unique()))

# Colorbar scale fixed
sst_min, sst_max = 27, 31

# ---------------------------
# 2) Figure layout
# ---------------------------
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([95, 141, -11, 6], crs=ccrs.PlateCarree())

# Axis khusus colorbar
cax = fig.add_axes([0.92, 0.2, 0.02, 0.6])

# Colormap dan normalization tetap
cmap = plt.cm.turbo
norm = matplotlib.colors.Normalize(vmin=sst_min, vmax=sst_max)

# Static colorbar
sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
cbar = fig.colorbar(sm, cax=cax, orientation="vertical")
cbar.set_label("Suhu Permukaan Laut (°C)")

# Static title
fig.suptitle(
    "Rata-Rata Suhu Permukaan Laut (SST) Tahunan Indonesia "
    "Periode 1982 - 2022\n(Source: PSL NOAA OISST V2)",
    fontsize=12, fontweight="bold"
)


# ---------------------------
# 3) Update function
# ---------------------------
def update(year):
    ax.clear()
    ax.set_extent([95, 141, -11, 6], crs=ccrs.PlateCarree())

    # Basemap
    ax.add_feature(cfeature.LAND.with_scale("10m"), facecolor='white',
                   zorder=2)
    ax.add_feature(cfeature.BORDERS.with_scale("10m"), linestyle=':',
                   linewidth=0.5, zorder=3)
    ax.coastlines(resolution='10m', color='black', linewidth=0.6, zorder=3)

    # Garis ekuator
    ax.axhline(0, color='black', linewidth=0.8, linestyle='--', zorder=4)

    # Axis ticks
    xticks = np.arange(95, 141, 5)
    yticks = np.arange(-10, 6.1, 2.5)
    ax.set_xticks(xticks, crs=ccrs.PlateCarree())
    ax.set_yticks(yticks, crs=ccrs.PlateCarree())
    ax.xaxis.set_major_formatter(LongitudeFormatter(zero_direction_label=True))
    ax.yaxis.set_major_formatter(LatitudeFormatter())
    ax.tick_params(axis='x', labelsize=9)
    ax.tick_params(axis='y', labelsize=9)

    # Filter data tahunan
    df_y = df[df['year'] == year]
    if df_y.empty:
        print(f"⚠️ Tidak ada data untuk tahun {year}")
        return

    # Pivot ke grid
    sst_grid = df_y.pivot_table(index='lat', columns='lon', values='sst')

    # Plot SST
    pcm = ax.pcolormesh(
        sst_grid.columns, sst_grid.index, sst_grid.values,
        cmap=cmap, norm=norm, shading="auto", zorder=1
    )

    # Contour isoline setiap 1°C
    levels = np.arange(sst_min, sst_max + 1, 1)
    cs = ax.contour(
        sst_grid.columns, sst_grid.index, sst_grid.values,
        levels=levels, colors='k', linewidths=0.4, alpha=0.6, zorder=2
    )
    try:
        ax.clabel(cs, inline=True, fontsize=7, fmt="%d°C")
    except Exception:
        pass

    # Teks tahun
    ax.text(
        0.02, 0.05, f"Tahun {year}",
        transform=ax.transAxes, fontsize=12, fontweight="bold",
        bbox=dict(facecolor="white", alpha=0.8, boxstyle="round")
    )

    print(f"✅ Frame tahun {year} selesai diproses.")
    return [pcm]


# ---------------------------
# 4) Jalankan animasi
# ---------------------------
years = sorted(df['year'].unique())
ani = animation.FuncAnimation(
    fig, update, frames=years, interval=600, blit=True
)

ani.save("SST_Indonesia_1982_2022.gif", writer="pillow", fps=2)

print("✅ Animasi tahunan SST Indonesia berhasil disimpan")
plt.close()
