from ai.pipeline.processor import process_lesson


text = "Plants require water and sunlight in order to grow."
result = process_lesson(text, 2)

print(result)