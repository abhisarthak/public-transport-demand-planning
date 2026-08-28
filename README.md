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
---

## 📊 Dataset & Scenario Design

This project models multimodal passenger transportation across four interconnected corridors:

- **Howrah → Kolkata**
- **Kharagpur → Midnapore**
- **Midnapore → Uluberia**
- **Uluberia → Howrah**

The analysis integrates passenger demand, available bus capacity, rail capacity, festival demand surges, and transportation disruption scenarios.

### Core Variables

| Variable | Description |
|---|---|
| `passenger_demand` | Estimated passenger demand for a corridor |
| `festival_demand` | Increased demand during festival periods |
| `bus_capacity` | Passenger capacity provided by bus services |
| `rail_capacity` | Passenger capacity provided by rail services |
| `total_capacity` | Combined multimodal transportation capacity |
| `unmet_demand` | Passengers unable to be served |
| `coverage_pct` | Percentage of total demand successfully served |
| `bus_disruption` | Reduction in available bus capacity |
| `rail_disruption` | Reduction in available rail capacity |

### Scenario Framework

The system evaluates transportation decisions under multiple operating conditions:

| Scenario | Description |
|---|---|
| **Normal Operations** | Current fleet operating under baseline demand |
| **Festival Surge** | Increased passenger demand during high-demand periods |
| **Capacity Expansion** | Additional buses and rail capacity introduced |
| **Network Disruption** | Bus and rail capacity reduced by disruption scenarios |
| **Monte Carlo Simulation** | Thousands of uncertain demand and disruption scenarios |

> **Note:** The project uses a scenario-based transportation dataset designed to evaluate the complete Decision Intelligence pipeline, including forecasting, optimization, resilience testing, and risk analysis.


---

## 🤖 Demand Forecasting & Machine Learning

The first stage of the Decision Intelligence pipeline forecasts passenger demand before capacity decisions are made.

A **Random Forest Regressor** was developed and evaluated against a **Naïve Baseline model** to determine whether machine learning could provide a meaningful improvement in forecasting accuracy.

### Model Performance

| Model | MAE | R² |
|---|---:|---:|
| Naïve Baseline | 1,942 | 0.263 |
| Random Forest | 772 | **0.935** |

### Performance Improvement

Compared with the naïve baseline, the Random Forest model achieved:

- **60.26% reduction in Mean Absolute Error (MAE)**
- **70.32% reduction in RMSE**
- **R² improvement from 0.263 to 0.935**

### Why Forecasting Matters

Accurate demand forecasting is critical because transportation capacity decisions must be made **before passenger demand materializes**.

The forecasted demand is subsequently used to:

1. Estimate festival-period passenger demand
2. Calculate capacity shortages and unmet demand
3. Identify vulnerable transportation corridors
4. Determine additional bus and rail capacity requirements
5. Evaluate network resilience under disruption scenarios

> **Decision Insight:** The forecasting model transforms historical passenger patterns into an actionable estimate of future transportation demand, providing the foundation for downstream optimization and resilience analysis.

---

## 🚍 Festival Capacity & Corridor Vulnerability Analysis

Using the forecasted festival demand, the system evaluates whether the existing multimodal transportation network has sufficient capacity to serve passengers.

### Network-Level Capacity Gap

| Metric | Value |
|---|---:|
| **Festival Passenger Demand** | **150,864** |
| **Current Multimodal Capacity** | **120,000** |
| **Unmet Passenger Demand** | **30,864** |
| **Current Network Coverage** | **79.54%** |

The baseline analysis shows that the existing transportation network cannot fully absorb the projected festival demand, leaving more than **30,000 passengers unserved**.

### Corridor-Level Performance

| Corridor | Festival Demand | Unmet Demand | Coverage |
|---|---:|---:|---:|
| Howrah → Kolkata | 37,986 | **11,986** | **68.46%** |
| Midnapore → Uluberia | 36,963 | **10,963** | **70.35%** |
| Uluberia → Howrah | 38,555 | 7,655 | 80.15% |
| Kharagpur → Midnapore | 37,360 | 260 | **99.30%** |

