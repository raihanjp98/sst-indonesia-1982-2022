import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# ----------------------------
# 1️⃣ Load data
# ----------------------------
df = pd.read_excel("sst_climatology_indonesia_monthly.xlsx")
df['year'] = df['time'].str[:4].astype(int)

# Hitung rata-rata tahunan SST
df_yearly = df.groupby('year')['sst'].mean().reset_index()

# ----------------------------
# 2️⃣ Hitung baseline WMO (1991–2020)
# ----------------------------
baseline_period = (1991, 2020)
baseline = df_yearly[(df_yearly['year'] >= baseline_period[0]) &
                     (df_yearly['year'] <= baseline_period[1])]['sst'].mean()

# Hitung anomali terhadap baseline
df_yearly['sst_anom'] = df_yearly['sst'] - baseline

# ----------------------------
# 3️⃣ Analisis tren 1982–2022 (IPCC style)
# ----------------------------
slope, intercept, r, p, stderr = linregress(df_yearly['year'],
                                            df_yearly['sst_anom'])
trend_per_decade = slope * 10

# ----------------------------
# 4️⃣ Plot IPCC-style
# ----------------------------
fig, ax = plt.subplots(figsize=(10, 5))

# Area shading baseline 1991–2020
ax.axvspan(1991, 2020, color='gray', alpha=0.15,
           label='Periode Normal (1991–2020)')

# Plot anomali SST tahunan
ax.plot(df_yearly['year'], df_yearly['sst_anom'], marker='o', color='tab:blue',
        linewidth=1.8, label='Anomali SST Tahunan')

# Plot trend line
ax.plot(df_yearly['year'], intercept + slope * df_yearly['year'],
        color='red', linewidth=2.2, linestyle='--',
        label=f'Tren 1982–2022: {trend_per_decade:.2f} °C/dekade')

# Garis nol
ax.axhline(0, color='black', linewidth=0.8, linestyle='--')

# Label dan judul
ax.set_xlabel("Tahun", fontsize=11)
ax.set_ylabel("Anomali Suhu Permukaan Laut (°C)", fontsize=11)
ax.set_title("Tren Pemanasan Suhu Permukaan Laut Indonesia (1982–2022)\n"
             "Dihitung Terhadap Baseline Klimatologi 1991–2020 (WMO Standard)",
             fontsize=13, fontweight="bold")

# Legend
ax.legend(frameon=False, fontsize=9, loc='upper left')

# Info tambahan
text_note = (f"Koefisien korelasi (r): {r:.2f}\n"
             f"Tren: {trend_per_decade:.2f} °C/dekade\n"
             f"P-value: {p:.4f}")
ax.text(0.98, 0.05, text_note, transform=ax.transAxes, fontsize=9,
        ha='right', va='bottom', bbox=dict(facecolor='white', alpha=0.8,
                                           boxstyle='round,pad=0.3'))

plt.tight_layout()
plt.savefig("SST_Indonesia_Trend_IPCCstyle.png", dpi=300)
plt.show()

print("✅ Grafik IPCC-style selesai disimpan")
print(f"Tren pemanasan laut Indonesia (1982–2022): {trend_per_decade:.2f} °C per dekade")
