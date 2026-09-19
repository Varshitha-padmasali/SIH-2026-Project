from ai.pipeline.processor import process_lesson


test_cases = [
    {
        "text": "Plants need water and sunlight to grow.",
        "grade": 2
    },
    {
        "text": "Animals need food, water, and air to live.",
        "grade": 2
    },
    {
        "text": "Trees are plants that grow tall and give us oxygen.",
        "grade": 3
    },
    {
        "text": "Water is important for all living things.",
        "grade": 1
    },
    {
        "text": "Sunlight helps plants grow.",
        "grade": 2
    }
]


for i, test in enumerate(test_cases, start=1):

    print(f"\n--- Test {i} ---")

    result = process_lesson(
        test["text"],
        test["grade"]
    )

    print("Input:", result["original_text"])
    print("Grade:", result["grade"])
    print("Simplified:", result["simplified_text"])
    print("Concepts:", result["concepts"])
    print("Content:", result["content"])