# Dynamics Processing Reference

## Overview
Comprehensive guide to dynamic range control including compression, limiting, expansion, gating, and transient shaping. This reference covers technical parameters, practical applications, and advanced techniques for professional mixing and mastering.

---

## Table of Contents
1. [Dynamics Fundamentals](#dynamics-fundamentals)
2. [Compression Basics](#compression-basics)
3. [Compressor Types](#compressor-types)
4. [Compression Techniques](#compression-techniques)
5. [Limiting](#limiting)
6. [Gating & Expansion](#gating--expansion)
7. [Transient Shaping](#transient-shaping)
8. [Parallel Processing](#parallel-processing)
9. [Multiband Dynamics](#multiband-dynamics)
10. [Advanced Techniques](#advanced-techniques)
11. [Common Mistakes](#common-mistakes)

---

## Dynamics Fundamentals

### Understanding Dynamic Range

**Definition:**
- Difference between loudest and quietest parts
- Measured in decibels (dB)
- Natural dynamics vary by source:
  - Orchestra: 70+ dB
  - Rock band: 40-50 dB
  - Vocals: 20-30 dB
  - Electronic music: 10-20 dB

**Why Control Dynamics:**
- Maintain consistent levels
- Prevent clipping/distortion
- Improve clarity and punch
- Maximize perceived loudness
- Control competing elements
- Add character and tone

**Dynamic Processing Goals:**
- Control peaks (prevent distortion)
- Raise quiet parts (improve clarity)
- Shape tone and character
- Glue mix elements together
- Achieve competitive loudness
- Preserve musicality

### Peak vs RMS Measurement

**Peak Level:**
- Instantaneous maximum amplitude
- Measures transient peaks
- Important for preventing clipping
- Doesn't reflect perceived loudness
- Fast response time

**RMS (Root Mean Square):**
- Average level over time
- Better reflects perceived loudness
- Closer to how we hear
- Used in most compressors
- Slower response than peak

**Practical Application:**
```
Peak Detection:
- Use for: Fast transients (drums)
- Catches quick peaks
- Prevents overs
- Aggressive control

RMS Detection:
- Use for: Vocals, bass, mix bus
- Musical, natural sound
- Responds to average level
- Less aggressive
```

### Gain Reduction Basics

**Concept:**
- Amount of level reduction applied
- Measured in decibels (dB)
- Shown on GR meter
- Returned via makeup gain

**Typical Amounts:**
```
Subtle: 1-3 dB GR
  - Transparent control
  - Gentle shaping
  - Mix bus, mastering

Moderate: 3-6 dB GR
  - Noticeable control
  - Standard mixing
  - Most applications

Heavy: 6-12 dB GR
  - Obvious effect
  - Character/color
  - Drums, vocals (style-dependent)

Extreme: 12+ dB GR
  - Special effects
  - Parallel processing
  - Limiting
```

---

## Compression Basics

### Core Parameters

#### **1. Threshold**
```
Definition: Level at which compression begins

Setting Guidelines:
- Lower threshold = More compression
- Higher threshold = Less compression
- Adjust to taste and material

By Source:
- Vocals: -20 to -10 dBFS
- Drums: -15 to -5 dBFS
- Bass: -25 to -15 dBFS
- Mix bus: -10 to -3 dBFS

Tips:
- Start high, lower until desired GR
- Watch GR meter for feedback
- Listen for pumping/breathing
- Consider dynamic range of source
```

#### **2. Ratio**
```
Definition: Amount of gain reduction applied above threshold

Ratios Explained:
2:1 = Gentle (2 dB in = 1 dB out above threshold)
4:1 = Moderate (4 dB in = 1 dB out)
8:1 = Heavy (8 dB in = 1 dB out)
10:1+ = Limiting (virtually stops signal growth)
∞:1 = Hard limiting (brick wall)

By Application:
Subtle/Transparent:
- 1.5:1 to 2:1
- Mix bus
- Mastering
- Natural sources

Musical/Standard:
- 3:1 to 4:1
- Vocals
- Bass
- Most instruments

Aggressive/Character:
- 6:1 to 10:1
- Drums (parallel)
- Special effects
- Heavy control

Limiting:
- 10:1 to ∞:1
- Peak control
- Maximizing loudness
- Mastering
```

#### **3. Attack Time**
```
Definition: How quickly compressor responds to signal

Range: 0.1 ms - 100+ ms typical

Fast Attack (0.1-10 ms):
- Catches transients
- Controls peaks
- Can dull transients
- Tighter sound
Use for: Limiting, peak control

Medium Attack (10-30 ms):
- Balanced response
- Preserves some transient
- Natural sound
- Versatile
Use for: Vocals, bass, general

Slow Attack (30-100+ ms):
- Lets transients through
- Preserves punch
- More dynamic
- Can sound inconsistent
Use for: Drums, adding punch

By Instrument:
Vocals: 5-20 ms (medium)
Kick: 20-50 ms (slow, preserve punch)
Snare: 1-10 ms (fast) or 20-40 ms (slow for punch)
Bass: 10-30 ms (medium)
Mix bus: 20-40 ms (slow, preserve transients)
```

#### **4. Release Time**
```
Definition: How quickly compressor stops compressing

Range: 10 ms - 2+ seconds typical

Fast Release (10-100 ms):
- Quick recovery
- More audible
- Can pump/breathe
- Energetic
Use for: Fast material, energy

Medium Release (100-300 ms):
- Balanced, natural
- Most versatile
- Standard setting
Use for: Most applications

Slow Release (300 ms - 2+ seconds):
- Smooth, gentle
- Less noticeable
- Can sound sluggish
- Transparent
Use for: Mix bus, mastering, slow material

Auto Release:
- Adapts to material
- Program-dependent
- Convenient
- Usually works well

Tempo Sync:
- Match to song tempo
- Musical relationship
- Rhythmic effect
- Quarter note = 500ms at 120 BPM

By Application:
Vocals: Auto or 200-400 ms
Drums: 50-150 ms (fast for energy)
Bass: 150-300 ms (medium)
Mix bus: Auto or 300-500 ms
Mastering: 300-600 ms (slow, smooth)
```

#### **5. Knee**
```
Definition: How gradually compression engages

Hard Knee:
- Abrupt compression onset
- More obvious effect
- Precise control
- Vintage character
Use for: Aggressive compression, limiting

Soft Knee:
- Gradual compression onset
- More transparent
- Musical, gentle
- Modern sound
Use for: Subtle compression, vocals, mix bus

Settings:
- 0 dB = Hard knee
- 3-6 dB = Medium knee
- 10+ dB = Soft knee

Practical Impact:
- Soft knee = more transparent at low ratios
- Hard knee = more character, obvious effect
- Mix bus often uses soft knee
- Drums may benefit from hard knee
```

#### **6. Makeup Gain**
```
Definition: Compensates for gain reduction

Purpose:
- Match output to input level
- Maintain perceived loudness
- Enables fair comparison

Guidelines:
- Add gain equal to average GR
- Example: 6 dB GR → +6 dB makeup
- Listen at matched levels for accurate judgment
- Some compressors have auto-makeup

Caution:
- Don't over-compensate
- Can make everything sound "better" falsely
- True bypass comparison critical
- Watch output meters
```

### Compression Workflow

**Step-by-Step Process:**
```
1. Set Ratio:
   - Start with 3:1 or 4:1
   - Adjust based on goal

2. Adjust Threshold:
   - Lower until desired GR achieved
   - Watch GR meter
   - Aim for 3-6 dB typically

3. Set Attack:
   - Fast for peak control
   - Slow to preserve transients
   - Adjust to taste

4. Set Release:
   - Start with auto or 200-300 ms
   - Adjust for pumping/breathing
   - Match to material tempo

5. Adjust Knee:
   - Soft for transparent
   - Hard for character

6. Add Makeup Gain:
   - Match input level
   - Enable fair comparison

7. A/B Test:
   - Compare to bypass
   - Ensure improvement
   - Adjust as needed
```

---

## Compressor Types

### VCA (Voltage Controlled Amplifier)

**Characteristics:**
- Clean, precise, modern
- Fast, accurate response
- Transparent to colored (varies)
- Versatile, reliable
- Consistent performance

**Famous Examples:**
- SSL Bus Compressor (mix bus legend)
- API 2500
- DBX 160
- Focusrite Red 3

**Tone:**
- Clean to slightly colored
- Punchy, tight
- Controlled, predictable
- Professional standard

**Best For:**
- Mix bus compression
- Drums and percussion
- Modern productions
- When precision needed
- Rock, pop, electronic

**Typical Settings:**
```
Mix Bus:
- Ratio: 2:1 to 4:1
- Attack: 30 ms
- Release: Auto or 300 ms
- Knee: Soft
- GR: 2-3 dB
```

### Optical (Opto)

**Characteristics:**
- Smooth, musical compression
- Program-dependent behavior
- Slow attack naturally
- Non-linear response
- Gentle, transparent

**Technology:**
- Light-dependent resistor
- Natural release curve
- Slower than VCA
- Unique character

**Famous Examples:**
- LA-2A (legendary vocal comp)
- LA-3A (faster attack version)
- Tube-Tech CL 1B
- Universal Audio LA-610

**Tone:**
- Warm, smooth, musical
- Vintage character
- Slightly colored
- Flattering to sources

**Best For:**
- Vocals (especially lead)
- Bass guitar
- Acoustic instruments
- Smooth, natural compression
- When transparency critical

**Typical Settings:**
```
Vocals (LA-2A style):
- Peak Reduction: Adjust to 3-6 dB GR
- Gain: Makeup gain
- No attack/release (fixed)
- Simple, effective

Bass:
- Similar to vocals
- Smooth, consistent level
- Preserves tone
```

### FET (Field Effect Transistor)

**Characteristics:**
- Fast, aggressive
- Colored, character-rich
- Can be subtle or extreme
- Punch and energy
- Variable control

**Technology:**
- Solid-state (transistor)
- Very fast attack possible
- Distortion when pushed
- Adds harmonics

**Famous Examples:**
- 1176 (the most famous)
- Distressor
- Empirical Labs EL8

**Tone:**
- Aggressive, present
- Adds excitement
- Slight to heavy coloration
- Punchy, in-your-face

**1176 Characteristics:**
- Attack: 20-800 μs (incredibly fast)
- Release: 50-1100 ms
- Ratio: 4:1, 8:1, 12:1, 20:1
- "All buttons in" mode (special aggressive sound)

**Best For:**
- Aggressive vocals
- Drums (especially room mics)
- Guitars
- Parallel compression
- Rock, punk, indie

**Typical Settings:**
```
Vocals (1176 style):
- Ratio: 4:1 or 8:1
- Attack: Fastest (2-3 o'clock)
- Release: Fastest or 5 o'clock
- GR: 4-8 dB
- Character-rich

Drums Parallel:
- Ratio: All buttons in (20:1)
- Attack: Fast
- Release: Fast
- Heavy GR (10+ dB)
- Blend to taste
```

### Tube/Valve

**Characteristics:**
- Warm, vintage tone
- Soft, musical compression
- Harmonic saturation
- Slow, gentle action
- High-quality coloration

**Technology:**
- Vacuum tube gain stage
- Natural soft-knee response
- Adds even harmonics
- Vintage circuit design

**Famous Examples:**
- Fairchild 660/670 (holy grail)
- Manley Variable Mu
- Thermionic Culture Phoenix

**Tone:**
- Extremely warm
- Smooth, luxurious
- Obvious coloration
- Vintage character
- Expensive sound

**Best For:**
- Mix bus compression
- Mastering
- Vocals (ballads, jazz)
- When vintage vibe desired
- Luxury, high-end productions

**Typical Settings:**
```
Mix Bus (Variable Mu style):
- Ratio: 1.5:1 to 3:1
- Attack: Medium-slow
- Release: Auto or slow
- GR: 1-3 dB
- Warm, glued sound

Mastering:
- Very subtle
- 1-2 dB GR maximum
- Slow attack/release
- Adds cohesion and warmth
```

### Digital/Modern

**Characteristics:**
- Transparent to colored
- Precise, repeatable
- Advanced features
- Visual feedback
- Flexible routing

**Capabilities:**
- Any compressor type emulation
- Lookahead (perfect peak control)
- Mid-side processing
- Multiband options
- Linear phase possible

**Advantages:**
- Total recall
- Consistency
- No maintenance
- Affordable
- Versatile

**Best For:**
- Modern productions
- When precision needed
- Mastering (lookahead)
- Budget constraints
- In-the-box workflow

**Notable Plugins:**
- FabFilter Pro-C 2
- Waves C1/C4/C6
- UAD emulations
- iZotope dynamics

---

## Compression Techniques

### Serial Compression

**Concept:**
- Multiple compressors in series
- Each does small amount
- More transparent than single heavy comp
- Professional technique

**Benefits:**
- More natural sound
- Greater control
- Different character per stage
- Cumulative effect

**Example Chain:**
```
Vocal Serial Compression:

Stage 1 - Peak Control (FET):
- Ratio: 4:1
- Fast attack
- Catches peaks
- GR: 3-4 dB

Stage 2 - Tone/Body (Opto):
- Ratio: 3:1
- Medium attack
- Adds warmth
- GR: 2-3 dB

Stage 3 - Glue (VCA):
- Ratio: 2:1
- Slow attack
- Final polish
- GR: 1-2 dB

Total GR: 6-9 dB (split across 3 stages)
Result: Controlled yet natural
```

### Parallel Compression (NY Compression)

**Concept:**
- Heavily compress duplicate
- Blend with original
- Retains dynamics + adds power
- Essential technique

**Setup:**
```
Method 1: Aux Send
1. Send track to aux/bus
2. Heavy compression on aux (100% wet)
3. Blend aux fader with original
4. Control blend amount

Method 2: Duplicate Track
1. Duplicate audio track
2. Heavy compression on duplicate
3. Lower duplicate level
4. Blend to taste

Settings on Parallel Track:
- Ratio: 10:1 to 20:1 (very high)
- Attack: Fast (catch everything)
- Release: Fast to medium
- GR: 10-20 dB (extreme)
- High makeup gain
```

**Applications:**

**Drums Parallel:**
```
Compressor Settings:
- Ratio: 20:1 or "All buttons in" (1176)
- Attack: Fastest
- Release: Fast (50-100 ms)
- Threshold: Very low
- Makeup: High (+20 dB)
- GR: 15-20 dB

Blend:
- Mix at 20-40% with original
- Adds power without killing dynamics
- Punchy, energetic drums
- Maintains transients
```

**Vocals Parallel:**
```
Compressor Settings:
- Ratio: 8:1 to 10:1
- Attack: Medium (5-15 ms)
- Release: Auto or 150 ms
- GR: 10-15 dB
- Heavy makeup gain

Blend:
- Mix at 20-30% with original
- Brings up quiet parts
- Maintains dynamic range
- Present, consistent vocal
```

**Benefits:**
- Extreme processing without artifacts
- Retains natural dynamics
- Adds power and energy
- Very common technique
- Essential for modern mixes

### Sidechain Compression

**Concept:**
- External signal triggers compression
- Classic: Kick sidechains bass
- Creates rhythmic pumping
- Frequency-specific possible

**Applications:**

**Kick/Bass Ducking:**
```
Setup:
1. Insert compressor on bass track
2. Send kick to compressor sidechain
3. Bass ducks when kick hits

Settings:
- Ratio: 4:1 to 8:1
- Attack: Fast (1-10 ms)
- Release: 100-200 ms (adjust to tempo)
- GR: 3-6 dB when kick hits

Result:
- Clear kick/bass separation
- Tight low-end
- No frequency conflict
- Professional technique
```

**Frequency-Specific Sidechain:**
```
Advanced Technique:
1. Filter sidechain signal
2. Only certain frequencies trigger compression
3. More surgical control

Bass/Kick Example:
- HPF sidechain at 60 Hz
- LPF sidechain at 120 Hz
- Only kick fundamental triggers ducking
- More transparent than full-range

Vocal/Pad Example:
- Filter pad sidechain to vocal range
- Pad ducks only where vocal present
- Automatic space for vocals
```

**Creative Sidechaining:**
```
Pumping Effect (EDM):
- Ratio: 8:1 to 20:1
- Fast attack (0.1-1 ms)
- Medium-fast release (50-150 ms, sync to tempo)
- Heavy GR (6-12 dB)
- Obvious rhythmic pumping

Ducking Pads for Vocals:
- Moderate ratio (4:1)
- Medium attack (10-20 ms)
- Tempo-synced release
- Subtle GR (2-4 dB)
- Automatic vocal space
```

### Upward Compression

**Concept:**
- Opposite of normal compression
- Raises quiet parts instead of lowering loud parts
- Less common but powerful
- Requires specific processors

**Characteristics:**
- Increases level below threshold
- Useful for bringing up details
- Can increase noise
- More transparent than limiting

**Applications:**
```
Detailed Vocals:
- Brings up breaths and nuance
- More intimate sound
- Be careful with noise

Drum Rooms:
- Increases ambience
- More "roomy" sound
- Natural reverb enhanced

Mastering:
- Increase sustain and body
- Alternative to compression
- Preserves transients better
```

---

## Limiting

### Limiting Fundamentals

**Definition:**
- Extreme compression (∞:1 or 10:1+)
- Prevents signal exceeding threshold
- Brick wall protection
- Maximizes loudness

**Purpose:**
- Peak control
- Loudness maximization
- Prevent clipping/overs
- Final safety net
- Competitive loudness

**Parameters:**

**Ceiling:**
```
Definition: Maximum output level
- Set to -0.1 to -0.3 dBFS (digital safety)
- Or -1.0 dBFS (more headroom)
- Never 0.0 dBFS (can cause issues)

Mastering:
- True Peak limiting: -1.0 dBTP
- Accounts for inter-sample peaks
- Required for streaming
- Professional standard
```

**Threshold:**
```
Definition: Level at which limiting begins
- Lower threshold = More limiting
- Higher threshold = Less limiting
- Determines loudness

Target Levels:
- Mastering: Adjust for desired LUFS
- Mix bus: -3 to -6 dB headroom below ceiling
- Individual tracks: Varies by need
```

### Limiting Techniques

**Transparent Limiting:**
```
Goal: Maximum loudness with minimal artifacts

Settings:
- Attack: Fast (0.1-1 ms)
- Release: Auto or medium (100-300 ms)
- Lookahead: 5-10 ms (if available)
- GR: 3-6 dB maximum
- Oversampling: ON

Tips:
- Don't push too hard
- Watch for distortion
- Preserve dynamics
- Multiple gentle passes better than one heavy
```

**Brick Wall Limiting:**
```
Goal: Absolute peak control

Settings:
- Attack: Fastest (0.01-0.1 ms)
- Release: Fast (10-50 ms)
- Ceiling: -0.1 dBFS
- Hard clip protection: ON

Use Cases:
- Final safety limiter
- Preventing overs absolutely
- Dance music loudness
- Not for subtle work
```

**Multi-Stage Limiting:**
```
Concept: Multiple limiters in series
- Each does less work
- More transparent
- Professional mastering technique

Example Chain:
Stage 1 (Clip Control):
- Fast limiter
- Catches peaks
- GR: 1-2 dB
- Ceiling: -1.0 dB

Stage 2 (Loudness):
- Medium limiter
- Increases RMS
- GR: 2-4 dB
- Ceiling: -0.3 dB

Stage 3 (Safety):
- Brick wall
- Final protection
- GR: 0-1 dB
- Ceiling: -0.1 dB
```

### True Peak Limiting

**Concept:**
- Accounts for inter-sample peaks
- Prevents reconstruction distortion
- Essential for digital distribution
- Modern standard

**Technical Details:**
```
Problem:
- Sample peaks may not be true peaks
- D/A conversion can create higher peaks
- Can cause distortion on playback systems

Solution:
- True Peak limiting
- Oversample and detect inter-sample peaks
- Limit to -1.0 dBTP (True Peak)
- Required for Spotify, Apple Music, etc.
```

**Settings:**
```
Streaming Master:
- True Peak ceiling: -1.0 dBTP
- Oversampling: 4x minimum
- Target LUFS: -14 LUFS (Spotify/Apple Music)
- GR: Adjust to reach target

CD Master:
- Can be less strict (-0.3 dBTP)
- Higher loudness possible
- Still use true peak detection
```

---

## Gating & Expansion

### Noise Gate Basics

**Purpose:**
- Remove unwanted noise
- Clean up tracks
- Tighten recordings
- Control bleed

**Parameters:**

**Threshold:**
```
- Level at which gate opens
- Set just above noise floor
- Too high = cuts wanted signal
- Too low = doesn't gate noise

Setting:
- Find noise level
- Set 3-6 dB above
- Adjust while listening
```

**Attack:**
```
- How fast gate opens
- Fast: Natural transients preserved
- Slow: Can cut off beginning

Typical:
- Drums: 0.1-5 ms (fast)
- Vocals: 5-20 ms (medium)
- Effects: Varies
```

**Hold:**
```
- How long gate stays open after signal drops
- Prevents choppy gating
- Match to material decay

Settings:
- Drums: 10-50 ms
- Sustained instruments: 100-500 ms
- Adjust to avoid cutting decay unnaturally
```

**Release:**
```
- How fast gate closes
- Fast: Abrupt, unnatural
- Slow: Smoother, natural

Typical:
- Fast: 10-50 ms
- Medium: 50-200 ms
- Slow: 200-500 ms

Adjust to avoid audible pumping
```

### Gate Applications

**Drum Gating:**
```
Kick Drum:
- Tighten and control
- Remove bleed
Settings:
- Threshold: Just above bleed
- Attack: Fast (0.1-1 ms)
- Hold: 50-100 ms
- Release: 50-100 ms

Snare:
- Remove hi-hat bleed
- Tighten tone
Settings:
- Threshold: Above bleed
- Attack: Fast (0.1-1 ms)
- Hold: 30-80 ms
- Release: 30-100 ms
- Filter: HPF to ignore kick bleed

Toms:
- Only sound when hit
- Clean recording
Settings:
- Threshold: Above bleed
- Attack: Fast
- Hold: Longer (200-500 ms)
- Release: Match tom ring
```

**Vocal Gating:**
```
Purpose:
- Remove breath noise
- Clean up between phrases
- Tighten performance

Settings:
- Threshold: Above breaths
- Attack: Medium (10-20 ms)
- Hold: Short (20-50 ms)
- Release: Medium (100-200 ms)

Caution:
- Can sound unnatural
- Manual editing often better
- Use subtly
```

### Expander vs Gate

**Expander:**
- Gradual gain reduction below threshold
- More musical than hard gate
- Transparent noise reduction
- Preferred for music

**Characteristics:**
```
Gate:
- On/off (binary)
- Hard threshold
- Can sound obvious
- Good for extreme situations

Expander:
- Ratio-based (2:1, 3:1, etc.)
- Gradual reduction
- More transparent
- Better for music
```

**Expander Applications:**
```
Drum Ambience Control:
- Ratio: 2:1 or 3:1
- Reduces room sound between hits
- More natural than gate
- Maintains some ambience

Vocal Cleanup:
- Ratio: 1.5:1 to 2:1
- Gently reduces noise
- Sounds more natural
- Professional approach

Settings:
- Threshold: Above noise floor
- Ratio: 2:1 to 3:1 typical
- Attack: Medium
- Release: Medium
- Range: 6-12 dB reduction
```

---

## Transient Shaping

### Transient Designer Concept

**What It Does:**
- Independently control attack and sustain
- No threshold (always active)
- Shape transients without traditional compression
- Powerful drum tool

**Parameters:**

**Attack:**
```
- Enhances or reduces transient
- Positive = More punch
- Negative = Less punch/click

Applications:
- Kick: Increase for more click/punch
- Snare: Increase for more crack
- Room mics: Decrease for smoother sound
- Guitars: Increase pick attack
```

**Sustain:**
```
- Enhances or reduces body/decay
- Positive = More sustain/ring
- Negative = Tighter, shorter

Applications:
- Kick: Decrease for tighter sound
- Snare: Adjust ring/sustain
- Toms: Increase for more body or decrease to tighten
- Cymbals: Increase for more shimmer
```

### Transient Shaping Applications

**Drum Enhancement:**
```
Kick:
- Attack: +3 to +6 dB (more punch)
- Sustain: -3 to -6 dB (tighter)
Result: Punchy, controlled kick

Snare:
- Attack: +4 to +8 dB (more crack)
- Sustain: -2 to -4 dB (tighter)
Result: Aggressive, defined snare

Toms:
- Attack: +3 to +5 dB
- Sustain: Adjust for desired ring
Result: Clear attack, controlled decay

Overheads:
- Attack: -3 to -6 dB (smoother)
- Sustain: +2 to +4 dB (more shimmer)
Result: Smooth cymbals with sustain
```

**Bass Tightening:**
```
Electric Bass:
- Attack: +2 to +4 dB (more definition)
- Sustain: -2 to -4 dB (tighter)
Result: Defined, controlled bass

Synth Bass:
- Attack: +3 to +6 dB (more punch)
- Sustain: 0 to -3 dB
Result: Powerful transient, controlled body
```

**Acoustic Instruments:**
```
Acoustic Guitar:
- Attack: +2 to +4 dB (pick definition)
- Sustain: 0 to +2 dB (balanced)

Piano:
- Attack: +1 to +3 dB (hammer clarity)
- Sustain: 0 to +2 dB (natural body)
```

### Envelope Shaper vs Compressor

**When to Use Transient Shaper:**
- Need to enhance attack without compression
- Want to shape sound independent of level
- Drum shaping
- Quick transient control
- No threshold needed

**When to Use Compressor:**
- Need to control dynamic range
- Want to add character/color
- Level-dependent processing
- Gluing elements together
- Threshold-based control

**Combined Use:**
```
Professional Workflow:
1. Transient shaper first
   - Shape basic sound
   - Enhance/reduce transients
   
2. Compressor second
   - Control dynamics
   - Add tone/character
   - Glue sound

Example - Snare:
- Transient shaper: +6 dB attack, -3 dB sustain
- Then compressor: 4:1, fast attack, 3-4 dB GR
Result: Punchy, controlled, consistent
```

---

## Parallel Processing

### Parallel Compression Deep Dive

**Philosophy:**
- Best of both worlds
- Extreme processing + natural dynamics
- Modern mixing essential
- Professional standard

**Setup Methods:**

**Method 1: Aux/Bus Send**
```
Pros:
- Industry standard
- Easy blend control
- Minimal CPU (one instance)
- Can send multiple tracks to same bus

Setup:
1. Create aux track
2. Add compressor (100% wet)
3. Send source to aux
4. Blend with send level
```

**Method 2: Duplicate Track**
```
Pros:
- Independent processing
- Visual feedback
- Easy automation
- Can apply different plugins

Setup:
1. Duplicate audio track
2. Heavy compression on duplicate
3. Lower duplicate volume
4. Group both tracks
```

**Method 3: Built-in Parallel**
```
Some compressors have Mix/Blend knob:
- Single instance
- Internal parallel processing
- Convenient
- Less flexible

Examples:
- FabFilter Pro-C
- Waves CLA series
- Many modern plugins
```

### Advanced Parallel Techniques

**Parallel Saturation:**
```
Concept: Combine parallel compression + distortion

Setup:
1. Heavy compression on parallel track
2. Add saturation/distortion
3. Blend subtly (10-20%)

Result:
- Adds power and energy
- Harmonic excitement
- Maintains clean original
- Modern aggressive sound

Applications:
- Drums (huge sound)
- Bass (growl and power)
- Vocals (grit and presence)
```

**Parallel EQ:**
```
Concept: Extreme EQ blended with original

Vocal Presence Boost:
1. Duplicate vocal
2. Massive boost 3-5 kHz (+12 to +15 dB)
3. High shelf 10 kHz (+8 dB)
4. Blend 20-30%

Result:
- Extreme presence without harshness
- Natural tone preserved
- Vocal cuts through mix
```

**Multiband Parallel:**
```
Concept: Parallel process specific frequency ranges

Bass Example:
1. Duplicate bass
2. HPF duplicate at 100 Hz
3. Heavy compress high-passed version
4. Blend to add definition
5. Original provides natural low-end

Result:
- Defined midrange bass
- Natural low-end
- Clear on small speakers
- Powerful on big systems
```

---

## Multiband Dynamics

### Multiband Compression Basics

**Concept:**
- Split signal into frequency bands
- Compress each band independently
- Surgical dynamic control
- Professional tool

**Typical Band Division:**
```
3-Band:
- Low: 20-250 Hz
- Mid: 250 Hz - 5 kHz
- High: 5-20 kHz

4-Band:
- Sub: 20-100 Hz
- Low: 100-500 Hz
- Mid: 500 Hz - 5 kHz
- High: 5-20 kHz

Crossover Slopes:
- 12 dB/oct: Gentle, transparent
- 24 dB/oct: Steeper, more separation
- Linear phase: No phase shift (higher latency)
```

### Multiband Applications

**Vocal Processing:**
```
Low Band (80-250 Hz):
- Light compression (2:1)
- Remove excessive body
- Mono below 150 Hz
- Control mud

Mid Band (250 Hz - 5 kHz):
- Main compression (3:1 to 4:1)
- Core vocal range
- Most dynamic control here
- Careful balance

High Band (5-20 kHz):
- De-essing (dynamic EQ)
- Air and brilliance
- Ratio: 4:1 to 6:1 on sibilance
- Threshold: Catch "S" sounds only

Result: Balanced, polished vocal
```

**Bass Control:**
```
Sub Band (20-80 Hz):
- Heavy compression (4:1 to 8:1)
- Tight, controlled low-end
- Mono
- Prevent rumble

Low-Mid Band (80-300 Hz):
- Moderate compression (3:1)
- Body and weight
- Balance against sub
- Main bass tone

High Band (300 Hz - 5 kHz):
- Light compression (2:1)
- Definition and attack
- Helps small speaker translation
- Preserve dynamics

Result: Powerful yet controlled bass
```

**Mastering:**
```
Gentle multiband:

Low (20-150 Hz):
- Ratio: 1.5:1 to 2:1
- Tight, controlled
- Mono below 100 Hz
- GR: 1-2 dB max

Low-Mid (150 Hz - 1 kHz):
- Ratio: 2:1
- Balance warmth
- GR: 1-2 dB

High-Mid (1-6 kHz):
- Ratio: 2:1 to 3:1
- Control harshness
- Preserve presence
- GR: 1-2 dB

High (6-20 kHz):
- Ratio: 2:1
- Control sibilance
- Preserve air
- GR: 0-1 dB

Critical:
- Very subtle (1-2 dB GR per band)
- Transparent operation
- Don't overprocess
```

### Multiband vs Single-Band

**When to Use Multiband:**
- Frequency-specific dynamic problems
- Mastering (gentle control)
- Bass management
- Complex sources
- Vocal polish

**When to Use Single-Band:**
- Simpler, more transparent
- Musical compression
- Mix bus glue
- When problems not frequency-specific
- Most mixing situations

**Caution:**
- Multiband more complex
- Easy to overprocess
- Phase implications
- Single-band often better musically
- Use multiband when needed, not by default

---

## Advanced Techniques

### Compression Before or After EQ?

**Compression BEFORE EQ:**
```
Pros:
- Natural sound
- EQ works on consistent level
- Traditional approach
- Compressor responds to full spectrum

Use When:
- General compression
- Mix bus
- Maintaining natural tone

Example:
Vocal → Compressor → EQ
- Compress full frequency range
- Then shape tone
```

**Compression AFTER EQ:**
```
Pros:
- More controlled compression
- Can remove problem frequencies first
- Frequency-specific control
- Modern approach

Use When:
- Removing problem frequencies
- Surgical work
- De-essing
- Specific tonal goals

Example:
Vocal → EQ (cut 200-300 Hz) → Compressor
- Remove mud first
- Then compress cleaner signal
```

**Both (Sandwich):**
```
Professional Technique:

Signal Chain:
1. EQ (subtractive - remove problems)
2. Compressor (control dynamics)
3. EQ (additive - enhance tone)

Example - Vocal:
1. EQ: Cut 250 Hz (mud), HPF 100 Hz
2. Compressor: 4:1, 3-5 dB GR
3. EQ: Boost 4 kHz (presence), high shelf 12 kHz

Result: Clean, controlled, enhanced
```

### Sidechain Filtering

**Concept:**
- Filter the detection signal
- Compressor responds to specific frequencies
- Don't filter audio, just sidechain
- Surgical control

**Applications:**

**De-Essing:**
```
Setup:
- Compressor with filtered sidechain
- HPF sidechain at 5 kHz
- LPF sidechain at 10 kHz
- Only sibilance triggers compression

Settings:
- Ratio: 4:1 to 8:1
- Fast attack
- Fast-medium release
- GR: 3-6 dB when sibilance hits

Result:
- Only "S" sounds compressed
- Rest of vocal unchanged
- Transparent de-essing
```

**Kick/Bass Interaction:**
```
Setup:
- Compressor on bass
- Kick feeds sidechain
- Filter sidechain: 60-120 Hz (kick fundamental only)

Settings:
- Ratio: 4:1 to 6:1
- Attack: Fast (1-5 ms)
- Release: 100-150 ms
- GR: 3-5 dB

Result:
- Bass ducks only when kick fundamental hits
- More transparent than full-range sidechain
- Maintains bass midrange
```

**Harsh Frequency Control:**
```
Setup:
- Band-pass filter sidechain to harsh range (2-4 kHz)
- Compressor only reacts to harshness

Result:
- Dynamic control of specific problem
- Rest of signal unaffected
- More targeted than EQ
```

### Automation and Dynamics

**Vocal Riding:**
```
Concept:
- Manual level automation BEFORE compression
- Even out performance first
- Then compress consistent signal

Workflow:
1. Listen to vocal
2. Automate level (bring up quiet parts, lower loud parts)
3. Aim for even performance
4. Then apply compression

Benefits:
- Less compression needed
- More natural result
- Addresses performance issues
- Professional standard
```

**Dynamic Automation:**
```
Automate Compressor Parameters:

Threshold:
- Lower in chorus (more compression)
- Raise in verse (less compression)
- Dynamic intensity

Attack:
- Slower for sustained sections
- Faster for rhythmic sections
- Match to material

Release:
- Tempo sync to different sections
- Faster for energetic parts
- Slower for ballad sections
```

### Look-Ahead Compression

**Concept:**
- Delay audio, not sidechain
- Compressor "sees" signal before it happens
- Perfect peak detection
- Modern digital feature

**Benefits:**
- Zero overshoot
- Perfect transient control
- No pumping from unexpected peaks
- Transparent limiting

**Applications:**
```
Mastering:
- Look-ahead limiting
- Perfect peak control
- 5-10 ms look-ahead typical
- True Peak limiting

Mix Bus:
- Catch unexpected peaks
- Transparent control
- Small look-ahead (2-5 ms)

Caution:
- Adds latency
- Can delay entire track
- Compensate in DAW
- Use in mastering, less in mixing
```

---

## Common Mistakes

### Over-Compression

**Symptoms:**
- Lifeless, flat sound
- Pumping and breathing
- Loss of dynamics
- Fatigue inducing
- Unnatural

**Solutions:**
- Less GR (aim for 3-6 dB, not 10+)
- Higher ratio, less threshold
- Slower attack to preserve transients
- Check bypass frequently
- Use parallel compression

### Wrong Attack Time

**Too Fast:**
- Dulls transients
- Loses punch
- Flat sound
- Reduces impact

**Too Slow:**
- Doesn't catch peaks
- Inconsistent level
- Can cause distortion
- Ineffective compression

**Solution:**
- Match to material
- Drums: Often slower (preserve punch)
- Vocals: Medium (5-20 ms)
- Fast material: Faster attack
- Listen to transient response

### Pumping and Breathing

**Cause:**
- Release too fast for material
- Too much GR
- Threshold too low
- Wrong ratio

**Solutions:**
- Slower release
- Less GR (higher threshold)
- Lower ratio
- Use auto-release
- Sidechain filter (ignore bass triggering)

### Not Matching Levels (A/B Testing)

**Problem:**
- Louder always sounds "better"
- Can't judge accurately
- Over-processing common
- False improvements

**Solution:**
- Always match levels with makeup gain
- Use true bypass
- A/B at same volume
- Trust ears, not visual increase
- Take breaks

### Using Compression to Fix Other Problems

**Common Misuse:**
- Trying to fix poor recording
- Compensating for bad arrangement
- Fixing tuning issues
- Correcting bad performance

**Reality:**
- Compression enhances, doesn't fix
- Address source issues first
- Re-record if possible
- Edit performance issues
- Compress quality material

### Default Settings Reliance

**Problem:**
- Every source different
- Presets are starting points only
- Generic settings rarely optimal
- Missing character and control

**Solution:**
- Understand parameters
- Adjust for material
- Listen critically
- Develop taste and experience
- Save custom presets for your workflow

---

## Practical Application Guide

### Vocal Compression Chain

**Lead Vocal - Modern Pop:**
```
Stage 1: Peak Control (FET or VCA)
- Ratio: 4:1
- Attack: 5-10 ms (medium)
- Release: Auto or 150 ms
- GR: 3-4 dB
- Purpose: Catch peaks, initial control

Stage 2: Tone/Body (Optical)
- Ratio: 3:1
- Attack: Medium (natural)
- Release: Auto
- GR: 2-3 dB
- Purpose: Smooth, add character

Optional Parallel:
- Heavy compression (8:1, fast, 10 dB GR)
- Blend 20-30%
- Adds power and consistency

De-Esser:
- After compression
- 6-9 kHz
- Dynamic EQ or dedicated
- 3-6 dB reduction

Final Polish (Optical or Tube):
- Very subtle (1:1.5 to 2:1)
- Slow attack/release
- 1-2 dB GR
- Glue and warmth
```

### Drum Compression

**Kick:**
```
Individual Track:
- Ratio: 3:1 to 5:1
- Attack: 20-50 ms (slow - preserve punch)
- Release: 100-200 ms (auto)
- GR: 3-5 dB
- Purpose: Control, tighten

Parallel:
- Optional additional punch
- Heavy compression (10:1)
- Fast attack/release
- Blend 20-30%
```

**Snare:**
```
Individual Track:
- Ratio: 4:1 to 6:1
- Attack: Fast (1-5 ms) or slow (20-40 ms) for style
- Release: 100-200 ms
- GR: 4-6 dB
- Purpose: Consistency, punch

Parallel (Common):
- Extremely heavy (20:1, all buttons)
- Very fast attack/release
- 15-20 dB GR
- Blend 30-40%
- Massive crack
```

**Drum Bus:**
```
Overall Compression:
- Ratio: 2:1 to 4:1
- Attack: 20-40 ms (preserve transients)
- Release: Auto or 200-400 ms
- GR: 2-4 dB
- Purpose: Glue kit together

Type: VCA (SSL style) or Tube (Variable Mu)
```

### Bass Compression

**Electric Bass:**
```
Primary Compression:
- Ratio: 4:1 to 6:1
- Attack: 10-30 ms (medium)
- Release: Auto or 150-250 ms
- GR: 4-6 dB
- Purpose: Consistency, control

Optional Second Stage:
- Optical or tube
- Ratio: 3:1
- Slower settings
- GR: 2-3 dB
- Adds warmth, final control

Sidechain (if with kick):
- Kick triggers ducking
- 3-5 dB GR when kick hits
- Fast attack, medium release
```

**Synth Bass:**
```
Heavy Control:
- Ratio: 6:1 to 10:1
- Attack: Medium (10-20 ms)
- Release: 100-200 ms
- GR: 6-10 dB
- Purpose: Extreme control for power

Sidechain from Kick:
- Essential for EDM/electronic
- 4-6 dB ducking
- Creates rhythmic movement
```

### Mix Bus Compression

**Settings:**
```
Conservative Approach:
- Ratio: 2:1 (gentle)
- Attack: 30 ms (preserve transients)
- Release: Auto or 300-500 ms
- GR: 1-3 dB (subtle)
- Purpose: Glue, cohesion

Recommended Types:
- SSL VCA (industry standard)
- Variable Mu (warm, vintage)
- Clean VCA (transparent)

Critical:
- Very subtle
- Should barely be noticeable
- Less is more
- A/B frequently
```

---

## Conclusion

Dynamics processing is essential for professional mixing and mastering. Key principles:

**Core Concepts:**
- Understand attack, release, ratio, threshold fundamentally
- Match compressor type to source and goal
- Serial compression more transparent than single heavy stage
- Parallel compression essential for modern mixes
- Sidechain compression solves frequency conflicts

**Best Practices:**
- Start with conservative settings
- Preserve transients when possible (slower attack)
- Use GR metering to guide adjustments
- A/B with bypass at matched levels constantly
- Less is more - subtle control sounds professional

**Workflow:**
- Cut before compression (EQ problem frequencies first)
- Compress for control and character
- Enhance after compression (additive EQ)
- Reference dynamics against professional mixes
- Trust your ears over visual feedback

**Advanced Techniques:**
- Utilize serial compression chains
- Master parallel processing for power without sacrifice
- Apply multiband for surgical frequency-specific control
- Employ sidechain filtering for transparency
- Automate for dynamic mixes

**Avoiding Mistakes:**
- Don't over-compress (3-6 dB GR typical)
- Match levels when A/B testing
- Don't use compression to fix bad recordings
- Avoid pumping/breathing with proper release
- Don't set and forget - adjust for material

Mastery comes from understanding both technical parameters and developing critical listening skills. Know your compressor types, practice on various sources, and always serve the music first.

---

*End of Dynamics Processing Reference*
