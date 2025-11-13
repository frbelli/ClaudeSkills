# Low-End Treatment Reference

This reference provides comprehensive techniques for treating the low-end frequency range (30-200 Hz), focusing on the critical relationship between kick drum and bass in electronic music production.

---

## Introduction: Why Low-End Matters

The low-end (30-200 Hz) demands maximum attention to avoid **masking** between kick drum and bass/sub. Their coexistence defines the rhythmic power and impact of the track.

**Core challenge**: Kick and bass compete in the same frequency range, particularly 40-80 Hz, where both have their fundamental frequencies. The goal is to make both elements powerful and defined without them canceling each other out.

**Three-pronged approach**:
1. **Individual processing**: Optimize each element separately
2. **Interactive processing**: Use dynamic tools to create space between them
3. **Sound selection**: Choose complementary sounds from the start

---

## Part 1: Kick Drum Processing

Kick drum treatment aims to separate the **punch** (initial transient) from the **sustain** (body and decay).

### 1.1 Serial Compression for Punch

To emphasize punch, the compressor must allow the initial transient to pass the threshold before compression engages.

#### Parameters

- **Attack**: 10-30 ms (slow)
  - Allows transient to pass through uncompressed
  - If attack isn't punching through → slower attack
- **Ratio**: 4:1 to 8:1 (medium-high)
  - Increases impact
- **Release**: 50-120 ms, tempo-synced
  - Must fully disengage before next hit
  - If kick "pumps" → release too slow
- **Average Reduction**: 3-5 dB

#### Purpose

- Emphasizes the "click" or "beater" of the kick
- Preserves attack transient
- Controls sustain tail

#### Quick Verification

Mute the bass track and listen to whether the kick alone defines the rhythmic energy. If it sounds "empty" without bass, either:
- Sustain is too short
- Too much attenuation around 60-100 Hz

### 1.2 Parallel Compression (New York Compression)

Parallel compression adds **density** (sustain) without sacrificing original transient quality.

#### Setup

1. Send kick signal to an Aux channel
2. Apply extreme compression (Ratio 10:1 or higher, fast/zero Attack, aggressive Release)
3. Blend this heavily compressed signal with the dry signal

#### Parameters

- **Ratio**: 10:1 to 20:1
- **Attack**: Fast or zero
- **Release**: Fast
- **Blend**: Adjust dry/wet for desired density

#### Purpose

- Increases perceived density and sustain of body
- Keeps attack of original track intact
- More sustain, transient intact

#### Critical Tip

To prevent parallel compression from adding rumble:
- Insert **HPF at ~50-60 Hz** BEFORE the parallel compressor
- This keeps punch while keeping lows clean

### 1.3 Transient Designer

Modern EDM/Techno mixes often employ transient designers for precise attack/sustain control:

- **Boost Attack**: +2 to +4 dB on kick
  - Increases click and definition
- **Reduce Sustain**: On bass for tightness
  - Creates separation between kick and bass

### 1.4 Kick Drum EQ Strategy

#### Fundamental Frequency (Punch)

- **Range**: 60-80 Hz typically
- **Action**: Slight boost (+2 to +3 dB)
- **Q**: Medium-wide (Q 1.5-2.0)
- **Purpose**: Emphasizes the "thump" or fundamental

#### Sub-Bass Content

- **Range**: 30-50 Hz
- **Action**: Depends on style
  - **Boost** for 808-style kicks: +1 to +2 dB
  - **Cut** for tight, punchy kicks: -2 dB
- **Q**: Wide (Q 1.0-1.5)

#### Attack/Click

- **Range**: 2-6 kHz
- **Action**: Boost +2 to +4 dB
- **Q**: Medium (Q 2.0-3.0)
- **Purpose**: Emphasizes beater attack and definition

#### Remove Boxiness

