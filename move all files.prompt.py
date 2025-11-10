import shutil
from pathlib import Path

# --- CONFIGURATION ---
desktop = Path("C:/Users/USER/Desktop")
target_folder = desktop / "Documents_Collection"     # Folder to create & move into

# Create target folder if it doesn't exist
target_folder.mkdir(exist_ok=True)

# File extensions to move
extensions = {
    '.pdf', '.txt',
    '.xlsx', '.xls',
    '.docx', '.doc',
    '.py'
}

# Count moved files
moved = 0

print("Scanning Desktop for documents...")

for file_path in desktop.iterdir():
    if file_path.is_file() and file_path.suffix.lower() in extensions:
        dest = target_folder / file_path.name

        # Avoid overwriting: add _1, _2 if file already exists
        counter = 1
        original_dest = dest
        while dest.exists():
            stem = original_dest.stem
            dest = original_dest.with_name(f"{stem}_{counter}{original_dest.suffix}")
            counter += 1

        try:
            shutil.move(str(file_path), str(dest))
            print(f"  Moved: {file_path.name}")
            moved += 1
        except Exception as e:
            print(f"  Failed: {file_path.name} → {e}")

# Final message
if moved == 0:
    print("\nNo matching files found on Desktop.")
else:
    print(f"\n{moved} file(s) moved to:\n   {target_folder}")