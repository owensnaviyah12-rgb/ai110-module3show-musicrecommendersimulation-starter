import csv
import shutil

NEW = {
    1: (85, 2020, "bright|uplifting", 0, 0),
    2: (70, 2020, "calm|focused|nostalgic", 1, 0),
    3: (62, 2010, "aggressive|driving", 0, 0),
    4: (55, 2020, "calm|rainy|nostalgic", 1, 0),
    5: (90, 2020, "aggressive|uplifting|driving", 0, 0),
    6: (40, 2010, "calm|dreamy", 1, 0),
    7: (48, 2000, "relaxed|warm|nostalgic", 0, 0),
    8: (66, 2010, "moody|dreamy|driving", 1, 0),
    9: (60, 2020, "focused|calm", 1, 0),
    10: (72, 2010, "bright|uplifting|warm", 0, 0),
    11: (80, 2010, "confident|driving|aggressive", 0, 1),
    12: (58, 2000, "nostalgic|warm", 0, 0),
    13: (45, 1980, "romantic|dreamy|calm", 1, 0),
    14: (60, 2000, "aggressive|dark|driving", 0, 1),
    15: (75, 2010, "romantic|warm", 0, 0),
    16: (42, 2010, "sad|nostalgic|warm", 0, 0),
    17: (78, 2020, "euphoric|uplifting|driving", 1, 0),
    18: (68, 2000, "relaxed|warm|uplifting", 0, 0),
}

with open("data/songs.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

if "popularity" in rows[0]:
    print("Already done. Nothing changed.")
    raise SystemExit

shutil.copy("data/songs.csv", "data/songs_backup.csv")

for row in rows:
    pop, decade, tags, instr, expl = NEW[int(row["id"])]
    row.update(popularity=pop, release_decade=decade, mood_tags=tags,
               instrumental=instr, explicit=expl)

with open("data/songs.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

print("Added 5 columns to", len(rows), "songs.")