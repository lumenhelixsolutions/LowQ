# LowQ Architecture

## System view

```
Workload → LowQ Engine → Proof Run → Telemetry/Simulation → LowQ Certificate → ROI Report → Pilot Decision
```

## Module roles

### LowQ Lab
Browser proof interface for estimates, repeated trials, telemetry import, simulator import, and certificate export.

### LowQ Engine
Optimization layer that reduces wasteful tokens, repeated context, unnecessary state churn, and inefficient routing.

### LowQ Bridge
Optional telemetry connector for vendor counters, operating-system sensors, external meters, and simulator traces.

### LowQ SimTwin
Pre-hardware simulation mode for estimating energy/thermal outcomes before real telemetry is available.

### LowQ Certificate
Portable evidence artifact containing workload profile, proof confidence, baseline/optimized metrics, deltas, caveats, and audit hashes.

### LowQ ROI Calculator
Business-case layer translating technical deltas into possible energy/cooling/cost savings.

## Engineering rules

- Simple core.
- Replaceable edges.
- Measurable results.
- Reversible changes.
- No unsupported heat claims.
- Out-of-the-box it works.
