"""Verify that OPENAI_API_KEY is present and authenticates against the OpenAI API."""

from __future__ import annotations

import os
import sys

from openai import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    OpenAI,
    PermissionDeniedError,
    RateLimitError,
)

MODEL = "gpt-4o"
START_COMMAND = "python src/app.py"


def main() -> int:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or not api_key.strip():
        print("❌ OPENAI_API_KEY is missing or empty.")
        print("   Fix (PowerShell): $env:OPENAI_API_KEY='your-key'")
        return 1

    print(f"→ Key detected: {len(api_key)} chars, prefix '{api_key[:7]}…'")

    try:
        response = OpenAI(api_key=api_key, timeout=20.0, max_retries=0).chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": "ping"}],
            max_tokens=1,
        )
    except AuthenticationError:
        print("❌ Invalid key: the API rejected these credentials (401).")
        print("   Fix: regenerate the key at platform.openai.com and re-export it.")
        return 1
    except PermissionDeniedError:
        print(f"❌ Key authenticated but has no access to model '{MODEL}' (403).")
        print("   Fix: check the project/org permissions on this key.")
        return 1
    except RateLimitError:
        print("❌ Rate limited or out of quota (429). The key itself may still be valid.")
        print("   Fix: check billing and usage limits, then retry.")
        return 1
    except (APIConnectionError, APITimeoutError) as exc:
        print(f"❌ Network issue: could not reach the OpenAI API ({type(exc).__name__}).")
        print("   Fix: check connectivity, VPN, or proxy settings, then retry.")
        return 1
    except APIStatusError as exc:
        print(f"❌ API returned an unexpected error (HTTP {exc.status_code}).")
        return 1

    print("✅ OPENAI_API_KEY is active and authenticated!")
    print(f"   Model reachable: {response.model}")
    print(f"   Start the app with: {START_COMMAND}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