- **Range**: 200-500 Hz
- **Action**: Cut -2 to -4 dB if needed
- **Q**: Narrow (Q 3.0-5.0)
- **Purpose**: Remove hollow, boxy resonances

#### High-Pass Filter

- **Frequency**: 30-40 Hz
- **Slope**: 12-24 dB/octave
- **Purpose**: Remove inaudible subsonic energy that wastes headroom

### 1.5 Kick Processing Chain Order

Recommended signal flow for kick drum:

1. **High-Pass Filter** (30-40 Hz)
2. **EQ** (corrective cuts, especially boxiness)
3. **Serial Compressor** (punch emphasis)
4. **Parallel Compression** (send to aux)
5. **Transient Designer** (optional, for extra attack control)
6. **EQ** (final timbral shaping, attack boost)
7. **Saturation** (optional, for harmonics and character)

---

## Part 2: Bass/Sub Processing

Bass requires clarity and definition while maintaining power and weight.

### 2.1 Bass EQ Strategy

#### Tonal Shaping with Broad Q

**Remove Subsonic Energy**
- **Frequency**: 30 Hz
- **Action**: Cut -2 dB
- **Q**: Wide (Q 1.0-1.5)
- **Purpose**: Remove inaudible subsonic content not reproducible on most systems

**Musical Body and Fullness**
- **Frequency**: 60 Hz or 100 Hz (depends on key/style)
- **Action**: Boost +2 dB
- **Q**: Wide (Q 1.0-2.0)
- **Purpose**: Add musical weight and presence

#### Corrective Cuts with Narrow Q

**Mud Removal**
- **Range**: 200-400 Hz
- **Action**: Cut -2 to -4 dB as needed
- **Q**: Narrow (Q 3.0-5.0)
- **Purpose**: Remove unwanted resonances and muddiness
- **Technique**: Sweep with narrow boost to identify problematic resonances, then cut

### 2.2 Harmonic Saturation: Critical for Translation

A light application of harmonic saturation is **essential** for bass, especially sub bass.

#### Why Saturation Matters

Pure sine wave sub bass (808, sine synth) contains only the fundamental frequency (e.g., 40 Hz). Most consumer playback systems (smartphones, laptops, earbuds) cannot reproduce these low frequencies accurately or at all.

**Solution**: Saturation generates audible harmonics in the 100-400 Hz range, which ARE reproducible on small speakers.

#### Implementation

- **Type**: Tape or tube saturation (generates even harmonics)
- **Amount**: Subtle (5-15% wet, or drive until harmonics appear)
- **Purpose**: Makes bass perceptible on consumer systems without changing its character on full-range systems

#### Quick Test

If bass is invisible on smartphone speakers:
→ Add harmonics at 150-300 Hz through saturation

### 2.3 High-Pass Filtering on Bass

While counterintuitive, bass often benefits from a gentle high-pass filter:

- **Frequency**: 30-35 Hz
- **Slope**: 6-12 dB/octave (gentle)
- **Purpose**: Remove rumble and subsonic energy that wastes headroom without affecting the perceived weight

### 2.4 Bass Processing Chain Order

Recommended signal flow for bass:

1. **High-Pass Filter** (30-35 Hz)
2. **EQ** (corrective cuts, mud removal)
3. **Saturation** (harmonic generation)
4. **Compressor** (light ratio, musical control)
5. **Dynamic EQ** (sidechain from kick - see Part 3)
6. **EQ** (final timbral boosts)

---

## Part 3: Kick-Bass Interaction Techniques

The fundamental challenge: Kick and bass both compete in the 40-80 Hz range. Three primary techniques resolve this conflict.

### 3.1 Dynamic EQ Sidechain (Advanced, Recommended)

This technique has **superseded** traditional volume-based sidechain compression for precision and power.

#### Concept

Instead of ducking the entire bass volume when kick hits, **only reduce the bass at the kick's fundamental frequency** (typically 40-60 Hz).

#### Setup

