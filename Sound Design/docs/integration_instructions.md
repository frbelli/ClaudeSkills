# 🎹 COME INTEGRARE LE NUOVE FUNZIONALITÀ NELLA SKILL

Questa guida ti mostra **esattamente** come aggiungere teoria musicale e composizione alla tua skill sound-design.

---

## 📦 FILE CHE HO CREATO PER TE

### 1. File di Riferimento (da copiare in `/mnt/skills/user/sound-design/references/`)

✅ **music-theory.md**
- Intervalli, scale, modi
- Costruzione accordi
- Funzioni armoniche
- Voice leading
- Database completo di scale MIDI

✅ **chord-progressions.md**
- Progressioni organizzate per mood
- Progressioni per genere musicale
- Esempi MIDI
- Tecniche di variazione

### 2. Script (da copiare in `/mnt/skills/user/sound-design/scripts/`)

✅ **mood_to_composition.py**
- Genera suggerimenti di composizione da mood
- Output: scala, key, 3 progressioni
- Crea file MIDI delle progressioni

### 3. Documentazione

✅ **skill_expansion_guide.md**
- Guida completa all'espansione
- Come aggiungere synth
- Come aggiungere nuove features
- Best practices

---

## 🚀 PASSI PER L'INTEGRAZIONE

### PASSO 1: Copia i File di Riferimento

Apri il terminale e esegui:

```bash
# Copia music-theory.md
cp /mnt/user-data/outputs/music-theory.md /mnt/skills/user/sound-design/references/

# Copia chord-progressions.md  
cp /mnt/user-data/outputs/chord-progressions.md /mnt/skills/user/sound-design/references/
```

### PASSO 2: Copia lo Script

```bash
# Copia mood_to_composition.py
cp /mnt/user-data/outputs/mood_to_composition.py /mnt/skills/user/sound-design/scripts/

# Rendi eseguibile
chmod +x /mnt/skills/user/sound-design/scripts/mood_to_composition.py
```

### PASSO 3: Aggiorna SKILL.md

Apri `/mnt/skills/user/sound-design/SKILL.md` e aggiungi queste sezioni:

#### A) Sotto "Core Capabilities" (linea ~10), aggiungi:

```markdown
6. **Music Theory & Composition** - Suggest scales, keys, and chord progressions based on mood
7. **Harmonic Analysis** - Analyze and generate chord progressions with MIDI output
```

#### B) Dopo "Step 6: Step-by-Step Programming Guide" (linea ~300), aggiungi:

```markdown
## Music Theory & Composition Workflow

### When User Wants Composition from Mood

When user requests musical suggestions based on mood/atmosphere:

**Step 1: Identify Mood**
Ask what emotional/atmospheric quality they want:
- Dark, mysterious, ominous
- Happy, uplifting, bright
- Sad, melancholic, emotional
- Energetic, aggressive, driving
- Dreamy, nostalgic, floating
- Epic, cinematic, heroic
- Atmospheric, ambient, ethereal

**Step 2: Read Music Theory References**
```
view references/music-theory.md
view references/chord-progressions.md
```

**Step 3: Generate Composition Suggestions**
```bash
python scripts/mood_to_composition.py "dark atmospheric" D
```

This will output:
- Suggested scale/mode
- Root key recommendation  
- 3 chord progression variations with MIDI
- Production/orchestration tips

**Step 4: Provide to User**
Give complete breakdown:
- Scale with note names and MIDI values
- Each progression with Roman numerals and actual chords
- Musical feeling/character of each progression
- Production tips for achieving the mood
- MIDI files for testing

### Integration with Synth Programming

Combine composition with synth programming:

**Example Workflow**:
1. User: "I want a dark ambient track"
2. Generate composition suggestions (scale, progressions)
3. Suggest synth patches (e.g., Matriarch pad in D Phrygian)
4. Provide rhythm pattern (minimal, sparse)
5. Offer arrangement structure

**Code Example**:
```bash
# Generate composition
python scripts/mood_to_composition.py "dark ambient" D

# Generate rhythm (sparse)
python scripts/generate_rhythm.py ambient 90 8

# Suggest using existing pad patch
# "Use the Matriarch Ethereal Drift pad, tuned to D Phrygian"
```
```

#### C) Alla fine del file (dopo "Remember" section), aggiungi:

```markdown
## Music Theory Reference Quick Access

When suggesting compositions:
- Consult `references/music-theory.md` for scale theory, intervals, chord construction
- Consult `references/chord-progressions.md` for mood-specific progressions
- Use `scripts/mood_to_composition.py` to generate complete suggestions with MIDI
- Combine music theory with synth programming for complete production workflows
```

---

## 🧪 TESTA LE NUOVE FUNZIONALITÀ

### Test 1: Generazione Composizione Base

```bash
cd /mnt/skills/user/sound-design/scripts
python mood_to_composition.py dark
```

**Output atteso**: 
- Scala Phrygian/Locrian
- 3 progressioni dark
- MIDI files generati

### Test 2: Con Root Key Personalizzata

```bash
python mood_to_composition.py happy G
```

**Output atteso**:
- Scala Major/Lydian in G
- Progressioni uplifting
- MIDI in tonalità di G

### Test 3: Mood Combinati

```bash
python mood_to_composition.py "dark atmospheric"
```

**Output atteso**:
- Match migliore tra i mood
- Suggerimenti appropriati

---

## 💡 COME USARE LE NUOVE FUNZIONALITÀ

### Scenario 1: Utente Chiede Aiuto per Composizione

**User**: "Vorrei creare un brano dark ambient, da dove inizio?"

