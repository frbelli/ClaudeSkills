# Elektron Digitone II - Complete Reference
**Source**: Digitone II User Manual OS 1.00A (October 2024)

---

## 📋 OVERVIEW

**Type**: Digital 8-voice FM Synthesizer with Subtractive Filtering  
**Manufacturer**: Elektron  
**Release**: 2024 (Digitone II)  
**Architecture**: 4-operator FM + Analog-modeled Filter + Effects

### Key Features
- **Voices**: 8-voice polyphony (distributed across 4 tracks)
- **Operators**: 4 operators per voice (Groups: C, A, B1, B2)
- **Algorithms**: 8 different routing configurations
- **Synthesis**: Frequency Modulation (FM) + Subtractive
- **Filter**: Analog-modeled multimode filter with overdrive
- **Sequencer**: 64-step sequencer with parameter locks
- **Effects**: Per-track (Chorus, Delay, Reverb, Overdrive) + Master effects
- **Integration**: Overbridge support, MIDI tracks for external gear

---

## 🎛️ SYNTHESIS ARCHITECTURE

### Signal Flow

```
┌─────────────┐
│  FM Engine  │  (4 Operators: C, A, B1, B2)
│  8 Algos    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Overdrive  │  (Per-track)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ Multimode   │  (LP/HP/BP/Notch + more)
│   Filter    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Base-Width │  (Stereo imaging)
│   Filter    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│     Amp     │  (AHDSR envelope)
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Effects   │  (Chorus, Delay, Reverb)
└─────────────┘
```

**Key Difference from Classic FM**: The Digitone II treats FM as a **complex tone generator** rather than a complete synthesizer voice. The signal then goes through a subtractive-style filter and amp section, making it more approachable than traditional FM synths.

---

## 🔢 OPERATORS

### Operator Groups

The Digitone II divides its 4 operators into 3 groups for simplified control:

| Group | Operators | Role | Ratio Range |
|-------|-----------|------|-------------|
| **C** | 1 operator | Usually Carrier | Mostly integers (0.5-16) |
| **A** | 1 operator | Carrier or Modulator | Extensive (0.25-16) |
| **B** | 2 operators (B1 + B2) | Modulators | 0.25-16 (both controlled together) |

### Operator Structure

Each operator contains:
```
┌───────────────────┐
│    OPERATOR       │
│                   │
│  ┌─────────────┐  │
│  │  Waveform   │  │ ← Sine by default, harmonics adjustable
│  │  (Sine +    │  │
│  │  Harmonics) │  │
│  └──────┬──────┘  │
│         │         │
│  ┌──────▼──────┐  │
│  │  Envelope   │  │ ← ADE or ASDE (Attack-Decay-End / Attack-Sustain-Decay-End)
│  │  (AD/ASD)   │  │
│  └──────┬──────┘  │
│         │         │
│  ┌──────▼──────┐  │
│  │  Feedback   │  │ ← Optional (adds harmonics)
│  └──────┬──────┘  │
│         │         │
│  ┌──────▼──────┐  │
│  │  Modulation │  │ ← Input from other operators
│  │    Input    │  │
│  └──────┬──────┘  │
│         │         │
│         ▼         │
│      Output       │
└───────────────────┘
```

### Operator Roles

**Carrier**: Generates the audible tone (output to X or Y)  
**Modulator**: Modulates another operator's frequency (adds harmonics)  
**Hybrid**: Can be both carrier and modulator simultaneously

---

## 🔀 ALGORITHMS (8 Total)

An **algorithm** is a routing configuration that determines how the 4 operators are connected.

### Algorithm Diagram Legend

```
┌─────────┐
│  B²     │  ← Operator B2
│  ─ ─ ─  │
│  B¹     │  ← Operator B1
│  ─────  │
│    A    │  ← Operator A
│  ─────  │
│    C    │  ← Operator C
└──┬───┬──┘
   X   Y     ← Output (two carrier outputs)
   
Line Types:
────── Filled line  = Amplitude affected by operator envelope
- - - - Dotted line = Amplitude NOT affected by envelope
```

### The 8 Algorithms

**Algorithm 1**: Series Chain
```
    B²
     │ (modulates)
    B¹
     │ (modulates)
     A
     │ (modulates)
     C
    ─┴─
    X Y
    
• Classic FM stacking
• Maximum harmonic complexity
• All operators in series
```

