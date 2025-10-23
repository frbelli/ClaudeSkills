# Esempi Pratici - Sound Design Skill

Questo documento contiene esempi concreti di come utilizzare la Sound Design Skill.

## File di Esempio Inclusi

Troverai questi file nella cartella outputs:

1. **sound-design.skill** - La skill completa da importare in Claude
2. **esempio_bass_techno.json** - Specifica per generare un preset bass
3. **esempio_signal_flow.json** - Specifica per generare un diagramma
4. **Dark_Techno_Bass.vital** - Preset Vital generato automaticamente
5. **esempio_signal_flow_diagram.svg** - Diagramma SVG del routing
6. **pattern_techno_techno_128bpm.mid** - File MIDI del pattern generato

## Esempio 1: Creare un Bass Techno per Vital

### Conversazione con Claude:

```
Tu: Voglio creare un bass techno scuro e aggressivo per Vital, monophonic

Claude: Perfetto! Creo un preset per un bass techno. Vediamo le specifiche:

[Claude legge i reference files]
- synth-database.md per capire Vital
- sound-archetypes.md per caratteristiche del bass
- genre-styles.md per l'approccio techno

[Claude crea il file JSON delle specifiche]
[Claude esegue lo script generate_vital_preset.py]

✅ Ho generato il preset "Dark_Techno_Bass.vital" con queste caratteristiche:

PATCH: Dark Techno Bass
SYNTH: Vital
TYPE: Bass
VOICES: 1 (Monophonic with legato)

OSCILLATORS:
- OSC 1: Sawtooth, Level 80%, Unison OFF
- OSC 2: Sawtooth, Detune -0.1 cents, Level 60%
- OSC 3: Sine wave, -12 semitones (sub), Level 70%

FILTER:
- Type: Low Pass 24dB
- Cutoff: 35 (circa 400Hz)
- Resonance: 30%
- Envelope Amount: 50%

ENVELOPES:
- AMP: A:1ms D:300ms S:80% R:200ms
- FILTER: A:1ms D:500ms S:20% R:100ms

EFFECTS:
- Distortion: Drive 6dB, Mix 30% (per grinta)

[Claude fornisce anche il file .vital scaricabile]
```

### Risultato:
Un preset Vital pronto da caricare, con parametri ottimizzati per un bass techno!

---

## Esempio 2: Programmare un Pad sulla Moog Matriarch

### Conversazione con Claude:

```
Tu: Come programmo un pad ambient sulla Moog Matriarch?

Claude: Ottimo! La Matriarch è perfetta per pad evolving. Ecco la guida completa:

[Claude legge synth-database.md per specifiche Matriarch]
[Claude legge sound-archetypes.md per caratteristiche pad ambient]
[Claude legge genre-styles.md per approccio ambient]

═══════════════════════════════════════════════════════════
STEP-BY-STEP GUIDE: Ambient Pad - Moog Matriarch
═══════════════════════════════════════════════════════════

1. INITIAL SETUP
   - Power on, wait for warm-up
   - Set all filter cutoffs to max (fully open)
   - Set all resonances to minimum
   - Mixer levels all to 12 o'clock

2. OSCILLATORS
   - VCO1: Sawtooth wave, tune to concert pitch
   - VCO2: Sawtooth wave, detune +3 cents (slightly right)
   - VCO3: Triangle wave, tune -1 octave
   - VCO4: Sawtooth wave, detune -5 cents (slightly left)

3. MIXER
   - VCO1 Level: 70% (2 o'clock)
   - VCO2 Level: 60% (1 o'clock)
   - VCO3 Level: 50% (12 o'clock)
   - VCO4 Level: 65% (1:30)
   - Noise: 0%

4. FILTER 1 (Main)
   - Type: Low Pass (24dB/oct)
   - Cutoff: 65% (circa 3kHz) - 2 o'clock
   - Resonance: 15% (9 o'clock)
   - Envelope Amount: 20% (10 o'clock)
   - Keyboard Tracking: 30%

5. FILTER 2 (Secondary)
   - Type: High Pass (12dB/oct)
   - Cutoff: 10% (rimuove solo sub estremi)
   - Link to Filter 1: OFF (in parallelo)

6. ENVELOPES
   - ENV1 (Amplitude):
     * Attack: 1.5s (2 o'clock)
     * Decay: 1.0s (1 o'clock)
     * Sustain: 90% (3 o'clock)
     * Release: 2.5s (3 o'clock)
   
   - ENV2 (Filter):
     * Attack: 2.0s (2:30)
     * Decay: 1.5s (1:30)
     * Sustain: 60% (1 o'clock)
     * Release: 3.0s (3 o'clock)

7. LFO
   - Waveform: Triangle
   - Rate: VERY SLOW (7 o'clock - circa 0.1Hz)
   - Amount: Moderate

8. PATCH BAY ROUTING (OPZIONALE ma consigliato)
   Patch Cable 1: LFO TRI OUT → VCO1 FM IN
   Patch Cable 2: LFO TRI OUT → FILTER 1 CUTOFF (use attenuator at 30%)
   Patch Cable 3: ENV2 OUT → VCO2 PITCH (subtle pitch drift)

9. EFFECTS
   - Delay: ON, Time = 1/4 note, Feedback = 35%, Mix = 20%
   - Use external reverb with 3-4s decay

10. PLAYING TIPS
    - Hold chords for at least 4-5 seconds
    - Use sustain pedal
    - Layer multiple notes (4-voice paraphonic)
    - Experiment with velocity for filter brightness

═══════════════════════════════════════════════════════════

Vuoi che generi anche un diagramma visuale del signal flow?
```

