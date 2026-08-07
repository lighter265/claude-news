"""raw/github_trending.json からローカルLLM関連記事を抽出する。

キーワードは「広め」に設定し、機械フィルタで候補を落とさない方針。
最終的な取捨判断は要約ステップの Claude CLI に任せる。
0 件でもエラーにせず空 JSON を保存する（要約側で「該当なし」を出力する）。
"""
import json
import os
import re

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(REPO, "raw")
SRC = os.path.join(RAW_DIR, "github_trending.json")
DST = os.path.join(RAW_DIR, "local_llm_github.json")

# ローカル環境で動かす LLM / 推論基盤に関わるキーワード（小文字で判定）
KEYWORDS = [
    "ollama",
    "llama",            # llama.cpp / llamafile / Llama 3 等
    "llamafile",
    "gguf",
    "vllm",
    "lm studio",
    "lmstudio",
    "localai",
    "local-ai",
    "local llm",
    "local-llm",
    "llm local",
    "quantiz",          # 量子化 (quantization)
    "kobold",
    "oobabooga",
    "text-generation-webui",
    "gpt4all",
    "mlx-lm",
    "mlx",              # Apple Silicon 向け推論
    "whisper.cpp",
    "mistral.rs",
    "candle",           # Rust 製ローカル推論
    "onnxruntime",
    "exo",              # 分散ローカルLLM
    "tinygrad",
    "jan.ai",
    "self-hosted llm",
    "self hosted llm",
    "local inference",
    "offline llm",
    "run llm locally",
    "local model",
    "local models",
    "llama.cpp",
    "llama-cpp",
]

PATTERNS = [re.compile(re.escape(kw), re.IGNORECASE) for kw in KEYWORDS]


def is_local_llm(article):
    """タイトルと説明(extra)のどちらかにキーワードが含まれれば候補。"""
    haystack = " ".join(
        filter(None, [article.get("title"), article.get("extra")])
    )
    return any(p.search(haystack) for p in PATTERNS)


def main():
    if not os.path.exists(SRC):
        print(f"[local_llm] 入力なし: {SRC} が存在しません")
        os.makedirs(RAW_DIR, exist_ok=True)
        with open(DST, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        return 0

    with open(SRC, encoding="utf-8") as f:
        items = json.load(f)

    hits = [a for a in items if is_local_llm(a)]
    with open(DST, "w", encoding="utf-8") as f:
        json.dump(hits, f, ensure_ascii=False, indent=2)

    print(f"[local_llm] github_trending {len(items)} 件中 {len(hits)} 件を抽出 -> {DST}")
    return len(hits)


if __name__ == "__main__":
    main()
