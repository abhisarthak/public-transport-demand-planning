# 🚍 Multimodal Transport Demand & Resilience Decision Intelligence

### Forecast → Optimize → Stress-Test → Decide

An end-to-end **Decision Intelligence framework** for multimodal passenger transportation that integrates **machine learning demand forecasting, capacity planning, optimization, disruption stress testing, Monte Carlo simulation, and interactive decision support**.

The framework is designed to help transportation planners answer a critical question:

> **How can a transport network forecast passenger demand, allocate limited capacity efficiently, and remain resilient during demand surges and operational disruptions?**

---

## 🎯 Project Highlights

- 📊 Analyzed **150,864 festival-period passengers** across **4 major transport corridors**
- 🤖 Built a **Random Forest demand forecasting model** with **MAE = 772** and **R² = 0.935**
- 📉 Reduced forecasting MAE by **60.3%** compared with a naïve baseline
- ⚠️ Identified critical corridors with up to **11,986 unmet passengers**
- 🚌 Developed fleet expansion strategies improving coverage from **79.54% to 90.20%**
- 🚆 Achieved approximately **90% service coverage** using **26 additional buses + 2 additional rail capacity units**
- 🎲 Performed **5,000 Monte Carlo simulations** to quantify operational risk
- 🚨 Estimated a **22.72% probability of network coverage falling below 70%**
- 🖥️ Built an interactive **Streamlit Decision Intelligence Dashboard**

---

## 🌐 The Decision Intelligence Pipeline

```text
Passenger Data
      │
      ▼
Demand Forecasting
      │
      ▼
Capacity & Unmet Demand Analysis
      │
      ▼
Corridor Vulnerability Identification
      │
      ▼
Fleet Expansion Optimization
      │
      ▼
Network Disruption Stress Testing
      │
      ▼
Monte Carlo Risk Analysis
      │
      ▼
Management Recommendation
```
## 🚀 Key Features

- **Demand Forecasting:** Uses a Random Forest model to forecast multimodal passenger demand and achieves an **R² of 0.935**, substantially outperforming the naïve baseline.

- **Festival Surge Analysis:** Evaluates transportation capacity under peak festival demand of **150,864 passengers**, identifying a baseline service coverage of **79.54%**.

- **Optimization-Based Fleet Planning:** Determines the additional bus and rail capacity required to achieve different service targets, from **80% to 100% coverage**.

- **Corridor Vulnerability Analysis:** Identifies critical network segments based on unmet demand, coverage levels, and contribution to total network vulnerability.

- **Resilience Stress Testing:** Evaluates the impact of simultaneous **bus and rail disruptions** using a resilience coverage matrix.

- **Monte Carlo Risk Simulation:** Performs **5,000 simulations** to quantify uncertainty, showing a mean coverage of **74.14%** and a **22.72% probability of coverage falling below 70%**.

- **Decision Intelligence Dashboard:** Integrates forecasting, optimization, scenario analysis, resilience assessment, and management recommendations into an interactive dashboard.


---

## 🏗️ System Architecture

The project is designed as an integrated **Decision Intelligence framework** where predictive analytics, optimization, simulation, and risk analysis work together to support transportation planning decisions.

```text
Historical / Synthetic Passenger Data
                │
                ▼
        Data Processing & EDA
                │
                ▼
      Demand Forecasting (ML)
                │
                ▼
    Festival Demand Estimation
                │
        ┌───────┴────────┐
        ▼                ▼
Capacity Analysis    Corridor Analysis
        │                │
        └───────┬────────┘
                ▼
      Fleet Expansion Optimization
                │
                ▼
    Network Disruption Stress Testing
                │
                ▼
       Monte Carlo Risk Simulation
                │
                ▼
     Management Decision Recommendation
```