### Critical Corridor Identification

The analysis identifies **Howrah → Kolkata** as the most vulnerable corridor.

- **11,986 passengers remain unserved**
- Only **68.46% service coverage**
- Accounts for approximately **38.84% of total network unmet demand**

This demonstrates why uniform fleet expansion is inefficient. Additional transportation capacity should instead be **targeted toward the corridors experiencing the highest passenger shortages**.

> **Decision Insight:** Corridor-level analysis converts a network-wide capacity shortage into a prioritized intervention strategy, identifying where additional buses and rail capacity can generate the greatest service improvement.


---

## ⚙️ Fleet Expansion Optimization

The optimization framework determines the additional transportation resources required to achieve different passenger service coverage targets during the festival demand surge.

The model jointly considers:

- Bus fleet expansion
- Rail fleet expansion
- Service capacity constraints
- Passenger demand
- Modal substitution
- Unmet demand
- Operating cost

### Capacity Expansion Scenarios

| Target Coverage | Additional Buses | Additional Rail Vehicles | Final Bus Fleet | Final Rail Fleet | Achieved Coverage | Unmet Demand | Operating Cost |
|---|---:|---:|---:|---:|---:|---:|---:|
| **80%** | 0 | 1 | 40 | 51 | **80.87%** | 28,864 | 1,216 |
| **90%** | 26 | 2 | 66 | 52 | **90.20%** | 14,789 | 1,492 |
| **95%** | 41 | 2 | 81 | 52 | **95.17%** | 7,289 | 1,642 |
| **100%** | 57 | 2 | 97 | 52 | **100.00%** | 0 | 1,788 |

### Cost–Service Trade-off

Increasing service coverage requires additional transportation resources and operating expenditure.

From the **80% baseline scenario**:

- Achieving **90% coverage** recovers an additional **14,075 passengers**
- Achieving **95% coverage** recovers an additional **21,575 passengers**
- Achieving **100% coverage** eliminates all **28,864 unmet passengers**

The marginal cost of recovering additional passenger demand remains approximately:

- **19.61 cost units per 1,000 passengers recovered** for 90% coverage
- **19.75 cost units per 1,000 passengers recovered** for 95% coverage
- **19.82 cost units per 1,000 passengers recovered** for 100% coverage

### Key Optimization Insight

The results demonstrate that capacity planning should not be treated as a simple objective of maximizing fleet size.

Instead, the framework allows decision-makers to select an appropriate balance between:

**Passenger service level ↔ Additional fleet investment ↔ Operating cost**

> **Decision Insight:** A 90–95% service coverage target provides a strong planning range, substantially reducing unmet passenger demand while avoiding the maximum fleet expansion required for full 100% coverage.

---

## 🔄 Modal Substitution Analysis

During extreme demand conditions, passengers may be shifted from an overloaded transport mode to another mode with available capacity.

The optimization framework therefore evaluates **Bus → Rail modal substitution**, subject to passenger shifting constraints and available rail capacity.

### Modal Shift Scenarios

| Maximum Modal Shift | Passengers Shifted | Unmet Demand | Coverage | Operating Cost |
|---|---:|---:|---:|---:|
| **0%** | 0 | 32,881 | 78.20% | 1,200 |
| **10%** | 2,395 | 30,864 | **79.54%** | 1,200 |
| **20%** | 2,395 | 30,864 | **79.54%** | 1,200 |
| **30%** | 2,395 | 30,864 | **79.54%** | 1,200 |
| **40%** | 2,395 | 30,864 | **79.54%** | 1,200 |

### Key Findings

Allowing just **10% modal substitution**:

- Shifted **2,395 passengers** from bus to rail
- Reduced unmet demand by approximately **2,017 passengers**
- Improved network coverage from **78.20% to 79.54%**
- Required **no additional operating cost**

Increasing the allowed modal shift beyond **10% produced no further improvement**, indicating that the network had already exhausted the available opportunities for beneficial passenger redistribution.

### Corridor-Level Modal Shifts

The largest passenger shifts occurred on:

