# Sound Design Skill - Guida Rapida

## Congratulazioni! 🎉

La tua **Sound Design Skill** è stata creata con successo! Questa skill ti aiuterà a progettare suoni per tutti i tuoi synth hardware e software.

## Contenuto della Skill

### 📚 File di Riferimento (References)

1. **synth-parameters.md** - Parametri comuni di tutti i synth
   - Oscillatori, filtri, envelope, LFO, effetti
   - Architettura delle voci (mono/poly/unison)
   - Sintesi avanzata (wavetable, FM, granular)

2. **sound-archetypes.md** - Caratteristiche per tipo di suono
   - Bass (Sub Bass, Reese, Acid)
   - Lead (Synth Lead, Pluck, Supersaw)
   - Pad (Ambient, String, Drone)
   - Keys/Mallets (Electric Piano, Bells, Marimba)
   - Texture (Granular, Noise, Evolving)
   - Percussion (Kick, Snare, Hi-Hat)

3. **genre-styles.md** - Caratteristiche per genere musicale
   - Vintage/Analog (70s-80s)
   - Techno
   - IDM
   - Ambient/Drone
   - Synthwave/Retrowave
   - Dubstep/Bass Music
   - Trap/Hip-Hop
   - Psytrance
   - Industrial/EBM
   - House (Deep/Tech)

4. **synth-database.md** - Database dettagliato dei tuoi synth
   - **Hardware**: Digitone II, Matriarch, DFAM, Subharmonicon, Crave, 0-Coast
   - **Software**: Vital, Serum, Massive X, Diva, Pigments 6
   - Specifiche tecniche, formati file, approcci al sound design

### 🛠️ Script Automatici

1. **analyze_audio.py** - Analizza file audio
   - Estrae caratteristiche spettrali (brightness, bandwidth)
   - Analizza contenuto armonico vs noise
   - Rileva transient e ritmo
   - Suggerisce come ricreare il suono
   - **Richiede**: `pip install librosa --break-system-packages`

2. **generate_rhythm.py** - Genera pattern MIDI
   - Crea pattern per vari generi (techno, house, trap, dnb, dubstep, breakbeat)
   - Output: notazione testuale + file MIDI
   - Parametri: genere, BPM, numero di battute
   - **Richiede**: `pip install mido --break-system-packages`

3. **generate_vital_preset.py** - Genera preset Vital
   - Crea file .vital basati su specifiche JSON
   - Preset configurati per tipo di suono e genere
   - Formato JSON facilmente editabile

4. **generate_signal_diagram.py** - Crea diagrammi di routing
   - Genera diagrammi SVG del flusso del segnale
   - Mostra oscillatori, filtri, envelope, LFO, effetti
   - Visualizza connessioni e modulazioni

## Come Usare la Skill

### Esempio 1: Creare un Bass per Techno su Vital

**Conversazione con Claude:**
```
Tu: Vorrei creare un bass per techno su Vital

Claude: [Legge i file di riferimento]
        [Chiede specifiche: mono/poly, caratteristiche]
        [Genera specifiche JSON]
        [Esegue generate_vital_preset.py]
        [Crea diagramma del segnale]
        [Fornisce guida step-by-step]
```

### Esempio 2: Analizzare un Suono Esistente

**Conversazione con Claude:**
```
Tu: Ho questo file audio, come posso ricreare questo suono?
    [allega file audio]

Claude: [Esegue analyze_audio.py sul file]
        [Analizza le caratteristiche]
        [Suggerisce parametri del synth]
        [Propone quale synth usare]
```

### Esempio 3: Creare un Pattern Ritmico

**Conversazione con Claude:**
```
Tu: Vorrei un pattern techno a 128 BPM per 8 battute

Claude: [Esegue generate_rhythm.py techno 128 8]
        [Mostra notazione testuale]
        [Fornisce file MIDI]
```

### Esempio 4: Programmare un Synth Modulare

**Conversazione con Claude:**
```
Tu: Come programmo un pad ambient sulla Moog Matriarch?

Claude: [Legge synth-database.md per specifiche Matriarch]
        [Legge sound-archetypes.md per caratteristiche pad]
        [Legge genre-styles.md per approccio ambient]
        [Fornisce routing patch completo]
        [Guida step-by-step con posizioni dei controlli]
```

## Funzionalità Principali

### ✅ La skill SA:

1. **Identificare il synth** - Chiede sempre quale synth stai usando
2. **Suggerire parametri** - Basandosi su tipo di suono e genere
3. **Generare preset** - File .vital pronti all'uso
4. **Analizzare audio** - Estrae caratteristiche da file esistenti
5. **Creare pattern MIDI** - Ritmi per vari generi musicali
6. **Visualizzare routing** - Diagrammi SVG del flusso del segnale
7. **Guide passo-passo** - Istruzioni dettagliate per ogni synth
8. **Gestire voci** - Mono, poly, unison
9. **Adattare per genere** - Vintage, techno, IDM, ambient, ecc.
10. **Routing modulare** - Per synth semi-modulari con patch bay

### ⚙️ Workflow Tipico:

1. **Specifica il synth** → Claude identifica le capacità
2. **Descrivi il suono** → Tipo (bass, lead, pad) + genere + caratteristiche
3. **Ottieni la patch** → Parametri dettagliati + file se possibile
4. **Visualizza il routing** → Diagramma SVG del segnale
5. **Segui la guida** → Istruzioni passo-passo
6. **Raffina** → Tweaking basato sul feedback

## Synth Supportati

### Hardware
- **Elektron Digitone II** - FM 4-op, sequencer, parameter locks
- **Moog Matriarch** - Semi-modular 4-VCO, 2 filtri, 90 patch points
- **Moog DFAM** - Percussion synth analogico
- **Moog Subharmonicon** - Sintesi subarmonica, polyrhythmic
- **Behringer Crave** - Semi-modular, 18 patch points
- **Make Noise 0-Coast** - West Coast, waveshaping, no keyboard

### Software
- **Vital** - Wavetable con spectral warping (generazione preset)
- **Serum** - Wavetable (.fxp format)
- **Massive X** - Hybrid semi-modular (.nmsv format)
- **Diva** - Virtual analog (.h2p format)
- **Arturia Pigments 6** - Hybrid multi-engine (.pigments format)

## Installazione

### Importare la Skill

1. Scarica il file `sound-design.skill`
2. In Claude, vai su **Skills** nel menu
3. Clicca **Import Skill**
4. Seleziona `sound-design.skill`
5. La skill sarà disponibile immediatamente!

### Dipendenze Python (Opzionali)

Per usare tutte le funzionalità degli script:

```bash
# Per analisi audio
pip install librosa --break-system-packages

# Per generazione MIDI
pip install mido --break-system-packages
```

**Nota**: Gli script funzionano anche senza queste librerie, ma con funzionalità limitate.

## Tips & Tricks

### 💡 Per Ottenere i Migliori Risultati:

1. **Sii specifico** - "Bass techno mono aggressive dark" è meglio di "bass"
2. **Menziona il synth** - Claude adatterà le istruzioni al tuo hardware/software
3. **Chiedi esempi** - "Mostrami 3 variazioni di questo sound"
4. **Usa l'analisi** - Carica file audio di riferimento per sound design inverso
5. **Richiedi diagrammi** - Visualizza il routing per capire meglio
6. **Sperimenta** - Chiedi variazioni e tweaking suggeriti

### 🎛️ Workflow Efficace:

```
1. Descrivi il contesto musicale (genere, BPM, mood)
2. Specifica il tipo di suono desiderato
3. Indica il synth che userai
4. Ottieni la patch base
5. Chiedi variazioni o refinement
6. Genera file MIDI/preset se disponibili
```

### 🔧 Per Synth Modulari:

- Chiedi sempre il routing completo delle patch
- Specifica se hai limitazioni di patch cables
- Richiedi alternative se non hai certi moduli
- Claude può suggerire patch creative inaspettate!

## Esempi di Query

```
"Crea un reese bass per DnB sul Digitone II"
"Come programmo un pad ambient evolving sulla Matriarch?"
"Analizza questo kick e dimmi come ricrearlo"
"Genera un pattern trap a 140 BPM con hi-hat triplets"
"Voglio un lead supersaw per trance su Vital, genera il preset"
"Mostrami il signal flow per un bell sound FM"
"Come ottengo un suono tipo TB-303 sul Crave?"
"Crea una texture granular per IDM su Pigments"
```

## Supporto e Sviluppo Futuro

Questa skill può essere estesa con:
- Più synth nel database
- Template di preset per altri formati
- Pattern MIDI più complessi
- Analisi MIDI di pattern esistenti
- Integration con DAW specifiche

## Crediti

Creata per supportare il sound design professionale su:
- 6 synth hardware (Elektron, Moog, Behringer, Make Noise)
- 5 synth software (Vital, Serum, Massive X, Diva, Pigments)
- 10+ generi musicali
- 20+ tipologie di suono

**Buon sound design! 🎹🎛️🎵**
