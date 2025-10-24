# Music Theory Reference for Sound Design & Composition

## Intervals

### Interval Quality and Distance

| Interval | Semitones | Example (from C) | Quality | Feeling |
|----------|-----------|------------------|---------|---------|
| Unison | 0 | C - C | Perfect | Stable, foundation |
| Minor 2nd | 1 | C - Db | Dissonant | Tense, dark |
| Major 2nd | 2 | C - D | Consonant | Bright, open |
| Minor 3rd | 3 | C - Eb | Consonant | Sad, minor |
| Major 3rd | 4 | C - E | Consonant | Happy, major |
| Perfect 4th | 5 | C - F | Perfect | Stable, suspense |
| Tritone | 6 | C - F# | Dissonant | Unstable, evil |
| Perfect 5th | 7 | C - G | Perfect | Strong, power |
| Minor 6th | 8 | C - Ab | Consonant | Melancholic |
| Major 6th | 9 | C - A | Consonant | Smooth, jazzy |
| Minor 7th | 10 | C - Bb | Dissonant | Bluesy, tension |
| Major 7th | 11 | C - B | Dissonant | Ethereal, jazz |
| Octave | 12 | C - C | Perfect | Complete, same |

### Interval Usage in Sound Design

**Power Chords** (Root + 5th):
- Perfect for distorted sounds
- No 3rd = neither major nor minor
- Strong, aggressive feel
- MIDI: [60, 67] (C-G)