- **Midnapore → Uluberia:** 1,154 passengers shifted
- **Uluberia → Howrah:** 1,241 passengers shifted

### Decision Insight

> **Modal substitution provides a low-cost resilience mechanism by redistributing passengers toward available capacity before investing in additional transportation resources.**

However, the results also show an important limitation:

> **Modal substitution alone cannot solve a structural capacity shortage. Once available spare capacity is exhausted, additional fleet expansion becomes necessary.**


---

## 🛡️ Network Resilience & Disruption Analysis

Transportation networks must continue operating even when part of the fleet becomes unavailable.

The framework evaluates network performance under multiple **bus and rail disruption scenarios**, ranging from **0% to 30% service disruption**.

### Disruption Scenarios Evaluated

The model simulates:

- Bus fleet disruptions
- Rail fleet disruptions
- Combined bus and rail disruptions
- Capacity reduction under each scenario
- Passenger modal substitution
- Resulting unmet demand and network coverage

### Baseline Network Performance

Under normal festival operations:

| Metric | Value |
|---|---:|
| Bus Services Available | 400 |
| Rail Services Available | 100 |
| Total Network Capacity | 120,000 |
| Unmet Demand | 30,864 |
| Network Coverage | **79.54%** |

---

### Impact of Bus Disruptions

| Bus Disruption | Capacity | Unmet Demand | Coverage |
|---|---:|---:|---:|
| 0% | 120,000 | 30,864 | **79.54%** |
| 10% | 118,000 | 32,864 | 78.22% |
| 20% | 116,000 | 34,864 | 76.89% |
| 30% | 114,000 | 36,864 | **75.56%** |

Even with a **30% bus disruption**, the network retains relatively higher coverage because rail continues to provide substantial passenger capacity.

---

### Impact of Rail Disruptions

| Rail Disruption | Capacity | Unmet Demand | Coverage |
|---|---:|---:|---:|
| 0% | 120,000 | 30,864 | **79.54%** |
| 10% | 110,000 | 40,864 | 72.91% |
| 20% | 100,000 | 50,864 | 66.28% |
| 30% | 90,000 | 60,864 | **59.66%** |

Rail disruptions have a significantly larger impact on network performance because rail services carry substantially higher passenger capacity per service.

---

### Combined Disruption Resilience Matrix

| Bus Disruption ↓ / Rail Disruption → | 0% | 10% | 20% | 30% |
|---|---:|---:|---:|---:|
| **0%** | 79.54% | 72.91% | 66.28% | 59.66% |
| **10%** | 78.22% | 71.59% | 64.96% | 58.33% |
| **20%** | 76.89% | 70.26% | 63.63% | 57.00% |
| **30%** | 75.56% | 68.94% | 62.31% | **55.68%** |

### Key Findings

- A **30% bus disruption** reduces coverage by approximately **4 percentage points**
- A **30% rail disruption** reduces coverage by nearly **20 percentage points**
- The worst-case combined disruption reduces coverage to only **55.68%**
- Rail availability is therefore identified as the **dominant resilience factor** in the multimodal network

> **Resilience Insight:** The network is considerably more sensitive to rail disruptions than bus disruptions. This suggests that protecting rail operations and maintaining contingency rail capacity should be a strategic priority during extreme demand events.

---

## 🎲 Monte Carlo Risk Simulation

Deterministic optimization provides a solution for a specific demand and disruption scenario. However, real transportation systems operate under uncertainty.

To evaluate network performance under uncertain conditions, the framework performs a **Monte Carlo simulation with 5,000 iterations**.

### Simulation Inputs

| Parameter | Configuration |
|---|---:|
| **Number of Simulations** | **5,000** |
| Demand Uncertainty | **±10%** |
| Bus Disruption Levels | 0%, 10%, 20%, 30% |
| Rail Disruption Levels | 0%, 10%, 20%, 30% |

The disruption scenarios were sampled using the following probability distribution:

| Disruption Level | Probability |
|---|---:|
| 0% | 60% |
| 10% | 20% |
| 20% | 12% |
| 30% | 8% |

Each simulation generates a different combination of:

- Passenger demand uncertainty
- Bus service disruption
- Rail service disruption
- Available transportation capacity
- Modal substitution opportunities
- Resulting unmet passenger demand

---

### Monte Carlo Performance Summary

| Metric | Mean | Minimum | Maximum |
|---|---:|---:|---:|
| **Forecast Demand** | 150,836 | 140,557 | 161,493 |
| **Network Capacity** | 111,901 | 84,000 | 120,000 |
| **Unmet Demand** | 39,051 | 24,077 | 72,761 |
| **Network Coverage** | **74.14%** | **53.59%** | **83.16%** |
| **Operating Cost** | 1,118.88 | 840 | 1,200 |

---

### Risk Indicators

| Risk Metric | Result |
|---|---:|
| **Mean Coverage** | **74.14%** |
| **Median Coverage** | **76.68%** |
| **5th Percentile Coverage** | **59.42%** |
| **Probability of Coverage < 70%** | **22.72%** |
| **Probability of Coverage < 75%** | **41.24%** |
| **Probability of Unmet Demand > 30,000** | **83.42%** |
| **Worst Simulated Coverage** | **53.59%** |
| **Worst Simulated Unmet Demand** | **72,761 passengers** |

### Key Findings

The Monte Carlo analysis shows that the network's deterministic performance can significantly overestimate real-world service reliability.

Although the baseline festival scenario achieves approximately **79.54% coverage**, the average coverage under demand uncertainty and disruption falls to only **74.14%**.

In the worst simulated scenario:

- Network coverage falls to **53.59%**
- More than **72,000 passengers remain unserved**
- Available capacity drops to **84,000 passengers**

> **Risk Insight:** Planning based only on average demand and deterministic capacity can underestimate operational risk. The Monte Carlo framework quantifies the probability of poor network performance and helps decision-makers prepare for low-probability, high-impact disruption scenarios.

---

## 📉 Resilience Score & Risk Classification

Beyond measuring unmet demand and service coverage, the framework converts simulation outcomes into interpretable **resilience and risk indicators**.

This allows decision-makers to understand not only the expected network performance, but also the severity and frequency of performance deterioration under uncertainty.

### Resilience Loss Analysis

Resilience loss measures the reduction in network performance relative to the baseline operating condition.

| Metric | Result |
|---|---:|
| **Mean Resilience Loss** | **5.40 percentage points** |
| **Median Resilience Loss** | **2.87 percentage points** |
| **95th Percentile Loss** | **20.12 percentage points** |
| **Maximum Resilience Loss** | **25.95 percentage points** |

The difference between the median and the 95th percentile resilience loss highlights an important risk characteristic:

> Most scenarios experience relatively moderate performance degradation, but a smaller number of disruption scenarios can produce severe service deterioration.

---

### Resilience Score

The simulation outcomes were further converted into a resilience score representing the ability of the transportation network to maintain performance under uncertain demand and disruption conditions.

| Metric | Resilience Score |
|---|---:|
| **Mean Score** | **93.22** |
| **5th Percentile Score** | **74.70** |
| **Minimum Score** | **67.37** |

While the average resilience score remains high, the lower-tail results indicate that severe disruption combinations can substantially reduce network performance.

---

### Risk Classification

The **5,000 Monte Carlo simulations** were classified into four operational risk categories.

| Risk Category | Simulations | Percentage |
|---|---:|---:|
| 🟢 **Stable** | 2,938 | **58.76%** |
| 🟡 **Moderate Risk** | 926 | **18.52%** |
| 🟠 **High Risk** | 828 | **16.56%** |
| 🔴 **Critical** | 308 | **6.16%** |

### Key Insight

The network operates under stable conditions in approximately **59% of simulated scenarios**.

However:

- **41.24% of scenarios** experience some level of elevated operational risk
- **22.72% of simulations** fall below **70% service coverage**
- **6.16% of scenarios** enter the **critical risk category**

> **Decision Insight:** Average performance alone can create a false sense of security. The risk classification framework reveals the probability of severe operational degradation and helps planners design contingency capacity for high-impact scenarios.
