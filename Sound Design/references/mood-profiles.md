# Mood Profiles for Melody Generation

Algorithmic parameters for generating melodies that match specific emotional moods.

---

## 😊 HAPPY

### Interval Preferences
**Preferred Intervals** (semitones):
- 2 (Major 2nd) - Stepwise, smooth
- 4 (Major 3rd) - Bright, uplifting
- 5 (Perfect 4th) - Stable, strong
- 7 (Perfect 5th) - Perfect consonance

**Avoid Intervals**:
- 1 (Minor 2nd) - Too tense
- 6 (Tritone) - Dissonant
- 11 (Major 7th) - Too jazzy

### Movement Parameters
- **Direction Bias**: 0.6 (60% upward movement)
- **Leap Probability**: 0.3 (30% chance of jumps)
- **Step Probability**: 0.7 (70% stepwise motion)
- **Rest Probability**: 0.1 (10% rests - minimal pauses)

### Rhythm Characteristics
- **Rhythm Variety**: 0.6 (moderate variation)
- **Preferred Patterns**: steady, varied, flowing
- **Note Durations**: Quarter and eighth notes
- **Syncopation**: Moderate

### Range & Register
- **Range Preference**: middle-high
- **Typical Register**: C4-C6
- **Octave Span**: 1.5-2 octaves
- **Starting Notes**: 3rd or 5th of scale

### Recommended Scales
- Ionian (Major)
- Lydian
- Mixolydian

### Tempo Preference
- **Ideal**: 120-140 BPM
- **Range**: 110-160 BPM

---

## 😢 SAD

### Interval Preferences
**Preferred Intervals**:
- 1 (Minor 2nd) - Sighing effect
- 2 (Major 2nd) - Stepwise descent
- 3 (Minor 3rd) - Sad, melancholic
- 5 (Perfect 4th) - Gentle movement

**Avoid Intervals**:
- 4 (Major 3rd) - Too bright
- 7 (Perfect 5th) - Too strong

### Movement Parameters
- **Direction Bias**: 0.3 (70% downward - descending)
- **Leap Probability**: 0.2 (20% - mostly stepwise)
- **Step Probability**: 0.8 (80% stepwise)
- **Rest Probability**: 0.25 (25% - breathing pauses)

### Rhythm Characteristics
- **Rhythm Variety**: 0.4 (lower variation - consistent)
- **Preferred Patterns**: steady, sparse
- **Note Durations**: Quarter notes, half notes
- **Syncopation**: Minimal

### Range & Register
- **Range Preference**: low-middle
- **Typical Register**: C3-G4
- **Octave Span**: 1-1.5 octaves
- **Starting Notes**: Root or minor 3rd

### Recommended Scales
- Aeolian (Natural Minor)
- Phrygian
- Dorian

### Tempo Preference
- **Ideal**: 70-90 BPM
- **Range**: 60-100 BPM

---

## 🌑 DARK

### Interval Preferences
**Preferred Intervals**:
- 1 (Minor 2nd) - Chromatic tension
- 3 (Minor 3rd) - Dark color
- 6 (Tritone) - Devil's interval, ominous
- 8 (Minor 6th) - Haunting

**Avoid Intervals**:
- 4 (Major 3rd) - Too bright
- 7 (Perfect 5th) - Too stable

### Movement Parameters
- **Direction Bias**: 0.35 (65% downward)
- **Leap Probability**: 0.4 (40% - dramatic jumps)
- **Step Probability**: 0.6 (60% stepwise)
- **Rest Probability**: 0.2 (20% - dramatic pauses)

### Rhythm Characteristics
- **Rhythm Variety**: 0.5 (moderate)
- **Preferred Patterns**: sparse, syncopated
- **Note Durations**: Long notes with sudden changes
- **Syncopation**: Moderate to high

### Range & Register
- **Range Preference**: low
- **Typical Register**: C2-C4
- **Octave Span**: 1-1.5 octaves
- **Starting Notes**: Root or flat 2nd

### Recommended Scales
- Phrygian
- Locrian
- Phrygian Dominant
- Harmonic Minor

### Tempo Preference
- **Ideal**: 80-100 BPM
- **Range**: 60-120 BPM

---

## ⚡ ENERGETIC

### Interval Preferences
**Preferred Intervals**:
- 2 (Major 2nd) - Quick movement
- 4 (Major 3rd) - Bright
- 5 (Perfect 4th) - Strong
- 7 (Perfect 5th) - Powerful
- 9 (Major 6th) - Wide leaps

