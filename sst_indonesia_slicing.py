import xarray as xr
import pandas as pd

# 1. Buka dataset NetCDF
ds = xr.open_dataset("sst.mnmean.nc", use_cftime=True)

# 2. Subset wilayah Indonesia (lon: 90–150E, lat: -15–15N)
subset = ds.sel(lon=slice(95, 141), lat=slice(6, -11))  # lat dibalik: utara ke selatan

# 3. Ambil variabel SST
sst_subset = subset['sst']

# 4. Konversi ke DataFrame
df = sst_subset.to_dataframe().reset_index()

# 5. Simpan ke CSV dan Excel
df.to_excel("sst_climatology_indonesia_monthly.xlsx", index=False)

print("File berhasil disimpan:")
print(" - sst_climatology_indonesia_monthly.xlsx")
