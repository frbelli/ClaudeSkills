# Mastering Chain Reference

This reference provides comprehensive mastering techniques, processing chains, loudness standards, and delivery specifications for electronic music production.

---

## Table of Contents

1. [Mastering Philosophy](#mastering-philosophy)
2. [Pre-Mastering: Mix Preparation](#pre-mastering-mix-preparation)
3. [The Mastering Chain](#the-mastering-chain)
4. [EQ in Mastering](#eq-in-mastering)
5. [Compression in Mastering](#compression-in-mastering)
6. [Loudness and Limiting](#loudness-and-limiting)
7. [Stereo Processing](#stereo-processing)
8. [Dithering and Bit Depth](#dithering-and-bit-depth)
9. [Delivery Standards](#delivery-standards)
10. [Genre-Specific Approaches](#genre-specific-approaches)

---

## Mastering Philosophy

### What Mastering Is (and Isn't)

**Mastering IS**:
- Final sonic enhancement and "sweetening"
- Creating consistency across an album/EP
- Technical preparation for distribution
- Optimization, not repair

**Mastering IS NOT**:
- Fixing fundamental mix problems
- Making a bad mix sound good
- Radical tonal or dynamic changes
- A substitute for proper mixing

### The Three Primary Objectives

**1. The Sound of a Record**
- Apply final polish that elevates mix to professional master
- Refine tonal balance
- Enhance clarity and cohesion
- Impart competitive edge and sonic authority

**2. Consistency Across Album**
- Match perceived loudness between tracks
- Create cohesive tonal character
- Maintain consistent dynamic range
- Seamless listening experience (no volume adjustment needed)

**3. Preparation for Distribution**
- Sample rate/bit depth conversion
- Application of dither (when needed)
- Metadata inclusion
- Format-specific optimization

### Critical Philosophy: "Mastering with Intention"

**Never start processing without a plan**. Follow this workflow:

1. **Critical Listening** (85 dB SPL)
   - Listen to entire mix without processing
   - Take detailed notes
   - Document tonal balance, dynamics, stereo image, defects

2. **Reference Tracks**
   - Select 1-2 professionally mastered songs in similar genre
   - Provides target for loudness, tone, dynamics
   - Prevents "losing the plot" in details

3. **Define Goals**
   - Make track louder
   - Make track sound better
   - Ensure translation across systems

4. **Assess Mix Quality**
   - **"The mix should sound professional already"**
   - If fundamental issues exist → send back to mixing
   - Mastering enhances, doesn't fix

---

## Pre-Mastering: Mix Preparation

### Ideal Mix Delivery Specifications

| Parameter | Target Value | Notes |
|-----------|--------------|-------|
| **Peak Level** | -6 dBFS | Provides adequate headroom |
| **RMS Level** | -18 dBFS average | Proper gain staging |
| **Sample Rate** | 44.1 kHz or higher | Match or exceed final delivery |
| **Bit Depth** | 24-bit or 32-bit float | Never 16-bit |
| **Format** | WAV or AIFF | Lossless, uncompressed |
| **Processing** | No limiter on master | Leave headroom for mastering |
| **Dither** | None | Applied only in mastering |

### Red Flags: When to Send Back to Mixing

- Peak levels consistently at 0 dBFS (no headroom)
- Excessive clipping or distortion
- Fundamental balance issues (vocal too quiet, bass too loud, etc.)
- Severe frequency problems (extreme mud or harshness)
- Major phase issues
- Unintended noise or clicks

**Philosophy**: Better to spend time mixing properly than attempting to "fix in mastering."

---

## The Mastering Chain

### Standard Processing Order

The order is **logical and functional**, not arbitrary. Each stage influences the next.

| Stage | Function | Key Consideration |
|-------|----------|-------------------|
| **1. Gain Staging/Trim** | Balance input level | Proper level into first processor |
| **2. Corrective EQ** (Minimum Phase) | Remove problems | Address mud, harshness, resonances |
| **3. Compression** (Glue) | Dynamic cohesion | Gentle, musical (1.5:1 - 2:1) |
| **4. Sweetening EQ** (Linear Phase) | Final tonal balance | Broad, musical adjustments |
| **5. Multiband/Dynamic EQ** (Optional) | Frequency-specific dynamics | Surgical control of problem areas |
| **6. Stereo/M-S Processing** | Spatial control | Width, mono-compatibility |
| **7. Limiter** (True Peak) | Loudness maximization | Peak control, LUFS target |
| **8. Dithering** (If needed) | Bit depth reduction | Only when going to 16-bit |

### Alternative Chain Philosophies

**Minimal Chain** (Transparent approach):
1. Corrective EQ (light)
2. Glue compression (very subtle)
3. Limiter (True Peak control)

**Aggressive Chain** (Loud, competitive):
1. Corrective EQ
2. Multiband compression
3. Glue compression
4. Sweetening EQ
5. Aggressive limiter

**Genre matters**: Electronic music often uses more aggressive chains than acoustic.

---

## EQ in Mastering

### Phase Technology: Linear vs. Minimum Phase

**Minimum Phase EQ**:
- **Characteristics**: 
  - Traditional, "musical" sound
  - Introduces slight phase shift
  - Zero latency
  - Lower CPU usage
- **Best for**: 
  - Corrective EQ (before compression)
  - When transient preservation critical
  - When phase shift is musically beneficial
- **Use when**: Processing rhythm section, drums, percussive material

**Linear Phase EQ**:
- **Characteristics**:
  - Minimizes phase shift
  - Preserves temporal coherence
  - High latency
  - Higher CPU usage
  - Potential pre-ringing artifacts
- **Best for**:
  - Sweetening EQ (after compression)
  - Stereo material (preserves stereo image)
  - Final tonal adjustments
  - When phase coherence critical
- **Use when**: Processing full mix, M-S processing, final polish

### EQ Strategy: Dual-Stage Approach

**Professional workflow: EQ → Compression → EQ**

**Stage 1: Corrective EQ** (Before Compression)
- **Technology**: Minimum Phase
- **Purpose**: Remove problems before compression reacts to them
- **Typical moves**:
  - HPF at 20-30 Hz (subsonic removal)
  - Cut mud (200-500 Hz) if needed (-1 to -3 dB, wide Q)
  - Notch out resonances (narrow Q)
  - Attenuate harshness (2-4 kHz) if needed

**Stage 2: Sweetening EQ** (After Compression)
- **Technology**: Linear Phase
- **Purpose**: Final tonal balance and enhancement
- **Typical moves**:
  - Broad tonal tilts (shelving)
  - Subtle presence boost (2-5 kHz, +1 to +2 dB)
  - Air enhancement (10-16 kHz, +1 to +2 dB, wide shelf)

### Mastering EQ Guidelines

**Critical principles**:
- **Rarely exceed ±6 dB** - Larger moves suggest mix problems
- **Use wide Q values** - Mastering EQ is broad, not surgical
- **Boost gently, cut surgically** - Cuts are more transparent
- **Always A/B** - Compare processed vs unprocessed

**Typical Q values**:
- **Shelving**: N/A (affects all frequencies above/below point)
- **Broad tonal shaping**: Q 0.5 - 1.5
- **Targeted adjustments**: Q 1.5 - 3.0
- **Problem frequency removal**: Q 3.0 - 6.0 (rare in mastering)

### Common Mastering EQ Moves

**Low-End Control**:
- HPF at 20-30 Hz: Remove subsonic waste
- Subtle low shelf (-1 to +1 dB at 60-100 Hz): Adjust weight

**Mid-Range Balance**:
- Cut mud (200-400 Hz, -1 to -2 dB, Q 1.0-1.5): Clean up
- Presence boost (2-4 kHz, +1 to +2 dB, Q 1.0-2.0): Clarity

**High-End Enhancement**:
- Air shelf (10-16 kHz, +1 to +2 dB): Openness and sparkle
- Be very gentle: High-end boosts easily sound harsh

---

## Compression in Mastering

### Primary Purpose: "Glue"

Mastering compression creates **cohesion**, making individual elements sound like unified whole. It does NOT make track louder (that's limiting).

### Standard Glue Compression

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Ratio** | 1.5:1 - 2:1 | Very gentle |
| **Attack** | 20-30 ms | Preserve transients |
| **Release** | 100-200 ms (Auto preferred) | Musical, tempo-aware |
| **Threshold** | Set for 1-2 dB GR MAX | Subtle cohesion only |
| **Knee** | Soft | Transparent, musical |

**Critical philosophy**: Compression should be **nearly imperceptible**. When bypassed, you should miss the "glue," not hear obvious level change.

**Target**: 1-2 dB gain reduction at loudest moments, NOT constant compression.

### Compressor Type Selection

**SSL-style VCA**:
- Clean, punchy, modern
- Best for: Electronic music, pop, rock
- Most common for electronic genres

**Opto** (LA-2A-style):
- Smooth, program-dependent release
- Best for: Smooth, musical genres
- Good for organic electronic (deep house, ambient)

**Variable-Mu** (Fairchild-style):
- Warm, rich, expensive sound
- Best for: Acoustic, jazz, high-end productions
- Can work for lounge/downtempo electronic

**Tube**:
- Colored, warm, harmonic enhancement
- Best for: When compression + saturation desired
- Good for vintage-styled electronic

### Advanced: Multiband Compression

**Purpose**: Independent dynamic control of frequency bands

**Use cases**:
- Control specific frequency ranges dynamically
- Tame harsh cymbals without affecting entire mix
- Control bass energy independently
- Manage frequency-specific dynamics

**Critical parameters**:
- **Soft Knee**: Essential for transparency
- **Crossover frequencies**: Typical splits: 80-100 Hz, 1-2 kHz, 8-10 kHz
- **Gentle ratios**: 2:1 - 3:1 per band
- **Minimal GR**: 1-2 dB per band MAX

**Warning**: Multiband compression introduces phase issues at crossovers. Use sparingly and with care.

**When to use**:
- Problem frequencies that need dynamic control (harsh cymbals, boomy bass)
- Electronic music with widely different frequency content
- When traditional compression doesn't solve issue

**When NOT to use**:
- Everywhere (overuse is common mistake)
- When simpler solution exists (EQ often better)
- If you can't hear clear improvement

### Parallel Compression in Mastering

**Rare but effective** when needing extra weight without sacrificing dynamics.

**Setup**:
1. Duplicate master track
2. Compress parallel track heavily (10:1+, fast attack/release)
3. Blend subtly (10-20% wet)

**Best for**: Adding body to sparse electronic tracks, enhancing sub-bass weight

---

## Loudness and Limiting

### Understanding LUFS

**LUFS** (Loudness Units relative to Full Scale) measures **perceived loudness**, not just peak level.

**Key concepts**:
- **Integrated LUFS**: Average loudness over entire track
- **Short-term LUFS**: Average over 3 seconds (more dynamic)
- **Momentary LUFS**: Average over 400ms (instantaneous)

**What matters most**: **Integrated LUFS** - this is streaming platform target

### True Peak vs Peak

**Peak** (dBFS):
- Sample-accurate measurement
- Shows highest sample value
- Misses inter-sample peaks

**True Peak** (dBTP):
- Accounts for inter-sample peaks
- More accurate representation of analog output
- What matters for delivery

**Critical**: Always use **True Peak limiting**, never standard peak limiting.

**Why**: When digital audio is converted to analog (DAC) or lossy codecs (MP3), inter-sample peaks can exceed 0 dBFS, causing distortion even if peak meter shows -0.1 dBFS.

### Limiter Setup

**Critical parameters**:

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **Ceiling** | -1.0 dBTP | Safe for all formats (can use -0.5 dBTP if needed) |
| **Attack** | 0-5 ms | Fast enough to catch peaks |
| **Release** | 50-200 ms | Musical, prevents pumping |
| **Lookahead** | ON (1-5 ms) | Allows limiter to "see" peaks ahead |
| **Oversampling** | ON (4x or 8x) | Accurate inter-sample peak detection |

**Loudness target approach**:
1. Set ceiling to -1.0 dBTP
2. Adjust threshold until reaching target LUFS (see platform targets below)
3. Check that gain reduction never exceeds 3-4 dB
4. If more GR needed → mix has problems, don't force it

**Red flags**:
- Consistent 5+ dB gain reduction → Over-limiting, will sound squashed
- Pumping/breathing → Release too fast or too much GR
- Loss of transients → Too aggressive limiting

---

## Stereo Processing

### Mid/Side (M-S) Processing

**Concept**: Process center (Mid) and sides (Side) independently

**Mid channel**: Mono sum of L+R (center content)
**Side channel**: Difference between L-R (stereo width content)

### M-S EQ Strategy

**Critical application: Low-end mono compatibility**

**Setup**:
- **HPF on Side channel**: 100-200 Hz
- **Purpose**: Makes low-end essentially mono
- **Benefit**: Powerful, focused bass; mono-compatible; prevents phase issues

**High-end width enhancement**:
- **Boost Side channel**: 8-16 kHz (+1 to +2 dB, wide shelf)
- **Purpose**: Adds stereo width and air
- **Result**: Wider, more open mix without affecting center power

### Stereo Width Control

**Make wider**:
- Boost Side channel (especially high frequencies)
- Use stereo widener (use with extreme caution)
- M-S imager

**Make narrower** (more mono-compatible):
- Reduce Side channel
- HPF on Side channel (remove low-end width)
- Check correlation meter (aim for +0.5 to +1.0)

### Correlation Meter

Displays phase relationship between L and R:
- **+1**: Perfect mono (identical L and R)
- **+0.5 to +1**: Good stereo, mono-compatible
- **0**: Uncorrelated (very wide stereo)
- **-1**: Perfect anti-phase (serious problems)

**Target**: Average around +0.7, never consistently below +0.3

**Warning**: Consistent readings below 0 indicate phase problems that will cause cancellation in mono.

---

## Dithering and Bit Depth

### What is Dithering?

**Dithering** adds intentional low-level noise to mask quantization distortion when reducing bit depth.

**When to use**: **ONLY when reducing to 16-bit** (e.g., CD)
**When NOT to use**: 24-bit or 32-bit float exports (streaming, archival)

### Quantization Distortion

When reducing bit depth (24-bit → 16-bit), audio that doesn't fit into new resolution gets truncated, introducing:
- Non-linear distortion
- Harmonic artifacts
- Especially audible in quiet passages and reverb tails

**Solution**: Dithering "linearizes" this distortion by trading it for slight noise floor increase (practically inaudible).

### Dither + Noise Shaping

**Noise Shaping**: Filters dither noise into frequency range where human hearing is less sensitive (above 14 kHz).

**Result**: Lower perceived noise floor, cleaner sound.

### Dither Algorithm Selection

**POW-r Type 1** (No Shaping):
- Flat dither noise across spectrum
- Best for: 24-bit exports (where dither nearly imperceptible anyway)
- Use when: Noise shaping not needed

**POW-r Type 2** (Moderate Shaping):
- Balanced noise shaping
- Best for: Pop, rock, electronic music to 16-bit
- Most common choice for general music

**POW-r Type 3** (Aggressive Shaping):
- Maximum noise reduction in audible range
- Best for: Classical, acoustic, high-dynamic music to 16-bit
- Use when: Preserving quiet passages critical

### Critical Dither Rules

1. **Apply ONLY ONCE** - At final export
2. **Last process in chain** - After limiter, after everything
3. **Never dither 24-bit exports** - Only 16-bit
4. **Can't undo** - Once dithered, done

---

## Delivery Standards

### Streaming Platform Targets

| Platform | Integrated LUFS Target | Max True Peak | Notes |
|----------|----------------------|---------------|-------|
| **Spotify** | -14 LUFS | -1 dBTP | Most common standard |
| **Apple Music** | -16 LUFS | -1 dBTP | More dynamic |
| **YouTube/YouTube Music** | -13 to -14 LUFS | -1 dBTP | Often normalizes to -14 |
| **Tidal** | -14 LUFS | -1 dBTP (HiFi: -0.5 dBTP) | Higher quality formats |
| **Amazon Music** | -13 LUFS | -1 dBTP | Slightly louder |
| **Deezer** | -14 to -15 LUFS | -1 dBTP | Similar to Spotify |

### Universal Target (Recommended)

**-14 LUFS Integrated + -1.0 dBTP ceiling**

**Rationale**:
- Spotify: No adjustment
- Apple Music: Turns down 2 dB (preserves dynamics)
- YouTube: Minimal or no adjustment
- Works for 95% of streaming scenarios

**Result**: Single master works across platforms without separate versions.

### Export Specifications

**For Streaming** (Most common):
- **Format**: WAV or AIFF
- **Bit Depth**: 24-bit (never 16-bit for streaming)
- **Sample Rate**: 44.1 kHz or 48 kHz
- **Dither**: NO (platforms handle their own encoding)

**For CD**:
- **Format**: WAV
- **Bit Depth**: 16-bit
- **Sample Rate**: 44.1 kHz (CD standard)
- **Dither**: YES (POW-r Type 2 or 3)

**For High-Resolution**:
- **Format**: WAV or FLAC
- **Bit Depth**: 24-bit
- **Sample Rate**: 96 kHz or 192 kHz
- **Dither**: NO

### Mix Delivery to Mastering Engineer

**Specifications**:
- **Peak Level**: -6 dBFS
- **Format**: 24-bit or 32-bit float WAV
- **Sample Rate**: Match recording (44.1 kHz or higher)
- **Processing**: NO limiter on master, NO dither
- **Headroom**: Essential for mastering engineer to work

---

## Genre-Specific Approaches

### Techno / Minimal

**Loudness target**: -8 to -10 LUFS (louder than streaming standard)
**Dynamics**: Minimal (heavily compressed)
**Focus**: Sub-bass power, tight low-end, bright hi-hats

**Chain**:
1. Corrective EQ (clean low-end, tame harshness)
2. Multiband compression (independent bass/mid/high control)
3. Glue compression (2:1, 2-3 dB GR)
4. Aggressive limiter (3-4 dB GR)

**Special considerations**:
- M-S: HPF Side at 100-150 Hz (mono sub-bass)
- May need multiband to control bright hi-hats
- Focus on consistent, driving energy

### House / Deep House

**Loudness target**: -10 to -12 LUFS (balanced)
**Dynamics**: Moderate (more dynamic than techno)
**Focus**: Warmth, groove, balanced spectrum

**Chain**:
1. Corrective EQ (balance warmth vs clarity)
2. Gentle glue compression (1.5:1-2:1, 1-2 dB GR)
3. Sweetening EQ (enhance air, warmth)
4. Moderate limiter (2-3 dB GR)

**Special considerations**:
- Preserve groove and dynamics
- Warmer overall tone than techno
- M-S: Subtle Side boost at 8-16 kHz for width

### Drum & Bass / Dubstep

**Loudness target**: -8 to -10 LUFS (very loud)
**Dynamics**: Aggressive (bass-focused, bright)
**Focus**: Massive bass, tight drums, aggressive high-end

**Chain**:
1. Corrective EQ (manage massive bass energy)
2. Multiband compression (essential for bass control)
3. Glue compression (2:1, 2-3 dB GR)
4. Aggressive limiter (3-5 dB GR acceptable)

**Special considerations**:
- Bass often dominates spectrum
- May need multiband to control bass without affecting drums
- Very bright, aggressive master
- M-S: HPF Side at 150-200 Hz (bass is mono)

### Trap / Hip-Hop

**Loudness target**: -10 to -12 LUFS
**Dynamics**: Moderate (vocal-focused)
**Focus**: 808 sub-bass, vocal clarity, air

**Chain**:
1. Corrective EQ (balance 808 power vs vocal clarity)
2. Gentle glue compression (2:1, 1-2 dB GR)
3. Sweetening EQ (enhance vocal presence, air)
4. Moderate limiter (2-3 dB GR)

**Special considerations**:
- 808 kick/bass is often tuned, needs space
- Vocal must cut through without being harsh
- Extreme high-end air (10-16 kHz)
- M-S: HPF Side at 100 Hz, boost Side at 10-16 kHz

---

## Mastering Workflow: Complete Process

### Phase 1: Preparation (Before Processing)

1. **Import Mix**
   - Verify specifications (-6 dBFS peak, 24-bit)
   - Check for clipping or distortion
   - Note any issues

2. **Critical Listening** (No processing)
   - Listen at 85 dB SPL
   - Take detailed notes
   - Assess: Tonal balance, dynamics, stereo image, defects

3. **Reference Tracks**
   - Load 1-2 commercial masters in similar genre
   - Level-match (turn reference DOWN to match mix)
   - A/B frequently

4. **Define Goals**
   - Identify what needs improvement
   - Set target LUFS (usually -14)
   - Plan processing approach

### Phase 2: Processing

1. **Gain Staging**
   - Trim input if needed
   - Target: -18 dBFS RMS average

2. **Corrective EQ** (Minimum Phase)
   - HPF at 20-30 Hz
   - Remove mud (200-500 Hz)
   - Tame harshness if needed

3. **Glue Compression**
   - Ratio: 1.5:1 - 2:1
   - Target: 1-2 dB GR
   - A/B frequently

4. **Sweetening EQ** (Linear Phase)
   - Broad tonal adjustments
   - Presence boost
   - Air enhancement

5. **Multiband** (If needed)
   - Address specific frequency problems
   - Gentle ratios, minimal GR

6. **M-S Processing**
   - HPF Side at 100-200 Hz
   - Optional: Boost Side at 8-16 kHz

7. **Limiting**
   - Ceiling: -1.0 dBTP
   - Adjust threshold for target LUFS
   - Check GR never exceeds 3-4 dB

### Phase 3: Verification

1. **A/B with Reference**
   - Match loudness (turn yours DOWN)
   - Compare: Tone, dynamics, width
   - Adjust as needed

2. **Metering Check**
   - Integrated LUFS: Target achieved?
   - True Peak: Below -1.0 dBTP?
   - Correlation: Averaging +0.7?

3. **Translation Test**
   - Listen on multiple systems
   - Check mono compatibility
   - Verify on earbuds, laptop, car

4. **Final Checks**
   - No clipping or distortion
   - Smooth fade-ins/outs if needed
   - Verify metadata

### Phase 4: Export

1. **For Streaming**:
   - 24-bit WAV
   - 44.1 kHz or 48 kHz
   - NO dither

2. **For CD**:
   - 16-bit WAV
   - 44.1 kHz
   - YES dither (POW-r Type 2)

3. **Archive Master**:
   - 24-bit or 32-bit float WAV
   - Same sample rate as project
   - NO limiting version (safety)

---

## Common Mastering Mistakes

### 1. Over-Processing

**Problem**: Too much EQ, compression, or limiting
**Symptoms**: Lifeless, squashed, harsh
**Solution**: Less is more; always A/B bypass

### 2. Ignoring Headroom

**Problem**: Mix delivered at 0 dBFS peak
**Symptoms**: No room for mastering processing
**Solution**: Request proper mix (-6 dBFS peak)

### 3. Chasing Loudness

**Problem**: Over-limiting to achieve extreme loudness
**Symptoms**: Pumping, distortion, lifeless
**Solution**: Target appropriate LUFS for genre/platform

### 4. Poor Room Acoustics

**Problem**: Untreated room, unreliable monitoring
**Symptoms**: Inconsistent results, poor translation
**Solution**: Treat room or use quality headphones + references

### 5. No Reference Tracks

**Problem**: Working in isolation without comparison
**Symptoms**: Losing perspective, wrong tonal balance
**Solution**: Always use reference tracks

### 6. Incorrect Dither Usage

**Problem**: Dithering 24-bit files or multiple times
**Symptoms**: Unnecessary noise floor
**Solution**: Dither only once, only to 16-bit

### 7. Fixing Mix Problems in Mastering

**Problem**: Attempting radical fixes
**Symptoms**: Unnatural sound, new problems created
**Solution**: Send back to mixing

---

## Critical Mastering Reminders

### Philosophy

1. **Enhancement, not repair** - Good masters come from good mixes
2. **Subtlety is power** - Small adjustments, big impact
3. **Context is everything** - Always use references
4. **Ears over meters** - Meters guide, ears decide
5. **Less is more** - Process only what's needed

### Technical

1. **Always use True Peak limiting** - Never standard peak
2. **Dither only once** - To 16-bit only, as last step
3. **HPF the Side** - Mono low-end essential (100-200 Hz)
4. **Target -14 LUFS** - Universal streaming standard
5. **Leave -1.0 dBTP headroom** - Safety for all codecs

### Workflow

1. **Listen first** - No processing until plan formed
2. **Use references** - Level-matched A/B comparison
3. **Process chain order matters** - Correct → Compress → Sweeten → Limit
4. **Check on multiple systems** - Translation is critical
5. **Take breaks** - Ear fatigue is real

---

## Summary: Mastering Approach

1. **Understand purpose** - Enhancement, consistency, preparation
2. **Prepare properly** - Good mix with headroom essential
3. **Listen critically** - Form plan before processing
4. **Process intentionally** - Each move has clear purpose
5. **Use appropriate tools** - Right tool for each job
6. **Target platform standards** - -14 LUFS, -1.0 dBTP for streaming
7. **Verify thoroughly** - Check meters, references, multiple systems
8. **Export correctly** - 24-bit for streaming, 16-bit with dither for CD

**Remember**: Mastering is the final 10% that elevates a mix to professional release. It requires specialized skills, critical listening, and proper monitoring. When done well, mastering is nearly invisible—the track just sounds "right" across all systems.

Use this reference to understand mastering principles, processing chains, and technical standards. Then apply with subtlety and musical intention to create professional, competitive masters.