**Tritone** (Root + Tritone):
- Maximum tension
- Horror, metal, industrial
- Resolves strongly
- MIDI: [60, 66] (C-F#)

**Major 7th** (Root + Major 7th):
- Dreamy, floating
- Jazz, ambient
- Rich harmonics
- MIDI: [60, 71] (C-B)

---

## Scales & Modes

### Major Scale (Ionian Mode)

**Formula**: W-W-H-W-W-W-H  
(W = whole step/2 semitones, H = half step/1 semitone)

**C Major**: C D E F G A B C  
**MIDI Notes**: [60, 62, 64, 65, 67, 69, 71, 72]

**Chord Built on Each Degree**:
- I: Cmaj (C-E-G) - Tonic
- ii: Dm (D-F-A) - Supertonic
- iii: Em (E-G-B) - Mediant
- IV: F (F-A-C) - Subdominant
- V: G (G-B-D) - Dominant
- vi: Am (A-C-E) - Submediant
- vii°: Bdim (B-D-F) - Leading tone

### Natural Minor Scale (Aeolian Mode)

**Formula**: W-H-W-W-H-W-W

**A Minor**: A B C D E F G A  
**MIDI Notes**: [57, 59, 60, 62, 64, 65, 67, 69]

**Chord Built on Each Degree**:
- i: Am (A-C-E) - Tonic
- ii°: Bdim (B-D-F) - Supertonic
- III: C (C-E-G) - Mediant
- iv: Dm (D-F-A) - Subdominant
- v: Em (E-G-B) - Dominant
- VI: F (F-A-C) - Submediant
- VII: G (G-B-D) - Subtonic

### Harmonic Minor

**Formula**: W-H-W-W-H-W+H-H

**A Harmonic Minor**: A B C D E F G# A  
**MIDI Notes**: [57, 59, 60, 62, 64, 65, 68, 69]

**Characteristics**:
- Raised 7th degree (G → G#)
- Creates augmented 2nd interval (F → G#)
- Very Middle Eastern/exotic sound
- Strong V-i resolution (E major → A minor)

### Melodic Minor (Ascending)

**Formula**: W-H-W-W-W-W-H

**A Melodic Minor**: A B C D E F# G# A  
**MIDI Notes**: [57, 59, 60, 62, 64, 66, 68, 69]

**Characteristics**:
- Raised 6th and 7th (F→F#, G→G#)
- More major-like sound
- Jazz favorite
- Descending = natural minor

---

## The Seven Modes

All modes derived from major scale, starting on different degrees:

### Ionian (Major Scale)
**From C**: C D E F G A B C  
**Feel**: Happy, bright, traditional  
**Use**: Pop, classical, uplifting

### Dorian
**From D**: D E F G A B C D  
**Feel**: Minor but brighter than Aeolian  
**Use**: Jazz, funk, smooth minor

### Phrygian
**From E**: E F G A B C D E  
**Feel**: Dark, Spanish, exotic  
**Use**: Metal, flamenco, dark ambient

### Lydian
**From F**: F G A B C D E F  
**Feel**: Dreamy, floating, magical  
**Use**: Film scores, ambient, ethereal

### Mixolydian
**From G**: G A B C D E F G  
**Feel**: Bluesy, rock, slightly darker than major  
**Use**: Rock, blues, folk

### Aeolian (Natural Minor)
**From A**: A B C D E F G A  
**Feel**: Sad, melancholic, traditional minor  
**Use**: Most minor key music

### Locrian
**From B**: B C D E F G A B  
**Feel**: Unstable, dissonant, unsettling  
**Use**: Experimental, horror, metal

---

## Chord Construction

### Triads

**Major Triad**: Root + Major 3rd + Perfect 5th  
Example: C major = C-E-G = [60, 64, 67]

**Minor Triad**: Root + Minor 3rd + Perfect 5th  
Example: C minor = C-Eb-G = [60, 63, 67]

**Diminished Triad**: Root + Minor 3rd + Diminished 5th  
Example: C dim = C-Eb-Gb = [60, 63, 66]

**Augmented Triad**: Root + Major 3rd + Augmented 5th  
Example: C aug = C-E-G# = [60, 64, 68]

### Seventh Chords

**Major 7th**: Root + M3 + P5 + M7  
Example: Cmaj7 = C-E-G-B = [60, 64, 67, 71]  
**Feel**: Jazzy, sophisticated, warm

**Minor 7th**: Root + m3 + P5 + m7  
Example: Cm7 = C-Eb-G-Bb = [60, 63, 67, 70]  
**Feel**: Smooth, jazzy minor

**Dominant 7th**: Root + M3 + P5 + m7  
Example: C7 = C-E-G-Bb = [60, 64, 67, 70]  
**Feel**: Bluesy, wants to resolve

**Minor 7 Flat 5 (Half-Diminished)**: Root + m3 + dim5 + m7  
Example: Cm7b5 = C-Eb-Gb-Bb = [60, 63, 66, 70]  
**Feel**: Jazzy, tense, dark

**Diminished 7th**: Root + m3 + dim5 + dim7  
Example: Cdim7 = C-Eb-Gb-Bbb = [60, 63, 66, 69]  
**Feel**: Very tense, transitional

### Extended Chords

**9th Chords**: Add 9th (2nd an octave up)  
Example: Cmaj9 = C-E-G-B-D = [60, 64, 67, 71, 74]  
**Use**: Lush pads, jazz, sophisticated harmony

**11th Chords**: Add 11th (4th an octave up)  
Example: Cm11 = C-Eb-G-Bb-D-F = [60, 63, 67, 70, 74, 77]  
**Use**: Very jazzy, complex ambient

**13th Chords**: Add 13th (6th an octave up)  
Example: C13 = C-E-G-Bb-D-F-A = [60, 64, 67, 70, 74, 77, 81]  
**Use**: Jazz, funk, very colorful

### Sus Chords (Suspended)

**Sus2**: Root + Major 2nd + Perfect 5th  
Example: Csus2 = C-D-G = [60, 62, 67]  
**Feel**: Open, ambiguous, modern

**Sus4**: Root + Perfect 4th + Perfect 5th  
Example: Csus4 = C-F-G = [60, 65, 67]  
**Feel**: Suspended, wants to resolve, rock

---

## Harmonic Function

### Three Main Functions

**Tonic (T)** - Home, stability, resolution  
Chords: I, vi, iii (in major)  
Example: C, Am, Em in C major

**Subdominant (S)** - Movement away from tonic  
Chords: IV, ii  
Example: F, Dm in C major

**Dominant (D)** - Tension, wants to resolve to tonic  
Chords: V, vii°  
Example: G, Bdim in C major

### Common Progressions by Function

**T → S → D → T**  
Example: I - IV - V - I (C - F - G - C)  
Feel: Complete, resolved, traditional

**T → S → T**  
Example: I - IV - I (C - F - C)  
Feel: Gentle movement, back home

**T → D → T**  
Example: I - V - I (C - G - C)  
Feel: Strong resolution, powerful

---

## Voice Leading

### Rules for Smooth Chord Progressions

1. **Move voices by smallest distance possible**
   - Cmaj (C-E-G) → Fmaj (C-F-A)
   - Keep C, move E→F, G→A

2. **Common tones stay in same voice**
   - Cmaj (C-E-G) → Am (C-E-A)
   - Keep C and E, only move G→A

3. **Avoid parallel fifths and octaves**
   - Bad: C-G moving to D-A (parallel 5ths)
   - Good: C-G moving to D-F (contrary motion)

4. **Leading tone resolves up**
   - In G7→C, B should move to C

### MIDI Implementation Example

**Smooth progression**: C → Am → F → G  

```
C:  [60, 64, 67]  (C-E-G)
Am: [60, 64, 69]  (C-E-A)  - only top note moves
F:  [60, 65, 69]  (C-F-A)  - only middle note moves
G:  [59, 62, 67]  (B-D-G)  - all move by step
```

---

## Rhythm & Time Signatures

### Common Time Signatures

**4/4** - Four quarter notes per bar  
Use: Most popular music, house, techno  
Feel: Stable, danceable

**3/4** - Three quarter notes per bar  
Use: Waltz, some ambient  
Feel: Lilting, flowing

**6/8** - Six eighth notes per bar (felt in 2)  
Use: Ballads, some electronic  
Feel: Rolling, compound

**5/4** - Five quarter notes per bar  
Use: Progressive, experimental  
Feel: Uneven, interesting

**7/8** - Seven eighth notes per bar  
Use: Balkan, progressive metal  
Feel: Complex, driving

### Polyrhythms

**3 against 4**:  
- Layer 1: Quarter note triplets
- Layer 2: Regular 16th notes
- Creates tension and interest

**5 against 4**:
- Layer 1: Quintuplets
- Layer 2: 16th notes
- Very complex, IDM style

---

## Tension & Release

### Creating Tension

1. **Harmonic**: Use dominant 7th, diminished chords
2. **Melodic**: Use dissonant intervals (m2, tritone)
3. **Rhythmic**: Syncopation, polyrhythms
4. **Textural**: Increase density, add noise
5. **Dynamic**: Crescendo, louder elements

### Creating Release

1. **Harmonic**: Resolve to tonic, use sus chords
2. **Melodic**: Use consonant intervals (5th, octave)
3. **Rhythmic**: Return to steady pulse
4. **Textural**: Reduce layers, simplify
5. **Dynamic**: Decrescendo, softer elements

---

## Key Relationships

### Circle of Fifths

```
        C
    F       G
  Bb          D
 Eb            A
F#/Gb        E
  Db          B
    Ab      F#
        Cb
```

**Moving clockwise**: Up a 5th (brighter)  
**Moving counter-clockwise**: Down a 5th (darker)

### Relative Keys

**Relative Minor**: 3 semitones down from major  
- C major → A minor (share same notes)

**Parallel Keys**: Same root, different quality  
- C major → C minor (different notes)

---

## Transposition

### How to Transpose

**By Interval**:
- Original: C-E-G (C major)
- Up a 4th: F-A-C (F major)
- Semitone shift: +5

**By Scale Degree**:
- I-IV-V in C = C-F-G
- I-IV-V in D = D-G-A
- Same relationships, different key

### MIDI Transposition

Simply add/subtract semitones:
```python
original = [60, 64, 67]  # C major
up_5_semitones = [65, 69, 72]  # F major
down_3_semitones = [57, 61, 64]  # A major
```

---

## Sound Design Applications

### Using Theory in Patch Design

**Unison Detuning**:
- Use harmonic intervals (5 cents, 7 cents, 12 cents)
- Creates natural, musical width

**Chord Stacking in Pads**:
- Layer 1: Root note
- Layer 2: Root + 5th
- Layer 3: Root + 3rd + 5th + 7th
- Creates thick, harmonically rich pad

**Bassline Construction**:
- Follow chord roots
- Add passing tones (scale notes between chords)
- Use rhythmic syncopation

**Melody Over Harmony**:
- Use chord tones on strong beats
- Use scale tones on weak beats
- Passing tones for movement

---

## Reference: All Keys & Scales (MIDI)

### C Major / A Minor
**Major**: [60, 62, 64, 65, 67, 69, 71]  
**Minor**: [57, 59, 60, 62, 64, 65, 67]

### D Major / B Minor
**Major**: [62, 64, 66, 67, 69, 71, 73]  
**Minor**: [59, 61, 62, 64, 66, 67, 69]

### E Major / C# Minor
**Major**: [64, 66, 68, 69, 71, 73, 75]  
**Minor**: [61, 63, 64, 66, 68, 69, 71]

### F Major / D Minor
**Major**: [65, 67, 69, 70, 72, 74, 76]  
**Minor**: [62, 64, 65, 67, 69, 70, 72]

### G Major / E Minor
**Major**: [67, 69, 71, 72, 74, 76, 78]  
**Minor**: [64, 66, 67, 69, 71, 72, 74]

### A Major / F# Minor
**Major**: [69, 71, 73, 74, 76, 78, 80]  
**Minor**: [66, 68, 69, 71, 73, 74, 76]

### B Major / G# Minor
**Major**: [71, 73, 75, 76, 78, 80, 82]  
**Minor**: [68, 70, 71, 73, 75, 76, 78]

---

**Use this reference when:**
- Suggesting scales for mood-based composition
- Building chord progressions
- Analyzing harmonic content
- Creating melodic lines
- Transposing music to different keys