**Algorithm 2**: Parallel Carriers + Modulated Carrier
```
    B²        B¹
     │         │
     A    ┌────┘
     │    │
     C    │
    ─┴────┴─
    X     Y
    
• Two independent outputs
• B1 modulates A
• B2 modulates itself
• Good for crossfading timbres
```

**Algorithm 3**: Dual Modulators on Single Carrier
```
    B²   B¹
     │   │
     └─┬─┘
       A
       │
       C
      ─┴─
      X Y
      
• Both B operators modulate A
• Complex modulation
• Rich harmonics
```

**Algorithm 4**: Parallel Paths with Shared Modulator
```
    B²
     │
    ┌┴┐
    A B¹
    │ │
    C │
   ─┴─┴─
   X   Y
   
• Two carrier outputs (C and B1)
• B2 modulates both A and B1
• Independent timbres on X and Y
```

**Algorithm 5**: Parallel (All Carriers)
```
    B²  B¹  A   C
     │   │  │   │
    ─┴───┴──┴───┴─
    X           Y
    
• All operators are carriers
• No FM modulation between operators
• Additive-style synthesis
• Detuning creates thickness
```

**Algorithm 6**: Split Chain
```
    B²  B¹
     │   │
     A   C
     │   │
    ─┴───┴─
    X     Y
    
• Two independent chains
• B2→A on X output
• B1→C on Y output
• Different timbres per output
```

**Algorithm 7**: Feedback Modulator
```
    ┌─┐
    │ B²  B¹
    │  │   │
    └─→A   C
       │   │
      ─┴───┴─
      X     Y
      
• B2 has self-feedback
• B2 modulates A
• B1 modulates C
• Aggressive harmonics from feedback
```

**Algorithm 8**: Complex Routing
```
        B²
         │
    ┌────┼────┐
    A    B¹   C
    │    │    │
   ─┴────┴────┴─
   X          Y
   
• B2 modulates all three operators
• Most complex routing
• Maximum modulation possibilities
• Three carrier outputs
```

---

## 🎚️ FM PARAMETERS (SYN PAGE 1)

### RATIO C
**Range**: 0.5 - 16.0 (mostly integers)  
**Function**: Sets the frequency ratio for operator C  
**Details**: Limited mostly to integers since C typically carries the base note

### RATIO A
**Range**: 0.25 - 16.0 (extensive)  
**Function**: Sets the frequency ratio for operator A  
**Details**: More extensive range for inharmonic relationships

### RATIO B (B1 and B2)
**Range**: 0.25 - 16.0 (dual control)  
**Function**: Controls both B1 and B2 ratios simultaneously  
**Behavior**: 
- B2 increases from 0.25 to 16.0 first
- When B2 reaches 16.0, it resets to 0.25 and B1 increments
- Like a clock: B2 is the "minute hand", B1 is the "hour hand"
- Continues until both reach maximum (16.0)

**Example sequence**:
```
Value 0:   B1=0.25, B2=0.25
Value 32:  B1=0.25, B2=8.00
Value 64:  B1=0.25, B2=16.00  ← B2 maxed, B1 increments
Value 65:  B1=0.50, B2=0.25   ← B2 resets
Value 96:  B1=0.50, B2=16.00
Value 97:  B1=0.75, B2=0.25
...
Value 127: B1=16.00, B2=16.00 ← Both maxed
```

### HARM (Harmonics)
**Range**: -26.00 to +26.00 (bipolar)  
**Function**: Adds upper partials to operators  
**Behavior**:
- **Negative values** (-26 to 0): Change operator C harmonics
- **Positive values** (0 to +26): Change operators A and B1 harmonics
- Intermediate values interpolate between harmonics (wavetable-like)

**Harmonic Series**:
```
-26 ──────────────── 0 ──────────────── +26
     Operator C         Operators A, B1
     
Series progression:
1. Sine (pure)
2. Saw reduction
3. Odd/Even mix
4. Square (odd partials)
5. Square reduction
6. Bell tones
7. Saw (all partials)
```

