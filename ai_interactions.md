# AI Interactions Log

Stretch features only. Only fill in the sections that apply to stretch
features I attempted.

---

## Agentic Workflow (SF8)

### What task did you give the agent?

I asked the AI to add 5 new attributes to my song catalog and update both
`data/songs.csv` and the scoring logic in `src/recommender.py` so the new
attributes change the scores. The new attributes were `popularity` (0-100),
`release_decade`, `mood_tags`, `instrumental`, and `explicit`. I required
that older profiles keep working.

### Prompts used

- "Add 5 new columns to my songs.csv: popularity, release_decade, mood_tags,
  instrumental, explicit. Update load_songs to convert them to the right
  types, and update score_song so each one affects the score. Make every new
  preference optional so my old profiles still work."
- "Keep the original scoring unchanged when a profile does not use the new
  features."

### What did the agent generate or change?

- A script that added the 5 new columns to all 18 songs and saved a backup
  of the original CSV.
- An updated `load_songs` that converts the new numeric columns to numbers
  and splits `mood_tags` into a list.
- New scoring rules in `score_song`: popularity closeness, decade match,
  mood tag overlap, instrumental preference, and a penalty for explicit
  songs when the user wants clean songs only.
- Each new rule applies only when the profile asks for it, so older profiles
  score the same as before.

### What did you verify or fix manually?

- I ran the Deep Intense Rock profile in balanced mode and confirmed Storm
  Runner still scored about 4.44, so the original scoring was not broken.
- I opened `songs.csv` and checked that all 18 rows had the new columns
  filled in with no blanks.
- I checked that the Nostalgic Study profile showed tag match, decade match,
  and instrumental fit in its reasons.
- I fixed small problems myself, such as a row missing values and file
  changes that had not been saved.

---

## Design Pattern (SF10)

### Which design pattern did you use?

A simple Strategy pattern. The scoring steps stay the same, and each ranking
mode is a different set of weights passed into the scoring function.

### How did AI help you brainstorm or implement it?

I told the AI I wanted several ranking styles (genre-first, mood-first,
energy-focused) without copying the scoring code for each one. It suggested
storing each mode as a dictionary of weights and passing the chosen
dictionary into the scoring function. I chose this over writing a separate
function per mode because adding a new mode takes one small dictionary and
leaves the scoring steps untouched. I picked the weight numbers for each
mode myself.

### How does the pattern appear in your final code?

- `MODES` is a dictionary in `src/recommender.py` holding four modes:
  balanced, genre_first, mood_first, and energy_focused.
- `score_song(user_prefs, song, weights)` takes the weights as an input
  instead of using fixed numbers.
- `recommend_songs(user_prefs, songs, k, mode)` looks up the chosen mode and
  passes its weights to `score_song`.
- `main.py` loops through every mode for each profile so results can be
  compared side by side.
