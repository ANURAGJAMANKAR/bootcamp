import json
import os
import shutil
import re

# Constants – adjust if needed
SOURCE_JSON = "day_two/source_map.json"
DEST_JSON = "language-drills/destination_map.json"
SOURCE_ROOT = "day_two"
DEST_ROOT = "language-drills"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_exercise_number(filename):
    """Extracts exercise number from a file like 'exercise_3.2_*.py' → 'ex-3-2'"""
    match = re.match(r"exercise_(\d+)\.(\d+)", filename)
    if match:
        major, minor = match.groups()
        return f"ex-{major}-{minor}"
    return None

def collect_transfers(source_map, dest_map, allowed_sections={"5", "6", "7"}):
    """Returns list of (source_path, destination_path) only for specified sections"""
    transfers = []
    for full_path, data in source_map.items():
        match = re.match(r"section_(\d+)[^/]*/exercise_[^/]+", full_path)
        if not match:
            continue

        section_num = match.group(1)
        if section_num not in allowed_sections:
            continue

        for file in data.get("files", []):
            if not file.endswith(".py"):
                continue

            ex_id = extract_exercise_number(file)
            if not ex_id:
                continue

            src_path = os.path.join(SOURCE_ROOT, full_path.replace("/", os.sep), file)
            dest_path = os.path.join(DEST_ROOT, f"section-{section_num}", ex_id, file)

            transfers.append((src_path, dest_path))

    return transfers

def copy_files(transfers):
    copied = 0
    skipped = 0
    for src, dest in transfers:
        if not os.path.exists(src):
            print(f"❌ Missing source: {src}")
            continue

        if os.path.exists(dest):
            print(f"⏩ Already exists, skipping: {dest}")
            skipped += 1
            continue

        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(src, dest)
        print(f"✅ Copied: {src} → {dest}")
        copied += 1

    print(f"\n📦 Transfer complete: {copied} files copied, {skipped} skipped.")

def main():
    source_map = load_json(SOURCE_JSON)
    dest_map = load_json(DEST_JSON)

    # Limit to section 5, 6, 7 only
    transfers = collect_transfers(source_map, dest_map, allowed_sections={"5", "6", "7"})
    copy_files(transfers)

if __name__ == "__main__":
    main()