**Avoid Intervals**:
- 1 (Minor 2nd) - Slows momentum

### Movement Parameters
- **Direction Bias**: 0.5 (balanced - no bias)
- **Leap Probability**: 0.5 (50% - many jumps)
- **Step Probability**: 0.5 (50% stepwise)
- **Rest Probability**: 0.05 (5% - almost no rests)

### Rhythm Characteristics
- **Rhythm Variety**: 0.8 (high variation)
- **Preferred Patterns**: syncopated, varied, flowing
- **Note Durations**: Eighth and sixteenth notes
- **Syncopation**: High

### Range & Register
- **Range Preference**: full
- **Typical Register**: C3-C6
- **Octave Span**: 2-3 octaves
- **Starting Notes**: 5th for power

### Recommended Scales
- Mixolydian
- Dorian
- Major (Ionian)

### Tempo Preference
- **Ideal**: 130-145 BPM
- **Range**: 120-160 BPM

---

## 🧘 CALM

### Interval Preferences
**Preferred Intervals**:
- 2 (Major 2nd) - Gentle steps
- 3 (Minor 3rd) - Soft
- 5 (Perfect 4th) - Stable

**Avoid Intervals**:
- 6 (Tritone) - Too dissonant
- 11 (Major 7th) - Too tense

### Movement Parameters
- **Direction Bias**: 0.5 (balanced - horizontal)
- **Leap Probability**: 0.15 (15% - very few leaps)
- **Step Probability**: 0.85 (85% stepwise)
- **Rest Probability**: 0.2 (20% - breathing space)

### Rhythm Characteristics
- **Rhythm Variety**: 0.3 (low - consistent)
- **Preferred Patterns**: steady, flowing
- **Note Durations**: Quarter notes, half notes
- **Syncopation**: Very low

### Range & Register
- **Range Preference**: middle
- **Typical Register**: G3-G5
- **Octave Span**: 1 octave
- **Starting Notes**: Root or 5th

### Recommended Scales
- Pentatonic Major
- Ionian (Major)
- Lydian

### Tempo Preference
- **Ideal**: 75-95 BPM
- **Range**: 60-110 BPM

---

## 🕵️ MYSTERIOUS

### Interval Preferences
**Preferred Intervals**:
- 1 (Minor 2nd) - Chromatic sneaking
- 3 (Minor 3rd) - Uncertain
- 6 (Tritone) - Unsettling
- 10 (Minor 7th) - Unresolved

**Avoid Intervals**:
- 4 (Major 3rd) - Too clear
- 7 (Perfect 5th) - Too stable

### Movement Parameters
- **Direction Bias**: 0.5 (no bias - unpredictable)
- **Leap Probability**: 0.35 (35% - some surprises)
- **Step Probability**: 0.65 (65% stepwise)
- **Rest Probability**: 0.3 (30% - many pauses)

### Rhythm Characteristics
- **Rhythm Variety**: 0.6 (varied)
- **Preferred Patterns**: syncopated, sparse
- **Note Durations**: Irregular, unpredictable
- **Syncopation**: Moderate to high

### Range & Register
- **Range Preference**: wide
- **Typical Register**: C3-C6
- **Octave Span**: 2+ octaves
- **Starting Notes**: Unusual (flat 2nd, tritone)

### Recommended Scales
- Locrian
- Phrygian Dominant
- Diminished
- Whole Tone

### Tempo Preference
- **Ideal**: 95-115 BPM
- **Range**: 80-130 BPM

### 🎞️ CINEMATIC

**Context:** Moderat, Rival Consoles, Jon Hopkins

**Interval Preferences**

- Preferred: 3 (Minor 3rd), 5 (Perfect 4th), 7 (Perfect 5th), 9 (Major 6th)
- Avoid: 1 (Minor 2nd), 11 (Major 7th)

**Movement Parameters**

- Direction Bias: 0.55 (slightly upward)
- Leap Probability: 0.25
- Step Probability: 0.75
- Rest Probability: 0.15

**Rhythm Characteristics**

- Rhythm Variety: 0.5 (moderate)
- Patterns: flowing, syncopated, cinematic phrasing
- Durations: Quarter, dotted-quarter, half
- Syncopation: medium-high

**Range & Register**

- Range Preference: wide (C3–C6)
- Starting Notes: 3rd or 5th

**Scales**

- Dorian, Lydian, Harmonic Minor

