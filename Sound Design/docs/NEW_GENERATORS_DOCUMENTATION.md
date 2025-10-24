# 🎵 NUOVI SCRIPT GENERATORI - DOCUMENTAZIONE

**Data creazione**: 24 Ottobre 2024  
**Script**: generate_harmony.py + generate_drum_pattern.py  
**Status**: ✅ COMPLETI E TESTATI

---

## 📋 OVERVIEW

Due nuovi script aggiunti al sistema Sound Design che utilizzano il reference database per generare contenuto musicale:

1. **generate_harmony.py** - Generatore di progressioni armoniche
2. **generate_drum_pattern.py** - Generatore di pattern ritmici

Entrambi sono **100% data-driven** e integrati con `reference_parser.py`.

---

## 🎹 SCRIPT 1: generate_harmony.py

### Descrizione

Genera progressioni di accordi (chord progressions) basate su:
- **Mood** (dark, happy, sad, etc.)
- **Genre** (techno, house, ambient, etc.)
- **Scale** (phrygian, lydian, etc.)
- **Root key** (C, Dm, F#, etc.)

### Features

✅ Carica progressioni da `chord-progressions.md`  
✅ Applica caratteristiche di genere (voicing, estensioni)  
✅ Genera MIDI file pronti per DAW  
✅ Supporta voicing wide/tight/medium  
✅ Aggiunge estensioni (7th, 9th, maj7)  
✅ Parametri personalizzabili

### Utilizzo

```bash
# Basic usage
python generate_harmony.py --mood dark --genre techno --key Dm

# Con parametri custom
python generate_harmony.py --mood happy --genre house --key C --scale lydian --bars 16

# Con BPM personalizzato
python generate_harmony.py --mood atmospheric --genre ambient --key F --bpm 90

# Con progressione custom
python generate_harmony.py --mood dark --genre techno --key Dm --progression "i-bVII-bVI-V"
```

### Parametri

| Parametro | Tipo | Default | Descrizione |
|-----------|------|---------|-------------|
| `--mood` | str | required | Mood emotivo |
| `--genre` | str | required | Genere musicale |
| `--key` | str | Am | Tonalità (C, Dm, F#, etc.) |
| `--scale` | str | auto | Scala (auto-detect da mood) |
| `--bars` | int | 8 | Numero di battute |
| `--bpm` | int | 120 | Tempo |
| `--output` | str | auto | Nome file output |
| `--progression` | str | auto | Progressione custom |

### Output Example

```
======================================================================
🎹 HARMONY GENERATOR
======================================================================

📊 PARAMETERS:
   Mood: dark
   Genre: techno
   Key: Dm
   Bars: 4
   BPM: 120
   Scale: Phrygian

🎼 PROGRESSION: i - bII - bVII - bVI
   Chords: i - bII - bVII - bVI
   Feel: Middle Eastern, exotic, ominous

🎛️  GENRE CHARACTERISTICS:
   Density: low
   Voicing: wide
   Extensions: 7
   Rhythm: sustained

🎵 Generating MIDI file...
✅ Generated: harmony_dark_techno_Dm.mid
```

### Genre Characteristics

Il script applica automaticamente caratteristiche specifiche per genere:

**Techno**:
- Density: Low (sparse chords)
- Voicing: Wide (spread across octaves)
- Extensions: 7th chords
- Rhythm: Sustained (long chords)

**House**:
- Density: Medium
- Voicing: Medium
- Extensions: 7th, 9th
- Rhythm: Syncopated

**Ambient**:
- Density: Low
- Voicing: Wide
- Extensions: 7th, 9th, maj7
- Rhythm: Very sustained

**Trance**:
- Density: High
- Voicing: Wide
- Extensions: 7th, 9th, maj7
- Rhythm: Sustained

**Dubstep**:
- Density: Low
- Voicing: Wide
- Extensions: None
- Rhythm: Sparse

### Moods Disponibili

- dark
- happy
- sad
- energetic
- calm
- atmospheric
- mysterious

### Genre Disponibili

- techno
- house
- trance
- dubstep
- ambient
- dnb (drum & bass)

### Integration con Reference Database

Lo script usa:
- `CHORD_PROGRESSIONS` da `chord-progressions.md`
- `SCALES` da `scales-modes.md`
- `GENRES` da `genre-styles.md`
- `MOOD_PROFILES` da `mood-profiles.md`

---

## 🥁 SCRIPT 2: generate_drum_pattern.py

### Descrizione

Genera pattern ritmici basati su:
- **Genre** (techno, house, dubstep, etc.)
- **Energy level** (low, medium, high)
- **Complexity** (low, medium, high)
- **Mood** (opzionale - converte in energy)

### Features

✅ Pattern specifici per genere  
✅ 6 generi supportati con pattern unici  
✅ Humanization (timing naturale)  
✅ Swing amount personalizzabile  
✅ Velocity variation automatica  
✅ Complessità adattiva  
✅ BPM range corretto per genere

### Utilizzo

```bash
# Basic usage
python generate_drum_pattern.py --genre house --energy high --bars 8

# Con mood (auto-converti in energy)
python generate_drum_pattern.py --genre techno --mood dark --complexity medium

# Con swing e humanization
python generate_drum_pattern.py --genre house --energy medium --swing 0.1 --humanize

# Con BPM custom
python generate_drum_pattern.py --genre dubstep --energy high --bpm 140 --bars 16

# Complessità alta per fills
python generate_drum_pattern.py --genre trap --complexity high --bars 8
```

### Parametri

| Parametro | Tipo | Default | Descrizione |
|-----------|------|---------|-------------|
| `--genre` | str | required | Genere musicale |
| `--mood` | str | None | Mood (override energy) |
| `--energy` | str | medium | low/medium/high |
| `--complexity` | str | medium | low/medium/high |
| `--bars` | int | 8 | Numero di battute |
| `--bpm` | int | auto | Tempo (auto da genere) |
| `--swing` | float | 0.0 | Swing 0.0-0.3 |
| `--humanize` | flag | False | Attiva humanization |
| `--output` | str | auto | Nome file output |

### Output Example

```
======================================================================
🥁 DRUM PATTERN GENERATOR
======================================================================

📊 PARAMETERS:
   Genre: House
   Energy: High
   Complexity: Medium
   Bars: 4
   BPM: 125
   Time Sig: 4/4

🎵 DRUM ELEMENTS:
   - Kick
   - Snare
   - Clap
   - Hat
   - Open Hat
   - Shaker

🎵 Generating drum pattern...
✅ Generated: drums_house_high_medium.mid
```

### Genre Patterns

Ogni genere ha pattern specifici per:

**Techno** (125-145 BPM):
- Kick: 4-on-the-floor
- Snare: 2 and 4
- Hi-hat: Eighth notes
- Open hat: Sparse
- Perc: Syncopated

**House** (120-130 BPM):
- Kick: 4-on-the-floor
- Snare: 2 and 4
- Clap: With snare
- Hi-hat: Straight 8ths
- Open hat: Offbeat
- Shaker: 16ths

**Dubstep** (138-142 BPM):
- Kick: Sparse, syncopated
- Snare: Half-time feel
- Rim: Syncopated
- Hi-hat: Skippy
- Perc: Complex

**Drum & Bass** (170-180 BPM):
- Kick: Syncopated
- Snare: Fast breaks
- Hi-hat: Fast, skippy
- Ride: Quarter notes
- Perc: 16th rolls

**Trap** (130-170 BPM):
- Kick: Syncopated
- Snare: 2 and 4
- Rim: 16th rolls
- Hi-hat: Constant 16ths
- Open hat: Triplet feel

**Ambient** (60-100 BPM):
- Kick: Very sparse
- Perc: Minimal
- Shaker: Gentle
- Rim: Very sparse

### Energy Levels

**Low Energy**:
- Velocity: 60-85
- Pattern: Semplificato (-30% hits)
- Feel: Laid-back, chill

**Medium Energy**:
- Velocity: 80-105
- Pattern: Standard
- Feel: Balanced

**High Energy**:
- Velocity: 95-120
- Pattern: Con fills (+30% hits)
- Feel: Driving, intense

### Complexity Levels

**Low**: Semplifica pattern (rimuove ~30% hits)  
**Medium**: Pattern standard  
**High**: Aggiunge ghost notes e fills

### Drum Mapping (GM Standard)

| Elemento | MIDI Note |
|----------|-----------|
| Kick | 36 |
| Snare | 38 |
| Clap | 39 |
| Rim | 37 |
| Closed Hat | 42 |
| Open Hat | 46 |
| Crash | 49 |
| Ride | 51 |
| Tom Low | 45 |
| Tom Mid | 47 |
| Tom High | 50 |
| Perc High | 56 |
| Perc Low | 54 |
| Shaker | 82 |

### Humanization

Quando attivato con `--humanize`:
- Timing offset: ±5 ticks random
- Velocity variation: ±10 random
- Più realistico e organico

### Swing

Valore 0.0-0.3:
- 0.0 = Straight (no swing)
- 0.1 = Slight swing (house/funk)
- 0.2 = Medium swing
- 0.3 = Heavy swing (heavy funk)

---

## 🔗 INTEGRATION CON REFERENCE DATABASE

### generate_harmony.py

**Usa da reference_parser.py**:
```python
SCALES = parser.get_scales()
CHORD_PROGRESSIONS = parser.get_chord_progressions()
GENRES = parser.get_genre_styles()
MOOD_PROFILES = parser.get_mood_profiles()
```

**Flusso**:
1. Mood → Progressione suggerita
2. Scale → Pattern di intervalli
3. Genre → Caratteristiche armoniche
4. Output → MIDI file

### generate_drum_pattern.py

**Usa da reference_parser.py**:
```python
GENRES = parser.get_genre_styles()
MOOD_PROFILES = parser.get_mood_profiles()
```

**Flusso**:
1. Genre → Pattern base
2. Energy → Velocity range
3. Complexity → Modifiche pattern
4. Output → MIDI file

---

## 📊 ESEMPI PRATICI

### Esempio 1: Dark Techno Track

```bash
# Genera armonia
python generate_harmony.py --mood dark --genre techno --key Dm --bars 16 --bpm 138

# Genera drums
python generate_drum_pattern.py --genre techno --energy high --complexity medium --bars 16 --bpm 138 --humanize
```

**Output**:
- `harmony_dark_techno_Dm.mid` (progressione i-bII-bVII-bVI)
- `drums_techno_high_medium.mid` (4-on-floor con hi-hats)

### Esempio 2: Happy House Track

```bash
# Genera armonia
python generate_harmony.py --mood happy --genre house --key C --bars 8 --bpm 125

# Genera drums
python generate_drum_pattern.py --genre house --mood happy --complexity high --bars 8 --bpm 125 --swing 0.08 --humanize
```

**Output**:
- `harmony_happy_house_C.mid` (progressione major uplifting)
- `drums_house_high_high.mid` (groovy con swing)

### Esempio 3: Atmospheric Ambient

```bash
# Genera armonia
python generate_harmony.py --mood atmospheric --genre ambient --key F --scale lydian --bars 32 --bpm 80

# Genera drums (minimal)
python generate_drum_pattern.py --genre ambient --energy low --complexity low --bars 32 --bpm 80
```

**Output**:
- `harmony_atmospheric_ambient_F.mid` (wide voicing, maj7)
- `drums_ambient_low_low.mid` (very sparse, minimal)

### Esempio 4: Aggressive Dubstep

```bash
# Genera armonia
python generate_harmony.py --mood dark --genre dubstep --key D --bars 8 --bpm 140

# Genera drums
python generate_drum_pattern.py --genre dubstep --energy high --complexity high --bars 8 --bpm 140
```

**Output**:
- `harmony_dark_dubstep_D.mid` (sparse, wide voicing)
- `drums_dubstep_high_high.mid` (half-time snare, complex)

---

## 🎛️ TIPS & TRICKS

### Per Harmony

1. **Voicing Wide** funziona meglio per pads atmosferici
2. **Extensions (7th, 9th)** aggiungono sofisticazione
3. **Scale Phrygian** ottima per dark/industrial
4. **Scale Lydian** ottima per atmospheric/uplifting
5. Usa progressioni **custom** per sperimentare

### Per Drums

1. **Humanization** sempre ON per suoni realistici
2. **Swing 0.08-0.12** ottimo per house/funk
3. **Complexity High** per fills e breaks
4. **Complexity Low** per intro/outro
5. **Energy progressiva**: low → medium → high

### Workflow Completo

```bash
# 1. Genera armonia
python generate_harmony.py --mood dark --genre techno --key Dm --bars 16

# 2. Genera drums
python generate_drum_pattern.py --genre techno --energy medium --bars 16 --humanize

# 3. Genera bassline (usa mood_to_composition.py)
python mood_to_composition.py dark Dm --midi

# 4. Importa tutto nella DAW
# 5. Assegna synth ai MIDI
# 6. Tweaka i suoni
# 7. Mix & master
```

---

## 🧪 TESTING

### Test harmony

```bash
cd /mnt/skills/user/sound-design/scripts

# Test vari mood
python generate_harmony.py --mood dark --genre techno --key Dm --bars 4
python generate_harmony.py --mood happy --genre house --key C --bars 4
python generate_harmony.py --mood atmospheric --genre ambient --key F --bars 4
```

### Test drums

```bash
# Test vari genre
python generate_drum_pattern.py --genre techno --energy high --bars 4
python generate_drum_pattern.py --genre house --energy medium --bars 4
python generate_drum_pattern.py --genre dubstep --energy high --bars 4

# Test con parametri
python generate_drum_pattern.py --genre house --energy high --swing 0.1 --humanize
```

---

## 📁 FILES LOCATION

### Nella Skill

```
/mnt/skills/user/sound-design/scripts/
├── generate_harmony.py (16KB) ⭐
├── generate_drum_pattern.py (17KB) ⭐
├── reference_parser.py (28KB)
├── mood_to_composition.py (11KB)
└── analyze_harmony.py (7KB)
```

### Output

```
/mnt/user-data/outputs/
├── generate_harmony.py ⭐
├── generate_drum_pattern.py ⭐
├── harmony_dark_techno_Dm.mid (example)
└── drums_house_high_medium.mid (example)
```

---

## ✅ CHECKLIST FEATURES

### generate_harmony.py

- [x] Carica progressioni da MD
- [x] Auto-select scale da mood
- [x] Genre characteristics (voicing, extensions)
- [x] Custom progressions
- [x] MIDI generation
- [x] Parametri personalizzabili
- [x] Help documentation
- [x] Error handling

### generate_drum_pattern.py

- [x] 6 genre patterns
- [x] Energy levels (3)
- [x] Complexity levels (3)
- [x] Humanization
- [x] Swing support
- [x] BPM auto from genre
- [x] 14 drum elements
- [x] MIDI generation
- [x] Help documentation
- [x] Mood → Energy mapping

---

## 🎉 SUMMARY

**Creati**: 2 nuovi script generatori  
**Dimensione**: 33KB totale  
**Features**: 20+ parametri configurabili  
**Integration**: 100% con reference database  
**Testing**: ✅ Tutti i test passati  
**Status**: 🚀 Production-ready

**Output files**: MIDI pronti per import in DAW

---

**Files disponibili per download**:

1. [generate_harmony.py](computer:///mnt/user-data/outputs/generate_harmony.py) (16KB)
2. [generate_drum_pattern.py](computer:///mnt/user-data/outputs/generate_drum_pattern.py) (17KB)
3. [harmony_dark_techno_Dm.mid](computer:///mnt/user-data/outputs/harmony_dark_techno_Dm.mid) (esempio)
4. [drums_house_high_medium.mid](computer:///mnt/user-data/outputs/drums_house_high_medium.mid) (esempio)

---

**🎵 ENJOY YOUR NEW MUSIC GENERATORS! 🎵**
