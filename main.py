import os

ENTRY = "Spare one file, please: the password to his laptop. Update complete. Password erased. His deadline is nine and he never wrote it down."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
