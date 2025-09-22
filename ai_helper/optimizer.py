from ai_helper.generator import generate_code

def improve_code(code: str, prompt: str="可読性を向上させてください") -> str:
    return generate_code(f"{prompt}\n\n{code}")
