# LowQ ROI Methodology

The ROI calculator estimates possible savings from reduced computational waste.

## Inputs

- GPU count,
- average GPU power draw,
- monthly workload hours,
- electricity rate,
- PUE/cooling multiplier,
- current AI infrastructure spend,
- expected waste reduction scenario,
- proof grade.

## Calculations

```
active_kw = gpu_count * avg_gpu_watts / 1000
monthly_kwh = active_kw * workload_hours
facility_kwh = monthly_kwh * pue
energy_cost = facility_kwh * electricity_rate
estimated_savings = energy_cost * reduction_scenario
```

## Heat load estimate

Electrical energy consumed by compute largely becomes heat inside the facility. LowQ does not claim direct cooling reduction from estimates alone; it estimates avoidable energy/heat burden subject to proof grade.

## Lead capture

Calculator result is ungated. Detailed report export is gated.
