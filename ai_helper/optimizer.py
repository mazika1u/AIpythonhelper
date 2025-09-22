def improve_code(code: str, prompt: str="可読性を向上させてください") -> str:
    """
    コードを改善するプロンプトを送って最適化
    """
    from generator import generate_code
    return generate_code(f"{prompt}\n\n{code}")
