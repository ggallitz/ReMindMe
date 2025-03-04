import random
import os

def get_random_line(file_path):
    """Reads a random line from a file."""
    if not os.path.exists(file_path):
        return "⚠️ No content available."
    
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return random.choice(lines) if lines else "⚠️ No content available."

def get_random_summary(file_path):
    """Reads a random summary from a file (separated by '---')."""
    if not os.path.exists(file_path):
        return "⚠️ No summaries available."
    
    with open(file_path, "r", encoding="utf-8") as f:
        summaries = f.read().split("---")
    return random.choice(summaries).strip() if summaries else "⚠️ No summaries available."

if __name__ == "__main__":
    print(get_random_line("data/quotes.txt"))
    print(get_random_summary("data/summaries.txt"))

