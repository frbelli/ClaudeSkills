# 📑 SOUND DESIGN SKILL - FILE MANIFEST

Indice completo di tutti i file della skill con descrizioni e utilizzo.

**Versione**: 2.0  
**Ultimo aggiornamento**: Ottobre 2024  
**File totali**: 30+

---

## 📂 ROOT DIRECTORY

### File Principali

| File | Dimensione | Descrizione | Uso |
|------|-----------|-------------|-----|
| **SKILL.md** | ~15KB | File principale con istruzioni per Claude | Core skill - non modificare |
| **README.md** | ~20KB | Documentazione principale | Leggi per panoramica completa |
| **Sound_Design_Skill_Guida.md** | ~12KB | Guida completa in italiano | Tutorial e best practices |
| **Esempi_Pratici.md** | ~8KB | Tutorial step-by-step | Segui per imparare workflow |
| **sound-design.skill** | ~1KB | File configurazione skill | Metadata skill |
| **.skillrc** | ~2KB | Configurazione avanzata | Settings e paths |

---

## 📖 docs/ - DOCUMENTAZIONE (6 file)

### Guide Complete

| File | Dimensione | Contenuto | Quando Usarlo |
|------|-----------|-----------|---------------|
| **MASTER_SUMMARY.md** | 12KB | Panoramica completa di tutto | Primo file da leggere |
| **quick_start_guide.md** | 9KB | 3 passi per iniziare + esempi | Per iniziare subito |
| **integration_instructions.md** | 12KB | Come integrare nuovi file | Quando aggiungi features |
| **skill_expansion_guide.md** | 10KB | Come espandere la skill | Per aggiungere synth/tool |
| **analyze_harmony_documentation.md** | 14KB | Doc analisi armonica completa | Quando usi analyze_harmony.py |
| **HARMONIC_ANALYSIS_UPDATE.md** | 11KB | Aggiornamenti tool analisi | Info sul nuovo tool |

