import pandas as pd

# Only these names are allowed inside the executed code.
# Anything else (os, sys, open, __import__, etc.) simply won't exist in this scope.
SAFE_GLOBALS = {
    "pd": pd,
    "__builtins__": {
        "len": len,
        "sum": sum,
        "min": min,
        "max": max,
        "abs": abs,
        "round": round,
        "sorted": sorted,
        "list": list,
        "dict": dict,
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
    },
}

# Keywords that should never appear in generated code - a first line of defense
# before we even try to execute it.
FORBIDDEN_KEYWORDS = [
    "import", "exec", "eval", "open", "__", "os.", "sys.",
    "subprocess", "input", "compile", "globals", "locals",
    "file", "write", "delete", "remove", "system",
]


def is_code_safe(code: str) -> tuple[bool, str]:
    """
    Checks generated code against a blocklist before execution.
    Returns (is_safe, reason_if_not).
    """
    code_lower = code.lower()

    for keyword in FORBIDDEN_KEYWORDS:
        if keyword in code_lower:
            return False, f"Blocked: code contains forbidden keyword '{keyword}'"

    if "result" not in code:
        return False, "Blocked: code does not assign to 'result'"

    if "\n" in code.strip():
        return False, "Blocked: multi-line code is not allowed"

    return True, ""


def run_sandboxed_query(code: str, df: pd.DataFrame):
    """
    Executes validated pandas code against the given DataFrame, safely.
    Returns (success, result_or_error_message).
    """
    is_safe, reason = is_code_safe(code)
    if not is_safe:
        return False, reason

    local_scope = {"df": df}

    try:
        exec(code, SAFE_GLOBALS, local_scope)
    except Exception as e:
        return False, f"Execution error: {str(e)}"

    if "result" not in local_scope:
        return False, "Code did not produce a 'result' variable"

    return True, local_scope["result"]