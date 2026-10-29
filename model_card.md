# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

MatchYourVibe 1.0

---

## 2. Intended Use  

MatchYourVibe 1.0 suggests the top 5 songs for a listener, based on a small taste
profile: favorite genre, favorite mood, target energy, and whether they like
acoustic sound. Each suggestion comes with the reasons it was picked.

---

## 3. How the Model Works  

Every song in the catalog gets points, and the points are added up:

- If the song's genre matches the listener's favorite genre: +2.0 points.
- If the song's mood matches the listener's favorite mood: +1.0 point.
- Energy: up to +1.0 point. The closer the song's energy is to what the
  listener wants, the more points it gets.
- Acoustic sound: up to +0.5 points. Listeners who like acoustic music get
  more points for acoustic songs. Other listeners get more points for
  non-acoustic songs.

Then all the songs are lined up from most points to fewest, and the top 5 are
shown. Each one lists the reasons it earned its points.
---

## 4. Data  

- The catalog has 18 songs: 10 from the starter file and 8 I added.
- Genres include pop, indie pop, lofi, rock, ambient, jazz, synthwave,
  hip hop, country, classical, metal, r&b, folk, electronic, and reggae.
- Moods include happy, chill, intense, relaxed, moody, focused, confident,
  nostalgic, romantic, angry, sad, and euphoric.
- I added 8 songs with new genres and moods, and I fixed one starter row that
  was missing values.
- Missing from the data: lyrics, language, artist popularity, listening
  history, and what people do in real apps, like skips and playlists. The
  numbers were written by hand, not measured from real audio.

---

## 5. Strengths  

- It works well for listeners with clear, matching tastes. Chill Lofi gets
  slow, quiet, acoustic lofi songs. Deep Intense Rock gets Storm Runner first.
  Both matched my intuition.
- Different profiles give different lists, so the scoring really reacts to
  what the listener asks for.
- The reasons next to each score make the results easy to understand and
  check by hand.
---

## 6. Limitations and Bias 

Genre is worth +2.0 and mood only +1.0, so a song with the right genre but
the wrong mood can beat a song with the right mood. This is why Gym Hero
(pop, intense) beats Rooftop Lights (indie pop, happy) for a Happy Pop
listener. Genre must match exactly, so "indie pop" gets no credit for being
close to "pop." In my Loud but Sad test, a quiet folk song ranked first even
though the listener wanted high energy, so the energy wish was mostly
ignored. The catalog is also tiny, and lofi has 3 songs while most genres
have 1, so lofi fans get more choices.
---

## 7. Evaluation  


Profiles tested: High-Energy Pop, Chill Lofi, Deep Intense Rock, Loud but Sad, and Unknown Genre (polka).

What surprised me: In Loud but Sad, the quiet folk song ranked first even though the listener wanted high energy. Genre and mood points added up to more than the energy gap could fix. With the polka profile, no song gets genre points, so the results come only from mood, energy, and acoustic sound.

High-Energy Pop vs. Chill Lofi: The pop profile gets fast, loud songs like Sunrise City and Gym Hero. The lofi profile gets slow, quiet, acoustic songs like Library Rain. They share no songs because every preference points the opposite way.

High-Energy Pop vs. Deep Intense Rock: Both want loud songs, so Gym Hero shows up in both lists. It’s pop (good for the first) and intense (good for the second). The #1 songs differ because each listener’s genre and mood match a different song.

Chill Lofi vs. Deep Intense Rock: These are opposites on genre, mood, energy, and acoustic taste, so their lists have nothing in common.

Why Gym Hero keeps showing up for Happy Pop listeners: It is a pop song, which earns +2.0, and its energy is very close to what they want. That beats songs that have the right mood but a different genre, because genre points count double.  

## 8. Future Work  

- Add many more songs, so every genre has several.
- Give partial credit for similar genres and moods, like "pop" and "indie pop."
- Let a listener pick more than one favorite genre or mood.
- Use valence and tempo in the scoring, so "intense but dark" songs differ
  from "intense but upbeat" ones.
- Show a short plain-language explanation for each pick, and avoid
  repeating the same genre in the top 5.
---

## 9. Personal Reflection  

I learned that a recommender is scoring plus ranking: every song gets points,
then the songs are sorted. Seeing the reasons beside each score made it feel
clear instead of magical. Something unexpected was how real the results felt
with only four simple rules. Chill Lofi gave me quiet study songs, and Deep
Intense Rock gave me loud ones. It made me think that apps like Spotify may
feel smart partly because simple rules, plus lots of data, can look like
understanding. I also saw that when a song keeps showing up, like Gym Hero,
it can be because of how the points are set, not because the app knows me.
I also learned to check the AI's work. I compared its predicted scores with
my real output and fixed code problems myself. 
