# LEAD AGGRESSIVO - ELEKTRON DIGITONE

## INFORMAZIONI PATCH
**Nome**: Aggressive FM Lead  
**Tipo**: Synth Lead  
**Carattere**: Aggressivo, brillante, tagliente  
**Voci**: Monofonica (con legato)  
**Genere**: Techno / Industrial / IDM

---

## ALGORITMO FM

**Algoritmo selezionato**: **ALGORITHM 6**  
```
    ┌─────┐
    │ OP4 │
    └──┬──┘
       ↓
    ┌─────┐     ┌─────┐
    │ OP3 │ ←─→ │ OP2 │
    └──┬──┘     └──┬──┘
       ↓          ↓
       └────┬─────┘
            ↓
         ┌─────┐
         │ OP1 │ → OUTPUT
         └─────┘
```

**Perché questo algoritmo?**  
L'algoritmo 6 offre una struttura complessa con feedback tra OP2 e OP3, ideale per generare armonici metallici e dissonanze aggressive. OP4 modula OP3 aggiungendo complessità timbrica superiore.

---

## CONFIGURAZIONE OPERATORI

### OPERATOR 1 (Carrier Principale)
- **Ratio**: 1.00 (fondamentale)
- **Fine Tune**: 0 cents
- **Level**: 100 (massimo output)
- **Feedback**: 0

**ENVELOPE OP1**:
- Attack: **5 ms** (attacco veloce ma non istantaneo)
- Hold: **0 ms**
- Decay: **150 ms** (decadimento medio)
- Release: **200 ms**
- Depth: **0** (non affetto da velocity)

---

### OPERATOR 2 (Modulatore Primario)
- **Ratio**: 3.50 (terza armonica + quinta)
- **Fine Tune**: +7 cents (lieve detuning per battimenti)
- **Level**: 70 (modulazione intensa)
- **Feedback**: 25 (feedback con OP3 per texture metallica)

**ENVELOPE OP2**:
- Attack: **1 ms** (attacco istantaneo)
- Hold: **10 ms**
- Decay: **300 ms** (decadimento più lungo)
- Release: **150 ms**
- Depth: **30** (leggera risposta alla velocity)

---

### OPERATOR 3 (Modulatore Secondario)
- **Ratio**: 5.00 (quinta armonica)
- **Fine Tune**: -5 cents (detuning opposto a OP2)
- **Level**: 65
- **Feedback**: 25 (feedback con OP2)

**ENVELOPE OP3**:
- Attack: **0 ms** (istantaneo)
- Hold: **5 ms**
- Decay: **200 ms**
- Release: **100 ms**
- Depth: **50** (buona risposta alla velocity per espressività)

---

### OPERATOR 4 (Modulatore di Alta Frequenza)
- **Ratio**: 11.00 (undicesima armonica - molto alta)
- **Fine Tune**: +3 cents
- **Level**: 45 (modulazione moderata per aggiungere brillantezza)
- **Feedback**: 0

**ENVELOPE OP4**:
- Attack: **0 ms**
- Hold: **0 ms**
- Decay: **80 ms** (decadimento molto rapido)
- Release: **50 ms**
- Depth: **70** (forte risposta alla velocity)

**Nota**: OP4 decade rapidamente creando un transiente iniziale brillante e aggressivo che poi si dissolve, lasciando la struttura FM più stabile di OP1-2-3.

---

## FILTRO ANALOGICO

**Tipo**: **Low-Pass 24 dB/oct** (Moog-style ladder filter)

- **Cutoff Frequency**: 3500 Hz (~65%)
- **Resonance**: 35% (sufficiente per enfatizzare la frequenza di taglio)
- **Filter Type**: LP24 (low-pass 24dB per togliere solo le alte frequenze eccessive)

**FILTER ENVELOPE**:
- Attack: **3 ms**
- Hold: **0 ms**
- Decay: **250 ms**
- Release: **150 ms**
- Depth: **+50** (modulazione positiva significativa)
- Base: **65** (punto di partenza del cutoff)

**KEYBOARD TRACKING**: **75%** (il filtro si apre con note più alte)

**VELOCITY TO FILTER**: **+40** (velocity aumenta il cutoff per suoni più brillanti su note forti)

---

## AMPLIFIER

**AMP ENVELOPE**:
- Attack: **3 ms** (leggermente più lento per evitare click)
- Hold: **0 ms**
- Decay: **300 ms**
- Sustain: **75%** (sustain alto per note tenute)
- Release: **250 ms**

**VELOCITY TO AMP**: **50** (velocity moderata per dinamica naturale)

**OVERDRIVE**: **30%** (saturazione analogica per aggressività)

---

## MODULAZIONE

### LFO 1 - Vibrato
- **Waveform**: Sine
- **Speed**: 6.5 Hz
- **Fade In**: 200 ms (vibrato si sviluppa gradualmente)
- **Destination**: Pitch (tutti gli operatori)
- **Depth**: ±8 cents (vibrato sottile ma percettibile)