1. **Kick** → sidechain trigger for **Dynamic EQ on Bass**
2. **Target frequency**: 40-60 Hz (with medium-wide Q)
3. **Reduction**: 3-6 dB
4. **Attack**: 0-5 ms (fast) - reacts instantly to kick transient
5. **Release**: 30-80 ms - allows bass to restore level immediately after kick peak

#### Advantages Over Traditional Sidechain

- Preserves overall bass volume
- Preserves upper harmonics of bass
- Intervenes only where strictly necessary (the fundamental)
- Result: Low-end perceived as more powerful and defined
- Gain reduction not distributed across entire spectrum

#### Smart Sidechaining Principle

**Duck only the fundamental, not the entire bass**

### 3.2 Traditional Sidechain Compression

Still valid for creative "pumping" effects common in EDM, house, techno.

#### Setup

1. **Kick** → sidechain trigger for **Compressor on Bass**
2. **Threshold**: Set so kick triggers 3-6 dB gain reduction on bass
3. **Ratio**: 4:1 to 8:1
4. **Attack**: 0-5 ms (instant)
5. **Release**: 50-150 ms (taste-dependent)
   - Faster release = tighter pumping effect
   - Slower release = smoother ducking

#### Purpose

- Creates rhythmic space for kick
- Generates characteristic "pumping" effect in dance music
- Prevents low-end masking

#### Limitation

Reduces entire bass volume, not just conflicting frequencies. Can make bass feel weaker compared to Dynamic EQ approach.

### 3.3 Complementary EQ (Classic Technique)

Carve complementary frequency pockets for kick and bass using static EQ.

#### Strategy

1. **Identify kick fundamental**: Typically 60-80 Hz
   - **On kick**: Boost +2 to +3 dB at this frequency
   - **On bass**: Cut -2 to -3 dB at the SAME frequency

2. **Identify bass body**: Typically 100-250 Hz
   - **On bass**: Boost +2 dB at this frequency
   - **On kick**: Cut -1 to -2 dB at the SAME frequency (if needed)

#### Visualization

```
Kick:  [Boost @ 70 Hz] [Cut @ 150 Hz]
Bass:  [Cut @ 70 Hz]   [Boost @ 150 Hz]
```

#### Purpose

- Creates static frequency separation
- Each element occupies its own sonic space
- No dynamic interaction required

#### Limitation

Less powerful than dynamic techniques; works best when kick and bass rhythms are tightly synchronized.

### 3.4 Arrangement and Sound Selection (Preventative)

**Best solution**: Choose sonically distinct kick and bass from the start.

#### Strategies

**1. Frequency Separation**
- 808-style sub-heavy kick (30-50 Hz fundamental)
- Bass rich in midrange harmonics (fundamental at 60-100 Hz)
- Natural separation in frequency domain

**2. Transposition**
If kick and bass share the same fundamental frequency:
- Transpose bass by a **third** or **fifth**
- Changes fundamental without changing musical relationship
- Example: If kick is at 50 Hz (G), transpose bass to 60 Hz (B♭, minor third up)

**3. Waveform Change**
- Change bass oscillator waveform:
  - Saw → Square (shifts harmonic content)
  - Sine → PWM (adds upper harmonics)
- Changes spectral distribution without changing pitch

**4. Layering Technique**
- **Sub layer**: Pure sine or triangle, handles 30-60 Hz
- **Harmonic layer**: Saw/square, handles 80-300 Hz
- Process each layer independently
- Sub layer stays clean and centered
- Harmonic layer can be stereo-widened, saturated, filtered

---

## Part 4: Technical Parameters Summary

### 4.1 Kick Dynamics Table

