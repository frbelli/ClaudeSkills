# Sound Design Skill - Official Nomenclature Reference

**Version**: 1.0  
**Last Updated**: October 28, 2025  
**Purpose**: Ensure rigorous accuracy in patch documentation by using official manufacturer terminology

---

## 📋 OVERVIEW

This document provides the **official nomenclature** for all supported synthesizers. When creating patch documentation, **ALL control names, patch points, and parameter names MUST match the official manuals exactly**.

This ensures:
- ✅ Accuracy and usability for real hardware/software users
- ✅ Consistency across all patch documentation
- ✅ Professional credibility of the sound-design skill
- ✅ No confusion about control names

---

## 🎹 SUPPORTED SYNTHESIZERS

### 1. Elektron Digitone II
**Reference**: `/mnt/skills/user/sound-design/references/synths/Elektron-Digitone-II-Complete-Reference.md`  
**Manual Version**: OS 1.00A (October 2024)

#### Nomenclature Rules
- **Operators**: OP A, OP B, OP C, OP D (not "VCO" or "Oscillator")
- **Parameters**: Use EXACT names from manual (e.g., "Harmonics", not "Harm")
- **Effects**: Use full names (e.g., "OVERDRIVE", not "OD")
- **Algorithms**: Always specify by number (Algorithm 1-8)

#### Key Terms
- **Tracks**: TRACK 1-4 (not "Channel")
- **Pages**: [TRIG], [SRC], [FLTR], [AMP], [LFO]
- **Sound Locks**: TRIG + Parameter (not "P-Lock")
- **Sequencer**: PATTERN, CHAIN, SONG
- **Filter Types**: LP12, LP24, HP12, HP24, BP12, BP24, etc.

---

### 2. Moog Matriarch
**Reference**: `/mnt/skills/user/sound-design/references/synths/Moog-Matriarch-Reference-Guide.md`  
**Manual Version**: Rev. 2020

#### Nomenclature Rules
- **Oscillators**: VCO 1, VCO 2, VCO 3, VCO 4 (not "Osc")
- **Voice Modes**: MONOPHONIC, PARAPHONIC (4-note)
- **Filter**: Always specify mode (LP/HP/BP/Series/Parallel)
- **Envelopes**: FILTER ENV, AMP ENV (not "EG1", "EG2")

