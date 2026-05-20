# LowQ Proof Ladder

LowQ claims are graded by evidence level.

## S-level: simulation and estimates

- **S0 Browser Estimate** — token/workload model only.
- **S1 Lightweight Simulation** — built-in lightweight energy/thermal model.
- **S2 Accelerator Simulation** — imported accelerator energy/performance simulator result.
- **S3 Thermal Simulation** — imported chip/package thermal simulation.
- **S4 Facility Simulation** — imported data-center or facility simulation.

## C-level: computational telemetry

- **C1 Imported Telemetry** — CSV/log import from power/temp tools.
- **C2 Vendor Counters** — DCGM/NVML/AMD SMI/RAPL/lm-sensors style counters.
- **C3 External Meter** — independent wall/device/sensor measurement.
- **C4 Formal Analyzer** — MLPerf/SPEC-style analyzer workflow.

## Claim rules

- S0/S1 may support internal product development and simulation-only claims.
- C1/C2 may support hardware-adjacent benchmark claims if telemetry quality passes.
- C3/C4 are preferred for public energy/thermal claims.
- No certificate may claim direct hardware heat reduction without telemetry or external measurement.
