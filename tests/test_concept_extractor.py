from ai.educational_nlp.concept_extractor import extract_concepts


test_cases = [
    {
        "text": "Plants need water and sunlight to grow.",
        "expected": ["plants", "water", "sunlight", "growth"]
    },
    {
        "text": "Animals need food, water, and air to live.",
        "expected": ["water", "air", "animals", "food"]
    },
    {
        "text": "Water is important for all living things.",
        "expected": ["water", "living_things"]
    },
    {
        "text": "Trees are plants that give us oxygen.",
        "expected": ["plants", "trees", "oxygen"]
    },
    {
        "text": "The child plays with a ball.",
        "expected": []
    }
]


for i, test in enumerate(test_cases, start=1):
    actual = extract_concepts(test["text"])

    if actual == test["expected"]:
        print(f"✅ Test {i} passed")
    else:
        print(f"❌ Test {i} failed")
        print("Expected:", test["expected"])
        print("Actual:  ", actual)