**Tempo**

- Ideal: 100–115 BPM

> [!TIP]  
> Use tension–release arcs: start in minor intervals, ascend toward perfect 5ths for emotional resolution.

---

### 🌫️ ATMOSPHERIC

**Context:** Weval, Christian Löffler, Kiasmos

**Interval Preferences**

- Preferred: 2 (Major 2nd), 4 (Major 3rd), 5 (Perfect 4th)
- Avoid: 6 (Tritone)

**Movement Parameters**

- Direction Bias: 0.45
- Leap Probability: 0.1
- Step Probability: 0.9
- Rest Probability: 0.25

**Rhythm Characteristics**

- Rhythm Variety: 0.3
- Patterns: flowing, sparse
- Durations: Half and dotted-half
- Syncopation: Low

**Range & Register**

- Middle to low (C3–C5)
- Starting Notes: Root

**Scales**

- Mixolydian, Dorian, Pentatonic Major

**Tempo**

- Ideal: 90–105 BPM

> [!TIP]  
> Long envelopes and gentle legato motion amplify emotional depth; think “breathing through sound”.

---

### 🌀 TEXTURAL

**Context:** Rival Consoles, Max Cooper, Pantha du Prince

**Interval Preferences**

- Preferred: 1 (Minor 2nd), 2 (Major 2nd), 6 (Tritone), 10 (Minor 7th)
- Avoid: 7 (Perfect 5th)

**Movement Parameters**

- Direction Bias: 0.5
- Leap Probability: 0.35
- Step Probability: 0.65
- Rest Probability: 0.2

**Rhythm Characteristics**

- Rhythm Variety: 0.6
- Patterns: syncopated, polymetric
- Durations: Irregular (mix of eighths, dotted, and tied)
- Syncopation: High

**Range & Register**

- Full (C2–C6)
- Starting Notes: Tritone or minor 7th

**Scales**

- Dorian, Whole Tone, Locrian

**Tempo**

- Ideal: 110–125 BPM

> [!TIP]  
> Use controlled dissonance: short intervals modulated dynamically create spectral movement rather than tonal melody.

---

### 🫧 ORGANIC

**Context:** Weval, Monolink, Ben Böhmer

**Interval Preferences**

- Preferred: 2 (Major 2nd), 4 (Major 3rd), 5 (Perfect 4th)
- Avoid: 6 (Tritone), 11 (Major 7th)

**Movement Parameters**

- Direction Bias: 0.55 (gentle upward)
- Leap Probability: 0.15
- Step Probability: 0.85
- Rest Probability: 0.25

**Rhythm Characteristics**

- Rhythm Variety: 0.4
- Patterns: flowing, humanized
- Durations: Quarter and dotted-quarter
- Syncopation: Medium

**Range & Register**

- Low–middle (C3–C5)
- Starting Notes: 3rd

**Scales**

- Mixolydian, Pentatonic Major, Dorian

**Tempo**

- Ideal: 95–110 BPM

> [!TIP]  
> Introduce micro-timing shifts (±5–15ms) to emulate human swing; organic melodies prefer imperfect phrasing.

---

### 💭 INTROSPECTIVE

**Context:** Rival Consoles, Nils Frahm, Olafur Arnalds

**Interval Preferences**

- Preferred: 3 (Minor 3rd), 5 (Perfect 4th), 8 (Minor 6th), 10 (Minor 7th)
- Avoid: 4 (Major 3rd), 7 (Perfect 5th)

**Movement Parameters**

- Direction Bias: 0.4 (mostly downward)
- Leap Probability: 0.25
- Step Probability: 0.75
- Rest Probability: 0.35

**Rhythm Characteristics**

- Rhythm Variety: 0.4
- Patterns: sparse, reflective
- Durations: Long (half, whole)
- Syncopation: Low

**Range & Register**

- Middle–low (C3–C5)
- Starting Notes: Minor 3rd or 6th

**Scales**

- Aeolian, Dorian, Melancholic Minor

**Tempo**

- Ideal: 80–95 BPM

> [!TIP]  
> Use velocity curves that fade slowly; introspection emerges from restraint, not silence.

---

### 🔥 EUPHORIC

**Context:** Jon Hopkins, Moderat (live versions), Max Cooper

**Interval Preferences**

- Preferred: 4 (Major 3rd), 5 (Perfect 4th), 7 (Perfect 5th), 9 (Major 6th)
- Avoid: 1 (Minor 2nd), 6 (Tritone)