**Claude fa**:
1. Legge `references/music-theory.md`
2. Legge `references/chord-progressions.md`
3. Esegue `python scripts/mood_to_composition.py "dark ambient" C#`
4. Risponde con:
   - Scala suggerita (es. C# Locrian)
   - 3 progressioni con MIDI
   - Tips per orchestration
   - Link ai file MIDI generati

### Scenario 2: Utente Vuole Espandere un'Idea

**User**: "Ho questo riff in Em, che progressione posso usare per un feel epico?"

**Claude fa**:
1. Legge `references/chord-progressions.md`
2. Cerca progressioni "epic" in minor key
3. Suggerisce 3 varianti appropriate
4. Opzionalmente genera MIDI per test

### Scenario 3: Workflow Completo

**User**: "Voglio creare un track energetic techno"

**Claude fa**:
1. **Composizione**: Mood → progressioni (Mixolydian, energetic chords)
2. **Synth**: Suggerisce bass patch + lead
3. **Ritmo**: Genera pattern techno 128 BPM
4. **Arrangiamento**: Suggerisce struttura intro-build-drop

---

## 🎛️ AGGIUNGERE ALTRI MOOD

Per aggiungere un nuovo mood (esempio: "nostalgic"):

### 1. Apri `scripts/mood_to_composition.py`

### 2. Aggiungi entry in MOOD_DATABASE:

```python
"nostalgic": {
    "scales": ["Major", "Dorian", "Mixolydian"],
    "root_keys": ["C", "F", "G", "D"],
    "chord_progressions": [
        {
            "name": "Vintage Warmth",
            "chords": ["I", "vi", "IV", "V"],
            "feel": "50s/60s, warm, familiar"
        },
        {
            "name": "Bittersweet Memory",
            "chords": ["IVmaj7", "IIIm7", "VIm7", "IIm7"],
            "feel": "Jazzy, sophisticated, reflective"
        },
        {
            "name": "Golden Hour",
            "chords": ["vi", "IVmaj7", "I", "V"],
            "feel": "Sunset vibes, peaceful"
        }
    ],
    "tips": [
        "Use analog-style synths with slight detuning",
        "Add vinyl crackle or tape saturation",
        "Medium tempo (95-110 BPM)",
        "Warm reverb and tape delay"
    ]
},
```

### 3. Salva e testa:

```bash
python mood_to_composition.py nostalgic
```

---

## 🔧 AGGIUNGERE NUOVI SYNTH

### Esempio: Aggiungere Korg Minilogue XD

### 1. Apri `references/synth-database.md`

### 2. Aggiungi sotto `## Hardware Synths`:

```markdown
### Korg Minilogue XD
- **Type**: Four-voice polyphonic analog synthesizer with digital multi-engine
- **Oscillators**: 2 analog VCOs + 1 digital multi-engine
- **Multi-Engine**: 16 user slots for digital oscillators (FM, wavetable, noise)
- **Filter**: 2-pole analog filter (LP/HP), analog drive
- **Voices**: 4-voice polyphonic
- **Effects**: Modulation, delay, reverb (32 effect types)
- **Sequencer**: 16-step sequencer with motion sequencing
- **Keyboard**: 37 slim keys
- **Modulation**: 2 EGs, 1 LFO
- **Specialties**: Hybrid analog/digital, motion sequencing, 
  oscilloscope display, very hands-on interface
```

### 3. Aggiorna la lista in SKILL.md sotto "Available synths":

```markdown
- Korg Minilogue XD (Hybrid analog/digital)
```

---

## 📊 FILE STRUCTURE FINALE

Dopo l'integrazione, la struttura sarà:

```
/mnt/skills/user/sound-design/
├── SKILL.md ✅ (aggiornato)
├── references/
│   ├── synth-database.md
│   ├── synth-parameters.md
│   ├── sound-archetypes.md
│   ├── genre-styles.md
│   ├── music-theory.md ✅ (nuovo)
│   └── chord-progressions.md ✅ (nuovo)
└── scripts/
    ├── generate_vital_preset.py
    ├── generate_rhythm.py
    ├── generate_signal_diagram.py
    ├── analyze_audio.py
    └── mood_to_composition.py ✅ (nuovo)
```

---

## ✅ CHECKLIST FINALE

Prima di considerare l'integrazione completa:

- [ ] Copiati file di riferimento in `/references/`
- [ ] Copiato script in `/scripts/`
- [ ] Aggiornato SKILL.md con nuove sezioni
- [ ] Testato `mood_to_composition.py` con vari mood
- [ ] Verificato che MIDI files vengano generati
- [ ] Aggiunto almeno un nuovo synth a `synth-database.md` (opzionale)

---

## 🎯 FUNZIONALITÀ FUTURE DA AGGIUNGERE

Ora che hai teoria musicale, puoi espandere con:

### 1. Melody Generator
```python
# scripts/generate_melody.py
# Input: scale, rhythm pattern, range
# Output: MIDI melody that fits scale
```

### 2. Bass Line Generator  
```python
# scripts/generate_bassline.py
# Input: chord progression, genre, groove
# Output: Bass MIDI that follows chords
```

### 3. Arrangement Suggester
```python
# scripts/suggest_arrangement.py
# Input: genre, track length, energy curve
# Output: Detailed arrangement structure (intro, verse, build, drop, etc.)
```

### 4. Harmonic Analysis
```python
# scripts/analyze_harmony.py
# Input: MIDI file
# Output: Detected key, scale, chord progression, suggestions
```

### 5. Scale Matcher
```python
# scripts/match_scale.py
# Input: List of MIDI notes
# Output: Best matching scale/mode
```

---

## 🎵 ESEMPI DI USO REALE

### Esempio Completo 1: Creare un Dark Techno Track

```bash
# 1. Genera composizione
python scripts/mood_to_composition.py "dark energetic" D

# 2. Genera ritmo
python scripts/generate_rhythm.py techno 130 16

# 3. Claude suggerisce:
#    - Matriarch bass in D Phrygian
#    - Digitone FM stabs per percussive elements
#    - Vital pad per atmosphere
```

### Esempio Completo 2: Ambient Soundscape

```bash
# 1. Composizione
python scripts/mood_to_composition.py atmospheric C

# 2. Claude suggerisce:
#    - Matriarch Ethereal Drift pad in C Lydian
#    - Layered con Vital wavetable pad
#    - Minimal to no drums
#    - Field recordings as texture
```

---

## 🎓 RISORSE AGGIUNTIVE

### Per Approfondire Teoria Musicale:
- `music-theory.md` → Sezione "Voice Leading"
- `music-theory.md` → Sezione "Tension & Release"
- `chord-progressions.md` → Sezione "Variation Techniques"

### Per Sound Design:
- `sound-archetypes.md` → Tipi di suoni esistenti
- `synth-parameters.md` → Parametri comuni
- `genre-styles.md` → Stili musicali specifici

---

## 🎉 COMPLIMENTI!

Hai appena espanso la tua skill con:
✅ Teoria musicale completa
✅ Database di progressioni per mood
✅ Generatore automatico mood → composizione
✅ Output MIDI per testing immediato

**La skill ora può:**
- Suggerire scale basate su mood
- Generare progressioni di accordi
- Creare MIDI per testare idee
- Combinare teoria con sound design
- Offrire workflow completi di produzione

---

**Prossimo step**: Testa creando un brano completo usando tutte le funzionalità insieme! 🎛️✨

**Domande?** Usa `skill_expansion_guide.md` per riferimenti dettagliati.
