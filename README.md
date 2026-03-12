# Unblock-Google-Scholar
Fetch Google Scholar author metadata with GitHub Actions and publish JSON outputs on a `metadata` branch.

## Outputs
- `data/metadata.json` - full SerpApi response with run metadata.
- `data/total_citations.json` - only the total citations count.

## Configure
Edit [config/scholar_config.json](config/scholar_config.json) to set:
- `author_id`
- `hl`
- `sort`

Store your SerpApi key as a GitHub Actions secret named `SERPAPI_API_KEY`:
GitHub repo Settings -> Secrets and variables -> Actions -> New repository secret.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SERPAPI_API_KEY="YOUR_KEY"
python scripts/fetch_scholar_metadata.py
```

## Workflow
See [workflow file](.github/workflows/fetch-scholar-metadata.yml).
