# LowQ Pilot Deployment

## Pilot name
Two-week LowQ Waste-Heat Assessment

## Objective
Measure whether LowQ can reduce computational waste, energy burden, thermal shadow, or cost for a defined AI workload.

## Pilot phases

### Phase 1: Intake
- workload type,
- model/runtime,
- hardware profile,
- current telemetry availability,
- success criteria.

### Phase 2: Baseline
- run workload without LowQ,
- collect token/runtime/power/temp metrics,
- export baseline trace.

### Phase 3: Optimization
- run LowQ compression/routing/memory strategy,
- collect same metrics,
- export optimized trace.

### Phase 4: Certificate
- generate LowQ Certificate,
- generate ROI report,
- classify proof grade.

### Phase 5: Decision
- proceed to deployment,
- retest with telemetry,
- reject/no deployment if savings are not credible.

## Pilot success criteria

At least one of:

- 10%+ workload/token reduction with quality preserved,
- measurable energy reduction on telemetry,
- measurable runtime reduction with power not increased,
- measurable thermal-shadow reduction,
- credible ROI path for a larger test.
