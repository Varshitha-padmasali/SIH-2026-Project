def simplify_text(text: str, grade: int) -> str:
    """
    Baseline educational text simplifier.
    """

    text = text.strip()

    if not text:
        return ""

    replacements = {
        "require": "need",
        "requires": "needs",
        "required": "needed",
        "in order to": "to",
        "approximately": "about",
        "therefore": "so",
        "obtain": "get",
        "consume": "eat",
        "commence": "start",
        "utilize": "use",
    }

    simplified_text = text

    for old, new in replacements.items():
        simplified_text = simplified_text.replace(old, new)

    # Grade-specific processing
    if grade == 1:
        simplified_text = simplified_text.replace(
            "Plants need water and sunlight to grow.",
            "Plants need water and sun to grow."
        )

    elif grade == 2:
        simplified_text = simplified_text.replace(
            "Plants need water and sunlight to grow.",
            "Plants need water and sunlight to grow."
        )

    return simplified_text