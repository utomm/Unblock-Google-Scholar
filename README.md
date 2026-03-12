# Unblock-Google-Scholar
Fetch Google Scholar author metadata with GitHub Actions and publish JSON outputs on a `metadata` branch.

## Outputs
- `data/metadata.json` - full SerpApi response with run metadata.
- `data/total_citations.json` - only the total citations count.

## Motivation
Other Google Scholar citation libraries often get blocked by robot tests, especially in GitHub Actions. This project uses a free SerpApi endpoint to retrieve data in a legal and reliable way.

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

## use case (jsDelivr + shields.io)
Example badge showing total citations for the Repo owner from the `metadata` branch:

![Google Scholar citations](https://img.shields.io/badge/dynamic/json?label=Scholar%20Citations&color=4285F4&query=%24.total_citations&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Futomm%2FUnblock-Google-Scholar%40metadata%2Fdata%2Ftotal_citations.json)

```markdown
![Google Scholar citations](https://img.shields.io/badge/dynamic/json?label=Scholar%20Citations&color=4285F4&query=%24.total_citations&url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Futomm%2FUnblock-Google-Scholar%40metadata%2Fdata%2Ftotal_citations.json)
```

Direct JSON URL (jsDelivr):

```
https://cdn.jsdelivr.net/gh/utomm/Unblock-Google-Scholar@metadata/data/total_citations.json
```

## Workflow
See [workflow file](.github/workflows/fetch-scholar-metadata.yml).