| Parameter | Kick Punch (Serial) | Kick Sustain (Parallel) | Transient Designer |
|-----------|-------------------|----------------------|-------------------|
| **Attack** | 10-30 ms | 0-5 ms | N/A (Boost +2/+4 dB) |
| **Release** | 50-120 ms | Fast | N/A |
| **Ratio** | 4:1 - 8:1 | 10:1 - 20:1 | N/A |
| **Target** | Transient | Sustain | Attack enhancement |
| **Reduction** | 3-5 dB | Heavy | N/A |

### 4.2 Bass Processing Table

| Parameter | Compressor | Dynamic EQ (Sidechain) | Saturation |
|-----------|-----------|----------------------|-----------|
| **Attack** | 10-30 ms | 0-5 ms | N/A |
| **Release** | 50-150 ms | 30-80 ms | N/A |
| **Ratio** | 3:1 - 4:1 | N/A | N/A |
| **Target** | Overall dynamics | 40-60 Hz duck | Harmonic generation |
| **Amount** | 2-4 dB reduction | 3-6 dB reduction | Subtle (harmonics @ 150-300 Hz) |

### 4.3 Kick-Bass Interaction Summary

| Technique | Strength | Use Case | Complexity |
|-----------|----------|----------|-----------|
| **Dynamic EQ Sidechain** | ★★★★★ | Modern electronic music, maximum power | Advanced |
| **Traditional Sidechain** | ★★★★☆ | Creative pumping effect, EDM/House | Intermediate |
| **Complementary EQ** | ★★★☆☆ | Static separation, acoustic music | Beginner |
| **Sound Selection** | ★★★★★ | Preventative solution, all genres | Beginner |

---

## Part 5: Genre-Specific Considerations

### 5.1 Techno / Minimal

**Kick characteristics**:
- Very prominent, often loudest element
- Sub-heavy (30-50 Hz emphasis)
- Tight transient (short sustain)

**Bass characteristics**:
- Often rhythmically syncopated with kick
- Harmonically rich (not pure sub)
- Dynamic EQ sidechain essential

**Target balance**: Kick slightly louder than bass in mix

### 5.2 House / Deep House

**Kick characteristics**:
- Warm, rounded
- 60-80 Hz fundamental
- Medium sustain

**Bass characteristics**:
- Often chord-based or melodic
- 80-150 Hz fundamental range
- Traditional sidechain for classic "pumping"

**Target balance**: Kick and bass relatively equal, both prominent

### 5.3 Drum & Bass / Dubstep

**Kick characteristics**:
- Extremely tight transient
- Often layered (attack layer + sub layer)
- Attack emphasis at 3-6 kHz

**Bass characteristics**:
- Dominant element in mix
- Often modulated/wobbling
- Multiple layers (sub + mid-bass + high-end)

**Target balance**: Bass often louder than kick, kick provides rhythmic definition

### 5.4 Trap / Hip-Hop

**Kick characteristics**:
- 808-style sub kick
- Very long sustain (tuned to key)
- Fundamental at 30-60 Hz

**Bass characteristics**:
- Often minimal or absent
- If present, occupies 80-200 Hz range
- 808 kick functions as bass instrument

**Special consideration**: 808 kick IS the bass - tune to musical key, use arrangement to create space

---

## Part 6: Common Problems and Solutions

### Problem 1: Kick Lacks Punch

**Symptoms**: Kick sounds weak, gets lost in mix

**Solutions**:
1. **Check attack compression**: Ensure attack time is 10-30 ms (not too fast)
2. **Boost click frequency**: +3 dB at 2-6 kHz with Q 2.0-3.0
3. **Use transient designer**: Boost attack +2 to +4 dB
4. **Remove competition**: High-pass other elements more aggressively
5. **Layer approach**: Add bright "attack" layer to sub-heavy kick

### Problem 2: Kick Lacks Weight

**Symptoms**: Kick sounds thin, no chest impact

**Solutions**:
1. **Check fundamental**: Boost +2 to +3 dB at 60-80 Hz
2. **Check sub content**: Ensure 30-50 Hz is present (not over-filtered)
3. **Parallel compression**: Add for sustain and body
4. **Remove boxiness**: Cut 200-500 Hz if kick sounds hollow
5. **Sample selection**: Choose kick with better low-end content

