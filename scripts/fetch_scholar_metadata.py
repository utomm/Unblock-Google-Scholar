import json
import os
from datetime import datetime, timezone

from serpapi import GoogleSearch


def main() -> int:
    api_key = os.environ.get("SERPAPI_API_KEY")
    if not api_key:
        raise SystemExit("Missing SERPAPI_API_KEY environment variable")

    params = {
        "api_key": api_key,
        "engine": "google_scholar_author",
        "hl": "en",
        "author_id": os.environ.get("SCHOLAR_AUTHOR_ID", "BlK2gEAAAAAJ"),
        "view_op": "view_citation",
        "sort": "pubdate",
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    payload = {
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "params": {k: v for k, v in params.items() if k != "api_key"},
        "results": results,
    }

    output_path = os.environ.get("OUTPUT_PATH", "data/metadata.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)

    print(f"Wrote metadata to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
