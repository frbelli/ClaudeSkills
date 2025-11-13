# Frequency Ranges Reference

This reference provides comprehensive frequency information for all common instruments in electronic music production, including specific ranges, EQ targets, and processing strategies.

---

## Table of Contents

1. [Universal Frequency Chart](#universal-frequency-chart)
2. [Drums](#drums)
3. [Bass & Sub-Bass](#bass--sub-bass)
4. [Synths & Keys](#synths--keys)
5. [Vocals](#vocals)
6. [Effects Processing](#effects-processing)
7. [Genre-Specific Considerations](#genre-specific-considerations)

---

## Universal Frequency Chart

### Frequency Bands and Psychoacoustic Characteristics

| Frequency Range | Name | Characteristics | Psychoacoustic Impact |
|-----------------|------|-----------------|---------------------|
| **20-40 Hz** | Sub-Sonic | Felt more than heard, requires high volume | Physical pressure, chest impact, unease, disorientation |
| **40-80 Hz** | Sub-Bass | Fundamental of bass and kick | Power, weight, foundation of groove |
| **80-300 Hz** | Low-Mid | Body of many instruments | Warmth, fullness (excess = mud/boxiness) |
| **300-1,000 Hz** | Lower Midrange | Neutral anchor, stabilizer | Balance foundation (absence = thin/unbalanced) |
| **1,000-8,000 Hz** | Upper Midrange | Most sensitive human hearing range | Presence, clarity, punch (excess = harsh/fatiguing) |
| **8,000-20,000 Hz** | Treble/Air | Detail, sparkle, sizzle | Excitement, detail (absence = dull, excess = harsh) |

### Critical Frequency Points

| Frequency | Common Issues | Musical Context |
|-----------|--------------|-----------------|
| **30-40 Hz** | Subsonic rumble, wastes headroom | Remove with HPF on most tracks |
| **60-80 Hz** | Kick fundamental, bass power | Key range for kick-bass interaction |
| **100-150 Hz** | Snare body, bass warmth | Adds weight, can create mud if excessive |
| **200-500 Hz** | "Boxiness," "mud" | Most common corrective cut range |
| **1-3 kHz** | Vocal presence, harshness | Critical for intelligibility, easily fatiguing |
| **3-6 kHz** | Attack, definition, sibilance | Adds clarity but can be piercing |
| **7-8 kHz** | Sibilance peak | Target for de-essing |
| **10-16 kHz** | "Air," sparkle | Adds openness and detail |

---

## Drums

### Kick Drum

#### Frequency Breakdown

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **30-50 Hz** | Sub content, chest impact | Boost +1 to +2 dB (808-style)<br>or Cut -2 dB (tight kicks) | Wide (Q 1.0-1.5) | HPF at 30-40 Hz to remove subsonic waste |
| **60-80 Hz** | Fundamental, "thump" | Boost +2 to +3 dB | Medium-Wide (Q 1.5-2.0) | Core power frequency |
| **80-120 Hz** | Upper fundamental, warmth | Adjust as needed | Medium (Q 2.0) | Balance with bass |
| **200-500 Hz** | Boxiness, hollow resonance | Cut -2 to -4 dB if needed | Narrow (Q 3.0-5.0) | Removes cardboard quality |
| **2-6 kHz** | Beater attack, click, definition | Boost +2 to +4 dB | Medium (Q 2.0-3.0) | Adds punch and clarity |
| **8-12 kHz** | Air, high-end detail | Optional slight boost | Wide shelf | Adds modern sheen |

#### Genre-Specific Targets

| Genre | Sub (30-50 Hz) | Fundamental (60-80 Hz) | Attack (2-6 kHz) | Character |
|-------|---------------|----------------------|-----------------|-----------|
| **Techno** | Heavy emphasis | Very present | Tight, defined | Sub-heavy, short sustain |
| **House** | Moderate | Strong | Balanced | Warm, rounded, medium sustain |
| **Trap** | Dominant (808 tuned) | Very strong | Minimal | Long sustain, IS the bass |
| **DnB/Dubstep** | Strong | Present | Heavy emphasis | Layered (attack + sub) |

#### Processing Chain Order

1. **HPF** at 30-40 Hz (12-24 dB/octave)
2. **Corrective EQ** (remove boxiness 200-500 Hz)
3. **Serial Compression** (punch: Attack 10-30ms, Ratio 4:1-8:1)
4. **Parallel Compression** (sustain: Ratio 10:1+, fast attack) - send to aux
5. **Transient Designer** (optional: +2/+4 dB attack)
6. **Timbral EQ** (boost fundamental, boost click)
7. **Saturation** (optional: harmonics and character)

---

### Snare Drum

#### Frequency Breakdown

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 50 Hz** | Remove completely | HPF | 12-24 dB/oct | Unnecessary low-end |
| **100-150 Hz** | Body, weight, power | Boost +4 to +6 dB | Q 3.0 | Adds physical presence |
| **200 Hz** | Shell resonance | +2 dB or -2 dB | Q 2.0-3.0 | Genre-dependent, often resonant |
| **400-600 Hz** | Boxiness (critical!) | Cut -9 dB (Top)<br>Cut -12 dB (Bottom) | Q 1.5 | If sounds "in a box" |
| **1-2 kHz** | Crack, definition | Adjust as needed | Q 2.0 | Adds presence |
| **5-8 kHz** | Snap, attack, brightness | Boost +3 dB | Q 3.0 | Emphasizes stick attack |
| **10+ kHz** | Air, sheen | Optional boost | Wide shelf | Modern polish |

#### Top vs Bottom Mic Considerations

**Top Mic**:
- Captures stick attack (5-8 kHz)
- Less boxiness issue
- Gate recommended (Attack 0ms, Hold 0.05ms, Release ~150ms)

**Bottom Mic**:
- Captures snare wires (3-6 kHz)
- More prone to boxiness (400-600 Hz)
- Often left **without gate** to capture ghost notes
- Blend to taste with top mic

#### Compression Parameters

| Purpose | Attack | Release | Ratio | Notes |
|---------|--------|---------|-------|-------|
| **Punch (Serial)** | 10-30 ms | 50-120 ms | 4:1 - 8:1 | Slow attack lets snap through |
| **Sustain (Parallel)** | 0-5 ms | Fast | 10:1 - 20:1 | Heavy compression, blend with dry |

**Feed-forward topology** (SSL/DBX-style) recommended for aggressive transient emphasis.

---

### Hi-Hats & Cymbals

#### Frequency Breakdown

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 200 Hz** | Remove completely | HPF | 12-24 dB/oct | No useful information |
| **200-500 Hz** | Bleed from other drums | Additional HPF if needed | 12 dB/oct | Clean up low-mid |
| **3-6 kHz** | Harshness, "honk" | Cut -2 to -4 dB if too piercing | Medium (Q 2.0-3.0) | Most problematic range |
| **6-10 kHz** | Presence, detail | Adjust as needed | Medium | Core cymbal character |
| **10-12 kHz** | Air, sparkle | Micro-boost +1 to +2 dB | Wide shelf | Adds openness (use moderately) |
| **15+ kHz** | Extreme air | Optional | Very wide shelf | Can add "digital" quality |

#### Hi-Hat Specific Processing

**Closed Hi-Hats**:
- HPF at 300-500 Hz
- Tight, controlled sound
- Transient designer: Attack +10, Sustain -10 (tight tick)

**Open Hi-Hats**:
- HPF at 200-300 Hz
- More decay needed
- Transient designer: Attack -10, Sustain +10 (longer decay)

**Electronic Hi-Hats** (Trap/Dance):
- Often need more aggressive HPF (400-500 Hz)
- Transient shaping critical for character
- Can be very bright (check 3-6 kHz for harshness)

---

### Overhead Mics & Room Mics

#### Frequency Breakdown

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 150 Hz** | Kick/bass bleed | HPF at 150-200 Hz | 12-18 dB/oct | Critical for clean overheads |
| **300-500 Hz** | Room boxiness | Cut -2 to -3 dB if small room | Medium (Q 2.0) | Common in untreated spaces |
| **5-8 kHz** | Cymbal attack | Adjust for balance | Medium | Natural cymbal presence |
| **10-12 kHz** | Air, dimension | Boost +2 to +3 dB (jazz/ambient) | Wide shelf | Adds openness |
| **Above 15 kHz** | Harshness, sizzle | LPF if needed | Gentle slope | Tame digital harshness |

#### Purpose in Mix

- **Primary function**: Stereo image and "glue" for drum kit
- **Secondary function**: Natural ambience
- **Not for**: Punch or weight (use close mics for that)

#### Processing Notes

- Focus on stereo width, not impact
- Complement close mics, don't compete
- EQ to support overall drum sound, not dominate

---

### Toms

#### Frequency Breakdown (Depends on Size)

**High Tom**:
- Fundamental: 150-250 Hz (boost +2 to +4 dB, Q 2.0)
- Attack: 3-5 kHz (boost +2 dB, Q 2.0)
- HPF: 80-100 Hz

**Mid Tom**:
- Fundamental: 100-150 Hz (boost +2 to +4 dB, Q 2.0)
- Attack: 2.5-4 kHz (boost +2 dB, Q 2.0)
- HPF: 60-80 Hz

**Floor Tom**:
- Fundamental: 60-100 Hz (boost +2 to +4 dB, Q 2.0)
- Attack: 2-3 kHz (boost +2 dB, Q 2.0)
- HPF: 40-50 Hz

**All Toms**:
- Remove boxiness: 200-400 Hz (cut -3 to -5 dB, narrow Q)
- Remove ring if needed: Narrow notch at resonant frequency

---

## Bass & Sub-Bass

### Frequency Breakdown by Type

#### Sub-Bass (Sine/808)

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 30 Hz** | Subsonic waste | HPF at 30-35 Hz | 6-12 dB/oct | Gentle slope |
| **30-60 Hz** | Pure fundamental | Boost +1 to +2 dB if needed | Wide (Q 1.0-1.5) | Core sub energy |
| **60-100 Hz** | Upper fundamental | Balance with kick | Medium (Q 2.0) | Duck with Dynamic EQ when kick hits |
| **100-300 Hz** | Harmonics (from saturation) | Check level after saturation | — | Critical for small speaker translation |
| **Above 300 Hz** | Not typical for pure sub | Roll off gently | — | Keep clean and focused |

#### Mid-Bass (Synth Bass, Reese, etc.)

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 30 Hz** | Remove | HPF at 30-35 Hz | 12 dB/oct | Clean low-end |
| **30-60 Hz** | Sub component | Moderate level | Wide | Leave room for kick |
| **60-100 Hz** | Fundamental | Boost +2 dB | Wide (Q 1.5-2.0) | Core bass power |
| **100-250 Hz** | Body, warmth, character | Boost +2 to +3 dB | Medium (Q 2.0-3.0) | Defines bass timbre |
| **200-400 Hz** | Mud zone | Cut -2 to -4 dB if muddy | Narrow (Q 3.0-5.0) | Most common problem area |
| **400-1,000 Hz** | Upper harmonics | Adjust for character | Medium | Contributes to "growl" or "grind" |
| **2-6 kHz** | Bite, presence | +1 to +2 dB for aggression | Medium-Wide | Helps bass cut through |
| **8-12 kHz** | High-end detail | Optional subtle boost | Wide shelf | Adds modern clarity |

### Critical Processing: Harmonic Saturation

**Purpose**: Generate harmonics at 100-400 Hz for small speaker translation

**Implementation**:
- Type: Tape or tube saturation (even harmonics)
- Amount: Subtle (5-15% wet, or drive until harmonics visible on analyzer)
- Placement: After corrective EQ, before dynamics

**Why it matters**: Pure sine sub (808) contains only fundamental (e.g., 40 Hz). Consumer systems (phones, laptops) can't reproduce this. Saturation adds harmonics at 150-300 Hz that ARE audible on small systems.

**Test**: If bass disappears on laptop/phone speakers → need more harmonics

### Processing Chain Order

1. **HPF** at 30-35 Hz
2. **Corrective EQ** (mud removal 200-400 Hz)
3. **Harmonic Saturation** (generate 100-400 Hz content)
4. **Compression** (light ratio 3:1-4:1, musical control)
5. **Dynamic EQ** (sidechain from kick, duck 40-60 Hz)
6. **Timbral EQ** (final boosts for character)

---

## Synths & Keys

### Synth Leads

#### Frequency Breakdown

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 80 Hz** | Remove (unless intended sub) | HPF at 80-150 Hz | 12-18 dB/oct | Clean low-end, leave room for bass |
| **100-300 Hz** | Body, warmth | Adjust as needed | Medium | Can add weight or mud |
| **300-500 Hz** | Mud zone | Cut -2 to -3 dB if needed | Medium | Common problem area |
| **1-3 kHz** | Presence, cut | Boost +2 to +4 dB | Medium-Wide (Q 1.5-2.5) | Helps lead cut through dense mix |
| **3-6 kHz** | Definition, brightness | Boost +2 to +3 dB | Medium | Adds clarity and attack |
| **8-16 kHz** | Air, sparkle | Boost +2 to +4 dB | Wide shelf | Modern, bright character |

#### Common Lead Types

**Supersaw Lead**:
- Naturally bright, full spectrum
- Often needs HPF at 150-200 Hz
- Boost 2-4 kHz for presence
- May need 3-6 kHz reduction if too harsh

**Pluck Lead**:
- Transient-heavy
- HPF at 100-150 Hz
- Boost 1-3 kHz for clarity
- Short decay often needs less EQ

**Mono Lead (Acid, etc.)**:
- Often filter-modulated (needs EQ after filter)
- HPF at 80-120 Hz
- Boost where filter sweeps
- May need de-essing if filter resonance harsh

---

### Pads & Ambient Synths

#### Frequency Breakdown

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 100 Hz** | Remove | HPF at 100-200 Hz | 12-18 dB/oct | Leave low-end for rhythm section |
| **200-500 Hz** | Warmth vs mud | Cut -3 to -5 dB often needed | Medium (Q 2.0) | Pads easily get muddy |
| **500-1,000 Hz** | Lower mid body | Adjust as needed | Medium | Balance with other instruments |
| **1-3 kHz** | Potential vocal masking | **Mid channel cut** -4 to -6 dB | Medium-Narrow (Q 2.5-3.5) | Create pocket for vocal (see M/S) |
| **3-6 kHz** | Definition | Light boost if needed | Medium-Wide | Usually gentle |
| **8-16 kHz** | Air, atmosphere | **Side channel boost** +2 to +4 dB | Wide shelf | Stereo width without masking vocal |

#### Mid/Side Processing Strategy (Critical for Pads)

**Mid Channel**:
- Cut 1-3 kHz (-4 to -6 dB) to create pocket for vocal
- Keep lower mids clean
- Focus on not competing with center elements

**Side Channel**:
- Boost high frequencies (8-16 kHz, +2 to +4 dB, wide shelf)
- Creates stereo "halo" around vocal
- HPF at 100-200 Hz for mono-compatibility

**Result**: Pad feels wide and airy but doesn't mask vocal

---

### Arpeggiators & Rhythmic Synths

#### Frequency Breakdown

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 100 Hz** | Remove | HPF at 100-200 Hz | 12-18 dB/oct | Keep rhythm section clear |
| **300-800 Hz** | Body vs mud | Often needs cut | Medium | Rhythmic elements easily get muddy |
| **1-4 kHz** | Rhythmic definition | Boost +2 to +3 dB | Medium-Wide | Emphasizes rhythmic clarity |
| **5-10 kHz** | Attack, transients | Boost +2 to +4 dB | Medium | Adds "tick" to rhythm |
| **10+ kHz** | Air | Optional boost | Wide shelf | Adds sparkle |

#### Processing Notes

- Transient designer often more useful than EQ
- Sidechain often used for rhythmic pumping
- Stereo width important (but check mono compatibility)

---

### Piano & Keys

#### Acoustic Piano

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 30 Hz** | Rumble | HPF at 30-40 Hz | 12 dB/oct | Remove rumble |
| **80-200 Hz** | Low note fundamentals | Adjust for genre | Medium | Fuller = more, cleaner = less |
| **200-500 Hz** | Warmth vs mud | Cut -2 to -3 dB if muddy | Medium | Common issue in dense mixes |
| **1-3 kHz** | Note definition | Boost +2 to +3 dB | Medium-Wide | Adds clarity |
| **3-8 kHz** | Hammer attack, brightness | Boost +2 to +4 dB | Medium | Defines character |
| **8-12 kHz** | Air, sparkle | Boost +1 to +2 dB | Wide shelf | Adds presence |

#### Electric Piano (Rhodes, Wurlitzer)

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 50 Hz** | Remove | HPF at 50-80 Hz | 12 dB/oct | Clean low-end |
| **100-250 Hz** | Body, warmth | Boost +2 to +4 dB | Medium | Core Rhodes character |
| **500-1,000 Hz** | Bell tone | Boost +2 to +3 dB | Medium-Wide | Classic sound |
| **2-5 kHz** | Presence, bark | Adjust for style | Medium | More aggressive = more boost |
| **8-12 kHz** | Air | Boost +1 to +2 dB | Wide shelf | Adds sheen |

---

## Vocals

### Lead Vocals

#### Frequency Breakdown

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 80 Hz** | Pops, rumble, proximity | HPF at 80-100 Hz | 12-18 dB/oct | Essential for clean low-end |
| **100-250 Hz** | Chest resonance, warmth | Adjust for character | Medium | More = warmer, less = cleaner |
| **300-500 Hz** | Mud zone | Cut -2 to -3 dB typically | Medium (Q 2.0-3.0) | Most common corrective cut |
| **1-3 kHz** | Presence, intelligibility | **Critical range** | — | Core vocal clarity |
| **2-4 kHz** | Presence boost | +2 to +4 dB | Medium-Wide (Q 1.5-2.5) | Helps vocal sit forward in mix |
| **5-8 kHz** | Clarity, detail | +1 to +2 dB | Medium | Adds definition |
| **7-8 kHz** | Sibilance peak | Control with de-esser | — | Harshness/lisping if excessive |
| **10-16 kHz** | Air, breath, intimacy | +2 to +4 dB | Wide shelf | Modern vocal sound |

#### De-Essing

**Target Range**: 5-12 kHz (sweep to find exact frequency)
**Typical Peak**: 7-8 kHz
- Male vocals: Often 5-8 kHz
- Female vocals: Often 7-10 kHz

**Parameters**:
- Ratio: ~8:1
- Knee: Hard (-6 dB)
- Maximum reduction: 8-10 dB (more = sounds "lispy")
- Attack: Fast enough to catch sibilance

**Strategy**: 
- Light de-esser pre-compression (optional)
- Main de-esser post-EQ
- Additional de-esser post-reverb/delay if effects amplify sibilance

#### Vocal Processing Chain Order

1. **Gain staging** (proper level for plugins)
2. **Fader automation** (macro-dynamic control)
3. **Light de-esser** (optional, if extreme sibilance)
4. **Compressor 1** (soft, leveling: Ratio 2:1-3:1, Attack 10-30ms, Release 100-200ms)
5. **Compressor 2** (fast, transient control: Ratio 4:1-6:1, Attack 1-5ms)
6. **EQ** (corrective cuts + presence boost)
7. **Saturation** (harmonics and body)
8. **De-esser** (final sibilance control)
9. **Spatial FX** (send to reverb/delay)

---

### Backing Vocals

#### Frequency Breakdown

| Range | Function | Typical Action | Q Value | Notes |
|-------|----------|---------------|---------|-------|
| **Below 100 Hz** | Remove | HPF at 100-150 Hz | 12-18 dB/oct | More aggressive than lead |
| **200-500 Hz** | Mud (more aggressive cut) | Cut -3 to -5 dB | Medium | Create more space for lead |
| **1-3 kHz** | Reduce to avoid masking lead | Cut -2 to -4 dB in **Mid** | Medium | Make room for lead vocal |
| **3-8 kHz** | Some presence okay | Light boost if needed | Medium | Less than lead vocal |
| **8-16 kHz** | Air and width | Boost in **Side** +3 to +5 dB | Wide shelf | Creates stereo halo |

#### Mid/Side Strategy for Backing Vocals

**Goal**: Wide, airy backing vocals that don't compete with centered lead

**Mid Channel**:
- More aggressive HPF (150 Hz)
- Cut 1-3 kHz (-2 to -4 dB) for lead vocal space
- Keep backing vocals recessed in center

**Side Channel**:
- Boost high frequencies (8-16 kHz, +3 to +5 dB)
- Creates width without center competition
- HPF at 200-250 Hz for mono-compatibility

---

## Effects Processing

### Reverb EQ Strategy (Abbey Road Technique)

Reverb EQ is **critical** for clarity. Reverbs expand unwanted frequencies, causing muddiness.

#### Standard Reverb Return EQ

| Range | Function | Typical Action | Slope | Notes |
|-------|----------|---------------|-------|-------|
| **Below 200 Hz** | Low-end rumble | HPF at 200-400 Hz | 12-18 dB/oct | Most important cut |
| **400-800 Hz** | Mud | Cut -2 to -4 dB | Medium (Q 2.0) | Removes boxiness from reverb |
| **3-6 kHz** | Harshness | Cut -2 to -3 dB if harsh | Medium | Depends on reverb type |
| **Above 10 kHz** | Excessive sizzle | LPF at 10-12 kHz | Gentle slope | Tames digital artifacts |

#### Reverb Type Specific EQ

**Plate Reverb** (Vocal):
- HPF at 300-400 Hz
- Cut 2-4 kHz (-2 dB) if too bright
- Naturally bright, may need LPF at 10 kHz

**Room Reverb** (Drums):
- HPF at 200-300 Hz
- Watch for 400-600 Hz mud
- Keep relatively balanced

**Hall Reverb** (Pads/Orchestral):
- HPF at 150-250 Hz
- More air acceptable (less aggressive LPF)
- Can be brighter

**Creative/Long Reverbs**:
- More aggressive HPF (400-500 Hz)
- Often need more cutting (mud accumulates with long decay)
- May need LPF at 8-10 kHz

### Delay EQ Strategy

Similar principles to reverb but often less aggressive:

| Range | Function | Typical Action | Notes |
|-------|----------|---------------|-------|
| **Below 150 Hz** | Remove | HPF at 150-250 Hz | Prevent low-end buildup |
| **200-500 Hz** | Mud | Cut -2 to -3 dB if needed | Cleaner repeats |
| **Above 10 kHz** | Tame harshness | LPF at 10-12 kHz | Softer, more analog feel |

#### Tempo-Synced Delays

Often benefit from more aggressive EQ:
- HPF at 250-400 Hz (rhythmic delays can get muddy fast)
- Cut 400-800 Hz (-2 to -4 dB)
- LPF at 8-10 kHz for "tape delay" character

---

## Genre-Specific Considerations

### Techno / Minimal

**Low-End Priority**:
- Kick and bass dominate (loudest elements)
- Sub-bass: 30-60 Hz (heavy emphasis)
- Minimize 200-500 Hz globally (very clean)

**Midrange**:
- Hi-hats: Often bright (8-12 kHz emphasis)
- Synths: Often dark/filtered (less 2-8 kHz)
- Focus on 1-3 kHz for "hypnotic" elements

**High-End**:
- Hi-hats and percussion very present
- Controlled brightness (not harsh)

### House / Deep House

**Low-End Priority**:
- Balanced kick and bass (equal importance)
- Warmer than techno (more 80-300 Hz)
- Less sub-heavy (more musical bass)

**Midrange**:
- Warmer overall (more 300-1,000 Hz)
- Vocals more present if present
- Piano/keys often featured (full range)

**High-End**:
- Smooth, not aggressive
- Air and warmth coexist

### Drum & Bass / Dubstep

**Low-End Priority**:
- Bass often LOUDEST element
- Sub-bass: 30-60 Hz (extreme emphasis)
- Bass harmonics: 80-300 Hz (very important)
- Kick: Tight and fast (less sustain)

**Midrange**:
- Often more aggressive (growling basses)
- 500-2,000 Hz can be very active
- Space for bass modulation

**High-End**:
- Very bright hi-hats
- Crispy snares (5-10 kHz emphasis)

### Trap / Hip-Hop

**Low-End Priority**:
- 808 kick IS the bass (30-80 Hz)
- Often tuned to musical key
- Long sustain (arrangement-based)

**Midrange**:
- 200-500 Hz: Often scooped
- Vocal clarity critical (2-5 kHz)
- Hi-hats dominant (very bright)

**High-End**:
- Extreme air (10-16 kHz common)
- Rolled-off 808s (< 1 kHz often)

---

## Workflow: Frequency-First Mixing Approach

### Step 1: Establish Low-End Foundation

1. **Kick alone**: Get fundamental (60-80 Hz) right
2. **Bass alone**: Get body (60-100 Hz) and harmonics (100-300 Hz) right
3. **Together**: Implement kick-bass interaction (Dynamic EQ or sidechain)
4. **Verify**: Check on multiple systems

### Step 2: Build Midrange Clarity

1. **Identify masking**: Which elements compete in 200-500 Hz and 1-3 kHz?
2. **Create pockets**: Cut competing frequencies in supporting elements
3. **Boost leads**: Only after clearing space
4. **Verify mono**: Check that clarity remains

### Step 3: Add High-End Detail

1. **Remove harshness first**: Cut 3-6 kHz where needed
2. **Add air gradually**: Boost 8-16 kHz conservatively
3. **Control sibilance**: De-ess as needed
4. **Balance**: Don't over-emphasize highs

### Step 4: Check Full Spectrum

1. **Spectrum analyzer**: Visual verification of balance
2. **Reference track**: A/B comparison at matched volume
3. **Multiple systems**: Monitors, Auratones, headphones, laptop
4. **Mono check**: Verify no phase issues or masking

---

## Critical Reminders

### Q Value Guidelines

- **Wide Q (0.5-1.5)**: Broad tonal shaping (musical, transparent)
- **Medium Q (1.5-3.0)**: Targeted adjustments (character changes)
- **Narrow Q (3.0-8.0)**: Surgical corrections (problem frequencies)

### Cut vs Boost Philosophy

**Always cut first, boost second**:
- Cutting creates space and clarity
- Boosting adds character but consumes headroom
- 1 dB cut on competing element often better than 1 dB boost on desired element

### HPF (High-Pass Filter) on Everything

Almost every track benefits from HPF:
- Removes unnecessary sub-bass content
- Frees up headroom
- Reduces masking
- Cleans up mud
- Makes mix more powerful overall

**Recommended HPF starting points**:
- Kick: 30-40 Hz
- Bass: 30-35 Hz
- Snare: 50 Hz
- Toms: 40-100 Hz (size-dependent)
- Hi-hats/Cymbals: 200-500 Hz
- Synth leads: 80-150 Hz
- Pads: 100-200 Hz
- Vocals: 80-100 Hz
- Acoustic instruments: 30-80 Hz (instrument-dependent)

### Mono-Compatibility

**Critical ranges for mono**:
- Below 100-130 Hz: Should be essentially mono
- 100-300 Hz: Careful with stereo width
- Above 300 Hz: Stereo width acceptable
- **Always HPF the Side channel** at 100-200 Hz in M/S processing

---

## Summary: Frequency Approach to Mixing

1. **Start with HPF on everything** (clean slate)
2. **Build low-end foundation** (kick + bass interaction)
3. **Create midrange pockets** (remove masking, then boost leads)
4. **Add high-end air** (after controlling harshness)
5. **EQ effects returns** (prevent reverb/delay mud)
6. **Verify on multiple systems** (translation check)
7. **Check in mono** (phase/masking verification)

Remember: **Frequency management is about creating space, not filling it**. The goal is for each element to occupy its own frequency pocket, allowing all elements to be heard clearly without conflict.

Use this reference to identify which frequencies to target for each instrument, then use your ears to fine-tune the exact frequencies and amounts needed for your specific mix.