### Problem 3: Bass Inaudible on Small Speakers

**Symptoms**: Bass sounds great on monitors, disappears on phone/laptop

**Solutions**:
1. **Add harmonic saturation**: Generate harmonics at 150-300 Hz
2. **Ensure mid-bass content**: Bass should have energy at 100-250 Hz, not just sub
3. **Layer technique**: Add subtle "harmonic layer" above sub layer
4. **Test frequently**: Check mix on laptop speakers during mixing

### Problem 4: Kick and Bass Muddy/Unclear

**Symptoms**: Low-end sounds congested, lacks definition

**Solutions**:
1. **Dynamic EQ sidechain**: Implement if not already using
2. **High-pass both**: Ensure HPF at 30-40 Hz on kick, 30-35 Hz on bass
3. **Remove mud**: Cut 200-400 Hz on both elements
4. **Check phase**: Ensure kick and bass not phase-canceling
5. **Sound selection**: Choose more complementary sounds

### Problem 5: Excessive Pumping Effect

**Symptoms**: Bass ducks too much, mix breathes unnaturally

**Solutions**:
1. **Switch to Dynamic EQ**: From traditional sidechain compression
2. **Adjust release time**: Make release faster (50-80 ms)
3. **Reduce reduction amount**: Aim for 2-3 dB instead of 6 dB
4. **Check attack time**: Ensure 0-5 ms (not too slow)
5. **Multiband sidechain**: Duck only low frequencies, not entire bass

### Problem 6: Kick and Bass Fight Rhythmically

**Symptoms**: Kick and bass rhythms clash, create confusion

**Solutions**:
1. **Arrangement**: Move bass notes away from kick hits
2. **Note length**: Shorten bass notes to create space for kick
3. **Volume automation**: Manual ducking at specific moments
4. **Rhythm simplification**: Simplify one element's rhythm
5. **Musical solution**: This is an arrangement problem, not a mixing problem

---

## Part 7: Workflow Integration

### Recommended Order of Operations

**Phase 1: Individual Optimization**
1. Process kick drum in solo (compression, EQ, transient design)
2. Process bass in solo (saturation, EQ, compression)
3. Verify each element sounds good individually

**Phase 2: Interaction**
4. Listen to kick and bass together (mute everything else)
5. Identify frequency conflicts using spectrum analyzer
6. Implement primary interaction technique (Dynamic EQ or traditional sidechain)
7. Apply complementary EQ if additional separation needed

**Phase 3: Context**
8. Bring in rest of arrangement
9. Verify kick and bass still powerful and defined
10. Make final micro-adjustments to levels and interaction parameters

**Phase 4: Reference**
11. A/B compare with reference track in same genre
12. Verify low-end translation on multiple systems
13. Check mono compatibility

### Critical Monitoring Points

- **Full-range monitors**: Check overall balance and power
- **Auratone/midrange speaker**: Verify bass translation (harmonics present?)
- **Headphones**: Check for phase issues and subtle conflicts
- **Laptop speakers**: Verify bass translation to consumer systems
- **Mono**: Ensure kick and bass don't disappear or weaken

---

## Summary: The Low-End Hierarchy

1. **Sound selection** - Choose complementary sounds from the start
2. **Individual processing** - Optimize kick and bass separately
3. **Interaction processing** - Create dynamic or static separation
4. **Arrangement** - Ensure rhythms work together musically
5. **Context verification** - Check in full mix and on multiple systems

**Remember**: A powerful low-end comes from a combination of good sound selection, precise processing, and musical arrangement. No amount of processing can fix poor sound choices or rhythmic conflicts.

The goal is not to hear kick OR bass, but to hear kick AND bass - each powerful, each defined, working together to create rhythmic impact.
