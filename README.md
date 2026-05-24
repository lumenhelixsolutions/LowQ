# LowQ — AI Waste-Heat Reduction System

**Lower compute waste before it becomes heat.**

LowQ is an AI infrastructure optimization layer for reducing wasteful computation, repeated context processing, memory movement, and inefficient workload routing before those costs become power draw, heat, and cooling burden.

This repository is the **Phase 1 Proof Launch Stack**. It packages the public proof lab, ROI calculator, landing page copy, certificate schema, pilot kit, licensing structure, and go-to-market material.

## What is included

- `lab/lowq_lab.html` — robust single-file proof lab.
- `roi/lowq_roi_calculator.html` — static MVP calculator with gated report export.
- `landing/lowq_landing_page.html` — launch landing page preview.
- `schemas/lowq_certificate.schema.json` — proof certificate schema.
- `docs/` — architecture, proof ladder, ROI methodology, claim guardrails, pilot deployment, and marketplace readiness.
- `assets/campaign/` — LinkedIn ad copy, launch posts, and creative direction.
- `pilot/` — two-week pilot kit and success criteria.
- `marketplace/` — AWS/GCP onboarding readiness checklist.

## Start here

Open these files directly in a browser:

1. `landing/lowq_landing_page.html`
2. `roi/lowq_roi_calculator.html`
3. `lab/lowq_lab.html`

No build system is required for Phase 1.

## Product hierarchy

- **LowQ** — waste-heat reduction system.
- **LowQ Lab** — benchmark/proof interface.
- **LowQ Engine** — optimization layer.
- **LowQ Bridge** — telemetry connector.
- **LowQ SimTwin** — simulation/pre-hardware proof layer.
- **LowQ Certificate** — evidence artifact.
- **LowQ ROI Calculator** — business-case generator.
- **LowQ Pilot** — enterprise validation package.

## Proof stance

LowQ does not claim hardware heat reduction without telemetry or formal measurement. Browser estimates are labeled as estimates. Simulation is labeled as simulation. Telemetry and external meter data increase confidence levels.

## Next Run Plan

### 1) Set explicit run goals (pass/fail before execution)

Use these target gates:

- **Primary:** estimated energy reduction ≥ **2.0%** (up from 1.57%)
- **Secondary:** telemetry-aware workload reduction ≥ **1.0%** (up from 0.78%)
- **Stability:** no regression in p95 latency or error rate
- **Evidence quality:** move beyond **S0-LONG-BENCH** by passing telemetry quality gate

### 2) Run matrix (small, controlled, informative)

Use a controlled matrix instead of one large undifferentiated run:

- **A/B:** `LowQ OFF` vs `LowQ ON`
- **Workload profiles:** light, medium, heavy
- **Trials per cell:** 50

Total planned trials: **300** (`2 × 3 × 50`).

Execution strategy:

- Use a **fixed seed set** for reproducibility.
- Add one **random-seed pass** for robustness.

### 3) Instrumentation to add now

Capture the following per trial:

- tokens/work-units processed
- dedupe hit rate
- routing decision counts
- memory movement proxy (copy/transfer counts)
- estimated energy score inputs (all components)
- optional hardware telemetry when available:
  - package power
  - node power
  - thermal sensor snapshots

### 4) Output schema (JSONL for automatic analysis)

Write one JSON object per trial as a JSONL row with:

- `run_id`
- `trial_id`
- `config_id`
- `seed`
- `baseline_or_treatment`
- `workload_class`
- `metrics.workload_reduction`
- `metrics.work_unit_reduction`
- `metrics.energy_estimate_reduction`
- `metrics.thermal_shadow_reduction`
- `guardrails.p95_latency_ms`
- `guardrails.error_rate`
- `telemetry_quality_gate.pass`
- `telemetry_quality_gate.reason`

Example row:

```json
{"run_id":"run_2026_05_23_a","trial_id":17,"config_id":"on_heavy","seed":424242,"baseline_or_treatment":"treatment","workload_class":"heavy","metrics":{"workload_reduction":0.011,"work_unit_reduction":0.016,"energy_estimate_reduction":0.021,"thermal_shadow_reduction":0.028},"guardrails":{"p95_latency_ms":182,"error_rate":0.0012},"telemetry_quality_gate":{"pass":true,"reason":"telemetry complete and analyzer checks passed"}}
```

### 5) Analysis to run immediately after completion

For each metric, compute:

- mean
- standard deviation
- 95% confidence interval

Also compute:

- effect size vs baseline per workload class
- significance test (choose one method and keep it consistent: bootstrap or t-test)
- failure slice: trials that failed telemetry quality gate, grouped by reason/workload/config

### 6) Decision rule (go / no-go)

- **Go** if:
  - estimated energy improvement confidence interval excludes 0,
  - guardrails remain stable,
  - telemetry quality gate pass rate is high (target: **>95%**).

- **No-go / iterate** if:
  - gains are seed-sensitive,
  - confidence interval overlaps 0,
  - or telemetry quality gate failures cluster in specific workload tiers.

## License stance

Noncommercial research, education, testing, remixing, and experimentation are encouraged. Commercial deployment, resale, hosted services, enterprise optimization, or use inside paid infrastructure requires a commercial license.

See `LICENSE.md` and `COMMERCIAL_LICENSE.md`.

## Launch line

**Run the workload. Measure the delta. Export the proof.**
