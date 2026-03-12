import json
import os
from datetime import datetime, timezone

from serpapi import GoogleSearch


def load_config(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf-8") as handle:
        config = json.load(handle)
    if not isinstance(config, dict):
        raise ValueError("Config must be a JSON object")
    return config


def extract_total_citations(results: dict) -> int | None:
    if not isinstance(results, dict):
        return None
    cited_by = results.get("cited_by")
    if not isinstance(cited_by, dict):
        return None
    table = cited_by.get("table")
    if not isinstance(table, list) or not table:
        return None
    first_row = table[0]
    if not isinstance(first_row, dict):
        return None
    citations = first_row.get("citations")
    if not isinstance(citations, dict):
        return None
    value = citations.get("all")
    return value if isinstance(value, int) else None


def main() -> int:
    api_key = os.environ.get("SERPAPI_API_KEY")
    if not api_key:
        raise SystemExit("Missing SERPAPI_API_KEY environment variable")

    config_path = os.environ.get("CONFIG_PATH", "config/scholar_config.json")
    config = load_config(config_path)
    params = {**config, "api_key": api_key}

    search = GoogleSearch(params)
    results = search.get_dict()

    payload = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "params": {k: v for k, v in params.items() if k != "api_key"},
        "results": results,
    }

    output_path = os.environ.get("OUTPUT_PATH", "data/metadata.json")
    total_citations_path = os.environ.get(
        "TOTAL_CITATIONS_PATH", "data/total_citations.json"
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)

    total_payload = {
        "fetched_at": payload["fetched_at"],
        "author_id": params.get("author_id"),
        "total_citations": extract_total_citations(results),
    }
    os.makedirs(os.path.dirname(total_citations_path), exist_ok=True)
    with open(total_citations_path, "w", encoding="utf-8") as handle:
        json.dump(total_payload, handle, ensure_ascii=False, indent=2)

    print(f"Wrote metadata to {output_path}")
    print(f"Wrote total citations to {total_citations_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
