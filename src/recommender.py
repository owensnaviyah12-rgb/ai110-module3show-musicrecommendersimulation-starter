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
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against user preferences and return (score, reasons)."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["favorite_genre"]:
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song["mood"] == user_prefs["favorite_mood"]:
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_points = 1 - abs(song["energy"] - user_prefs["target_energy"])
    score += energy_points
    reasons.append(f"energy close to target (+{energy_points:.2f})")

    if user_prefs["likes_acoustic"]:
        acoustic_points = 0.5 * song["acousticness"]
    else:
        acoustic_points = 0.5 * (1 - song["acousticness"])
    score += acoustic_points
    reasons.append(f"acousticness fit (+{acoustic_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, sort best first, and return the top k as (song, score, explanation)."""
    scored = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored.append((song, score, ", ".join(reasons)))

    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return ranked[:k]

