"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs

PROFILES = {
    "High-Energy Pop": {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.9, "likes_acoustic": False},
    "Chill Lofi": {"favorite_genre": "lofi", "favorite_mood": "chill", "target_energy": 0.4, "likes_acoustic": True},
    "Deep Intense Rock": {"favorite_genre": "rock", "favorite_mood": "intense", "target_energy": 0.9, "likes_acoustic": False},
    "TRICKY: Loud but Sad": {"favorite_genre": "folk", "favorite_mood": "sad", "target_energy": 0.9, "likes_acoustic": True},
    "TRICKY: Unknown Genre": {"favorite_genre": "polka", "favorite_mood": "happy", "target_energy": 0.8, "likes_acoustic": False},
}

def main() -> None:
    songs = load_songs("data/songs.csv")

    # Starter example profile
    user_prefs = {"favorite_genre": "pop", "favorite_mood": "happy", "target_energy": 0.8, "likes_acoustic": False}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for song, score, explanation in recommendations:
        print(f"{song['title']} by {song['artist']}")
        print(f"  Score: {score:.2f}")
        print(f"  Why: {explanation}")
        print()


if __name__ == "__main__":
    main()