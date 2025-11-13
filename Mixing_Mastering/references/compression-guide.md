# Compression Guide Reference

This reference provides comprehensive compression and dynamics processing techniques for all instruments in electronic music production, including specific parameters, strategies, and advanced techniques.

---

## Table of Contents

1. [Compression Fundamentals](#compression-fundamentals)
2. [Drums Compression](#drums-compression)
3. [Bass Compression](#bass-compression)
4. [Vocal Compression](#vocal-compression)
5. [Instrument Compression](#instrument-compression)
6. [Advanced Techniques](#advanced-techniques)
7. [Mix Bus Compression](#mix-bus-compression)
8. [Genre-Specific Approaches](#genre-specific-approaches)

---

## Compression Fundamentals

### What Compression Does

Compression **reduces dynamic range** - the difference between the loudest and quietest parts of a signal.

**Primary functions**:
1. **Control inconsistent levels** - Make performances sit more solidly in mix
2. **Shape transients** - Emphasize or de-emphasize attack
3. **Add sustain** - Bring up quiet, decaying tails
4. **Add character** - Many compressors (especially analog emulations) add sonic color

### Core Parameters

| Parameter | Function | Impact on Sound |
|-----------|----------|-----------------|
| **Threshold** | Level (in dB) above which compression begins | Lower = more compression, Higher = only peaks compressed |
| **Ratio** | Amount of gain reduction (e.g., 4:1 = for every 4 dB over threshold, only 1 dB passes) | Low (2:1) = gentle, High (10:1+) = aggressive |
| **Attack** | Time (ms) compressor takes to reach full compression after signal exceeds threshold | Slow = transient passes (punch), Fast = clamps transient (smooth) |
| **Release** | Time compressor takes to stop compressing after signal falls below threshold | Too fast = pumping, Too slow = acts on next note |
| **Knee** | How gradually compression engages around threshold | Hard = immediate (precise), Soft = gradual (musical) |
| **Makeup Gain** | Compensates for volume loss from compression | Match pre/post compression levels for true comparison |

### Attack Time Philosophy

**Slow Attack (10-30 ms)**:
- Transient passes through uncompressed
- Compression acts on body/sustain
- Result: Emphasized punch, controlled sustain
- Use for: Kick, snare, percussive sounds

**Fast Attack (0-5 ms)**:
- Transient is compressed immediately
- Entire signal reduced
- Result: Smoothed transient, more even sound
- Use for: Sustaining instruments, leveling vocals

**Medium Attack (5-10 ms)**:
- Balanced approach
- Some transient emphasis with body control
- Use for: General-purpose compression

### Release Time Philosophy

**Release should match musical timing**:
- Too fast: Pumping/breathing artifacts
- Too slow: Compression doesn't reset before next note
- Sweet spot: Often 1/4 note or 1/8 note at song tempo

**Formula**: `Release (ms) = (60,000 / BPM) / subdivision`

Examples at 120 BPM:
- 1/4 note: 500 ms
- 1/8 note: 250 ms
- 1/16 note: 125 ms

Start with these values, then adjust by ear.

### Ratio Guidelines

| Ratio | Character | Use Cases |
|-------|-----------|-----------|
| **1.5:1 - 2:1** | Very gentle, transparent | Mix bus, subtle leveling |
| **2:1 - 4:1** | Moderate, musical | General vocal compression, buses |
| **4:1 - 8:1** | Aggressive, controlling | Punch emphasis (drums), dynamic vocals |
| **8:1 - 20:1** | Very aggressive, limiting | Parallel compression, heavy control |
| **∞:1 (Limiting)** | Absolute ceiling | Peak limiting, safety limiting |

### Knee Types

**Hard Knee**:
- Compression engages immediately at threshold
- Precise, surgical control
- Best for: Percussive sources, transient control, when you want compression to be "tight"

**Soft Knee**:
- Compression engages gradually around threshold
- More musical, transparent
- Best for: Vocals, bass, mix bus, whenever transparency is priority

**Rule of thumb**: Hard knee for drums, soft knee for everything else.

---

## Drums Compression

### Kick Drum

#### Serial Compression (Punch Emphasis)

**Goal**: Let transient pass, control sustain

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Attack** | 10-30 ms | Slow enough for beater click to pass through |
| **Release** | 50-120 ms | Tempo-synced, resets before next hit |
| **Ratio** | 4:1 - 8:1 | Moderate-aggressive control |
| **Threshold** | Set for 3-5 dB reduction | Enough control without over-compression |
| **Knee** | Hard | Precise transient control |

**Troubleshooting**:
- Attack not punching through? → Slower attack
- Kick "pumps" unnaturally? → Faster release

**Verification**: Mute bass track. If kick alone doesn't define rhythmic energy, either sustain too short or too much attenuation around 60-100 Hz.

#### Parallel Compression (Sustain/Density)

**Goal**: Add body and sustain without sacrificing transient quality

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Attack** | 0-5 ms (Fast or zero) | Compress entire signal heavily |
| **Release** | Fast (50-100 ms) | Aggressive compression, quick reset |
| **Ratio** | 10:1 - 20:1 | Extreme compression (parallel blend makes it work) |
| **Threshold** | Low (heavy compression) | Squash the signal |
| **Blend** | To taste (usually 20-40% wet) | Mix compressed with dry |

**Critical technique**: Insert **HPF at 50-60 Hz BEFORE parallel compressor** to prevent rumble buildup. This keeps punch clean while adding sustain.

**Result**: More sustain, transient intact.

#### Processing Chain

1. **Serial compressor** (insert) - Punch emphasis
2. **Parallel compressor** (send to aux) - Sustain/density
3. **Blend parallel** to taste

---

### Snare Drum

#### Serial Compression (Punch)

**Goal**: Emphasize snap/crack, control body

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Attack** | 10-30 ms | Slow enough for stick attack to pass |
| **Release** | 50-120 ms | Tempo-matched |
| **Ratio** | 4:1 - 8:1 | Moderate-aggressive |
| **Threshold** | Set for 3-5 dB reduction | Consistent snap |
| **Knee** | Hard | Precise snap control |

**Feed-forward topology** (SSL/DBX-style) recommended for weak dynamics:
- These compressors "overshoot" the initial transient
- Then work aggressively on body
- Result: Enhanced punch on naturally weak snares

#### Parallel Compression (Sustain)

**Goal**: Add density and ring without losing snap

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Attack** | 0-5 ms | Compress entire hit |
| **Release** | Fast (50-100 ms) | Quick reset |
| **Ratio** | 10:1 - 20:1 | Extreme parallel compression |
| **Blend** | 20-50% wet | Add to taste |

**Advanced technique** (Rock/Metal): Add **parallel distortion bus**
- Route snare to aux with heavy saturation/distortion
- 1176 "all buttons in" mode
- HPF at ~120 Hz before distortion
- Blend subtly for aggression

#### Gating

**Purpose**: Remove ring and bleed (especially hi-hats)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Attack** | 0 ms | Instant open |
| **Hold** | 0.05 ms | Very short |
| **Release** | ~150 ms | Natural decay |
| **Range** | ~40 dB | Amount of reduction |
| **Threshold** | Set to pass ghost notes | Don't cut quiet hits |

**Important**: Bottom snare mic often **left without gate** to capture ghost notes and wire detail.

**Advanced option**: Use **expander** instead of gate for more musical transitions.

---

### Hi-Hats & Cymbals

Generally **minimal or no compression** needed:
- Natural transients are part of character
- Over-compression kills "life" and sparkle
- Exception: Loops or samples with inconsistent levels

**If compression needed**:

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Attack** | 1-5 ms | Relatively fast |
| **Release** | 50-100 ms | Quick reset |
| **Ratio** | 2:1 - 4:1 | Gentle |
| **Threshold** | Set for 1-2 dB reduction | Very light |

**Better alternatives to compression**:
- **Transient designer**: More precise control of attack/sustain
- **Clip gain/volume automation**: Manual consistency control
- **Sample replacement/layering**: If fundamentally inconsistent

---

### Toms

**Similar to snare**: Slow attack (10-30 ms), tempo-matched release, 4:1-8:1 ratio

**Key consideration**: Attack time should allow tom's pitch to ring through.

**Processing strategy**:
1. Gate to remove bleed (especially critical for toms)
2. Compression for consistency
3. EQ for tone

---

### Drum Bus/Group Compression

**Goal**: Glue individual drum elements into cohesive kit

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Attack** | 10-30 ms | Preserve transients |
| **Release** | 50-150 ms | Musical, tempo-aware |
| **Ratio** | 2:1 - 4:1 | Gentle glue |
| **Threshold** | Set for 2-3 dB reduction | Subtle cohesion |
| **Knee** | Soft | Musical, transparent |

**Compressor type recommendations**:
- **VCA** (SSL-style): Punchy, tight, modern
- **FET** (1176-style): Aggressive, colored, rock/aggressive genres
- **Opto** (LA-2A-style): Smooth, musical, program-dependent release
- **Variable-Mu** (Fairchild-style): Warm, musical, expensive sound

**Best practice**: Add drum bus compression **after** individual drum processing is complete.

---

### Overhead Compression

**Purpose**: Control dynamics while preserving ambience

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Attack** | 5-15 ms | Balance transient preservation with control |
| **Release** | 100-200 ms | Slower, more natural |
| **Ratio** | 2:1 - 4:1 | Gentle |
| **Threshold** | Set for 2-4 dB reduction | Light touch |

**Philosophy**: Overheads provide ambience and width, not punch. Compression should be transparent.

---

## Bass Compression

### Goals

1. **Consistency**: Even out note-to-note volume variations
2. **Sustain**: Maintain note body in dense mixes
3. **Control**: Prevent bass from overpowering mix
4. **Translation**: Help bass maintain presence across systems

### Standard Bass Compression

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Attack** | 10-30 ms | Allow transient through (if present) |
| **Release** | 50-150 ms | Note-dependent, allow some ring |
| **Ratio** | 3:1 - 6:1 | Moderate control |
| **Threshold** | Set for 3-6 dB reduction | Consistent control |
| **Knee** | Soft | Musical, transparent |

**Key concept**: Bass compression is about **consistency**, not aggression.

### Sub-Bass Specific

**Pure sub (sine/808)**:
- Often needs **less compression** than harmonic bass
- Sub is naturally consistent
- Focus on arrangement and sidechain interaction with kick

**If compression needed**:
- Very gentle (2:1-3:1 ratio)
- Slow attack (20-30 ms)
- Purpose: Safety limiting, not shaping

### Mid-Bass (Synth Bass, Reese, etc.)

**More aggressive compression often needed**:

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Attack** | 5-20 ms | Depends on transient character |
| **Release** | 50-120 ms | Tempo-aware |
| **Ratio** | 4:1 - 8:1 | More aggressive control |
| **Threshold** | Set for 4-8 dB reduction | Tighter control for harmonic bass |

### Multi-Band Compression on Bass

**Advanced technique**: Compress different frequency ranges separately

**Typical setup**:
- **Low band** (30-150 Hz): Light compression (2:1-3:1), control sub
- **Mid band** (150-500 Hz): Moderate compression (4:1-6:1), control body
- **High band** (500+ Hz): Light compression (2:1-4:1), preserve harmonics

**Benefit**: Independent control of sub power, mid body, and high-end detail.

### Processing Chain Order

1. **Saturation** (generate harmonics first)
2. **Compression** (control overall dynamics)
3. **Dynamic EQ sidechain** (duck fundamental when kick hits)

**Rationale**: Saturation adds harmonics → compression evens out harmonics and fundamental → sidechain creates space for kick

---

## Vocal Compression

Vocals require the most sophisticated compression approach due to wide dynamic range and critical importance in mix.

### Philosophy: Staged Compression

**Never rely on single compressor** for vocals. Use **2-3 compressors in series**, each doing different job.

### Stage 1: Fader Automation (Macro-Dynamic Control)

**Before any compression**: Manual fader riding to level out large dynamic swings

**Why**: 
- Compression can't effectively handle 10+ dB swings between whisper and shout
- Manual leveling allows compressor to work more musically on micro-dynamics
- Results in more natural, professional sound

**Approach**: Automate volume fader phrase-by-phrase to create more consistent overall level, then compress the micro-dynamics.

### Stage 2: Primary Leveling Compressor

**Goal**: Musical, transparent gain reduction for overall consistency

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Attack** | 10-30 ms | Preserve vocal transients and consonants |
| **Release** | 100-200 ms | Natural, musical (not pumping) |
| **Ratio** | 2:1 - 3:1 | Gentle, transparent |
| **Threshold** | Set for 3-5 dB reduction | Consistent but not squashed |
| **Knee** | Soft | Musical, gradual compression |

**Compressor type**: Opto (LA-2A-style) or gentle tube (Fairchild-style)

**Philosophy**: This compressor should "breathe" with the singer.

### Stage 3: Fast Transient Control Compressor

**Goal**: Control sharp consonants and syllables

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Attack** | 1-5 ms | Fast response to catch transients |
| **Release** | 50-100 ms | Quick reset |
| **Ratio** | 4:1 - 8:1 | More aggressive |
| **Threshold** | Set for 2-4 dB additional reduction | Peak control |
| **Knee** | Hard | Precise transient control |

**Compressor type**: FET (1176-style) or VCA (SSL-style)

**Philosophy**: This "catches" peaks that slip through first compressor.

### Optional Stage 4: Parallel Compression

**Goal**: Add body and presence without over-compressing

**Setup**:
1. Send vocal to aux channel
2. Compress heavily (10:1-20:1 ratio, fast attack)
3. Blend subtly (10-30% wet) with main signal

**Benefit**: Adds thickness and sustain while maintaining natural dynamics of main signal.

### Complete Vocal Chain Order

1. **Gain staging** (proper input level)
2. **Fader automation** (macro-dynamics)
3. **Light de-esser** (optional, if extreme sibilance)
4. **Compressor 1** (gentle leveling: 2:1-3:1, Opto/Tube)
5. **Compressor 2** (transient control: 4:1-8:1, FET/VCA)
6. **EQ** (corrective + presence)
7. **Saturation** (harmonics, optional)
8. **De-esser** (final sibilance control)
9. **Spatial FX** (reverb/delay on sends)

### De-Essing (Specialized Compression)

**What it is**: Multiband compressor targeting sibilance frequencies (5-12 kHz)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Frequency range** | 5-12 kHz | Sweep to find exact sibilance |
| **Peak frequency** | 7-8 kHz typical | Male: 5-8 kHz, Female: 7-10 kHz |
| **Ratio** | ~8:1 | Aggressive on sibilance only |
| **Threshold** | Set to catch "S" sounds | Solo band to find |
| **Knee** | Hard (-6 dB) | Immediate, decisive reduction |
| **Max reduction** | 8-10 dB | More = "lispy" sound |

**Strategy**:
- **Light de-esser pre-chain**: If extreme sibilance needs control before compression
- **Main de-esser post-EQ**: Final sibilance control
- **Wide-band de-esser post-FX**: If reverb/delay amplify sibilance

**Troubleshooting**:
- Singer "whistles" after de-essing → Attack too slow
- Sounds "lispy" → Too much reduction (back off threshold)

---

## Instrument Compression

### Synth Leads

**Purpose**: Sustain and presence in dense mixes

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Attack** | 5-20 ms | Depends on transient character |
| **Release** | 50-150 ms | Musical, allows ring |
| **Ratio** | 3:1 - 6:1 | Moderate control |
| **Threshold** | Set for 3-5 dB reduction | Consistent presence |

**Note**: Many synth sounds designed with internal compression. External compression may not be needed.

### Pads

**Purpose**: Smooth, consistent bed of sound

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Attack** | 20-50 ms | Very slow, preserve gentle swells |
| **Release** | 200-500 ms | Long, musical |
| **Ratio** | 2:1 - 3:1 | Gentle |
| **Threshold** | Set for 2-3 dB reduction | Very subtle |

**Philosophy**: Pads should breathe and evolve. Over-compression kills their nature.

### Arps & Plucks

**Purpose**: Consistency in rhythmic patterns

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Attack** | 1-10 ms | Depends on desired pluck sharpness |
| **Release** | 50-100 ms | Quick, rhythmic |
| **Ratio** | 4:1 - 6:1 | Moderate-aggressive |
| **Threshold** | Set for consistent hits | Even level |

**Better alternative**: Often **clip gain** or **transient designer** more effective than compression for plucks/arps.

### Piano & Keys

**Acoustic Piano**:

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Attack** | 10-30 ms | Preserve hammer strike |
| **Release** | 100-300 ms | Allow natural decay |
| **Ratio** | 2:1 - 4:1 | Gentle-moderate |
| **Threshold** | Set for 2-4 dB reduction | Evening out only |

**Electric Piano** (Rhodes/Wurli):

| Parameter | Value | Notes |
|-----------|-------|-------|
| **Attack** | 5-20 ms | Balance attack preservation with control |
| **Release** | 100-200 ms | Musical |
| **Ratio** | 3:1 - 6:1 | More aggressive okay |
| **Threshold** | Set for 4-6 dB reduction | More body |

**Parallel compression works great** on electric pianos for vintage character.

---

## Advanced Techniques

### Parallel Compression (New York Compression)

**Concept**: Blend heavily compressed signal with dry signal

**Benefits**:
- Add density and sustain without sacrificing transients
- Increase average level without squashing peaks
- Add "weight" and "thickness" to sound

**Setup**:
1. Send signal to aux channel
2. Compress aux channel heavily:
   - Fast attack (0-5 ms)
   - Fast release (50-100 ms)
   - High ratio (10:1 - 20:1)
   - Low threshold (heavy compression)
3. Blend aux with original (typically 20-40%)

**Best for**: Drums (especially), vocals, bass, anything needing more body

**Critical**: Use HPF before parallel compressor on low-frequency sources to prevent rumble buildup.

### Serial Compression

**Concept**: Multiple compressors in series, each doing lighter work

**Benefits**:
- More transparent than single compressor doing all work
- Different compressors can target different aspects
- Allows combination of different compression characters

**Example** (Vocals):
- Compressor 1: Gentle leveling (2:1, slow attack)
- Compressor 2: Transient control (6:1, fast attack)
- Result: Natural-sounding but controlled

**Philosophy**: "3 dB + 3 dB = more transparent than 6 dB from one compressor"

### Sidechain Compression

**Concept**: External signal triggers compression

**Common uses**:

**1. Bass ducking** (when kick hits):
- Kick → sidechain input on bass compressor
- Bass ducks when kick plays
- Creates space for kick, prevents masking
- Creates characteristic "pumping" in dance music

**Parameters**:
- Fast attack (0-5 ms)
- Release: 50-150 ms (adjust for pumping feel)
- Ratio: 4:1 - 8:1
- Reduction: 3-6 dB

**2. Pad/synth ducking** (when vocal present):
- Vocal → sidechain input on pad compressor
- Pads duck slightly when vocal present
- Creates space without manual automation
- Very subtle (1-2 dB reduction)

**3. De-essing** (frequency-specific sidechain):
- High-frequency content triggers compression
- Only sibilant frequencies reduced
- See de-essing section

### Dynamic EQ vs Multiband Compression

Both can do similar jobs but with different characteristics:

**Dynamic EQ**:
- More surgical, precise
- Only affects specific frequency when threshold exceeded
- Better for targeted problems
- Example: Duck bass at 50 Hz only when kick hits

**Multiband Compression**:
- Always active, compresses multiple bands
- More "musical" interaction between bands
- Better for broad tonal shaping
- Example: Control overall bass spectrum

**When to use which**:
- **Dynamic EQ**: Specific frequency problems, kick-bass ducking
- **Multiband**: Overall spectral control, mastering-style processing

### Transient Designers vs Compression

**Transient Designer**:
- Direct attack/sustain control
- No threshold or ratio
- More transparent for transient shaping
- Best for: Drums, percussive sounds

**Compression**:
- Dynamic range control
- Level-dependent
- Can add character/color
- Best for: Leveling, consistency, glue

**Often better to use transient designer** for pure attack/sustain shaping, save compression for level control.

---

## Mix Bus Compression

### Purpose

- Add "glue" - makes individual elements sound like cohesive whole
- Subtle dynamic control over entire mix
- NOT for making mix louder (that's limiting/mastering)

### Critical Philosophy

**Mix bus compression should be nearly imperceptible**. When bypassed, you should miss the "glue," not hear obvious level or dynamic change.

### Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Attack** | 30 ms (medium-slow) | Preserve transients |
| **Release** | 100 ms (medium-fast, auto if available) | Musical, tempo-aware |
| **Ratio** | 1.5:1 - 2:1 | Very gentle |
| **Threshold** | Set for 1-2 dB reduction MAX | Subtle glue only |
| **Knee** | Soft | Transparent, musical |
| **Makeup Gain** | Compensate for reduction | Match levels |

### When to Add Mix Bus Compression

**Two approaches**:

**1. From the start** (recommended for experienced engineers):
- Add with very light settings at beginning of mix
- Mix "into" the compressor
- Final sound influenced by compression throughout
- More consistent result

**2. At the end** (safer for beginners):
- Mix without bus compression
- Add at end for final glue
- More control, less risk of mixing around artifacts

### Compressor Type Selection

**VCA** (SSL-style):
- Clean, punchy, modern
- Best for: Electronic music, pop, rock
- Character: Tight, controlled

**Opto** (LA-2A-style):
- Smooth, program-dependent release
- Best for: R&B, soul, singer-songwriter
- Character: Musical, gentle

**Variable-Mu** (Fairchild-style):
- Warm, rich, musical
- Best for: Jazz, classical, acoustic
- Character: Expensive, smooth

**FET** (1176-style):
- Fast, aggressive, colored
- Best for: Rock, aggressive pop
- Character: Punchy, colored

**Most common for electronic music**: VCA (SSL-style)

### Mix Bus Processing Chain Order

1. **EQ** (optional, corrective only)
2. **Compression** (glue)
3. **Saturation** (optional, subtle warmth)
4. **Limiter** (optional, peak catching only)

**Important**: Keep processing minimal on mix bus. Most work should be done on individual tracks.

---

## Genre-Specific Approaches

### Techno / Minimal

**Characteristics**:
- Very controlled dynamics (not much dynamic range)
- Tight, consistent hits
- Focus on groove, not dynamic expression

**Drum compression**:
- Kick: Moderate serial + aggressive parallel (pumping okay)
- Hi-hats: Minimal or none (transient designer preferred)
- Overall: Tight, consistent

**Bass compression**:
- Sub: Light (2:1-3:1) or none
- Mid-bass: Moderate (4:1-6:1), tight control
- Sidechain from kick: Heavy, obvious pumping

**Mix bus**:
- VCA compression, 2:1 ratio
- More compression than other genres (2-3 dB reduction okay)
- Tight, controlled sound

### House / Deep House

**Characteristics**:
- More dynamic than techno
- Warmer, more musical
- Groove-oriented but with expression

**Drum compression**:
- Kick: Moderate, musical (preserve warmth)
- Drums: Moderate compression, not over-controlled
- Overall: Musical, groovy

**Bass compression**:
- More moderate (3:1-4:1)
- Musical rather than tight
- Sidechain: Present but musical (not aggressive pumping)

**Mix bus**:
- Opto or VCA, gentle
- 1-2 dB reduction
- Musical glue, not control

### Drum & Bass / Dubstep

**Characteristics**:
- Very aggressive compression on drums
- Bass dominant (less compression needed)
- High energy, aggressive

**Drum compression**:
- Kick: Heavy serial, aggressive parallel
- Snare: Very tight (short attack/release)
- Overall: Aggressive, tight control

**Bass compression**:
- Often minimal on bass (bass is loud, not necessarily compressed)
- Focus on multiband control
- Sub left relatively dynamic, mid-bass controlled

**Mix bus**:
- VCA or FET, moderate
- 2-3 dB reduction
- Tight, controlled

### Trap / Hip-Hop

**Characteristics**:
- 808 kick/bass tuned to key (longer sustain)
- Very bright hi-hats (often uncompressed)
- Vocal-focused

**Drum compression**:
- 808: Light or none (arrangement controls dynamics)
- Hi-hats: Often none (transients are character)
- Snare: Tight but not over-compressed

**Bass compression**:
- 808 kick IS the bass
- Minimal compression (long sustain intended)
- Focus on arrangement

**Vocal compression**:
- Heavy (2-3 compressors in series)
- Very present, upfront
- De-essing critical

**Mix bus**:
- VCA or Opto, gentle
- 1-2 dB reduction
- Vocal stays on top

---

## Compression Troubleshooting

### Problem: Pumping/Breathing

**Causes**:
- Release too fast
- Too much compression (ratio too high or threshold too low)

**Solutions**:
- Slow down release
- Reduce ratio
- Raise threshold (less compression)
- Use parallel compression instead

### Problem: Loss of Punch

**Causes**:
- Attack too fast
- Over-compression

**Solutions**:
- Slow down attack (let transient through)
- Reduce amount of compression
- Use serial compression (lighter stages)
- Consider transient designer instead

### Problem: Sounds Unnatural/Squashed

**Causes**:
- Too much compression
- Ratio too high
- Hard knee on material needing soft knee

**Solutions**:
- Reduce compression amount
- Lower ratio
- Switch to soft knee
- Use multiple lighter compressors instead of one heavy

### Problem: No Apparent Effect

**Causes**:
- Attack too slow for fast material
- Release too slow (not resetting)
- Threshold too high

**Solutions**:
- Faster attack
- Faster release (tempo-sync)
- Lower threshold
- Check if compression actually needed

### Problem: Compressor "Fighting" With Music

**Causes**:
- Release not musical/tempo-synced
- Ratio too extreme

**Solutions**:
- Tempo-sync release (calculate musical timing)
- Use auto-release if available
- Reduce ratio
- Consider different compressor type (opto has program-dependent release)

---

## Compression Workflow

### Step-by-Step Compression Approach

**Phase 1: Individual Tracks**
1. **Drums first**: Get punch and consistency
   - Kick and snare (serial compression)
   - Overheads (light compression)
   - Parallel compression if needed
2. **Bass**: Consistency and sustain
   - Light compression for control
3. **Vocals**: Leveling and presence
   - Staged compression approach
4. **Instruments**: As needed
   - Most synths need minimal compression

**Phase 2: Group/Bus Compression**
1. **Drum bus**: Glue kit together
2. **Instrument buses**: If multiple similar instruments
3. **Vocal bus**: If multiple vocal tracks

**Phase 3: Mix Bus**
1. **Mix bus compression**: Final glue
   - Add early or late (approach-dependent)
   - Very light settings

**Phase 4: Verification**
1. **A/B comparison**: Bypass each compressor
2. **Check attack**: Bypass and check if losing punch
3. **Check release**: Listen for pumping
4. **Check overall**: Is compression helping or hurting?

### Compression Decision Tree

**Does track have dynamic problems?**
- No → No compression needed
- Yes → Continue

**Is problem large swings or micro-dynamics?**
- Large swings → Fader automation first
- Micro-dynamics → Compression

**Is problem transients or sustain?**
- Transients too loud → Fast attack, moderate ratio
- Need more sustain → Slow attack, higher ratio, or parallel

**Is one compressor enough?**
- No → Serial compression (multiple gentle stages)
- Need sustain too → Add parallel compression

---

## Critical Compression Reminders

### Philosophy

1. **Compression is not automatic** - Not every track needs it
2. **Less is more** - Light compression often better than heavy
3. **Ears over meters** - Trust what you hear, not just GR meter
4. **Attack is critical** - Often most important parameter for character
5. **Release should be musical** - Tempo-sync when possible

### Common Mistakes

1. **Over-compression** - Most common error
2. **Attack too fast** - Kills transients, sounds lifeless
3. **Same settings for everything** - Each source needs different approach
4. **Ignoring automation** - Compressor can't fix everything
5. **Stacking without purpose** - Multiple compressors should each have clear role

### Best Practices

1. **Always A/B** - Bypass compressor frequently
2. **Use makeup gain properly** - Match pre/post levels for fair comparison
3. **Start gentle** - Can always add more, hard to undo over-compression
4. **Different compressors for different jobs** - Use appropriate tool for task
5. **Check in context** - What works soloed may not work in mix

---

## Summary: Compression Approach

1. **Understand the goal** - What dynamic problem are you solving?
2. **Choose right technique** - Serial, parallel, sidechain, or automation?
3. **Set attack appropriately** - Fast or slow based on transient needs
4. **Match release to music** - Tempo-sync, musical timing
5. **Start gentle** - Can always increase
6. **Use staging** - Multiple light compressors often better than one heavy
7. **Verify in context** - Solo is for setting, mix is for verification
8. **Trust your ears** - Meters guide, ears decide

Remember: **Compression is a tool for solving specific problems**, not a default process. Every compression decision should have a clear purpose. When in doubt, compress less or use automation instead.

Use this reference to understand which compression approach and parameters to use for each situation, then fine-tune by ear for your specific mix.