### Risultato:
Una guida completa con posizioni precise dei controlli e routing modulare!

---

## Esempio 3: Analizzare un Suono Esistente

### Setup Necessario:
```bash
pip install librosa --break-system-packages
```

### Conversazione con Claude:

```
Tu: [carica file kick_drum.wav]
    Analizza questo kick e dimmi come ricrearlo

Claude: Analizzerò il tuo kick drum per estrarre le caratteristiche...

[Claude esegue analyze_audio.py sul file]

═══════════════════════════════════════════════════════════
AUDIO ANALYSIS RESULTS
═══════════════════════════════════════════════════════════

File: kick_drum.wav
Duration: 0.8 seconds
Sample Rate: 44100 Hz

SPECTRAL CHARACTERISTICS:
- Brightness: 285 Hz (mean spectral centroid)
  → Very dark/bass-heavy sound ✓
- Spectral Rolloff: 520 Hz
  → 85% of energy below 520Hz
- Bandwidth: 180 Hz
  → Narrow spectrum, focused

TEMPORAL CHARACTERISTICS:
- Onset Count: 1
  → Single transient/hit
- Energy: High RMS, 22dB dynamic range
  → Strong, punchy transient

HARMONIC CONTENT:
- Harmonic Ratio: 0.82
  → Highly pitched/harmonic
- This is a TUNED KICK with strong fundamental

SUGGESTED CHARACTERISTICS:
• Very dark/bass-heavy sound
• Highly harmonic (pitched instrument likely)
• Short hit/transient
• Single strong attack

═══════════════════════════════════════════════════════════
RECREATION GUIDE
═══════════════════════════════════════════════════════════

Per ricreare questo kick su un synth, usa questi parametri:

OSCILLATOR:
- Waveform: Sine wave (for clean fundamental)
- Start Pitch: 200-300 Hz
- Pitch Envelope: 
  * Fast decay (50-80ms)
  * Drop from starting pitch to 50-60 Hz

AMPLITUDE ENVELOPE:
- Attack: 0ms (instant)
- Decay: 600-800ms (matches your sample length)
- Sustain: 0%
- Release: 0ms

FILTER:
- Type: Low Pass 24dB
- Cutoff: 800-1000 Hz
- Resonance: Low (10-20%)
- Envelope: Fast attack (5ms), decay 100ms for "click"

EFFECTS:
- Light saturation/distortion for punch
- NO reverb (keep it dry)

SYNTH RECOMMENDATIONS:
1. Moog DFAM - Perfect for this! Use VCO2 with pitch envelope
2. Vital - Use sine wave osc with pitch mod envelope
3. Any analog synth with pitch envelope capability

Vuoi che generi un preset specifico per uno di questi synth?
```

### Risultato:
Analisi dettagliata + guida per ricreare il suono!

---

## Esempio 4: Generare Pattern Ritmici

### Conversazione con Claude:

```
Tu: Voglio un pattern techno a 128 BPM per 4 battute

Claude: Genero subito un pattern techno per te!

[Claude esegue generate_rhythm.py techno 128 4]

═══════════════════════════════════════════════════════════
RHYTHM PATTERN: TECHNO (128 BPM, 4 BARS)
═══════════════════════════════════════════════════════════

Kick:
------------------------------------------------------------
Bar 1: |X...|X...|X...|X...|
Bar 2: |X...|X...|X...|X...|
Bar 3: |X...|X...|X...|X...|
Bar 4: |X...|X...|X...|X...|

Clap:
------------------------------------------------------------
Bar 1: |....|x...|....|x...|
Bar 2: |....|x...|....|x...|
Bar 3: |....|x...|....|x...|
Bar 4: |....|x...|....|x...|

Closed_HH:
------------------------------------------------------------
Bar 1: |xoxo|xoxo|xoxo|xoxo|
Bar 2: |xoxo|xoxo|xoxo|xoxo|
Bar 3: |xoxo|xoxo|xoxo|xoxo|
Bar 4: |xoxo|xoxo|xoxo|xoxo|

Open_HH:
------------------------------------------------------------
Bar 1: |....|....|....|....|
Bar 2: |....|....|....|o...|
Bar 3: |....|....|....|....|
Bar 4: |....|....|....|o...|

Legend: X = accent/loud, x = medium, o = soft, . = rest

✅ MIDI file created: pattern_techno_128bpm.mid

Puoi importare questo file MIDI nella tua DAW!
Vuoi che generi variazioni o pattern per altri generi?
```

