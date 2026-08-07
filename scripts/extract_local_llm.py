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

# モデル名（単独ではヒットさせない。LOCAL_HINTS との共起でローカルLLM記事と判定）
MODEL_NAMES = [
    "deepseek",
    "qwen",
    "gemma",
    "phi",
    "mistral",
    "yi",
    "glm",
    "baichuan",
    "internlm",
    "minicpm",
    "granite",
    "olmo",
    "nemotron",
    "falcon",
    "rwkv",
    "mamba",
    "dolphin",
    "wizardlm",
    "stablelm",
    "codestral",
    "devstral",
    "gpt-oss",
    "llama 3",
    "llama3",
    "llama 4",
    "llama4",
]

# ローカル実行を示すヒント（モデル名との共起判定に使う）
LOCAL_HINTS = [
    "local",
    "locally",
    "ローカル",
    "offline",
    "オフライン",
    "on-device",
    "オンデバイス",
    "self-host",
    "selfhost",
    "自前",
    "手元",
    "端末",
    "自分のマシン",
    "自分のpc",
    "my machine",
    "on your machine",
    "run it yourself",
    "run on your",
    "ローカル実行",
    "local run",
    "runs locally",
    "inference at home",
    "home server",
    "自宅",
    "gguf",
    "quantiz",
]

PATTERNS = [re.compile(re.escape(kw), re.IGNORECASE) for kw in KEYWORDS]
MODEL_PATTERNS = [re.compile(r"\b" + re.escape(name) + r"\b", re.IGNORECASE) for name in MODEL_NAMES]
LOCAL_PATTERNS = [re.compile(re.escape(hint), re.IGNORECASE) for hint in LOCAL_HINTS]


def is_local_llm(article):
    """タイトルと説明(extra)で判定。

    1. 直接キーワード (ollama / llama.cpp / gguf 等) に一致 → ヒット
    2. モデル名 (deepseek / qwen 等) とローカルヒント (local / ローカル 等) が
       両方含まれる → ヒット（例: 「DeepSeek V4 284Bをローカルで動かせる！」）
    """
    haystack = " ".join(
        filter(None, [article.get("title"), article.get("extra")])
    )
    if any(p.search(haystack) for p in PATTERNS):
        return True
    has_model = any(p.search(haystack) for p in MODEL_PATTERNS)
    has_local = any(p.search(haystack) for p in LOCAL_PATTERNS)
    return has_model and has_local


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