#### Front Panel Controls
**Oscillator Section**:
- OCTAVE (32', 16', 8', 4', 2')
- WAVEFORM (Saw/Square/Triangle/Narrow Pulse)
- FREQUENCY (±7 semitones)
- SYNC (Off/On)
- FM AMOUNT (0-10)
- PW / PWM (0-10)
- MIXER LEVEL (0-10)

**Filter Section**:
- CUTOFF (20 Hz - 20 kHz)
- RESONANCE (0-10)
- ENVELOPE AMT (-10 to +10, bipolar)
- MODE (LP/HP/BP/Series/Parallel)
- KEYBOARD TRACK (Off/50%/100%)
- STEREO OFFSET (0-10)

**Modulation Section**:
- LFO: RATE, SHAPE, DEPTH, SYNC
- ENVELOPE: ATTACK, DECAY, SUSTAIN, RELEASE

**Delay Section**:
- TIME L / R (35 ms - 850 ms)
- FEEDBACK L / R (0-10)
- SYNC (OFF/ON)
- MIX (0-10)
- PING-PONG (OFF/ON)

#### Patch Points (Patchbay)
**Audio Outputs**:
- VCO 1-4 WAVE OUT
- VCO MIX OUT
- MIX OUT
- POST FILTER OUT L/R
- VCA OUT
- DELAY OUT L/R

**CV Inputs**:
- VCO 1-4 PITCH IN (1V/Oct)
- CUTOFF CV IN L/R
- RESONANCE CV IN
- VCA CV IN
- DELAY TIME CV IN L/R
- DELAY FB CV IN L/R

**CV Outputs**:
- LFO OUT
- FILTER ENV OUT
- AMP ENV OUT
- S&H OUT

**Gate/Trigger**:
- GATE IN
- LFO SYNC IN
- ENV GATE IN

---

### 3. Make Noise 0-Coast
**Reference**: `/mnt/skills/user/sound-design/references/synths/Make-Noise-0-Coast-Complete Reference.md`  
**Manual Version**: Rev. 2018 (Reference Version 2.0)

#### ⚠️ CRITICAL NOMENCLATURE RULES

**The 0-Coast uses VERY specific terminology. Follow the manual EXACTLY:**

#### Front Panel Controls (Knobs)
| Official Name | Never Call It | Notes |
|---------------|---------------|-------|
| **OSC FREQ** | "Frequency", "Pitch" | Master oscillator frequency |
| **FINE** | "Fine Tune" | Fine tuning ±1 octave |
| **OVERTONE** | "Harmonics", "Timbre" | Harmonic control knob |
| **MULTIPLY** | "Wavefold", "Fold" | Wavefolding depth knob |
| **DYNAMICS** | "VCA", "Level", "Volume" | Dynamics control knob |
| **CONTOUR ATTACK** | "Attack" alone | Attack time of Contour |
| **CONTOUR DECAY** | "Decay" alone | Decay time of Contour |
| **SLOPE RISE** | "Attack", "Rise Time" alone | Rise time of Slope |
| **SLOPE FALL** | "Decay", "Fall Time" alone | Fall time of Slope |
| **BALANCE** | "Mix", "Crossfade" | Mixer control |
| **TEMPO** | "Clock Rate" | Internal clock tempo |
| **VOLUME** | "Output Level" | Final output volume |

#### Front Panel Buttons
- **CYCLE** (for SLOPE) - Enables looping
- **PROG** - Enters Program Pages

#### Patch Points - Audio (OUT = Output)
| Official Name | Type | Never Call It |
|---------------|------|---------------|
| **OSC SINE OUT** | Audio Out | "Sine Wave Out", "Sine Output" |
| **OSC SQR OUT** | Audio Out | "Square Out", "Square Wave" |
| **MULTIPLY OUT** | Audio Out | "Wavefolder Out", "Fold Out" |
| **MULTIPLY IN** | Audio In | "Wavefolder In", "Fold In" |
| **DYNAMICS IN** | Audio In | "VCA In", "Amp In" |
| **LINE OUT** | Audio Out | "Output", "Main Out" |
| **EXT AUDIO IN** | Audio In | "External In", "Audio In" |

#### Patch Points - Control Voltage (CV)
| Official Name | Type | Direction | Never Call It |
|---------------|------|-----------|---------------|
| **1 V/OCT IN** | CV In | Input | "Pitch In", "V/Oct" |
| **FM IN (LIN)** | CV In | Input | "FM", "FM Input", "Linear FM" |
| **OVERTONE CV IN** | CV In | Input | "Harmonic CV", "Timbre CV" |
| **MULTIPLY CV IN** | CV In | Input | "Wavefold CV", "Fold CV" |
| **DYNAMICS CV IN** | CV In | Input | "VCA CV", "Amp CV" |
| **RISE CV IN** | CV In | Input | "Rise Mod", "Attack CV" |
| **FALL CV IN** | CV In | Input | "Fall Mod", "Decay CV" |
| **SLOPE IN** | Gate In | Input | "Slope Trigger", "Slope Gate" |
| **CONTOUR IN** | Gate In | Input | "Contour Trigger", "Contour Gate" |
| **TEMPO IN** | CV In | Input | "Clock In", "Tempo CV" |
| **SLOPE OUT** | CV Out | Output | "Slope CV", "Envelope Out" |
| **CONTOUR OUT** | CV Out | Output | "Contour CV", "AD Out" |
| **EOC OUT** | Gate Out | Output | "End of Cycle", "EOC" |
| **GATE OUT** | Gate Out | Output | "Gate Output", "MIDI Gate" |
| **CLOCK OUT** | Gate Out | Output | "Clock Output", "Tempo Out" |
| **MOD OUT** | CV Out | Output | "Mod Wheel", "Modulation" |
| **VEL OUT** | CV Out | Output | "Velocity Out", "Velocity CV" |

#### Sections (Modules)
Official names from manual:
- **OSCILLATOR** (not "VCO" or "OSC section")
- **OVERTONE** (section, not "harmonic section")
- **MULTIPLY** (section, not "wavefolder")
- **DYNAMICS** (not "VCA" or "Low-Pass Gate" alone - it's both)
- **CONTOUR** (not "Envelope" or "EG")
- **SLOPE** (not "Function Generator" or "LFO")
- **BALANCE** (mixer section)
- **TEMPO** (internal clock)

#### Special Terminology
- **"No-Coast"** synthesis (not "West-Coast" alone)
- **"Krell Patch"** (generative self-triggering patch)
- **"Drone Mode"** (DYNAMICS fully open, no gate)
- **"Normalized"** (default internal routing)
- **"Breaking normalization"** (inserting patch cable)

#### Voltage Ranges (CRITICAL for accuracy)
- **Audio**: ±5 V
- **Control Voltage (CV)**: ±5 V (bipolar)
- **Envelope/Gate**: 0 to +8 V (unipolar)
- **1 V/Oct**: 0 to +8 V
- **Clock/Trigger**: 0 to +8 V

---

## 📝 PATCH DOCUMENTATION TEMPLATE

When creating patch documentation, always follow this structure:

### 1. Header Information
```markdown
# [Synth Name] - "[Patch Name]"

**Synth**: [Official model name]
**Genre**: [Genre]
**Style**: [Artist/Style reference]
**Character**: [Sound description]

**Source Reference**: [Path to official manual reference]
**Reference Version**: [Manual version number]
```

### 2. Control Settings
Use EXACT names from manuals:

```markdown
## [SECTION NAME - Official]

### [Control Name - Official]
**Front Panel**:
- **[PARAMETER NAME]**: [Value/Setting]
- **[PARAMETER NAME]**: [Value/Setting]

**Character**: [Description]
```

### 3. Patch Points
Use EXACT patch point names:

```markdown
## PATCHBAY ROUTING

### Essential Patches
1. **[OFFICIAL OUT NAME] → [OFFICIAL IN NAME]**
   *Description of what this does*
```

---

## ✅ QUALITY CHECKLIST

Before publishing any patch, verify:

- [ ] All control names match the official manual EXACTLY
- [ ] All patch points use official nomenclature
- [ ] Section names match official terminology
- [ ] Parameter ranges are accurate (check reference)
- [ ] Voltage ranges are specified correctly
- [ ] No invented or shortened names
- [ ] Cross-referenced with official reference document
- [ ] Tested against manual (if possible)

---

## 🚫 COMMON MISTAKES TO AVOID

### ❌ WRONG
```markdown
## VCO 1 (0-Coast)
- Pitch: 5/10
- Harmonic CV → Filter

## Oscillator (Matriarch)  
- Osc 1 Frequency: +3 cents
```

### ✅ CORRECT
```markdown
## OSCILLATOR (0-Coast)
- OSC FREQ: 5/10
- OVERTONE CV IN ← SLOPE OUT

## VCO 1 (Matriarch)
- FREQUENCY: +3 cents (±7 semitones range)
```

---

## 🔄 UPDATE PROCEDURE

When a synth reference is updated:

1. Extract new archive to `/mnt/skills/user/sound-design/`
2. Read the updated reference carefully
3. Update this nomenclature guide if needed
4. Review existing patches for nomenclature accuracy
5. Update any patches that use outdated terminology
6. Document changes in patch version history

---

## 📚 REFERENCE DOCUMENTS

All nomenclature is derived from:

1. **Elektron Digitone II**: `/mnt/skills/user/sound-design/references/synths/Elektron-Digitone-II-Complete-Reference.md`
2. **Moog Matriarch**: `/mnt/skills/user/sound-design/references/synths/Moog-Matriarch-Reference-Guide.md`
3. **Make Noise 0-Coast**: `/mnt/skills/user/sound-design/references/synths/Make-Noise-0-Coast-Complete Reference.md`

**Always consult these references BEFORE creating any patch documentation.**

---

## 🎯 PHILOSOPHY

**"Use the language of the instrument, not our interpretation of it."**

Manufacturers spend years perfecting their terminology. Users expect patch documentation to match their hardware/software. By using official nomenclature rigorously, we ensure:

1. **Usability** - Users can implement patches without confusion
2. **Professionalism** - Documentation reflects industry standards
3. **Accuracy** - No ambiguity about which control to use
4. **Credibility** - Skill is taken seriously by professionals
5. **Learning** - Users learn correct terminology

---

## 📊 NOMENCLATURE PRIORITY

When in doubt, follow this priority:

1. **Official Manual** (always first source)
2. **Front Panel Silkscreen** (physical labels on hardware)
3. **Software GUI** (for software synths)
4. **Manufacturer Website** (official specifications)
5. **Community Consensus** (only if no official source)

**NEVER invent your own names or use shortened versions without checking the manual first.**

---

**Last Updated**: October 28, 2025  
**Maintained by**: Sound Design Skill  
**Version**: 1.0

**CRITICAL**: This document MUST be consulted before creating ANY new patch documentation.