**Movement Parameters**

- Direction Bias: 0.65 (ascending bias)
- Leap Probability: 0.35
- Step Probability: 0.65
- Rest Probability: 0.05

**Rhythm Characteristics**

- Rhythm Variety: 0.8
- Patterns: syncopated, progressive
- Durations: Eighths and sixteenths
- Syncopation: High

**Range & Register**

- Middle-high (C4–C6)
- Starting Notes: 5th

**Scales**

- Lydian, Ionian, Mixolydian

**Tempo**

- Ideal: 120–135 BPM

> [!TIP]  
> Pair rising intervals with rhythmic density; euphoria comes from energy escalation, not harmonic change.

---

### 👁‍🗨 HAUNTING

**Context:** Moderat, Rival Consoles (slow pieces), Clark

**Interval Preferences**

- Preferred: 1 (Minor 2nd), 3 (Minor 3rd), 6 (Tritone), 8 (Minor 6th)
- Avoid: 4 (Major 3rd), 7 (Perfect 5th)

**Movement Parameters**

- Direction Bias: 0.4
- Leap Probability: 0.3
- Step Probability: 0.7
- Rest Probability: 0.3

**Rhythm Characteristics**

- Rhythm Variety: 0.5
- Patterns: sparse, staggered
- Durations: Long with dotted attacks
- Syncopation: Moderate

**Range & Register**

- Low–middle (C2–C5)
- Starting Notes: Flat 2nd or tritone

**Scales**

- Phrygian, Locrian, Harmonic Minor

**Tempo**

- Ideal: 85–105 BPM

> [!TIP]  
> Introduce subtle dissonance within reverb tails; the “haunting” effect lies in harmonics bleeding into silence.

---

## 🎼 RHYTHM PATTERNS

Common rhythm patterns referenced by mood profiles.

### Steady
**Pattern**: [4, 4, 4, 4]  
**Description**: Quarter notes, even, predictable  
**Use**: Calm, Happy  
**Feel**: Grounded, stable

### Varied
**Pattern**: [4, 4, 2, 2, 4]  
**Description**: Mix of quarters and eighths  
**Use**: Happy, Energetic  
**Feel**: Interesting but controlled

### Flowing
**Pattern**: [2, 2, 2, 2, 4, 4]  
**Description**: Eighth notes flowing to quarters  
**Use**: Calm, Atmospheric  
**Feel**: Gentle movement

### Syncopated
**Pattern**: [2, 4, 2, 4, 2, 2]  
**Description**: Off-beat accents  
**Use**: Energetic, Mysterious  
**Feel**: Driving, unexpected

### Triplet
**Pattern**: [3, 3, 3, 3]  
**Description**: Triplet feel (approximate)  
**Use**: Flowing, special effects  
**Feel**: Rolling, continuous

### Sparse
**Pattern**: [4, 8, 4, 8]  
**Description**: Notes with rests  
**Use**: Sad, Dark, Mysterious  
**Feel**: Spacious, dramatic

---

## 📊 PARAMETER TABLES

### Direction Bias Explained

| Value | Meaning | Movement |
|-------|---------|----------|
| 0.0-0.3 | Downward | 70-100% down |
| 0.3-0.4 | Mostly down | 60-70% down |
| 0.4-0.6 | Balanced | 50/50 |
| 0.6-0.7 | Mostly up | 60-70% up |
| 0.7-1.0 | Upward | 70-100% up |

### Leap vs Step Probability

| Leap Prob | Step Prob | Feel |
|-----------|-----------|------|
| 0.1-0.2 | 0.8-0.9 | Very smooth, flowing |
| 0.2-0.35 | 0.65-0.8 | Mostly smooth |
| 0.35-0.5 | 0.5-0.65 | Balanced |
| 0.5-0.7 | 0.3-0.5 | Jumpy, energetic |

### Rest Probability Impact

| Value | Description | Use |
|-------|-------------|-----|
| 0.0-0.1 | Almost none | Energetic, driving |
| 0.1-0.2 | Minimal | Happy, flowing |
| 0.2-0.3 | Moderate | Calm, dark |
| 0.3+ | Frequent | Sad, mysterious |

### Rhythm Variety Scale

| Value | Description | Feel |
|-------|-------------|------|
| 0.0-0.3 | Very consistent | Predictable, calm |
| 0.3-0.5 | Moderate | Balanced |
| 0.5-0.7 | Varied | Interesting |
| 0.7-1.0 | Highly varied | Exciting, complex |

