import os
import time

from google import genai
from dotenv import load_dotenv

from logging_config import get_logger

# Load the .env file so we can read GEMINI_API_KEY from it
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

logger = get_logger(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_NAME = "gemini-3.5-flash-lite"

VALID_CATEGORIES = [
    "Food", "Travel", "Shopping", "Bills", "Entertainment",
    "Groceries", "Salary", "Rent", "Other"
]


def categorize_with_llm(description: str) -> str:
    """
    Asks Gemini to categorize a transaction description.
    Returns one of VALID_CATEGORIES.
    """
    prompt = f"""You are a financial transaction categorizer.
Classify this bank transaction description into exactly ONE of these categories:
{", ".join(VALID_CATEGORIES)}

Transaction description: "{description}"

Respond with ONLY the category name, nothing else. No explanation, no punctuation."""

    logger.info("Gemini request -> task=categorize model=%s description=%r", MODEL_NAME, description)
    logger.debug("Gemini prompt: %s", prompt)

    start = time.perf_counter()
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
    except Exception as e:
        logger.error("Gemini categorize failed for %r: %s", description, e)
        raise
    elapsed = time.perf_counter() - start

    category = response.text.strip()
    if category not in VALID_CATEGORIES:
        logger.warning("Gemini returned unexpected category %r for %r", category, description)
        return "Other"

    logger.info("Gemini response <- task=categorize category=%r latency=%.3fs", category, elapsed)
    return category