**Additive Synthesis Method**:
```
Sine:       1st partial only
            ▂

Saw:        All partials, decreasing amplitude
            ▂▁▁▁▁▁

Square:     Odd partials only
            ▂ ▁ ▁ ▁

Bell:       Custom partial selection
            ▂  ▁▁  ▁
```

### DTUN (Detune)
**Range**: -64 to +64  
**Function**: Detunes operators A and B2  
**Behavior**:
- Values 0-64: Subtle detuning (chorus effect)
- Values >64: Heavy detuning (creates dissonance)
- Adds movement and width to sounds

### FDBK (Feedback)
**Range**: 0-127  
**Function**: Self-modulation amount for operator with feedback  
**Effect**: 
- Adds harmonics and brightness
- Creates aggressive, sharp timbres
- Operator with feedback shown in algorithm diagram (feedback loop symbol)
- Can turn sine wave into saw/square-like waveforms

### MIX
**Range**: -64 to +64 (bipolar)  
**Function**: Crossfades between X and Y outputs  
**Behavior**:
- **-64**: Only X output (from first carrier)
- **0**: 50/50 mix of X and Y
- **+64**: Only Y output (from second carrier)
- Allows morphing between two different timbres created by different operators

---

## 📊 OPERATOR ENVELOPES (SYN PAGE 2)

### Envelope Groups

**Envelope A**: Controls operator A modulation  
**Envelope B**: Controls both B1 and B2 modulation (macro-mapped)

### Envelope Types

**ADE (Triggered)**:
```
Level
  │     ╱╲
  │    ╱  ╲____
  │   ╱         ╲___ End Level
  │  ╱               ╲___
  └──┴────┴────┴────┴────── Time
     Atk  Dec       
     
Note On only (ignores Note Off)
```

**ASDE (Gated)**:
```
Level
  │     ╱─────╲
  │    ╱       ╲____
  │   ╱   Sus        ╲___ End Level
  │  ╱                   ╲___
  └──┴────┴────┴────┴────┴── Time
     Atk       Dec    Rel
     │◄──Note On──►│◄─Note Off─►│
     
Responds to Note On and Note Off
```

### Parameters

**ATCK (Attack)**
- Time to reach peak modulation level
- Range: 0 - 127 (0ms - several seconds)

**DEC (Decay)**
- Time to decay from peak to sustain/end level
- Range: 0 - 127

**END** (End Level)
- Final modulation level
- Range: 0 - 127
- **Key difference from standard AD**: Doesn't go to zero
- Allows sustained modulation after initial pluck

**LEV (Level)**
- Maximum modulation amount
- Range: 0 - 127
- Acts as sustain level in gated mode

**ATRG/BTRG** (Trigger Mode)
- ON: ADE mode (triggered)
- OFF: ASDE mode (gated)

**ARST/BRST** (Reset on Retrigger)
- ON: Envelope resets to zero when retriggered
- OFF: Envelope continues from current position

```
Reset ON:
  ╱╲     ╱╲
 ╱  ╲   ╱  ╲
▼   ▼  ▼   ▼
Trig1  Trig2

Reset OFF:
  ╱╲   ╱──╲
 ╱  ╲ ╱    ╲
▼   ▼▼     ▼
Trig1 Trig2
```

### B Level Macro Mapping

The **LEV B** parameter controls both B1 and B2 levels:

```
Level
127 ┤         ╱────── B2
    │       ╱
    │     ╱
64  │   ╱       B1 ───╲
    │ ╱                 ╲
0   ┴─────┬──────┬──────┬─── Parameter Value
         43     64     85
```

- Values 0-43: Only B1 increases (B2 = 0)
- Values 43-85: B1 maxes out, B2 starts increasing  
- Values 85-127: B2 continues to max

---

## 🔊 FILTER SECTION

### Filter Types (Multi-Mode)

The Digitone II has multiple filter machines available:

**MULTI-MODE** (Default):
- LP (Low Pass): 12dB/24dB slopes
- HP (High Pass): 12dB/24dB slopes
- BP (Band Pass)
- Notch
- Peak

**LOWPASS 4**:
- Classic 4-pole low pass
- Analog-modeled Moog-style

**LEGACY LP/HP**:
- Original Digitone filter (from Digitone I)
- Character from first generation

**COMB-** and **COMB+**:
- Comb filtering
- Creates metallic, resonant sounds

