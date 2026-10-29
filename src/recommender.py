import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

intense_rock = {
    "favorite_genre": "rock",
    "favorite_mood": "intense",
    "target_energy": 0.9,
    "likes_acoustic": False
}

chill_lofi = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.4,
    "likes_acoustic": True
}

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs from a CSV file and return a list of dictionaries with numeric fields converted."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            row["energy"] = float(row["energy"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            row["popularity"] = int(row["popularity"])
            row["release_decade"] = int(row["release_decade"])
            row["instrumental"] = int(row["instrumental"])
            row["explicit"] = int(row["explicit"])
            row["mood_tags"] = row["mood_tags"].split("|")
            songs.append(row)
    return songs

MODES = {
    "balanced": {
        "genre": 2.0, "mood": 1.0, "energy": 1.0, "acoustic": 0.5,
        "popularity": 0.5, "decade": 0.5, "tags": 1.0,
        "instrumental": 0.5, "clean": 1.0,
    },
    "genre_first": {
        "genre": 4.0, "mood": 0.5, "energy": 0.5, "acoustic": 0.25,
        "popularity": 0.25, "decade": 0.25, "tags": 0.5,
        "instrumental": 0.25, "clean": 1.0,
    },
    "mood_first": {
        "genre": 0.5, "mood": 3.0, "energy": 1.0, "acoustic": 0.5,
        "popularity": 0.25, "decade": 0.25, "tags": 1.5,
        "instrumental": 0.5, "clean": 1.0,
    },
    "energy_focused": {
        "genre": 0.5, "mood": 0.5, "energy": 3.0, "acoustic": 0.5,
        "popularity": 0.25, "decade": 0.25, "tags": 0.5,
        "instrumental": 0.5, "clean": 1.0,
    },
}


def score_song(user_prefs: Dict, song: Dict, weights: Optional[Dict] = None) -> Tuple[float, List[str]]:
    """Score one song with the given mode weights and return (score, reasons)."""
    w = weights or MODES["balanced"]
    score = 0.0
    reasons = []

    def add(points: float, text: str) -> None:
        nonlocal score
        score += points
        reasons.append(f"{text} ({points:+.2f})")

    if song["genre"] == user_prefs["favorite_genre"]:
        add(w["genre"], "genre match")

    if song["mood"] == user_prefs["favorite_mood"]:
        add(w["mood"], "mood match")

    energy_fit = 1 - abs(song["energy"] - user_prefs["target_energy"])
    add(w["energy"] * energy_fit, "energy close to target")

    if user_prefs["likes_acoustic"]:
        acoustic_fit = song["acousticness"]
    else:
        acoustic_fit = 1 - song["acousticness"]
    add(w["acoustic"] * acoustic_fit, "acousticness fit")

    # New features. Each one only counts if the profile asks for it.
    if "target_popularity" in user_prefs:
        pop_fit = 1 - abs(song["popularity"] - user_prefs["target_popularity"]) / 100
        add(w["popularity"] * pop_fit, "popularity fit")

    if song["release_decade"] == user_prefs.get("favorite_decade"):
        add(w["decade"], "decade match")

    wanted = user_prefs.get("favorite_tags")
    if wanted:
        hits = [t for t in wanted if t in song["mood_tags"]]
        if hits:
            add(w["tags"] * len(hits) / len(wanted), "tag match: " + "/".join(hits))

    if "prefers_instrumental" in user_prefs:
        if bool(song["instrumental"]) == user_prefs["prefers_instrumental"]:
            add(w["instrumental"], "instrumental fit")

    if user_prefs.get("clean_only") and song["explicit"]:
        add(-w["clean"], "explicit song")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5, mode: str = "balanced") -> List[Tuple[Dict, float, str]]:
    """Score every song using the chosen mode, sort best first, and return the top k."""
    weights = MODES[mode]
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song, weights)
        scored.append((song, score, ", ".join(reasons)))
    return sorted(scored, key=lambda item: item[1], reverse=True)[:k]