---

## 🎯 PRACTICAL USAGE

### Combining Parameters

**Example: Happy Melody**
```python
mood = "happy"
profile = MOOD_PROFILES[mood]

# Generate note
if random.random() < profile["leap_probability"]:
    # Make a leap from preferred intervals
    interval = random.choice(profile["preferred_intervals"])
else:
    # Stepwise motion (2 semitones max)
    interval = random.choice([1, 2])

# Apply direction bias
if random.random() < profile["direction_bias"]:
    pitch += interval  # Move up
else:
    pitch -= interval  # Move down
```

### Adaptive Generation

**Energy Build-Up**:
```python
# Start calm, build to energetic
progress = current_bar / total_bars

# Interpolate between profiles
leap_prob = interpolate(
    calm["leap_probability"],
    energetic["leap_probability"],
    progress
)
```

---

## 🎨 MOOD COMBINATIONS

### Layering Moods

**Bittersweet** = Sad + Happy
- Use sad intervals and movement
- Add happy rhythm variety
- Middle register
- Moderate tempo

**Intense Mystery** = Dark + Energetic
- Dark intervals (tritones, minor 2nds)
- Energetic rhythm (high variety)
- Wide leaps
- Fast tempo

**Peaceful Sadness** = Calm + Sad
- Sad intervals (minor 3rds)
- Calm rhythm (low variety)
- Narrow range
- Slow tempo

- _“Cinematic Calm”_ = Calm + Cinematic
- _“Organic Melancholy”_ = Sad + Organic
- _“Euphoric Dark”_ = Energetic + Haunting
- _“Reflective Drive”_ = Introspective + Energetic

---

## 🔬 TECHNICAL DETAILS

### Interval Distance in Semitones

| Interval Name | Semitones | Example (from C) |
|--------------|-----------|------------------|
| Minor 2nd | 1 | C → C# |
| Major 2nd | 2 | C → D |
| Minor 3rd | 3 | C → Eb |
| Major 3rd | 4 | C → E |
| Perfect 4th | 5 | C → F |
| Tritone | 6 | C → F# |
| Perfect 5th | 7 | C → G |
| Minor 6th | 8 | C → Ab |
| Major 6th | 9 | C → A |
| Minor 7th | 10 | C → Bb |
| Major 7th | 11 | C → B |
| Octave | 12 | C → C |

### Range Preference Mapping

| Preference | MIDI Range | Register |
|------------|------------|----------|
| low | 36-60 | C2-C4 |
| low-middle | 48-72 | C3-C5 |
| middle | 60-84 | C4-C6 |
| middle-high | 64-88 | E4-E6 |
| high | 72-96 | C5-C7 |
| full | 36-96 | C2-C7 |
| wide | 36-84 | C2-C6 |

---

## 💡 COMPOSITION TIPS

### Starting a Melody

1. **Choose mood** → Get profile
2. **Pick scale** → From recommended
3. **Set tempo** → Within ideal range
4. **Choose register** → Based on range preference
5. **Generate phrase** → Apply parameters
6. **Add rests** → Based on rest probability
7. **Vary rhythm** → Based on rhythm variety

### Phrase Structure

**Typical 4-bar phrase**:
- Bar 1: Establish mood (follow profile closely)
- Bar 2: Develop (slight variation)
- Bar 3: Contrast (try opposite direction)
- Bar 4: Resolve (return to starting area)

### Dynamic Application

**Intro** (bars 1-4):
- Lower rhythm variety
- Fewer leaps
- Establish character

**Build** (bars 5-12):
- Increase rhythm variety
- More leaps
- Wider range

**Climax** (bars 13-16):
- Maximum parameters
- Highest notes
- Most variation

**Outro** (bars 17-20):
- Return to intro levels
- Fewer rests
- Narrow range

---

## 🎨 MOOD COMBINATIONS

| Combination | Blend | Example Context |
|--------------|--------|----------------|
| **Cinematic Calm** | Cinematic + Atmospheric | Jon Hopkins – “Emerald Rush” |
| **Organic Melancholy** | Organic + Introspective | Weval – “Someday” |
| **Euphoric Dark** | Euphoric + Haunting | Moderat – “A New Error” |
| **Reflective Drive** | Introspective + Euphoric | Rival Consoles – “Lone” |
| **Textural Warmth** | Textural + Organic | Max Cooper – “Resynthesis” |
| **Haunting Serenity** | Haunting + Atmospheric | Clark – “Suspension” |

