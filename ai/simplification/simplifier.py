def simplify_text(text: str, grade: int) -> str:
    """
    Baseline educational text simplifier.

    This is only the initial implementation.
    A proper AI/ML model can replace this later.
    """

    text = text.strip()

    if not text:
        return ""

    return text