**EQUALIZER**:
- Parametric EQ
- Tone shaping

### Filter Parameters

**FREQ (Frequency/Cutoff)**
- Filter cutoff frequency
- Range: 0-127
- 20 Hz - 20 kHz (approximately)

**RES (Resonance)**
- Emphasis at cutoff frequency
- Range: 0-127
- Self-oscillates at maximum

**ENVD (Envelope Depth)**
- Amount of filter envelope modulation
- Bipolar: -64 to +64
- Negative: Inverted envelope

**FENV (Filter Envelope)**: ADSR
- Attack, Decay, Sustain, Release
- Modulates filter cutoff
- Independent from operator envelopes

**TRCK (Key Tracking)**
- Makes filter follow keyboard pitch
- 0%: Static filter (same cutoff for all notes)
- 100%: Full tracking (filter moves with pitch)
- Useful for maintaining brightness across octaves

**BASE and WIDTH**:
- **BASE**: Starting frequency for tracking
- **WIDTH**: Stereo width of filter
- Create stereo movement

---

## 💥 OVERDRIVE

**Type**: Analog-modeled saturation  
**Position**: Between FM engine and filter  
**Range**: 0-127

**Effect**:
- Adds harmonics and warmth
- Softens digital FM harshness
- Creates analog character
- Can be subtle (10-30%) or aggressive (70-100%)

**Routing Options**:
- Pre-filter (affects filter input)
- Post-filter (clean filter response)

---

## 🎵 EFFECTS

### Per-Track Effects

**CHORUS**:
- Adds shimmer and width
- Parameters: Depth, Speed, HPF, Width
- Creates detuned doubling effect

**DELAY**:
- Tempo-synced or free
- Parameters: Time, Feedback, HPF, LPF
- Pingpong mode available
- Can send to reverb

**REVERB**:
- Algorithmic reverb
- Parameters: Pre-delay, Decay, Shelving, HPF, LPF
- Shared between all tracks

### Master Effects

**COMPRESSOR**:
- Master bus compression
- Glues mix together
- Sidechain options

---

## 🎹 PERFORMANCE FEATURES

### Parameter Locks

**Most powerful feature**: Lock any parameter per step
- Create evolving sounds within a pattern
- Modulate filter cutoff per note
- Change operator ratios per trig
- Dynamic timbral shifts

**Example Use Cases**:
- Filter sweep: Lock increasing cutoff values
- Harmonic evolution: Lock different HARM values per step
- Ratio modulation: Different FM tones per note

### Trig Conditions

- Probability-based triggering
- Fill patterns
- Conditional playback
- Adds variation to patterns

### Micro-Timing

- Per-step timing adjustment
- ±23 microsteps
- Create swing, shuffle, humanization

### Pattern Chaining

- Link patterns for long arrangements
- Song mode available
- Create full tracks on device

---

## 🎛️ SOUND DESIGN STRATEGIES

### Creating Different Sound Types

**Bass**:
- Algorithm 1 or 2 (series for punch)
- Low ratio on operator C (1.0 or 0.5)
- Modulator with envelope for movement
- LP filter, high resonance
- Overdrive for warmth

**Lead**:
- Algorithm 3 or 7 (complex modulation)
- High ratio on modulators (3-7 for brightness)
- Feedback for aggression
- BP filter for presence
- Delay and chorus for width

**Pad**:
- Algorithm 5 (parallel operators)
- Slight detuning (DTUN 10-30)
- Slow envelope attacks
- LP filter, gentle resonance
- Heavy chorus and reverb

**Percussion**:
- Algorithm 1 (series)
- Fast envelopes (all zero decay)
- Pitch envelope on operator (ENVD high)
- HP or BP filter
- No reverb (keep dry)

**Keys/Bells**:
- Algorithm 2 or 4
- Integer ratios (1, 2, 3, 4, 5)
- Fast attack, medium decay
- LP filter, moderate resonance
- Subtle chorus

### FM Ratio Guidelines

**Harmonic Sounds** (Musical):
- Use integer ratios: 1, 2, 3, 4, 5, 6, 7, 8
- Creates harmonically related overtones
- Sounds musical and tonal

**Inharmonic Sounds** (Metallic):
- Use decimal ratios: 1.37, 2.51, 5.83
- Creates clangorous, bell-like tones
- Good for percussion and effects

