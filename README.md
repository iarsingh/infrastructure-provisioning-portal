# Infrastructure Provisioning Portal

Level: 14 — Cloud, DevOps & Platform Engineering

Skills: Python, name and region checks

Pass when name matches ^[a-z][a-z0-9-]{2,20}$ and region is allowlisted. Apply false.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
