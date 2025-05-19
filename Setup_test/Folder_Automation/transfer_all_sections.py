import json
import os
import shutil
import re

# Paths relative to the AganithaBootcamp root
SOURCE_JSON = "day_two/source_map.json"
DEST_JSON = "language-drills/destination_map.json"
SOURCE_ROOT = "day_two"
DEST_ROOT = "language-drills"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_exercise_number(filename):
    match = re.match(r"exercise_(\d+)\.(\d+)", filename)
    if match:
        major, minor = match.groups()
        return f"ex-{major}-{minor}"
    return None

def extract_section_number(section_name):
    match = re.match(r"section_(\d+)", section_name)
    return match.group(1) if match else None

def collect_transfers(source_map, dest_map):
    transfers = []
    for src_section_key, section_data in source_map.items():
        if not src_section_key.startswith("section_"):
            continue

        section_num = extract_section_number(src_section_key)
        if not section_num:
            continue

        for file in section_data.get("files", []):
            if not file.endswith(".py"):
                continue

            ex_id = extract_exercise_number(file)
            if not ex_id:
                continue

            src_path = os.path.join(SOURCE_ROOT, src_section_key.replace("/", os.sep), file)
            dest_path = os.path.join(DEST_ROOT, f"section-{section_num}", ex_id, file)

            transfers.append((src_path, dest_path))

    return transfers

def copy_files(transfers):
    for src, dest in transfers:
        if not os.path.exists(src):
            print(f"❌ Missing source file: {src}")
            continue

        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copy2(src, dest)
        print(f"✅ Copied: {src} → {dest}")

def main():
    source_map = load_json(SOURCE_JSON)
    dest_map = load_json(DEST_JSON)
    transfers = collect_transfers(source_map, dest_map)
    copy_files(transfers)

if __name__ == "__main__":
    main()
