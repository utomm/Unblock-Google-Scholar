# Unblock-Google-Scholar
Automate fetching Google Scholar author metadata with GitHub Actions and store the JSON output in a dedicated `metadata` branch.

## How it works
- A scheduled GitHub Actions workflow runs a Python script that calls SerpApi's Google Scholar author endpoint.
- The script writes `data/metadata.json` on each run.
- The workflow force-pushes the updated JSON to the `metadata` branch.

## Requirements
- A SerpApi account and API key stored as a GitHub Actions secret named `SERPAPI_API_KEY`.

## Configuration
The workflow currently uses:
- Author id: `BlK2gEAAAAAJ`
- Locale: `en`
- Sorting: `pubdate`

To change the author id or output path, update the environment variables in the workflow file.

## Local run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export SERPAPI_API_KEY="YOUR_KEY"
python scripts/fetch_scholar_metadata.py
```

## Workflow
See [workflow file](.github/workflows/fetch-scholar-metadata.yml).
