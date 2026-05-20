from pathlib import Path
root = Path(__file__).resolve().parents[1]
required = [
    root/'lab/lowq_lab.html',
    root/'roi/lowq_roi_calculator.html',
    root/'landing/lowq_landing_page.html',
    root/'schemas/lowq_certificate.schema.json',
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit('Missing files: ' + ', '.join(missing))
for p in required[:3]:
    text = p.read_text(encoding='utf-8')
    if 'LowQ' not in text:
        raise SystemExit(f'Missing LowQ marker in {p}')
print('LowQ smoke check passed.')