### LFO 2 - Modulazione timbrica
- **Waveform**: Triangle
- **Speed**: 0.3 Hz (molto lento)
- **Depth**: 15
- **Destination**: OP2 Level (modula l'intensità della modulazione FM)
- **Sync**: Free running

**Questo crea un'evoluzione timbrica lenta che aggiunge movimento al suono**

---

## EFFETTI

### CHORUS
- **Depth**: 40%
- **Rate**: 0.8 Hz (lento)
- **Feedback**: 20%
- **Mix**: 25% (sottile, solo per aggiungere larghezza)

### DELAY
- **Time**: 1/8 dotted (seguita dal tempo del progetto)
- **Feedback**: 35%
- **Filter**: LP 3 kHz (delay più scuro)
- **Width**: 60% (stereo spread)
- **Mix**: 18% (delay discreto)

### REVERB
- **Pre-Delay**: 15 ms
- **Decay Time**: 1.8 s
- **High Damp**: 6 kHz
- **Low Shelf**: -3 dB @ 200 Hz
- **Mix**: 12% (reverb molto discreto)

---

## PERFORMANCE SETTINGS

### PORTAMENTO/LEGATO
- **Mode**: Legato (portamento attivo solo in modalità legato)
- **Time**: 30 ms (glide veloce tra le note)
- **Type**: Exponential (curva naturale)

### VELOCITY CURVE
- **Response**: Medium (curva lineare ma con buona dinamica)

### PITCH BEND
- **Range**: ±2 semitoni

### MOD WHEEL
- **Destination 1**: LFO1 Depth (vibrato) - Amount: +100%
- **Destination 2**: Filter Cutoff - Amount: +30%

---

## NOTE DI PROGRAMMAZIONE

### Come ottenere il suono più aggressivo:

1. **Aumentare il feedback OP2/OP3**: Portare a 35-40 per suoni più metallici
2. **Alzare OP4 Level**: Portare a 55-60 per transiente più brillante
3. **Aumentare Resonance**: Portare a 45-50% per enfasi sulla frequenza di taglio
4. **Overdrive più spinto**: Portare a 40-50% per saturazione maggiore
5. **Velocity più estrema**: Aumentare tutte le depth di velocity per maggiore espressività

### Variazioni stilistiche:

**Per lead più scuro (Dark Techno)**:
- OP4 Level → 25
- Filter Cutoff → 2500 Hz
- Chorus Mix → 35%

**Per lead più industriale/harsh**:
- OP2 Feedback → 50
- OP3 Level → 85
- Overdrive → 60%
- Filter Resonance → 55%

**Per lead più melodico**:
- OP2 Level → 55
- OP4 Level → 30
- Filter Cutoff → 4500 Hz
- Chorus Mix → 40%
- Reverb Mix → 20%

---

## STEP-BY-STEP: Come programmare sul Digitone

### 1. SELEZIONE BASE
- Premere **[TRACK]** → selezionare Track 1
- Premere **[FUNC]** + **[YES]** per inizializzare nuovo sound
- Ruotare l'encoder **[ALGORITHM]** → selezionare **ALG 6**

### 2. OPERATORI (premere [OP1-4] per accedere a ciascuno)

**OPERATOR 1**:
- [OP1] → PAGE: TUNE
  - RATIO: 1.00, FINE: 0
- PAGE: LEVEL
  - LEVEL: 100
- PAGE: ENV
  - A: 5, D: 150, R: 200

**OPERATOR 2**:
- [OP2] → PAGE: TUNE
  - RATIO: 3.50, FINE: +7
- PAGE: LEVEL
  - LEVEL: 70
  - FEEDBACK: 25 (con OP3)
- PAGE: ENV
  - A: 1, H: 10, D: 300, R: 150
  - DEPTH: 30

**OPERATOR 3**:
- [OP3] → PAGE: TUNE
  - RATIO: 5.00, FINE: -5
- PAGE: LEVEL
  - LEVEL: 65
  - FEEDBACK: 25 (con OP2)
- PAGE: ENV
  - A: 0, H: 5, D: 200, R: 100
  - DEPTH: 50

**OPERATOR 4**:
- [OP4] → PAGE: TUNE
  - RATIO: 11.00, FINE: +3
- PAGE: LEVEL
  - LEVEL: 45
- PAGE: ENV
  - A: 0, D: 80, R: 50
  - DEPTH: 70

### 3. FILTRO
- Premere **[FILTER]**
- PAGE: TYPE
  - Type: LP24
  - Cutoff: 65% (~3500 Hz)
  - Resonance: 35%
- PAGE: ENV
  - A: 3, D: 250, R: 150
  - DEPTH: +50
  - BASE: 65
- PAGE: TRACK
  - Keyboard Tracking: 75%
- PAGE: MOD
  - VEL → CUTOFF: +40

### 4. AMPLIFIER
- Premere **[AMP]**
- PAGE: ENV
  - A: 3, D: 300, S: 75%, R: 250
- PAGE: MOD
  - VEL → AMP: 50
- PAGE: OVERDRIVE
  - Amount: 30%

### 5. LFO MODULATION
- Premere **[LFO]** → **[LFO 1]**
  - Wave: Sine
  - Speed: 6.5 Hz
  - Fade: 200 ms
  - Destination: PITCH
  - Depth: ±8 cents

- **[LFO 2]**
  - Wave: Triangle
  - Speed: 0.3 Hz
  - Destination: OP2 Level
  - Depth: 15

### 6. EFFETTI
- Premere **[FX]**

**Chorus**:
- PAGE: CHO
  - Depth: 40%, Rate: 0.8 Hz
  - Feedback: 20%, Mix: 25%

**Delay**:
- PAGE: DEL
  - Time: 1/8 dotted (o 3/16)
  - Feedback: 35%
  - HP: 200 Hz, LP: 3 kHz
  - Width: 60%, Mix: 18%

**Reverb**:
- PAGE: REV
  - Pre-delay: 15 ms
  - Decay: 1.8 s
  - HP: 200 Hz, LP: 6 kHz
  - Mix: 12%

### 7. PERFORMANCE
- Premere **[TRIG]** → PAGE: PORT
  - Mode: Legato
  - Time: 30 ms

- Premere **[FUNC]** + **[TRIG]** per settings globali
  - Pitch Bend Range: ±2 semitoni

---

## SUGGERIMENTI PER L'USO

### Contesto musicale ideale:
- **Techno aggressivo**: Usare in mid-range (C3-C5) con sequenze melodiche ripetitive
- **Industrial**: Note lunghe con modulazione dal mod wheel su cutoff
- **IDM/Experimental**: Sfruttare legato per glide espressivi tra note distanti
- **Bass Music**: Octave down per lead-bass ibrido (provare C2-C3)

### Combinazioni con altri suoni:
- Funziona bene con:
  - Kick aggressivo e profondo
  - Hi-hat veloci e brillanti
  - Bass sub pulito che lascia spazio nella gamma 300-800 Hz
- Evitare:
  - Pad troppo brillanti (competono nello stesso range)
  - Troppi layer di lead (il suono è già molto denso)

### Automazione consigliata:
- **Filter Cutoff**: Apri gradualmente durante le sezioni intense
- **OP2/OP3 Feedback**: Aumenta per buildup o drop
- **Overdrive**: Aumenta per transizioni aggressive
- **Reverb Mix**: Aumenta per pause o breakdown ambient

---

## ANALISI TIMBRICA

### Spettro armonico:
```
Fondamentale (OP1): ████████████████████ (100%)
3.5x armonica (OP2): ███████████████ (70%)
5x armonica (OP3):   ██████████████ (65%)
11x armonica (OP4):  ████████ (45% - transiente iniziale)
```

### Evoluzione temporale:
1. **0-50ms**: Attacco con forte presenza di OP4 (11x) → brillantezza metallica
2. **50-200ms**: OP4 decade, predominanza di OP2/OP3 con feedback → texture densa
3. **200ms+**: OP1 carrier stabile, OP2/OP3 continuano → sustain ricco ma controllato
4. **Release**: Decadimento coordinato con coda di reverb/delay

### Range frequenziale principale:
- **Fondamentale**: 100-800 Hz (nota dipendente)
- **Armonici primari**: 800-4000 Hz (corpo del suono)
- **Brillantezza/Presenza**: 4000-10000 Hz (controllata dal filtro)

---

## TROUBLESHOOTING

**Il suono è troppo metallico/dissonante?**
- Riduci OP2 e OP3 Feedback → 15-20
- Abbassa OP4 Level → 30-35
- Aumenta Filter Cutoff → 4000 Hz

**Il suono è troppo sottile?**
- Aumenta Chorus Mix → 35-40%
- Aggiungi unison detuning via Digitone (se disponibile)
- Layer con un secondo track con algoritmo più semplice

**Il suono non è abbastanza aggressivo?**
- Aumenta tutti i Feedback → 35-45
- Alza Overdrive → 45-60%
- Aumenta Filter Resonance → 45-55%
- OP4 Level → 60-70

**Manca definizione nel mix?**
- Riduci Reverb Mix → 5-8%
- Filtra il Delay più drasticamente → LP 2.5 kHz
- Applica EQ esterno: high-pass @150 Hz, boost @2.5 kHz

**Troppo harsh nelle alte frequenze?**
- Riduci Filter Cutoff → 2800 Hz
- Abbassa OP4 Level → 35
- Riduci Filter Resonance → 25%

---

## CONCLUSIONE

Questo patch sfrutta la potenza della sintesi FM del Digitone per creare un lead aggressivo e moderno, perfetto per generi elettronici intensi. La combinazione di:
- Algoritmo complesso con feedback
- Inviluppi differenziati per ogni operatore
- Filtro analogico con tracking e velocity
- Modulazione sottile ma efficace

...produce un suono dinamico, espressivo e che taglia attraverso il mix senza essere eccessivamente faticoso all'ascolto.

Sperimenta con le variazioni suggerite per adattare il suono al tuo stile specifico!