**Classic Waveforms**:
- Saw wave: Ratio 1:1 (carrier:modulator)
- Square wave: Ratio 1:2
- Triangle-ish: Ratio 1:3

### Modulation Amount Guidelines

**Subtle Modulation** (LEV 0-40):
- Slight harmonic enrichment
- Adds warmth without changing character
- Good for realistic instruments

**Medium Modulation** (LEV 40-80):
- Clear FM character
- Adds complexity and movement
- Sweet spot for most FM sounds

**Heavy Modulation** (LEV 80-127):
- Aggressive, harsh timbres
- Metallic, digital character
- Good for aggressive bass and leads

---

## ⚠️ LIMITATIONS AND WORKAROUNDS

### Limitations

1. **4 Operators Only**
   - Less complex than 6-op FM synths (DX7)
   - Workaround: Use parameter locks for evolving timbres

2. **No Built-in Keyboard**
   - Requires external MIDI controller
   - Workaround: Step sequencer is very powerful

3. **Menu Diving**
   - Some parameters require menu navigation
   - Workaround: Learn shortcuts, use Overbridge

4. **FM Can Be Harsh**
   - Digital FM can sound cold
   - Workaround: Use overdrive, filter carefully, add effects

5. **Shared Reverb**
   - One reverb for all tracks
   - Workaround: Use external reverb or freeze/render

### Pro Tips

1. **Start Simple**: Begin with 2 operators, add complexity
2. **Use the Filter**: Tame harsh FM timbres with LP filter
3. **Parameter Locks**: Make static sounds evolve
4. **Save Often**: FM sounds can be hard to recreate
5. **Reference Sounds**: Study factory presets
6. **Backup**: Export patterns and projects regularly

---

## 📚 SPECIFICATIONS

**Audio**:
- Sample Rate: 48 kHz
- Bit Depth: 24-bit
- Frequency Response: 20 Hz - 20 kHz
- Dynamic Range: >100 dB
- THD+N: <0.002%

**Connectivity**:
- Audio Output: 2x 6.35mm balanced TRS
- Audio Input: 2x 6.35mm balanced TRS
- MIDI: In, Out, Thru (5-pin DIN)
- USB: USB-C (MIDI + Overbridge)
- Headphones: 6.35mm stereo

**Physical**:
- Dimensions: 34 x 18.5 x 6.3 cm
- Weight: ~2 kg
- Build: Metal chassis, rubber encoders

**Power**:
- DC 12V 2.5A
- Power consumption: ~15W

---

## 🎓 LEARNING PATH

### Beginner
1. Learn basic FM concepts (carrier, modulator, ratio)
2. Start with Algorithm 1 (simplest)
3. Experiment with single operator sounds
4. Add one modulator at a time
5. Use factory presets as templates

### Intermediate
1. Understand all 8 algorithms
2. Learn operator envelope shaping
3. Master parameter locks
4. Create full patterns with variation
5. Integrate with DAW via Overbridge

### Advanced
1. Design complex timbres from scratch
2. Use multiple algorithms per track
3. Create evolving soundscapes with locks
4. Perform live with pattern chains
5. Integrate with modular systems

---

## 🔗 RESOURCES

**Official**:
- Elektron Website: elektron.se
- User Manual: (Included PDF)
- Elektron Forum: elektron.se/forums
- Video Tutorials: Elektron YouTube channel

**Community**:
- Elektronauts Forum
- Reddit: r/Elektron
- Facebook: Elektron User Groups

**Third-Party**:
- Sound packs and presets
- Video tutorials (YouTube)
- Online courses (Skillshare, Udemy)

---

## 📝 NOTES

**Document Version**: 1.0  
**Based on**: Digitone II User Manual OS 1.00A (October 2024)  
**Last Updated**: October 2024  
**Author**: Sound Design Skill Reference Database

**Changes from Digitone I**:
- Added machines (Wavetone, Swarmer, FM Drum)
- Expanded filter options
- Improved sequencer features
- Better MIDI implementation
- Overbridge 2.0 support

---

**END OF DIGITONE II REFERENCE**

This document is designed to be read alongside the official manual for complete understanding. All information is derived from official Elektron documentation.