**Totale docs/**: ~68KB, 6 file

---

## 📚 references/ - DATABASE TEORICI (6 file)

### Database Musicali

| File | Dimensione | Contenuto | Records |
|------|-----------|-----------|---------|
| **music-theory.md** | 11KB | Intervalli, scale, accordi, armonia | ~50 concetti |
| **chord-progressions.md** | 9.5KB | Progressioni per mood/genere | 50+ progressioni |
| **scales-modes.md** | 10KB | Scale con caratteristiche MIDI | 14+ scale |
| **synth-database.md** | 8.5KB | Specifiche synth HW/SW | 11 synth |
| **sound-archetypes.md** | 6KB | Tipi di suoni (bass, pad, lead) | 20+ archetipi |
| **genre-styles.md** | 7KB | Stili musicali specifici | 15+ generi |

**Totale references/**: ~52KB, 6 file

### Dettaglio Contenuti

#### music-theory.md
- ✅ Tutti gli intervalli (12) con caratteristiche
- ✅ 7 modi del maggiore completi
- ✅ Scale minori (natural, harmonic, melodic)
- ✅ Costruzione accordi (triadi, 7th, extended)
- ✅ Funzioni armoniche (T-S-D)
- ✅ Voice leading rules
- ✅ Database MIDI per tutte le scale
- ✅ Transposizione e modulazione

#### chord-progressions.md
- ✅ Progressioni per 8 mood principali
- ✅ Progressioni per genere (house, techno, trance, etc.)
- ✅ Esempi MIDI per ogni progressione
- ✅ Tecniche di variazione
- ✅ Modal interchange
- ✅ Suggerimenti rhythm e voicing

#### scales-modes.md
- ✅ 7 modi del maggiore dettagliati
- ✅ 3 scale minori
- ✅ Pentatoniche (2 tipi)
- ✅ Blues scale
- ✅ Whole tone
- ✅ Diminished scales
- ✅ Scale esotiche (Phrygian Dominant, Hungarian, Japanese)
- ✅ Tabelle MIDI per tutte le chiavi
- ✅ Caratteristiche e uso per ogni scala

#### synth-database.md
- ✅ 6 synth hardware completi
- ✅ 5 synth software completi
- ✅ Specifiche tecniche dettagliate
- ✅ Specialità e sound design approach
- ✅ Formati preset/patch

#### sound-archetypes.md
- ✅ Bass sounds (Sub, Reese, Acid)
- ✅ Lead sounds (Synth lead, Pluck, Supersaw)
- ✅ Pad sounds (Ambient, String, Drone)
- ✅ Keys & Mallets (EP, Bells, Marimba)
- ✅ Texture & Experimental
- ✅ Percussion (Kick, Snare, Hi-Hat)
- ✅ Parametri specifici per ogni tipo

#### genre-styles.md
- ✅ Techno (minimal, peak time, acid)
- ✅ House (deep, tech, progressive)
- ✅ Trance (uplifting, psytrance)
- ✅ IDM (Aphex Twin, Autechre style)
- ✅ Ambient (Brian Eno style)
- ✅ Dubstep/Bass Music
- ✅ Drum & Bass (liquid, neurofunk)
- ✅ E altri 8+ generi
- ✅ BPM ranges, caratteristiche, tecniche

---

## 🐍 scripts/ - TOOL PYTHON (3 file)

### Script Eseguibili

| Script | Dimensione | Funzione | Input | Output |
|--------|-----------|----------|-------|--------|
| **mood_to_composition.py** | 16KB | Genera composizione da mood | Mood, root key | Scala, 3 progressioni, MIDI files |
| **analyze_harmony.py** | 19KB | Analizza MIDI per armonia | MIDI file | Key, scale, chords, suggestions |
| **generate_melody.py** | 12KB | Genera melodie | Scala, mood, BPM | Melodia MIDI |

**Totale scripts/**: ~47KB, 3 file

### Dettaglio Script

#### mood_to_composition.py
**Linee di codice**: ~600  
**Dipendenze**: mido  
**Mood supportati**: 8 (dark, atmospheric, happy, sad, energetic, epic, dreamy, mysterious)

**Funzionalità**:
- ✅ Database interno di 8 mood
- ✅ Mapping mood → scale
- ✅ Generazione 3 progressioni per mood
- ✅ Export MIDI automatico
- ✅ Production tips specifici per mood
- ✅ CLI interface completa

**Esempio uso**:
```bash
python mood_to_composition.py "dark atmospheric" D
```

#### analyze_harmony.py
**Linee di codice**: ~700  
**Dipendenze**: mido  
**Algoritmo**: Krumhansl-Schmuckler key-finding

**Funzionalità**:
- ✅ Key detection (24 tonalità)
- ✅ Confidence scoring
- ✅ Scale matching (14+ scale)
- ✅ Chord detection (15+ tipi)
- ✅ Roman numeral analysis
- ✅ Pitch class distribution con grafico
- ✅ Suggerimenti musicali
- ✅ Parametri customizzabili

**Esempio uso**:
```bash
python analyze_harmony.py song.mid 4 4
```

#### generate_melody.py
**Linee di codice**: ~500  
**Dipendenze**: mido  

**Funzionalità**:
- ✅ Generazione melodie in qualsiasi scala
- ✅ Adattamento al mood
- ✅ Rhythm patterns variabili
- ✅ Range note customizzabile
- ✅ Export MIDI

**Esempio uso**:
```bash
python generate_melody.py D minor sad 120
```

---

## 🎼 examples/ - FILE DI ESEMPIO (13+ file)

### MIDI Files

| File | Tipo | Descrizione |
|------|------|-------------|
| **progression_1_dark_C.mid** | Progressione | Dark progression in C |
| **progression_2_dark_C.mid** | Progressione | Variante dark in C |
| **progression_3_dark_C.mid** | Progressione | Terza variante dark |
| **progression_1_happy_G.mid** | Progressione | Happy progression in G |
| **progression_2_happy_G.mid** | Progressione | Variante happy in G |
| **progression_3_happy_G.mid** | Progressione | Terza variante happy |
| **melody_D_D_Minor_sad_120bpm.mid** | Melodia | Melodia triste in D minor |
| **melody_E_E_Phrygian_dark_120bpm.mid** | Melodia | Melodia dark in E Phrygian |
| **pattern_techno_techno_128bpm.mid** | Pattern | Pattern drum techno |

**Totale MIDI**: 9 file

### Preset & Diagrammi

| File | Tipo | Descrizione |
|------|------|-------------|
| **Dark_Techno_Bass.vital** | Preset Vital | Bass patch techno dark |
| **esempio_bass_techno.json** | Spec JSON | Specifica bass per generazione |
| **esempio_signal_flow.json** | Spec JSON | Specifica per diagram generator |
| **esempio_signal_flow_diagram.svg** | Diagram SVG | Signal flow visualizzato |

**Totale altri**: 4 file

---

## 📊 STATISTICHE COMPLETE

### Per Categoria

| Categoria | File | Dimensione | Linee |
|-----------|------|-----------|-------|
| **Root** | 6 | ~58KB | ~3,000 |
| **docs/** | 6 | ~68KB | ~3,500 |
| **references/** | 6 | ~52KB | ~2,800 |
| **scripts/** | 3 | ~47KB | ~1,800 |
| **examples/** | 13+ | ~10KB | - |
| **TOTALE** | **34+** | **~235KB** | **~11,100** |

### Per Tipo

| Tipo | Quantità | Dimensione |
|------|----------|-----------|
| Markdown (.md) | 18 | ~190KB |
| Python (.py) | 3 | ~47KB |
| MIDI (.mid) | 9 | ~5KB |
| JSON (.json) | 2 | ~2KB |
| SVG (.svg) | 1 | ~5KB |
| Vital (.vital) | 1 | ~3KB |
| Config | 2 | ~3KB |

### Contenuti

| Tipo Contenuto | Quantità |
|----------------|----------|
| Synth supportati | 11 |
| Scale nel database | 14+ |
| Progressioni | 50+ |
| Tipi di accordi | 15+ |
| Mood mappati | 8 |
| Generi documentati | 15+ |
| Sound archetypes | 20+ |
| Guide complete | 6 |
| Script funzionanti | 3 |
| File esempio | 13+ |

---

## 🔄 WORKFLOW FILES

### Workflow 1: Composizione da Mood

**File coinvolti**:
1. `references/chord-progressions.md` (mood database)
2. `references/scales-modes.md` (scale selection)
3. `scripts/mood_to_composition.py` (generation)
4. `examples/progression_*.mid` (output)

### Workflow 2: Sound Design

**File coinvolti**:
1. `references/synth-database.md` (synth specs)
2. `references/sound-archetypes.md` (sound types)
3. `references/music-theory.md` (scale notes)
4. `examples/*.json` (patch specs)

### Workflow 3: Analisi & Replica

**File coinvolti**:
1. `scripts/analyze_harmony.py` (analysis)
2. `references/music-theory.md` (theory)
3. `scripts/mood_to_composition.py` (generation)
4. `examples/*.mid` (test files)

---

## 📋 CHECKLIST FILE ESSENZIALI

### File Obbligatori (Core)

- [x] `SKILL.md` - Istruzioni core per Claude
- [x] `README.md` - Documentazione principale
- [x] `references/music-theory.md` - Teoria base
- [x] `references/chord-progressions.md` - Progressioni
- [x] `references/synth-database.md` - Synth specs
- [x] `scripts/mood_to_composition.py` - Tool principale

### File Raccomandati (Extended)

- [x] `docs/quick_start_guide.md` - Quick start
- [x] `docs/MASTER_SUMMARY.md` - Overview
- [x] `references/scales-modes.md` - Scale database
- [x] `scripts/analyze_harmony.py` - Analisi
- [x] `examples/*.mid` - Esempi pratici

### File Opzionali (Advanced)

- [x] `docs/skill_expansion_guide.md` - Espansione
- [x] `docs/integration_instructions.md` - Integrazione
- [x] `scripts/generate_melody.py` - Melodie
- [x] `examples/*.vital` - Preset
- [x] `.skillrc` - Config avanzata

---

## 🗂️ FILE PER FUNZIONALITÀ

### Per Sound Design
- `references/synth-database.md`
- `references/sound-archetypes.md`
- `examples/Dark_Techno_Bass.vital`
- `examples/esempio_signal_flow_diagram.svg`

### Per Teoria Musicale
- `references/music-theory.md`
- `references/scales-modes.md`
- `references/chord-progressions.md`

### Per Composizione
- `scripts/mood_to_composition.py`
- `scripts/generate_melody.py`
- `examples/progression_*.mid`
- `examples/melody_*.mid`

### Per Analisi
- `scripts/analyze_harmony.py`
- `docs/analyze_harmony_documentation.md`
- `references/music-theory.md`

### Per Learning
- `docs/quick_start_guide.md`
- `docs/MASTER_SUMMARY.md`
- `Esempi_Pratici.md`
- `Sound_Design_Skill_Guida.md`

---

## 🔍 COME TROVARE FILE

### Per Funzionalità

**Voglio creare una composizione**:
```
→ docs/quick_start_guide.md (inizia qui)
→ references/chord-progressions.md (progressioni)
→ scripts/mood_to_composition.py (tool)
```

**Voglio programmare un synth**:
```
→ references/synth-database.md (specifiche synth)
→ references/sound-archetypes.md (tipo di suono)
→ examples/Dark_Techno_Bass.vital (esempio)
```

**Voglio analizzare un MIDI**:
```
→ scripts/analyze_harmony.py (tool)
→ docs/analyze_harmony_documentation.md (guida)
→ references/music-theory.md (teoria)
```

**Voglio imparare**:
```
→ README.md (overview)
→ docs/quick_start_guide.md (quick start)
→ Esempi_Pratici.md (tutorial)
→ Sound_Design_Skill_Guida.md (guida completa)
```

---

## 📝 FILE DA LEGGERE PER RUOLO

### Se sei un Produttore
1. README.md
2. quick_start_guide.md
3. synth-database.md
4. chord-progressions.md
5. Esempi_Pratici.md

### Se sei uno Studente di Teoria
1. music-theory.md
2. scales-modes.md
3. chord-progressions.md
4. analyze_harmony_documentation.md

### Se sei uno Sviluppatore
1. SKILL.md
2. skill_expansion_guide.md
3. integration_instructions.md
4. scripts/*.py (codice sorgente)

### Se vuoi Espandere la Skill
1. skill_expansion_guide.md
2. integration_instructions.md
3. SKILL.md
4. .skillrc

---

## 🎯 PRIORITÀ DI LETTURA

### Must Read (Essenziali)
1. ⭐⭐⭐ README.md
2. ⭐⭐⭐ quick_start_guide.md
3. ⭐⭐⭐ music-theory.md

### Should Read (Raccomandati)
4. ⭐⭐ MASTER_SUMMARY.md
5. ⭐⭐ chord-progressions.md
6. ⭐⭐ synth-database.md

### Nice to Read (Utili)
7. ⭐ Esempi_Pratici.md
8. ⭐ Sound_Design_Skill_Guida.md
9. ⭐ analyze_harmony_documentation.md

---

## ✅ VERIFICA INSTALLAZIONE

### Checklist File Presenti

```bash
# Verifica struttura base
ls -la /mnt/skills/user/sound-design/

# Verifica references
ls -la /mnt/skills/user/sound-design/references/

# Verifica scripts
ls -la /mnt/skills/user/sound-design/scripts/

# Verifica docs
ls -la /mnt/skills/user/sound-design/docs/

# Verifica examples
ls -la /mnt/skills/user/sound-design/examples/
```

### Test Funzionalità

```bash
# Test script principale
cd /mnt/skills/user/sound-design/scripts/
python mood_to_composition.py

# Se vedi help message → ✅ Tutto OK!
```

---

**FILE MANIFEST** | Sound Design Skill v2.0  
Totale: 34+ file, ~235KB, ~11,100 linee  
Ultimo aggiornamento: Ottobre 2024
