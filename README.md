# 🌊 Sea Surface Temperature (SST) Analysis over Indonesian Waters (1982–2022)

This repository contains a collection of Python scripts for analyzing long-term **Sea Surface Temperature (SST)** variability across Indonesian waters from **1982 to 2022**.  
The project aims to understand the **warming trend** and **spatial–temporal patterns** of SST using reanalysis datasets (e.g., NOAA OISST).

---

## 📁 Repository Structure

| File | Description |
|------|--------------|
| `sst_indonesia_slicing.py` | Extracts and preprocesses SST data for the Indonesian region from global NetCDF datasets. |
| `sst_indonesia_trend.py` | Calculates long-term SST trends using linear regression and computes correlation statistics. |
| `sst_indonesia_visualization.py` | Generates time-series and spatial visualizations of SST variations and trends. |

---

## 🧰 Requirements

Make sure you have the following Python packages installed:

```bash
pip install numpy pandas xarray netCDF4 matplotlib cmocean cartopy scipy
````
---

## ⚙️ Usage

### 1. **Slicing SST Data**

Extract the Indonesian region from global SST datasets.

```bash
python sst_indonesia_slicing.py
```

### 2. **Trend Analysis**

Compute SST trend and correlation for the 1982–2022 period.

```bash
python sst_indonesia_trend.py
```

### 3. **Visualization**

Generate maps, time series, and GIFs of SST variation.

```bash
python sst_indonesia_visualization.py
```

---

## 📊 Results Summary

* SST data covers **1982–2022** using NOAA OISST dataset.
* Linear regression shows a **warming trend of +0.11°C** over the last 40 years.
* The correlation between SST and time indicates a consistent **positive trend**, suggesting long-term ocean surface warming in Indonesian waters.

---

## 🌍 Context

This project supports **climate variability and change studies** across the Indonesian region, particularly within the context of:

* ENSO (El Niño–Southern Oscillation)
* Indian Ocean Dipole (IOD)
* Long-term ocean surface warming trends

---

## 🧑‍💻 Author

**Raihan Jauhari Pratama** | Oceanographic Engineer | Data, GIS, and Ocean Enthusiast
📫 [LinkedIn](www.linkedin.com/in/raihan-jauhari-pratama-a4a8b51a5)

---

## 📜 License

This project is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
© 2025 Raihan Jauhari Pratama
