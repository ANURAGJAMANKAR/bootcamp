import json
import os
import shutil

# Paths relative to the AganithaBootcamp root
SOURCE_JSON = "day_two/source_map.json"
DEST_JSON = "language-drills/destination_map.json"
ROOT_DIR = os.getcwd()

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def extract_exercise_mapping(source_section, destination_section_path):
    mapping = []
    for folder_name, folder_data in source_section.items():
        if not folder_name.startswith("section_1_Core_Python_Proficiency/exercise_"):
            continue

        for file in folder_data["files"]:
            if file.startswith("exercise_") and file.endswith(".py"):
                # Extract exercise number (e.g., 1.2 → ex-1-2)
                number = file.split("_")[1].replace(".", "-")
                dest_folder = os.path.join(destination_section_path, f"ex-{number}")
                mapping.append((folder_name, file, dest_folder))
    return mapping

def copy_files(mapping, source_root, destination_root):
    for src_folder_key, filename, dest_subfolder in mapping:
        src_full_path = os.path.join(source_root, src_folder_key.replace("/", os.sep), filename)
        dest_full_path = os.path.join(destination_root, dest_subfolder.replace("/", os.sep), filename)

        os.makedirs(os.path.dirname(dest_full_path), exist_ok=True)
        shutil.copy2(src_full_path, dest_full_path)
        print(f"✅ Copied: {src_full_path} → {dest_full_path}")

def main():
    source_data = load_json(os.path.join(ROOT_DIR, SOURCE_JSON))
    dest_data = load_json(os.path.join(ROOT_DIR, DEST_JSON))

    # Focus on Section 1 only
    section_1_source = {
        k: v for k, v in source_data.items()
        if k.startswith("section_1_Core_Python_Proficiency/exercise_")
    }

    mapping = extract_exercise_mapping(section_1_source, "language-drills/section-1")
    copy_files(mapping, os.path.join(ROOT_DIR, "day_two"), os.path.join(ROOT_DIR, "language-drills"))

if __name__ == "__main__":
    main()
