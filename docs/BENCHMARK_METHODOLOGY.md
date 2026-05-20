# LowQ Benchmark Methodology

## Basic protocol

1. Select representative workload.
2. Capture baseline run.
3. Apply LowQ optimization.
4. Run optimized workload.
5. Repeat in ABBA or randomized order.
6. Capture telemetry or simulation traces.
7. Compare deltas.
8. Export certificate.

## Minimum meaningful benchmark

- 1,000+ baseline tokens for S0-BENCH.
- 10+ trials minimum.
- 30 trials recommended.
- Quality guard above 80 unless workload is exploratory.
- Repeat-trial statistics included.

## Metrics

- token reduction,
- estimated work-unit reduction,
- estimated KV-cache reduction,
- estimated latency reduction,
- estimated energy reduction,
- thermal area-under-curve reduction,
- peak temperature delta,
- average power delta,
- quality guard,
- proof grade,
- telemetry quality.

## Warning
TAUC / thermal-shadow metrics are useful for early modeling, but public thermal claims require telemetry or external measurement.
