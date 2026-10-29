# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

What features does each Song use?
Each song has an id, title, artist, genre, mood, tempo_bpm, valence, danceabiity, and acousticness.In the numeric onces are on a 0.0 to 0.1 scale that except tempo that is in beats per minute. My scoring usese genre, mood, and enegry. The other features are stored so I Can add them later.

What does UserProfile store?

It stores four preferences: 
- favorite_genre (text,like "hip hop)
- favorite_mood (text,like "sad")
- target_energy (a number from 0.0 to 1.0)
- likes_acoustic (True or False such as does the user prefer acoustic soundng songs?)

The functional version od the code (score_song and reccommend_songs) stores the same four things in a dictionary instead

How does the Recommender compute a score for each song?

Each song is judged by its own and the points are added up 
- genre matches favorite_genre: +2.0
- mood matches favorite_mood: +1.0
- energy closeness: 1 - |song energy - target_energy| 
- acousticness: if likes_acoustic is True, add 0.5 x song acousticness. If it's False. add 0.5 x (1 - song acousticness).(0 to 0.5 points)

score_song return two things: the total score and a list of reasons, like "genre match (+2.0)" and "energy close to target (+0.98)" . explain_recommendation turn that reasons list into a sentence 

Song	Genre	Mood	Energy	Acoustic	Total
Sunrise City	+2.0	+1.0	0.98	0.41	4.39
Gym Hero	+2.0	0	0.87	0.48	3.35
Library Rain	0	0	0.55	0.07	0.62

How do you choose which songs to recommend?
1. Loop through every song and call score_song on it
2. Pair each song with its score and reasons 
3. Sort from highest score to lowest 
4. Return to the top of k (default 5)

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

Sunrise City by Neon Echo
  Score: 4.39
  Why: genre match (+2.0), mood match (+1.0), energy close to target (+0.98), acousticness fit (+0.41)

Gym Hero by Max Pulse
  Score: 3.35
  Why: genre match (+2.0), energy close to target (+0.87), acousticness fit (+0.47)

Rooftop Lights by Indigo Parade
  Score: 2.29
  Why: mood match (+1.0), energy close to target (+0.96), acousticness fit (+0.33)

Concrete Crown by Lyric Vance
  Score: 1.42
  Why: energy close to target (+0.98), acousticness fit (+0.44)

Neon Bassline by Kilo Static
  Score: 1.37
  Why: energy close to target (+0.91), acousticness fit (+0.46)
```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

**1. Weight shift (genre halved, energy doubled).**
I changed genre from +2.0 to +1.0 and doubled the energy points. For the
High-Energy Pop profile, Sunrise City stayed first and Gym Hero stayed
second, but Rooftop Lights (right mood, wrong genre) moved much closer to
Gym Hero. The results were different, not clearly better, because Gym Hero
(pop, intense) still ranked above a song that matches the "happy" mood.

**2. Different types of users.**
I tested five profiles:

- **High-Energy Pop:** got fast, loud pop songs like Sunrise City and Gym Hero.
- **Chill Lofi:** got slow, quiet, acoustic songs like Library Rain and
  Midnight Coding.
- **Deep Intense Rock:** got Storm Runner first, then loud songs from other
  genres.
- **Loud but Sad (folk, sad, energy 0.9):** a quiet folk song ranked first
  even though the listener wanted high energy. Genre and mood points
  outweighed the energy gap.
- **Unknown Genre (polka):** no song earned genre points, so results came
  only from mood, energy, and acoustic sound.

**3. Hand check.**
I calculated Storm Runner's score for Deep Intense Rock by hand (4.44) and
it matched the program's output.

---

## Limitations and Risks

- The catalog is tiny (18 songs), and most genres have only one song.
- Genre counts double compared with mood, so the system can over-favor
  genre. This is why Gym Hero keeps showing up for Happy Pop listeners.
- Genre and mood must match exactly, so "indie pop" gets no credit for
  being close to "pop."
- A listener can only have one favorite genre and one favorite mood.
- It does not understand lyrics, language, or artist, and it has no
  listening history like skips or playlists.
- The song numbers were written by hand, not measured from real audio.


---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

I learned that a recommender turns data into predictions by giving every
item a score and then sorting the scores. In my version, each song earned
points for matching the listener's genre and mood, and for having energy
and acoustic sound close to what they wanted. The reasons list showed
exactly where each score came from. That made the results easy to check,
and a hand calculation matched the program's output. Simple rules like
these already felt like real recommendations, which showed me how a system
can seem to "understand" taste when it is really just adding points.



