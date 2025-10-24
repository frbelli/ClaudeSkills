# 🎛️ Sound Design & Music Production Skill

**Versione**: 2.0  
**Ultima modifica**: Ottobre 2024  
**Linguaggio**: Python 3.12+

Una skill completa per sound design, teoria musicale, composizione e produzione musicale, integrata con Claude AI.

---

## 📋 Indice

1. [Panoramica](#panoramica)
2. [Struttura della Skill](#struttura-della-skill)
3. [Funzionalità Principali](#funzionalità-principali)
4. [Quick Start](#quick-start)
5. [Strumenti Disponibili](#strumenti-disponibili)
6. [Documentazione](#documentazione)
7. [Esempi Pratici](#esempi-pratici)
8. [Workflow Integrati](#workflow-integrati)
9. [Synth Supportati](#synth-supportati)
10. [Requisiti](#requisiti)
11. [Installazione](#installazione)
12. [Contribuire](#contribuire)

---

## 🎯 Panoramica

Questa skill trasforma Claude in un assistente completo per la produzione musicale, coprendo:

- **Sound Design**: Programmazione synth (Matriarch, Digitone, Vital, Serum, etc.)
- **Teoria Musicale**: Scale, accordi, armonia, voice leading
- **Composizione**: Generazione automatica da mood/genere
- **Analisi Armonica**: Rilevamento key, scale, progressioni da MIDI
- **Rhythm Programming**: Generazione pattern drum per ogni genere
- **Visualizzazioni**: Diagrammi signal flow, notazioni

### 🌟 Novità Versione 2.0

- ✅ **Analisi Armonica**: Tool completo per analizzare MIDI files
- ✅ **Generatore Melodie**: Crea melodie basate su scala e mood
- ✅ **Database Esteso**: 14+ scale, 50+ progressioni, 15+ chord types
- ✅ **Workflow Integrati**: Dalla composizione al mix completo
- ✅ **Documentazione Completa**: 6 guide dettagliate

---

## 📁 Struttura della Skill

```
sound-design/
├── SKILL.md                    # File principale (istruzioni per Claude)
├── README.md                   # Questo file
├── Sound_Design_Skill_Guida.md # Guida italiana completa
├── Esempi_Pratici.md           # Tutorial step-by-step
│
├── docs/                       # Documentazione
│   ├── MASTER_SUMMARY.md              # Panoramica completa
│   ├── quick_start_guide.md           # Guida rapida
│   ├── integration_instructions.md    # Istruzioni integrazione
│   ├── skill_expansion_guide.md       # Come espandere la skill
│   ├── analyze_harmony_documentation.md  # Doc analisi armonica
│   └── HARMONIC_ANALYSIS_UPDATE.md    # Aggiornamenti tool
│
├── references/                 # Database teorici
│   ├── music-theory.md         # Teoria musicale completa
│   ├── chord-progressions.md   # Progressioni per mood/genere
│   ├── scales-modes.md         # Database scale e modi
│   ├── synth-database.md       # Synth hardware/software
│   ├── sound-archetypes.md     # Tipi di suoni (bass, pad, lead)
│   └── genre-styles.md         # Stili musicali specifici
│
├── scripts/                    # Tool Python
│   ├── mood_to_composition.py  # Mood → composizione + MIDI
│   ├── analyze_harmony.py      # Analisi MIDI (key, scale, chords)
│   └── generate_melody.py      # Generatore melodie
│
├── examples/                   # File di esempio
│   ├── *.mid                   # MIDI progressioni/pattern
│   ├── *.vital                 # Preset synth Vital
│   ├── *.json                  # Specifiche patch
│   └── *.svg                   # Diagrammi signal flow
│
└── sound-design.skill          # File configurazione skill
```

---

## 🎹 Funzionalità Principali

### 1. **Sound Design & Synth Programming**

Programma patch dettagliati per:

**Hardware**:
- Moog Matriarch (semi-modular analog)
- Elektron Digitone II (FM digital)
- Moog DFAM, Subharmonicon
- Behringer Crave
- Make Noise 0-Coast

**Software**:
- Vital (wavetable)
- Serum (wavetable)
- Massive X (hybrid)
- Diva (virtual analog)
- Arturia Pigments 6

**Esempi**:
```
"Crea un pad ambientale sulla Matriarch in D Phrygian"
"Programma un bass Reese su Vital per techno"
"Sound design per lead aggressivo su Digitone"
```

---

### 2. **Teoria Musicale & Composizione**

Database completo con:
- **14+ Scale**: Major modes, minor scales, pentatonic, blues, exotic
- **50+ Progressioni**: Organizzate per mood e genere
- **15+ Tipi di Accordi**: Triadi, 7th, extended, suspended
- **Analisi Armonica**: Rilevamento key/scale da MIDI

**Esempi**:
```
"Suggerisci progressioni per mood dark atmospheric"
"Quale scala uso per musica sad ma con speranza?"
"Analizza questo MIDI e dimmi la tonalità"
```

---

### 3. **Generazione Automatica**

Tool per generare automaticamente:

#### A) **Composizione da Mood**
```bash
python scripts/mood_to_composition.py "dark atmospheric" D
```
**Output**:
- Scala suggerita (es. D Phrygian)
- 3 progressioni di accordi
- MIDI files delle progressioni
- Production tips

#### B) **Analisi MIDI**
```bash
python scripts/analyze_harmony.py song.mid
```
**Output**:
- Key detection (con confidenza %)
- Scale matching
- Chord progression (con numeri romani)
- Suggerimenti variazioni

#### C) **Generazione Melodie**
```bash
python scripts/generate_melody.py D minor sad 120
```
**Output**:
- Melodia MIDI in scala specificata
- Adatta al mood scelto
- BPM customizzabile

---

### 4. **Visualizzazioni**

Genera diagrammi professionali:
- **Signal Flow**: Routing synth con modulazioni
- **Notazioni Testuali**: Pattern drum ASCII-art
- **Grafici Analisi**: Distribuzione pitch class

---

## 🚀 Quick Start

### Installazione Rapida

```bash
# 1. Dipendenze Python
pip install mido --break-system-packages

# 2. Verifica installazione
cd scripts/
python mood_to_composition.py
```

### Primo Utilizzo

**Scenario 1**: Creare un brano da zero

```
User: "Voglio creare un dark techno track in Em, 130 BPM"

Claude eseguirà:
1. Analizza mood → dark + energetic
2. Genera composizione in E Phrygian
3. Crea progressioni MIDI
4. Suggerisce bass patch (Reese)
5. Genera pattern drum techno
6. Fornisce arrangement structure
```

**Scenario 2**: Analizzare un brano esistente

```
User: "Analizza questo MIDI e dimmi come replicare il sound"

Claude eseguirà:
1. Analisi armonica → key, scale, progressioni
2. Identifica mood/genere
3. Genera progressioni simili
4. Suggerisce synth patches appropriati
5. Ricrea rhythm pattern simile
```

**Scenario 3**: Sound design specifico

```
User: "Programma un pad per questo brano"

Claude eseguirà:
1. Identifica tonalità del brano
2. Sceglie synth appropriato (es. Matriarch)
3. Programma patch in scala corretta
4. Fornisce diagram signal flow
5. Suggerisce processing chain
```

---

## 🛠️ Strumenti Disponibili

### Scripts Python

| Script | Funzione | Input | Output |
|--------|----------|-------|--------|
| `mood_to_composition.py` | Genera composizione da mood | Mood, root key | Scala, 3 progressioni, MIDI |
| `analyze_harmony.py` | Analizza armonia MIDI | File MIDI | Key, scale, chords, suggestions |
| `generate_melody.py` | Crea melodie | Scala, mood, BPM | Melodia MIDI |

### Database Teorici

| File | Contenuto |
|------|-----------|
| `music-theory.md` | Intervalli, scale, accordi, armonia, voice leading |
| `chord-progressions.md` | 50+ progressioni per mood/genere |
| `scales-modes.md` | 14+ scale con caratteristiche e MIDI values |
| `synth-database.md` | Specifiche 10+ synth HW/SW |
| `sound-archetypes.md` | Bass, pad, lead, texture archetypes |
| `genre-styles.md` | Techno, house, ambient, IDM, etc. |

---

## 📖 Documentazione

### Guide Principali

1. **[MASTER_SUMMARY.md](docs/MASTER_SUMMARY.md)**
   - Panoramica completa di tutto
   - Statistiche e features
   - Come iniziare

2. **[quick_start_guide.md](docs/quick_start_guide.md)**
   - 3 passi per iniziare subito
   - Esempi di richieste
   - Workflow pratici

3. **[Sound_Design_Skill_Guida.md](Sound_Design_Skill_Guida.md)**
   - Guida completa in italiano
   - Tutorial dettagliati
   - Best practices

4. **[integration_instructions.md](docs/integration_instructions.md)**
   - Come integrare nuove funzionalità
   - Modifiche a SKILL.md
   - Testing e deployment

5. **[skill_expansion_guide.md](docs/skill_expansion_guide.md)**
   - Come espandere la skill
   - Aggiungere synth
   - Creare nuovi tool

6. **[analyze_harmony_documentation.md](docs/analyze_harmony_documentation.md)**
   - Documentazione completa analisi armonica
   - Algoritmi usati
   - Troubleshooting

### Guide Specifiche

- **[Esempi_Pratici.md](Esempi_Pratici.md)**: Tutorial step-by-step
- **[HARMONIC_ANALYSIS_UPDATE.md](docs/HARMONIC_ANALYSIS_UPDATE.md)**: Novità tool analisi

---

## 🎼 Esempi Pratici

### Esempio 1: Dark Ambient Track

```bash
# 1. Genera composizione
python scripts/mood_to_composition.py "dark atmospheric" C#

# Output: C# Locrian, 3 progressioni MIDI

# 2. Usa con Claude
"Crea pad Matriarch usando progression_1_dark_C#.mid"

# Output: Patch completo in C# Locrian

# 3. Aggiungi texture
"Genera melodia ambient in C# Locrian, molto lenta"

# Output: Melodia MIDI + suggerimenti layering
```

### Esempio 2: Analisi & Replica

```bash
# 1. Analizza reference
python scripts/analyze_harmony.py reference_track.mid

# Output: D Phrygian, i-bII-bVII-bVI progression

# 2. Genera simile
python scripts/mood_to_composition.py dark D

# Output: Nuove progressioni in D Phrygian

# 3. Confronta
python scripts/analyze_harmony.py my_new_track.mid

# Output: Verifica tonalità e progressione
```

### Esempio 3: Workflow Completo

```
User: "Crea un brano energetic techno completo"

Claude workflow:
1. mood_to_composition.py energetic E → Progressioni E Mixolydian
2. Sound design: Bass Reese + FM lead + Pad
3. Rhythm: Pattern techno 128 BPM, 16 bars
4. Arrangement: Intro-Build-Drop-Breakdown-Drop
5. Mix tips: Sidechain, compression, spatial effects

Output: MIDI files + synth patches + mix chain
```

---

## 🎛️ Workflow Integrati

### Workflow 1: Composizione → Produzione

```
[Mood] → [Composizione] → [Sound Design] → [Rhythm] → [Mix]
```

**Esempio**:
```
"dark" → D Phrygian → Matriarch pad + Vital bass → Techno 130 BPM → Mix chain
```

### Workflow 2: Analisi → Replicazione

```
[Reference MIDI] → [Analisi] → [Genera Simile] → [Sound Design] → [Verifica]
```

**Esempio**:
```
reference.mid → D Phrygian → Nuove progressioni → Synth patches → analyze my_track.mid
```

### Workflow 3: Sound First → Composizione

```
[Synth Patch] → [Estrai Tonalità] → [Genera Progressione] → [Complete Track]
```

**Esempio**:
```
Matriarch pad → D Phrygian → 3 progressioni → Bass + drums + arrangement
```

---

## 🎹 Synth Supportati

### Hardware (6)

| Synth | Tipo | Specialità |
|-------|------|-----------|
| **Moog Matriarch** | Semi-modular analog | Pad ricchi, bass warm, routing complesso |
| **Elektron Digitone II** | FM digital | Stabs percussivi, bell tones, FM bass |
| **Moog DFAM** | Analog percussion | Kick, drum, percussioni analogiche |
| **Moog Subharmonicon** | Subharmonic synth | Drone, texture subharmoniche |
| **Behringer Crave** | Semi-modular | Bass, lead, affordable modular |
| **Make Noise 0-Coast** | West Coast | Chaotic sounds, waveshaping |

### Software (5)

| Synth | Tipo | Specialità |
|-------|------|-----------|
| **Vital** | Wavetable | Moderno, versatile, gratuito |
| **Serum** | Wavetable | Industry standard, wavetable pulito |
| **Massive X** | Hybrid | Routing flessibile, sound moderno |
| **Diva** | Virtual analog | Emulazioni vintage autentiche |
| **Arturia Pigments 6** | Hybrid | Multi-engine, modulazione estesa |

---

## 📋 Requisiti

### Software

- **Python**: 3.12+ (o 3.10+)
- **Claude AI**: Accesso alla piattaforma
- **DAW** (opzionale): Ableton, Logic, FL Studio, etc.

### Librerie Python

```bash
pip install mido --break-system-packages
```

### Files Necessari

Tutti i file nella directory `sound-design/` devono essere presenti:
- `SKILL.md` (core)
- `references/` (database)
- `scripts/` (tool)
- `docs/` (documentazione)

---

## 🔧 Installazione

### Metodo 1: Già Installata (Se hai questa struttura)

La skill è già installata! Verifica con:

```bash
cd scripts/
python mood_to_composition.py
```

Se vedi l'help message, tutto funziona! ✅

### Metodo 2: Installazione da Zero

```bash
# 1. Crea directory
mkdir -p ~/sound-design
cd ~/sound-design

# 2. Scarica/copia tutti i file nella struttura corretta

# 3. Installa dipendenze
pip install mido --break-system-packages

# 4. Testa
cd scripts/
python mood_to_composition.py dark
```

### Metodo 3: Aggiornamento Versione Esistente

```bash
# Se hai una versione vecchia, aggiungi i nuovi file:
cd ~/sound-design

# Aggiungi nuovi script
cp nuovo_analyze_harmony.py scripts/
cp nuovo_generate_melody.py scripts/

# Aggiungi nuova documentazione
cp nuovo_*.md docs/

# Aggiorna references
cp nuovo_*.md references/
```

---

## 🎓 Uso con Claude

### Richieste Supportate

**Composizione**:
```
"Crea progressioni dark in D minor"
"Suggerisci scala per mood energetic"
"Genera melodia sad in A minor"
```

**Sound Design**:
```
"Programma pad Matriarch in C Lydian"
"Crea bass patch Vital per techno"
"Sound design lead aggressivo Digitone"
```

**Analisi**:
```
"Analizza questo MIDI e dimmi la tonalità"
"Che progressione usa questo brano?"
"Come replico questo sound?"
```

**Workflow Completi**:
```
"Crea dark techno track completo in Em"
"Voglio un brano simile a questo reference"
"Produce ambient track con questi elementi"
```

---

## 🤝 Contribuire

### Come Espandere

1. **Aggiungere Synth**:
   - Edita `references/synth-database.md`
   - Aggiungi specifiche complete
   - Documenta con esempi

2. **Aggiungere Scale**:
   - Edita `references/scales-modes.md`
   - Includi MIDI values
   - Descrivi caratteristiche

3. **Aggiungere Progressioni**:
   - Edita `references/chord-progressions.md`
   - Organizza per mood/genere
   - Fornisci esempi MIDI

4. **Creare Nuovi Tool**:
   - Aggiungi script in `scripts/`
   - Documenta in `docs/`
   - Aggiorna `SKILL.md`

Vedi **[skill_expansion_guide.md](docs/skill_expansion_guide.md)** per dettagli.

---

## 📊 Statistiche Skill

**Versione**: 2.0  
**File totali**: 30+  
**Linee di codice**: 3,000+  
**Linee documentazione**: 5,000+  
**Synth supportati**: 11  
**Scale nel database**: 14+  
**Progressioni nel database**: 50+  
**Tool Python**: 3  
**Guide**: 6  

---

## 📝 Changelog

### Version 2.0 (Ottobre 2024)
- ✨ Aggiunto tool analisi armonica completo
- ✨ Aggiunto generatore melodie
- ✨ Database espanso (scale, progressioni)
- ✨ 6 guide documentazione complete
- ✨ Workflow integrati completi
- 🔧 Refactoring struttura directory
- 📖 README completo aggiornato

### Version 1.0 (Ottobre 2024)
- 🎉 Release iniziale
- ✅ Sound design per Matriarch, Digitone
- ✅ Mood to composition generator
- ✅ Database teoria musicale
- ✅ Pattern drum generation

---

## 🆘 Supporto & Troubleshooting

### Problemi Comuni

**Script non funziona**:
```bash
# Verifica Python version
python --version  # Deve essere 3.10+

# Reinstalla dipendenze
pip install mido --break-system-packages
```

**Claude non usa i file**:
```
Ricorda a Claude: "Usa i file nella skill sound-design"
Specifica: "Leggi references/music-theory.md per questa richiesta"
```

**MIDI non si apre**:
- Verifica formato .mid
- Prova con DAW diversa
- Controlla che il file non sia vuoto

### Risorse Utili

- 📖 [MASTER_SUMMARY.md](docs/MASTER_SUMMARY.md) - Panoramica completa
- 🚀 [quick_start_guide.md](docs/quick_start_guide.md) - Guida rapida
- 🔧 [skill_expansion_guide.md](docs/skill_expansion_guide.md) - Espansione skill

---

## 📄 Licenza

Questa skill è fornita "as-is" per uso educativo e creativo.

---

## 🎉 Crediti

**Sviluppato con**: Claude AI (Anthropic)  
**Algoritmi**: Krumhansl-Schmuckler (key detection)  
**Teoria Musicale**: Standard Western music theory  

---

## 🎵 Inizia Ora!

```bash
# Testa la skill
cd scripts/
python mood_to_composition.py happy G

# Leggi la guida rapida
cat ../docs/quick_start_guide.md

# Oppure chiedi a Claude:
"Crea un brano [mood] in [key] con synth e drums"
```

**Happy music making!** 🎛️✨

---

**README.md** | Sound Design & Music Production Skill v2.0  
Ultima modifica: Ottobre 2024
