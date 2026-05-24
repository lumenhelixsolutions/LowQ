# LowQ Next Run Plan (Operational)

This document operationalizes the Next Run Plan from the root `README.md` into executable steps, run controls, and analysis rules.

## Scope and intent

- Convert benchmark-estimated gains into stronger statistical evidence.
- Preserve claim guardrails: no direct hardware heat claims without telemetry or analyzer evidence that passes quality gate.
- Maintain reproducibility and comparability across run batches.

## Step 1 — Define pass/fail gates before execution

Set and freeze these acceptance gates before any run starts:

- Primary target: `energy_estimate_reduction >= 0.020` (2.0%)
- Secondary target: `workload_reduction >= 0.010` (1.0%)
- Stability target: no regression in p95 latency or error rate vs baseline
- Evidence target: telemetry quality gate pass and movement beyond S0-LONG-BENCH

Record these values into run metadata and do not change during the run.

## Step 2 — Execute controlled run matrix

Matrix:

- Treatments: `off`, `on`
- Workload classes: `light`, `medium`, `heavy`
- Trials per cell: `50`

Total planned trials: `300`.

Execution controls:

- Use fixed seeds for the primary matrix.
- Add one random-seed robustness pass after the fixed-seed pass.
- Keep environment versioning fixed for one matrix run (browser/runtime/model config constants).

## Step 3 — Collect required instrumentation per trial

Minimum required fields per trial:

- work units/tokens processed
- dedupe hit rate
- routing decision counts
- memory movement proxies (copy/transfer)
- estimated energy score components
- guardrails (p95 latency, error rate)
- telemetry quality gate result and reason

Optional (recommended when available):

- package power
- node power
- thermal sensor snapshots

## Step 4 — Emit JSONL artifacts for automated analysis

Write one JSON object per trial in JSONL form. Use schema in:

- `lab/templates/trial_result.schema.json`

Use example in:

- `lab/templates/trial_result.example.jsonl`

Naming convention (recommended):

- `lab/runs/<run_id>/trial_results.jsonl`
- `lab/runs/<run_id>/summary.json`
- `lab/runs/<run_id>/metadata.json`

## Step 5 — Run post-processing statistics and quality slicing

Compute for each metric (global and per workload class):

- mean
- standard deviation
- 95% confidence interval

Compute comparative statistics:

- treatment vs baseline effect size per workload class
- significance via one consistent method (bootstrap OR t-test)

Compute quality diagnostics:

- telemetry quality gate pass rate
- grouped failure reasons by workload class and treatment

## Step 6 — Apply go/no-go decision rule

Go if ALL are true:

1. Energy estimate CI excludes zero in favorable direction.
2. Guardrails stable (no p95 latency or error-rate regression).
3. Telemetry quality gate pass rate > 95%.

Otherwise: no-go/iterate.

## Reproducibility checklist

- [ ] Run ID fixed and unique
- [ ] Matrix configuration frozen
- [ ] Seed strategy recorded
- [ ] Version stamps captured (lab version, runtime, model/profile)
- [ ] Raw JSONL preserved
- [ ] Summary outputs reproducibly generated from raw data

## Claim-safe reporting template

Use this language for public/internal summary:

> LowQ v0.5 produced benchmark-estimated reductions in workload, estimated work units, estimated energy proxy, and thermal-shadow proxy under controlled A/B trials. Results are model-estimated unless telemetry/formal analyzer evidence passes the quality gate.
