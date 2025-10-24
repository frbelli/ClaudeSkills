# GUIDA ALL'ESPANSIONE DELLA SKILL SOUND-DESIGN

Questa guida ti mostra come espandere la skill sound-design con nuove funzionalità, synth, teoria musicale e altro.

---

## 📁 STRUTTURA DELLA SKILL

```
/mnt/skills/user/sound-design/
├── SKILL.md                          # File principale (istruzioni per Claude)
├── references/                       # File di riferimento (database)
│   ├── synth-database.md            # Database dei synth esistenti
│   ├── synth-parameters.md          # Parametri comuni
│   ├── sound-archetypes.md          # Tipi di suoni
│   ├── genre-styles.md              # Stili musicali
│   ├── music-theory.md              # [NUOVO] Teoria musicale
│   ├── chord-progressions.md        # [NUOVO] Progressioni armoniche
│   ├── scales-modes.md              # [NUOVO] Scale e modi
│   └── composition-techniques.md    # [NUOVO] Tecniche compositive
└── scripts/                          # Script Python
    ├── generate_vital_preset.py
    ├── generate_rhythm.py
    ├── generate_signal_diagram.py
    ├── analyze_audio.py
    ├── mood_to_composition.py       # [NUOVO] Mood → composizione
    └── chord_progression_gen.py     # [NUOVO] Generatore progressioni
```

---

## 🎹 PARTE 1: AGGIUNGERE TEORIA MUSICALE E COMPOSIZIONE

### Step 1: Creare i file di riferimento

Creerò 4 nuovi file nella directory `references/`:
1. `music-theory.md` - Scale, intervalli, armonia
2. `chord-progressions.md` - Progressioni per mood/genere
3. `scales-modes.md` - Database scale e modi
4. `composition-techniques.md` - Tecniche compositive

### Step 2: Creare gli script

Creerò 2 nuovi script nella directory `scripts/`:
1. `mood_to_composition.py` - Mood → scala/key/progressione
2. `chord_progression_gen.py` - Generatore progressioni MIDI

### Step 3: Aggiornare SKILL.md

Aggiornerò il file principale per includere le nuove funzionalità.

---

## 🎛️ PARTE 2: AGGIUNGERE NUOVI SYNTH

### Opzione A: Synth Hardware

Per aggiungere un nuovo synth hardware (esempio: Arturia MicroFreak):

1. **Apri** `/mnt/skills/user/sound-design/references/synth-database.md`

2. **Aggiungi** una nuova sezione sotto `## Hardware Synths`:

```markdown
### Arturia MicroFreak
- **Type**: Digital hybrid paraphonic synthesizer
- **Oscillators**: Digital oscillator with multiple synthesis engines
- **Engines**: Basic Waves, Superwave, Harmo, KarplusStr, V.Analog, Waveshaping, 
  Two Op.FM, Granular, Wavetable, Harmonic OSC, SpeechSynth, Modal Resonator
- **Filter**: 12dB Multimode analog filter (LP/BP/HP)
- **Voices**: 4-voice paraphonic
- **Sequencer**: 64-step sequencer with 4 automation lanes
- **Keyboard**: Capacitive touch keyboard with poly aftertouch
- **Modulation**: Matrix with multiple sources (LFO, Envelopes, Keyboard, etc.)
- **Effects**: Chorus, delay, reverb
- **Patchbay**: Digital patch matrix (no physical cables)
- **Specialties**: Touch keyboard with pressure/timbre control, 
  multiple synthesis engines, very affordable
```

3. **Aggiungi** approccio sound design:

```markdown
### For hybrid digital synths (MicroFreak):
- Explore different oscillator engines per sound type
- Use matrix modulation for complex movement
- Leverage touch keyboard for expressive control
- Sequence modulation via automation lanes
```

### Opzione B: Synth Software

Per aggiungere un synth software (esempio: Omnisphere):

```markdown
### Spectrasonics Omnisphere 2
- **Type**: Hybrid synthesizer (sample + synthesis)
- **Sound Sources**: 14,000+ sounds, wavetables, granular
- **Layers**: 4 layers per patch (A+B in each part)
- **Synthesis**: Multi-timbral, wavetable, FM, sample-based
- **Filters**: Multiple analog-modeled filters
- **Effects**: 58 effect units with modulation
- **Arpeggiator**: Advanced with multiple modes
- **Modulation**: 8 LFOs, 12 envelopes, extensive mod matrix
- **File Format**: .prt_omn (Omnisphere format - proprietary)
- **Programming**: Via GUI, vast preset library
- **Specialties**: Massive sound library, deep synthesis, 
  hardware synth integration, Orb controller
```

---

## 🔧 PARTE 3: STRUTTURA DEI FILE DI RIFERIMENTO

### Template per `music-theory.md`:

```markdown
# Music Theory Reference

## Intervals
[Definizioni di intervalli, esempi MIDI]

## Scales
[Database scale con note MIDI]

## Chord Construction
[Come costruire accordi da scale]

## Harmonic Function
[Teoria delle funzioni armoniche: T, S, D]

## Voice Leading
[Regole per movimento delle voci]
```

### Template per `chord-progressions.md`:

```markdown
# Chord Progressions by Mood

## Happy/Uplifting
### Major Key Progressions
- I - V - vi - IV (C - G - Am - F)
- I - IV - V - IV (C - F - G - F)
[etc...]

## Sad/Melancholic
### Minor Key Progressions
- i - VI - III - VII (Am - F - C - G)
[etc...]

## Dark/Mysterious
### Minor/Phrygian Progressions
[etc...]

## Ambient/Ethereal
### Sus/Add Progressions
[etc...]
```

### Template per `composition-techniques.md`:

```markdown
# Composition Techniques

## Arrangement Structures
- Intro-Verse-Chorus-Bridge-Outro
- ABABCB
[etc...]

## Tension & Release
[Tecniche per creare tensione]

## Layering & Orchestration
[Come stratificare elementi]

## Rhythmic Variation
[Tecniche ritmiche]
```

---

## 🐍 PARTE 4: SCRIPT PER MOOD → COMPOSIZIONE

### Funzionalità `mood_to_composition.py`:

```python
# Input: mood keyword (es. "dark atmospheric")
# Output: 
#   - Scala suggerita (es. "D Phrygian")
#   - Root key
#   - 3 progressioni di accordi
#   - Suggerimenti per orchestrazione
#   - Opzionale: genera MIDI delle progressioni
```

### Come usarlo:

```bash
python scripts/mood_to_composition.py "dark atmospheric"

Output:
✅ MOOD: Dark Atmospheric
✅ SUGGESTED SCALE: D Phrygian (D-Eb-F-G-A-Bb-C)
✅ ROOT KEY: D minor
✅ CHORD PROGRESSIONS:
   1. Dm - Eb - F - Dm
   2. Dm - Bb - C - Dm  
   3. Dm - F - Eb - Bb - Dm
✅ MIDI files created: progression_1.mid, progression_2.mid, progression_3.mid
```

---

## 📝 PARTE 5: AGGIORNARE SKILL.md

Nel file principale `SKILL.md`, aggiungi nuove sezioni:

### Aggiungere sotto "Core Capabilities":

```markdown
6. **Music Theory & Composition** - Suggest scales, keys, and chord progressions based on mood
7. **Harmonic Analysis** - Analyze and generate chord progressions
```

### Aggiungere nuovo workflow:

```markdown
### Mood-Based Composition Workflow

When user wants composition suggestions based on mood:

1. **Identify Mood/Emotion**
   - Ask what feeling/atmosphere they want
   - Examples: dark, uplifting, melancholic, energetic, dreamy

2. **Read Music Theory References**
   ```
   view references/music-theory.md
   view references/chord-progressions.md
   view references/scales-modes.md
   ```

3. **Generate Suggestions**
   ```bash
   python scripts/mood_to_composition.py "dark atmospheric"
   ```

4. **Provide**:
   - Suggested scale/mode
   - Root key recommendation
   - 3+ chord progression variations
   - Orchestration suggestions
   - Optional: MIDI files
```

---

## 🎼 PARTE 6: ESEMPIO COMPLETO - WORKFLOW UTENTE

### Scenario: Utente chiede "Voglio creare un brano dark ambient"

**Claude legge:**
1. `references/music-theory.md` → comprende teoria base
2. `references/chord-progressions.md` → trova progressioni dark
3. `references/scales-modes.md` → identifica scale adatte
4. `references/composition-techniques.md` → suggerisce tecniche

**Claude esegue:**
```bash
python scripts/mood_to_composition.py "dark ambient"
```

**Claude risponde con:**
```
🎹 COMPOSIZIONE PER: Dark Ambient

SCALA SUGGERITA: C# Locrian
ROOT KEY: C# (Do diesis)

CHORD PROGRESSIONS:

Progressione 1 - "Deep Void":
C#dim - D - Emaj7 - F#m
[Atmosfera instabile, misterioso]

Progressione 2 - "Descending Darkness":  
C#dim - Bmaj7 - Amaj7 - G#m7
[Movimento discendente, malinconico]

Progressione 3 - "Suspended Tension":
C#sus2 - Dsus4 - Esus2 - F#sus4
[Sospeso, ambiguo, molto ambient]

ORCHESTRATION TIPS:
- Pad layer: Use Matriarch patch "Ethereal Drift" in C# Locrian
- Bass: Sub-bass drone on C# (root)
- Texture: Granular processing on sustained notes
- Rhythm: Minimal, sparse percussion (se necessario)

MIDI files creati per testare le progressioni!
```

---

## 🔍 PARTE 7: ESTENDERE ULTERIORMENTE

### Altre funzionalità future:

1. **Melody Generator**
   - `scripts/generate_melody.py`
   - Input: scala, mood
   - Output: linee melodiche MIDI

2. **Arrangement Suggester**
   - `scripts/suggest_arrangement.py`
   - Input: genere, lunghezza
   - Output: struttura dettagliata (intro, verse, drop, etc.)

3. **Sound Palette Builder**
   - `scripts/build_sound_palette.py`
   - Input: mood, genere
   - Output: lista di synth patches + drum samples consigliati

4. **Audio Analysis con AI**
   - Migliorare `analyze_audio.py`
   - Identificare key, scale, chord progression da audio

5. **Integration con DAW**
   - Script per esportare in formati DAW-specifici
   - Ableton Live Sets, Logic Pro projects, etc.

---

## 📋 CHECKLIST PER AGGIUNGERE FUNZIONALITÀ

Quando vuoi aggiungere una nuova feature:

- [ ] Identifica che tipo di funzionalità (teoria, synth, processing, etc.)
- [ ] Crea/aggiorna file di riferimento appropriato in `references/`
- [ ] Se serve codice, crea script in `scripts/`
- [ ] Aggiorna `SKILL.md` con nuovo workflow
- [ ] Testa la funzionalità
- [ ] Documenta con esempi

---

## 🚀 PROSSIMI PASSI

Vuoi che crei ora:

1. ✅ **I 4 nuovi file di teoria musicale** (music-theory.md, chord-progressions.md, etc.)
2. ✅ **Lo script mood_to_composition.py**
3. ✅ **L'aggiornamento di SKILL.md**

Oppure vuoi concentrarti prima su:
- Aggiungere synth specifici?
- Creare altre funzionalità?
- Migliorare script esistenti?

Dimmi cosa preferisci e procediamo! 🎛️✨