---

## 🧩 MOOD → GENRE MAPPING

| Mood | Core Genres | Example Artists |
|------|--------------|-----------------|
| Cinematic | Berlin Electronica, Post-Techno | Moderat, Jon Hopkins |
| Atmospheric | Organic Techno, Downtempo | Weval, Christian Löffler |
| Textural | Neo-IDM, Ambient Techno | Rival Consoles, Max Cooper |
| Organic | Indie Electronica, Organic Techno | Weval, Kiasmos |
| Introspective | Ambient, Modern Classical | Nils Frahm, Rival Consoles |
| Euphoric | Cinematic Techno, Melodic Electronica | Jon Hopkins, Ben Böhmer |
| Haunting | Dark Ambient, Post-Techno | Moderat, Clark |

---

## ⚙️ ADVANCED PARAMETERS

| Parameter | Range | Description |
|------------|--------|-------------|
| **density_curve** | 0–1 | Evolution of rhythmic and harmonic density through time |
| **modulation_complexity** | 0–1 | Depth and number of modulation layers per cycle |
| **texture_randomness** | 0–1 | Degree of timbral instability (LFO random depth) |
| **spatial_breathing** | 0–1 | Reverb/LFO fluctuation amplitude to simulate organic movement |
| **velocity_humanization** | 0–1 | Random offset on note velocities for humanized phrasing |

> [!TIP]
> For **Weval/Moderat/Rival Consoles**-style compositions, target `density_curve ≈ 0.45–0.65`, `modulation_complexity > 0.6`, and low but steady `spatial_breathing` (~0.4).

---

## 🧠 USAGE GUIDELINES
- Combine **Mood Profiles** with **Genre Style Tables** for cross-domain control.  
- Translate `Interval Preferences` into **probabilistic MIDI generators** or **LFO-controlled quantizers**.  
- For cinematic/organic moods, increase **attack and release times** of envelopes.  
- For euphoric/textural moods, automate **filter cutoff and stereo width** dynamically.  

---

## 📘 CREDITS
This extended mood taxonomy is based on field analysis of post-techno and emotive electronica:
- **Weval** – “The Weight”, “Everything”  
- **Moderat** – “Rusty Nails”, “Eating Hooks”  
- **Rival Consoles** – “Articulation”, “Persona”  
- **Jon Hopkins**, **Max Cooper**, **Christian Löffler**, **Nils Frahm**  

---

## 🎹 CODE INTEGRATION

### Loading Profile

```python
def get_mood_profile(mood_name):
    """
    Get melody generation profile for mood
    """
    from reference_parser import ReferenceParser
    
    parser = ReferenceParser()
    profiles = parser.get_mood_profiles()
    
    return profiles.get(mood_name, profiles["happy"])
```

### Applying Profile

```python
def generate_melody_note(profile, current_pitch, scale):
    """
    Generate next note based on mood profile
    """
    # Choose interval
    if random.random() < profile["leap_probability"]:
        interval = random.choice(profile["preferred_intervals"])
    else:
        interval = random.choice([1, 2])  # Step
    
    # Apply direction
    if random.random() < profile["direction_bias"]:
        next_pitch = current_pitch + interval
    else:
        next_pitch = current_pitch - interval
    
    # Constrain to scale
    next_pitch = snap_to_scale(next_pitch, scale)
    
    # Check for rest
    if random.random() < profile["rest_probability"]:
        return None  # Rest
    
    return next_pitch
```

---

## 📈 ADVANCED TECHNIQUES

### Micro-timing (Humanization)

Add subtle timing variations:
```python
humanize = {
    "happy": 0.02,      # Slight ahead of beat
    "sad": 0.03,        # Slight behind beat
    "energetic": 0.01,  # Very tight
    "calm": 0.04,       # Relaxed timing
    "dark": 0.03,       # Dramatic timing
    "mysterious": 0.05  # Unpredictable timing
}
```

### Velocity Contours

Apply dynamic curves:
```python
velocity_curves = {
    "happy": "crescendo",      # Build energy
    "sad": "diminuendo",       # Fade away
    "energetic": "accent_1st", # Strong beats
    "calm": "even",            # Consistent
    "dark": "sudden_loud",     # Sforzando
    "mysterious": "random"     # Unpredictable
}
```

---

**Last Updated**: October 2024  
**Version**: 1.0  
**Part of**: Sound Design Skill - Reference Database