### Risultato:
Notazione testuale + file MIDI pronto per l'uso!

---

## Esempio 5: Creare un Lead Supersaw per Trance

### Conversazione con Claude:

```
Tu: Crea un lead supersaw per trance su Serum, polifonico

Claude: Perfetto! Un supersaw classico per trance. Ecco la configurazione:

[Claude legge i reference per Serum e lead supersaw]

═══════════════════════════════════════════════════════════
PATCH: Trance Supersaw Lead
SYNTH: Serum
TYPE: Lead
VOICES: 16 polyphonic
═══════════════════════════════════════════════════════════

OSCILLATOR A:
- Wavetable: "Saw 7" (or any bright saw)
- Unison: 7 voices
- Detune: 12-15 cents
- Blend: 100% (full spread)
- Level: 100%
- Octave: 0
- Transpose: 0 semitones

OSCILLATOR B:
- Wavetable: "Saw 7" (same as Osc A)
- Unison: 7 voices
- Detune: 12-15 cents (match Osc A)
- Blend: 100%
- Level: 90%
- Octave: 0
- Transpose: +7 semitones (perfect fifth up)

SUB:
- Level: 0% (non necessario per lead)

FILTER:
- Type: MG Low 24 (Moog-style)
- Cutoff: 85% (circa 8kHz)
- Resonance: 25%
- Drive: 15% (slight saturation)
- Mix: 100%

FILTER ENVELOPE:
- Attack: 50ms (not instant, for smoothness)
- Decay: 600ms
- Sustain: 70%
- Release: 300ms

AMP ENVELOPE:
- Attack: 10ms (fast but not instant)
- Decay: 300ms
- Sustain: 85%
- Release: 400ms

LFO 1 (Vibrato):
- Shape: Sine
- Rate: 6 Hz (free-running)
- Delay: 300ms (vibrato kicks in after note start)
- Destination: Oscillator Pitch
- Amount: +/- 8 cents

MODULATION MATRIX:
1. Velocity → Filter Cutoff: +30%
2. Mod Wheel → LFO1 Amount: 0 to 100%
3. Aftertouch → Vibrato Depth: 0 to 50%

EFFECTS:
1. Chorus:
   - Mix: 25%
   - Rate: 0.5 Hz
   - Depth: 30%

2. Reverb:
   - Mix: 18%
   - Size: Medium
   - Decay: 2.5s
   - High Cut: 8kHz

3. Delay:
   - Mix: 15%
   - Time: 1/8 note (tempo synced)
   - Feedback: 25%
   - Filter: High Pass 400Hz

GLOBAL:
- Voices: 16
- Polyphony: 16
- Glide: 0ms (no portamento)
- Bend Range: +/- 2 semitones

═══════════════════════════════════════════════════════════
PERFORMANCE TIPS:
═══════════════════════════════════════════════════════════

1. Use mod wheel to control vibrato intensity during performance
2. Play in the range C3-C5 for best results
3. Hold chords for at least 2-3 seconds (let reverb/delay tail)
4. Layer with a subtle pad underneath for fuller sound
5. Use sidechain compression with kick for classic trance pumping

Vuoi che crei anche variazioni (più aggressive, più dolci, ecc.)?
```

### Risultato:
Configurazione completa per Serum con tips di performance!

---

## Riepilogo delle Capacità

### ✅ Cosa Può Fare la Skill:

1. **Programmazione Synth**
   - Parametri dettagliati per ogni synth
   - Guide step-by-step
   - Posizioni esatte dei controlli

2. **Generazione File**
   - Preset Vital (.vital)
   - Pattern MIDI (.mid)
   - Diagrammi SVG (.svg)

3. **Analisi Audio**
   - Caratteristiche spettrali
   - Contenuto armonico
   - Suggerimenti per ricreazione

4. **Supporto Modulare**
   - Routing patch completo
   - CV e gate connections
   - Patch alternative

5. **Adattamento Contestuale**
   - Per genere musicale
   - Per tipo di synth
   - Per stile di suono

### 📦 File Generati in Questa Demo:

1. ✅ **sound-design.skill** - Skill completa
2. ✅ **Dark_Techno_Bass.vital** - Preset Vital
3. ✅ **esempio_signal_flow_diagram.svg** - Diagramma routing
4. ✅ **pattern_techno_techno_128bpm.mid** - Pattern MIDI
5. ✅ **Sound_Design_Skill_Guida.md** - Guida completa
6. ✅ **Esempi_Pratici.md** - Questo documento

## Prossimi Passi

1. **Importa la skill** in Claude (file .skill)
2. **Installa le dipendenze** Python (opzionale):
   ```bash
   pip install librosa mido --break-system-packages
   ```
3. **Inizia a progettare suoni!** 🎹

Ricorda: la skill è progettata per essere conversazionale. Descrivi cosa vuoi ottenere e Claude ti guiderà attraverso l'intero processo!

**Buon sound design! 🎵🎛️**
