
import json
from pathlib import Path

MEMORY_FILE = Path("memory.json")


def load_memory():
    if MEMORY_FILE.exists():
        return json.loads(
            MEMORY_FILE.read_text(encoding="utf-8")
        )
    return []


def remember(content):
    memories = load_memory()
    memories.append(content)

    MEMORY_FILE.write_text(
        json.dumps(
            memories,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


def main():
    remember("知屿计划启动：建立长期记忆功能。")
    print("当前记忆：")
    for item in load_memory():
        print("-", item)


if __name__ == "__main__":
    main()
