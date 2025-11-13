# Frequency Management Reference

## Overview
Comprehensive guide to frequency management, equalization techniques, and spectral balance for professional mixing and mastering. This reference covers EQ types, frequency ranges, surgical techniques, and creative applications.

---

## Table of Contents
1. [Frequency Spectrum Fundamentals](#frequency-spectrum-fundamentals)
2. [EQ Types & Characteristics](#eq-types--characteristics)
3. [Frequency Ranges by Instrument](#frequency-ranges-by-instrument)
4. [EQ Techniques](#eq-techniques)
5. [Surgical vs Musical EQ](#surgical-vs-musical-eq)
6. [Problem Frequencies](#problem-frequencies)
7. [Genre-Specific Approaches](#genre-specific-approaches)
8. [Advanced Techniques](#advanced-techniques)
9. [Common Mistakes](#common-mistakes)

---

## Frequency Spectrum Fundamentals

### The Complete Audio Spectrum

**Sub-Bass (20-60 Hz)**
- Felt more than heard
- Foundation of low-end power
- Kick drum fundamental, bass synth subs
- Critical for electronic music
- Easily causes muddiness if excessive
- Requires good monitoring to judge accurately

**Bass (60-250 Hz)**
- Warmth and body
- Bass guitar, kick drum body, toms
- Low male vocals, cello, double bass
- Prone to room mode problems
- Most common area for muddiness
- Balance carefully against sub-bass

**Low Mids (250-500 Hz)**
- Body and fullness
- Snare body, guitar lower harmonics
- Male vocal chest resonance
- Can sound "boxy" or "muddy" if excessive
- Often needs reduction in modern mixes
- Critical transition zone

**Midrange (500 Hz - 2 kHz)**
- Core of most instruments
- Vocal presence starts here
- Guitar and piano body
- Snare fundamental
- Can sound "honky" or "nasal" if peaked
- Essential for mix clarity

**Upper Mids (2-6 kHz)**
- Presence and definition
- Vocal intelligibility
- Attack of most instruments
- Snare crack, guitar pick attack
- Harsh if excessive
- Most sensitive hearing range (3-4 kHz)

**Highs (6-12 kHz)**
- Brilliance and clarity
- Cymbal wash, hi-hats
- Vocal sibilance (6-9 kHz)
- Air and space (10-12 kHz)
- Adds "sparkle" when boosted
- Can cause listening fatigue

**Air/Presence (12-20 kHz)**
- "Air" and "openness"
- Cymbal shimmer
- Acoustic space
- Subtle but important for perceived quality
- Diminishes with age (hearing loss)
- Often enhanced in mastering

### Psychoacoustic Considerations

**Fletcher-Munson Curves:**
- Human hearing is most sensitive at 3-4 kHz
- Bass and treble require more level to be perceived equally
- Changes with listening volume
- Why mixes can sound different at various levels
- Consider when mixing at low volumes

**Masking:**
- Lower frequencies mask higher frequencies
- Louder sounds mask quieter sounds in nearby frequencies
- Temporal masking: loud sound masks before and after
- Use EQ to create space between competing elements

**Equal Loudness Contours:**
- Perception of frequency balance changes with volume
- Bass and treble seem reduced at low volumes
- Check mixes at multiple volume levels
- Reference tracks at same SPL

---

## EQ Types & Characteristics

### Parametric EQ

**Features:**
- Fully adjustable frequency, gain, and Q (bandwidth)
- Most flexible and precise
- Standard for mixing and mastering

**Parameters:**
- **Frequency**: Center point of EQ band (20 Hz - 20 kHz)
- **Gain**: Amount of boost or cut (±18 dB typical)
- **Q (Bandwidth)**: Width of affected frequency range
  - Low Q (0.5-1.0): Wide, musical
  - Medium Q (1.0-3.0): Balanced
  - High Q (3.0-10+): Narrow, surgical

**Best For:**
- Precision work
- Problem solving
- Tonal shaping
- Any situation requiring control

**Common Uses:**
- Channel EQ
- Mix bus processing
- Mastering
- Corrective work

### Graphic EQ

**Features:**
- Fixed frequency bands (typically 31, 15, or 10 bands)
- Visual representation via faders
- Limited control but intuitive

**Characteristics:**
- ISO standard frequencies (31.5 Hz, 63 Hz, 125 Hz, etc.)
- Fixed Q values
- Primarily boost/cut control
- Quick visual feedback

**Best For:**
- Live sound
- Room tuning
- Quick broad strokes
- Visual learners

**Limitations:**
- Less precise than parametric
- Fixed frequencies may not align with problem areas
- Less suitable for surgical work

### Shelving EQ

**Types:**

**High Shelf:**
- Affects all frequencies above corner frequency
- Gentle, musical curve
- Common at 8-12 kHz for "air"
- ±6 dB typical range

**Low Shelf:**
- Affects all frequencies below corner frequency
- Add warmth or remove mud
- Common at 80-120 Hz
- More subtle than filters

**Parameters:**
- **Frequency**: Corner/turnover frequency
- **Gain**: Amount of boost or cut
- **Slope**: Gentleness of transition (6 dB/oct typical)

**Applications:**
- Broad tonal adjustments
- Mastering
- Mix bus processing
- Less surgical than parametric

### High-Pass/Low-Pass Filters

**High-Pass Filter (HPF) / Low-Cut:**
- Removes frequencies below cutoff
- Essential mixing tool
- Reduces rumble, stage noise, proximity effect
- Prevents frequency buildup

**Common Settings:**
- Vocals: 80-120 Hz
- Acoustic guitar: 80-100 Hz
- Electric guitar: 100-120 Hz
- Snare: 80-100 Hz (optional)
- Kick/Bass: 20-40 Hz (remove sub-rumble only)

**Slopes:**
- 6 dB/octave: Gentle, transparent
- 12 dB/octave: Standard, musical
- 18 dB/octave: Steep, more obvious
- 24 dB/octave: Very steep, can cause phase issues

**Low-Pass Filter (LPF) / High-Cut:**
- Removes frequencies above cutoff
- Less common than HPF
- Creates warmth, vintage character
- Controls harshness

**Applications:**
- Darkening overly bright sources
- Creating lo-fi effects
- Controlling harsh synths
- Vintage emulation

### Dynamic EQ

**Concept:**
- EQ that responds to threshold crossings
- Combines EQ with compression
- Only activates when signal reaches threshold

**Parameters:**
- Standard EQ parameters (freq, gain, Q)
- Threshold: Level at which EQ activates
- Attack/Release: How quickly EQ responds
- Ratio: How much EQ is applied

**Applications:**
- De-essing (6-9 kHz)
- Controlling resonances
- Taming harsh transients
- Frequency-specific dynamics

**Advantages Over Static EQ:**
- Doesn't permanently alter tone
- Reacts to actual problems
- More transparent
- Solves intermittent issues

### Analog-Style EQ Emulations

**Pultec-Style:**
- Separate boost and cut controls
- Can boost and cut same frequency simultaneously
- Musical, vintage character
- Low-end boost with high-end cut = famous sound

**API 550-Style:**
- Fixed frequencies with proportional Q
- Surgical at high boost/cut amounts
- Aggressive, colored sound
- Excellent for drums and rock

**Neve-Style:**
- Musical, broad curves
- Colored transformers and circuits
- Warm, smooth character
- Great for buses and mastering

**SSL-Style:**
- Clean, precise
- Bell curves
- Versatile and transparent
- Mix bus standard

---

## Frequency Ranges by Instrument

### Drums

#### Kick Drum
```
Sub fundamental: 40-60 Hz
  - Deep sub energy
  - Felt in chest
  - Boost: +2 to +5 dB for power
  - Cut: if too boomy or conflicting with bass

Body/Punch: 60-100 Hz
  - Main weight and impact
  - Boost: +3 to +6 dB for thickness
  - Critical zone for electronic music

Attack/Click: 2-6 kHz
  - Beater definition
  - Boost: +2 to +4 dB for clarity
  - Cut: if too clicky or harsh

Air/Presence: 8-10 kHz
  - Subtle breath and space
  - Boost: +1 to +3 dB for modern sound
  - Optional, style-dependent

Common Problems:
- Muddy: Cut 200-400 Hz
- Boxy: Cut 400-800 Hz
- Cardboard: Cut 300-500 Hz
```

#### Snare Drum
```
Body/Fundamental: 150-250 Hz
  - Main tone and weight
  - Boost: +2 to +4 dB for fullness
  - Cut: if too tubby

Crack/Attack: 2-5 kHz
  - Snare wire rattle and attack
  - Boost: +3 to +6 dB for aggression
  - Essential for presence

Brightness: 5-10 kHz
  - High-end clarity and air
  - Boost: +2 to +4 dB for snap
  - Cut: if too harsh or brittle

Common Problems:
- Thin: Boost 150-250 Hz, cut 400-800 Hz
- Boxy: Cut 400-600 Hz with narrow Q
- Harsh: Cut 3-4 kHz slightly
- Ringy: Find resonance (400-800 Hz), narrow cut
```

#### Hi-Hats
```
Body: 300-800 Hz
  - Low-mid presence
  - Usually cut for clarity

Brightness: 8-15 kHz
  - Main energy
  - Boost: +2 to +4 dB for shimmer
  - Cut: if too harsh

Air: 10-20 kHz
  - Top-end sparkle
  - Boost: +1 to +3 dB for openness
  - Shelf EQ works well

Processing Tips:
- HPF at 300-500 Hz (aggressive)
- Boost 8-12 kHz for presence
- Subtle 15 kHz shelf for air
```

#### Toms
```
Fundamental: 80-150 Hz (floor tom)
             100-200 Hz (mid tom)
             150-300 Hz (rack tom)
  - Main tone
  - Boost: +3 to +6 dB for impact

Attack: 3-6 kHz
  - Stick definition
  - Boost: +2 to +4 dB for clarity
  - Helps toms cut through

Common Issues:
- Muddy: HPF at 60-80 Hz, cut 200-400 Hz
- Ringy: Find resonance, narrow cut (Q=5-10)
- Cardboard: Cut 400-800 Hz
```

#### Cymbals
```
Body: 300-800 Hz
  - Usually cut completely (HPF)
  - Reduces muddiness

Presence: 3-8 kHz
  - Main energy and crash
  - Adjust to taste
  - Can sound harsh if boosted

Air/Shimmer: 8-20 kHz
  - Top-end sparkle
  - Boost: +2 to +5 dB for brilliance
  - High shelf effective

Processing:
- Aggressive HPF at 400-600 Hz
- Tame harshness with gentle cut at 6-8 kHz
- High shelf boost at 10-12 kHz
```

### Bass Instruments

#### Electric Bass
```
Sub: 40-80 Hz
  - Deep fundamental
  - Often reduced for clarity
  - Conflicts with kick

Body: 80-200 Hz
  - Main bass tone
  - Boost: +3 to +6 dB for weight
  - Critical zone

Presence/Grind: 700 Hz - 1.5 kHz
  - Midrange definition
  - Helps bass heard on small speakers
  - Boost: +2 to +4 dB for clarity

Attack/String noise: 2-5 kHz
  - Pick/finger attack
  - Boost: +2 to +4 dB for articulation
  - Aggressive playing styles

Common Issues:
- Muddy: Cut 200-400 Hz
- Thin: Boost 80-150 Hz, cut low mids
- Not audible on small speakers: Boost 700-1000 Hz
```

#### Synth Bass
```
Sub: 30-60 Hz
  - Pure sub energy
  - Mono for tight low-end
  - Boost: +3 to +6 dB for power

Fundamental: 60-150 Hz
  - Main tone
  - Boost: +3 to +6 dB for weight

Harmonics: 150-500 Hz
  - Character and warmth
  - Balance against kick

Presence: 1-3 kHz
  - Helps on small speakers
  - Boost: +2 to +4 dB if needed

Processing Strategy:
- HPF below 30 Hz (remove DC)
- Boost 40-60 Hz for sub
- Cut 200-400 Hz to avoid mud
- Boost 1-2 kHz for small speaker translation
```

### Melodic Instruments

#### Acoustic Guitar
```
Body: 80-250 Hz
  - Warmth and fullness
  - Can muddy mix if excessive
  - Boost: +2 to +3 dB for body

Presence: 2-5 kHz
  - Pick attack and definition
  - Boost: +3 to +5 dB for clarity
  - Essential for cut-through

Brilliance: 8-15 kHz
  - Sparkle and air
  - Boost: +2 to +4 dB for shimmer
  - High shelf effective

Processing:
- HPF at 80-100 Hz
- Cut 200-400 Hz to reduce mud
- Boost 3-5 kHz for presence
- High shelf at 10 kHz for air
```

#### Electric Guitar
```
Body: 100-300 Hz
  - Weight and power
  - Can conflict with bass
  - Often reduced slightly

Main tone: 300 Hz - 1.5 kHz
  - Core guitar sound
  - Different per amp/style
  - Adjust to fit mix

Presence/Bite: 2-5 kHz
  - Attack and definition
  - Boost: +3 to +6 dB for aggression
  - Cut: if too harsh

Brilliance: 6-12 kHz
  - Top-end sparkle
  - Boost: +2 to +4 dB for clarity
  - Style-dependent

Genre Considerations:
- Clean/Jazz: Warmer, less highs
- Rock: Midrange focus (500-2k Hz)
- Metal: Scoop mids (cut 400-800 Hz), boost 80 Hz and 5 kHz
```

#### Piano
```
Low end: 80-250 Hz
  - Bass notes fundamental
  - Can muddy mix
  - Subtle cut often helps

Body: 250 Hz - 1 kHz
  - Main tone and warmth
  - Balance carefully

Presence: 2-6 kHz
  - Hammer attack and clarity
  - Boost: +2 to +4 dB for definition

Air: 8-15 kHz
  - Top-end sparkle
  - Boost: +1 to +3 dB for brilliance

Processing Strategy:
- HPF at 40-60 Hz
- Small cut at 200-300 Hz to avoid mud
- Boost 3-5 kHz for attack
- High shelf at 10 kHz for air
```

#### Strings (Orchestral)
```
Body: 200-500 Hz
  - Warmth and fullness
  - Careful balance needed

Main tone: 500 Hz - 2 kHz
  - Core string sound
  - Usually left natural

Presence: 2-6 kHz
  - Bow attack and definition
  - Boost: +2 to +3 dB for clarity

Air: 8-15 kHz
  - Top-end shimmer
  - Boost: +1 to +2 dB for space

By Section:
- Violins: Focus on 2-6 kHz for presence
- Violas: 500 Hz - 2 kHz midrange
- Cellos: 150-500 Hz body, 2-4 kHz attack
- Bass: 80-200 Hz fundamental
```

### Vocals

#### Lead Vocals (Male)
```
Fundamental: 100-200 Hz
  - Main pitch range
  - Too much = muddy
  - Cut: -2 to -3 dB if boomy

Chest resonance: 200-600 Hz
  - Warmth and body
  - Adjust to taste
  - Cut 200-300 Hz to reduce mud

Presence: 2-5 kHz
  - Intelligibility and clarity
  - Boost: +3 to +6 dB for cut-through
  - Most important range

Sibilance: 6-9 kHz
  - "S" and "T" sounds
  - Often needs de-essing
  - Dynamic EQ or dedicated de-esser

Air: 10-15 kHz
  - Breath and openness
  - Boost: +1 to +3 dB for modern sound
  - High shelf works well

Standard Processing:
- HPF at 80-100 Hz
- Cut 200-300 Hz by -2 to -3 dB
- Boost 3-5 kHz by +3 to +5 dB
- De-ess at 6-8 kHz
- High shelf at 10-12 kHz +2 dB
```

#### Lead Vocals (Female)
```
Fundamental: 200-400 Hz
  - Main pitch range
  - Higher than male
  - Less cutting needed

Body: 400 Hz - 1 kHz
  - Warmth and presence
  - Balance carefully

Presence: 3-6 kHz
  - Clarity and intelligibility
  - Boost: +3 to +5 dB
  - Essential for mix

Sibilance: 7-10 kHz
  - Higher than male
  - De-ess aggressively if needed

Air: 12-16 kHz
  - Breath and space
  - Boost: +2 to +4 dB

Processing:
- HPF at 100-120 Hz
- Small cut at 200-400 Hz if muddy
- Boost 4-6 kHz for presence
- De-ess at 7-9 kHz
- High shelf at 12 kHz
```

#### Backing Vocals
```
Strategy:
- Make space for lead
- Reduce competing frequencies
- Sit behind in mix

Processing:
- Aggressive HPF (150-200 Hz)
- Cut midrange where lead sits (2-4 kHz by -3 dB)
- Less presence than lead
- Can be darker overall
- Group processing common
```

---

## EQ Techniques

### Subtractive EQ (Cutting)

**Philosophy:**
- Cut before boost
- Solve problems first
- More transparent than boosting
- Doesn't add noise
- Creates headroom

**When to Cut:**
- Muddy low-mids (200-400 Hz)
- Boxy midrange (400-800 Hz)
- Harsh frequencies (2-4 kHz)
- Resonances and ringing
- Removing unwanted elements

**Technique:**
1. Find problem frequency (boost and sweep)
2. Cut with appropriate Q
3. Use narrower Q for surgical work
4. Use wider Q for musical shaping

**Benefits:**
- Cleaner mix
- More headroom
- Natural sound
- Better transient response

### Additive EQ (Boosting)

**Philosophy:**
- Enhance what's there
- Add character and color
- Use after subtractive work
- Less is more

**When to Boost:**
- Adding presence (2-5 kHz)
- Enhancing air (10-15 kHz)
- Increasing warmth (80-150 Hz)
- Creative tonal shaping

**Guidelines:**
- Use wider Q for musical boosts
- Typically +3 to +6 dB maximum
- A/B test frequently
- Watch for phase issues

### High-Pass Filtering Strategy

**Purpose:**
- Remove unnecessary low frequencies
- Create space for bass/kick
- Reduce mud and rumble
- Essential mixing technique

**Application by Source:**
```
Vocals: 80-120 Hz
Guitars: 80-120 Hz
Piano: 40-80 Hz
Strings: 80-150 Hz
Horns: 100-150 Hz
Snare: 60-100 Hz (optional)
Hi-hats: 300-600 Hz (aggressive)
Cymbals: 400-800 Hz
Percussion: 100-200 Hz

Never HPF:
- Kick drum (only below 20-30 Hz)
- Bass instruments (only below 30-40 Hz)
- Sub synths (only below 20 Hz)
```

**Slope Selection:**
- 12 dB/oct: Most common, musical
- 18 dB/oct: Steeper, more obvious
- 24 dB/oct: Very steep, can cause phase shift
- 6 dB/oct: Gentle, transparent

### Mid-Side EQ

**Concept:**
- Separate EQ for mid (center) and side (stereo)
- Surgical stereo image control
- Powerful mixing tool

**Applications:**

**Widen Mix:**
- Boost highs in sides
- Cut lows in sides (keep mono)
- Enhance stereo image

**Tighten Low-End:**
- Aggressive HPF on sides
- Keep bass in mid channel
- Mono low-end = tight mix

**Create Space:**
- Cut competing frequencies in sides
- Example: Cut vocal range in pad sides
- Leaves room for center elements

**Mastering:**
- High shelf boost in sides for width
- Low shelf cut in sides for tight bass
- Subtle adjustments only

### Frequency Matching

**Concept:**
- Analyze reference track spectrum
- Match your mix to reference
- Objective approach

**Process:**
1. Load reference track in analyzer
2. Compare to your mix spectrum
3. Identify differences
4. Apply compensating EQ
5. A/B test result

**Tools:**
- Spectrum analyzer (visual)
- Reference matching plugins
- Critical listening
- Frequency-specific comparison

**Caution:**
- Don't match exactly
- Consider different sources/mastering
- Use as guide, not rule
- Trust ears over eyes

---

## Surgical vs Musical EQ

### Surgical EQ

**Characteristics:**
- Narrow Q (5-20)
- Specific problem solving
- Cutting resonances
- Removing harsh frequencies
- Transparent results

**Applications:**
```
Ringing snare: 
- Sweep parametric EQ with high Q
- Find offending frequency
- Cut by -3 to -6 dB
- Very narrow (Q=10+)

Room mode:
- Identify problematic bass frequency
- Narrow cut (Q=5-10)
- Cut -3 to -6 dB
- Solves specific room issue

Vocal harshness:
- Sweep 2-5 kHz range
- Find harsh spot
- Narrow cut (Q=3-5)
- Cut -2 to -4 dB
```

**Guidelines:**
- Use linear phase for steep cuts
- Very narrow Q acceptable
- Can be aggressive (-6 to -12 dB)
- Problem-solving focused

### Musical EQ

**Characteristics:**
- Wide Q (0.5-2.0)
- Broad tonal shaping
- Enhancing character
- Natural, musical results

**Applications:**
```
Vocal presence:
- Boost 3-5 kHz
- Wide Q (1.0-1.5)
- +3 to +5 dB
- Enhances intelligibility

Bass warmth:
- Boost 80-120 Hz
- Wide Q (1.0)
- +3 to +6 dB
- Adds weight and power

Air/Brilliance:
- High shelf 10-12 kHz
- +2 to +4 dB
- Adds openness
- Smooth, natural
```

**Guidelines:**
- Wider curves sound more natural
- Modest amounts (+3 to +6 dB)
- Multiple gentle moves better than one drastic
- Consider analog-style EQs

### Combining Both Approaches

**Strategy:**
1. **Surgical first:** Remove problems
2. **Musical second:** Enhance character
3. **Reference:** A/B against bypass
4. **Refine:** Adjust both as needed

**Example (Vocal):**
```
Surgical:
- HPF at 100 Hz (12 dB/oct)
- Cut 300 Hz, Q=5, -3 dB (mud)
- Cut 3.5 kHz, Q=3, -2 dB (harshness)

Musical:
- Boost 150 Hz, Q=1.0, +2 dB (warmth)
- Boost 4 kHz, Q=1.5, +4 dB (presence)
- High shelf 12 kHz, +2 dB (air)
```

---

## Problem Frequencies

### Common Problem Areas

**Mud Zone (200-400 Hz)**
```
Symptoms:
- Unclear, muddy mix
- Lack of definition
- Sounds "cloudy"
- Elements blend together

Solutions:
- Cut 250-350 Hz on multiple tracks
- HPF non-bass elements higher
- Surgical cut on worst offenders
- A/B to avoid making mix thin

Instruments Often Needing Cut:
- Guitars: Cut 250-300 Hz
- Vocals: Cut 200-300 Hz
- Kick: Cut 300-400 Hz
- Snare: Cut 250-350 Hz
```

**Boxy Zone (400-800 Hz)**
```
Symptoms:
- "Cardboard" or "boxy" sound
- Hollow resonance
- Unpleasant midrange
- Telephone-like quality

Solutions:
- Narrow cut (Q=3-5)
- -3 to -6 dB typical
- Sweep to find exact frequency
- Often 400-600 Hz

Common on:
- Snare drums
- Toms
- Acoustic guitars
- Male vocals
- Small rooms
```

**Nasal Zone (800 Hz - 1.5 kHz)**
```
Symptoms:
- Honky, nasal quality
- Unpleasant vocal tone
- Cheap sound
- Lack of hi-fi

Solutions:
- Moderate Q (2-3)
- Cut -2 to -4 dB
- Be careful not to thin out
- Common on vocals

Affected Instruments:
- Vocals (especially male)
- Guitars
- Horns
- Organ
```

**Harshness (2-4 kHz)**
```
Symptoms:
- Fatiguing, harsh sound
- Aggressive, unpleasant
- Listening fatigue
- Sibilance related

Solutions:
- Gentle cut (Q=1.5-2.5)
- -2 to -4 dB
- Or dynamic EQ
- Very common problem

Common Culprits:
- Vocals
- Cymbals
- Hi-hats
- Electric guitars
- Brass instruments
```

**Sibilance (6-9 kHz)**
```
Symptoms:
- Excessive "S" sounds
- "T" and "Ch" too loud
- Piercing vocal quality
- Harsh consonants

Solutions:
- De-esser (dynamic EQ)
- Threshold-based reduction
- -3 to -6 dB when triggered
- Narrow band (Q=3-5)

Settings:
- Frequency: 6-8 kHz (male), 7-10 kHz (female)
- Threshold: Adjust to catch sibilance
- Reduction: -4 to -8 dB
- Fast attack, medium release
```

### Resonance Removal Technique

**Finding Resonances:**
```
Method:
1. Create narrow boost (Q=10, +12 dB)
2. Slowly sweep through frequency range
3. Listen for ringing, resonance, harshness
4. When found, switch to cut
5. Adjust Q and amount to taste
6. Typically need Q=5-10 and -3 to -6 dB

Common Resonances:
- Snare: 400-800 Hz (ringing)
- Toms: Varies, sweep to find
- Kick: 300-500 Hz (boxiness)
- Acoustic guitar: 200-400 Hz
- Room modes: 80-300 Hz (bass heavy)
```

---

## Genre-Specific Approaches

### Electronic/EDM

**Philosophy:**
- Clean, powerful low-end
- Bright, aggressive top-end
- Scooped or balanced mids (varies by subgenre)
- Loudness focused

**Kick:**
```
- Boost 50-60 Hz (+4 to +6 dB, wide Q)
- Cut 200-400 Hz (-2 to -4 dB, moderate Q)
- Boost 3-5 kHz (+3 to +5 dB, moderate Q)
- Optional boost 8-10 kHz (+2 dB, shelf)
```

**Bass:**
```
- HPF below 30 Hz
- Boost 40-60 Hz (+4 to +6 dB) for sub
- Cut 200-400 Hz (-2 to -4 dB) for clarity
- Boost 1-2 kHz (+2 to +3 dB) for presence
```

**Leads:**
```
- HPF at 150-300 Hz (aggressive)
- Boost 2-5 kHz (+3 to +6 dB) for presence
- High shelf at 10 kHz (+2 to +4 dB) for air
- Stereo width via mid-side EQ
```

### Rock/Metal

**Philosophy:**
- Powerful, aggressive midrange
- Tight, controlled low-end
- Bright without harshness
- In-your-face energy

**Guitars:**
```
- HPF at 100-120 Hz
- Cut 200-300 Hz (-2 to -3 dB)
- Boost 700 Hz - 1.5 kHz (+3 to +5 dB) for body
- Boost 3-5 kHz (+3 to +6 dB) for bite
- Optional: Scoop 400-800 Hz for metal
```

**Drums:**
```
Kick:
- Boost 60-80 Hz (+4 to +6 dB)
- Cut 300-400 Hz (-3 dB)
- Boost 3-5 kHz (+4 to +6 dB)

Snare:
- Boost 200 Hz (+3 dB) for body
- Cut 400-600 Hz (-2 dB) if boxy
- Boost 3-5 kHz (+5 to +8 dB) for crack

Toms:
- Similar to kick, adjusted per tom
- Focus on fundamental + attack
```

**Vocals:**
```
- HPF at 100-120 Hz
- Cut 200-300 Hz (-2 to -3 dB)
- Boost 3-5 kHz (+4 to +6 dB) for aggression
- De-ess at 6-8 kHz
- High shelf at 10 kHz (+2 to +3 dB)
```

### Hip-Hop/Trap

**Philosophy:**
- Massive sub-bass
- Clear, present vocals
- Minimal mid-range clutter
- 808-focused low-end

**808 Bass:**
```
- HPF only below 25 Hz (DC removal)
- Boost 40-60 Hz (+6 to +8 dB, wide Q)
- Cut 200-400 Hz (-3 to -4 dB)
- Boost 1-2 kHz (+2 to +3 dB) for presence
- Keep MONO below 150 Hz
```

**Kick:**
```
- Often minimal or absent
- If present: Cut low-end to avoid 808 conflict
- HPF at 60-80 Hz
- Focus on 2-6 kHz for click
```

**Vocals:**
```
- HPF at 100-120 Hz
- Cut 200-300 Hz (-2 to -3 dB)
- Boost 3-5 kHz (+5 to +7 dB) for presence
- De-ess at 6-9 kHz
- High shelf at 12 kHz (+3 to +4 dB) for air
- Very upfront and clear
```

**Hi-Hats:**
```
- Aggressive HPF at 500-800 Hz
- Boost 8-12 kHz (+3 to +5 dB)
- High shelf at 15 kHz (+2 to +3 dB)
- Very bright, crisp
```

### Pop

**Philosophy:**
- Balanced, polished spectrum
- Clear, present vocals
- Controlled low-end
- Radio-ready brightness

**Vocals:**
```
- HPF at 80-100 Hz
- Small cut 200-300 Hz (-2 dB)
- Boost 3-5 kHz (+3 to +5 dB)
- De-ess at 6-8 kHz
- High shelf at 10-12 kHz (+2 to +3 dB)
- Most important element
```

**Bass:**
```
- HPF at 40 Hz
- Boost 80-120 Hz (+3 to +5 dB)
- Cut 200-400 Hz (-2 dB)
- Boost 700 Hz - 1 kHz (+2 to +3 dB) for definition
```

**Drums:**
```
- Balanced spectrum
- Punchy but controlled
- Support vocal, not overpower
- Moderate EQ moves (+/-3 to +/-6 dB)
```

### Jazz/Acoustic

**Philosophy:**
- Natural, transparent sound
- Minimal processing
- Preserve acoustic character
- Subtle enhancements only

**Approach:**
```
- Minimal EQ overall
- Subtractive EQ preferred
- HPF to clean up low-end
- Gentle, wide curves only
- Very small boosts (+1 to +2 dB)

General Strategy:
- HPF on all instruments (except bass)
- Small cuts to remove mud (200-400 Hz)
- Minimal presence boosts if needed
- Preserve natural timbre
- Less is more
```

---

## Advanced Techniques

### Linear Phase vs Minimum Phase EQ

**Minimum Phase EQ:**
- Standard EQ type
- Phase shift occurs with EQ
- More "analog" sound
- Lower CPU usage
- Preferred for mixing (usually)

**Characteristics:**
- Phase shift proportional to EQ amount
- Natural, musical sound
- Can cause pre-ringing with extreme cuts
- Works like analog EQ

**Best For:**
- Individual tracks
- Musical EQ moves
- When phase coherence not critical
- General mixing

**Linear Phase EQ:**
- No phase shift
- Perfect frequency response
- Higher latency
- More CPU intensive

**Characteristics:**
- Maintains phase relationships
- Can cause pre-ringing artifacts
- Surgical, clinical sound
- Perfect for parallel processing

**Best For:**
- Mastering
- Mix bus processing
- Parallel compression chains
- Extreme surgical cuts
- When summing multiple bands

**When to Use Which:**
```
Minimum Phase:
- Individual tracks (vocals, drums, etc.)
- Musical, broad adjustments
- When latency matters (tracking)
- General mixing tasks

Linear Phase:
- Master bus
- Mastering
- Parallel processing
- Surgical corrections
- When phase matters
```

### Dynamic EQ Applications

**Concept Review:**
- EQ that only activates at threshold
- Combines benefits of EQ and compression
- More transparent than static EQ
- Solves intermittent problems

**De-Essing:**
```
Setup:
- Frequency: 6-9 kHz (male), 7-10 kHz (female)
- Q: Narrow to moderate (3-5)
- Threshold: Set to catch sibilance only
- Reduction: -4 to -8 dB
- Attack: Fast (1-5 ms)
- Release: Medium (50-100 ms)

Benefits:
- Only reduces when sibilance occurs
- Doesn't permanently dull vocals
- Natural, transparent
```

**Taming Resonances:**
```
Snare Resonance:
- Find ringing frequency (400-800 Hz)
- Set narrow band (Q=5-10)
- Threshold to catch ring only
- Reduce -4 to -6 dB when triggered
- Fast attack, medium release

Result:
- Resonance controlled
- Natural snare body preserved
```

**Frequency-Specific Compression:**
```
Bass Bloat Control:
- Frequency: 80-120 Hz
- Moderate Q (2-3)
- Threshold: Catch excessive bass hits
- Reduction: -3 to -6 dB
- Medium attack (10-30 ms)
- Auto release

Vocal Harshness:
- Frequency: 2-4 kHz
- Moderate Q (2-3)
- Threshold: Catch harsh peaks
- Reduction: -3 to -5 dB
- Fast attack, medium release
```

### Parallel EQ

**Concept:**
- Duplicate track
- Apply extreme EQ to duplicate
- Blend with original
- Retains natural tone while adding character

**Applications:**

**Bass Enhancement:**
```
Setup:
1. Duplicate bass track
2. Aggressive HPF at 100 Hz on duplicate
3. Boost 40-60 Hz by +10 dB on duplicate
4. Add saturation/distortion
5. Blend 20-40% with original

Result:
- Massive sub-bass
- Preserves natural bass tone
- Powerful yet controlled
```

**Vocal Presence:**
```
Setup:
1. Duplicate vocal
2. Boost 3-5 kHz by +8 to +12 dB
3. High shelf 10 kHz +6 dB
4. Optional: Mild saturation
5. Blend 30-50% with original

Result:
- Extreme presence
- Natural vocal timbre maintained
- Cuts through mix
```

**Drum Excitement:**
```
Setup:
1. Duplicate drum bus
2. Aggressive EQ:
   - HPF at 200 Hz
   - Boost 4-6 kHz +10 dB
   - Boost 10-15 kHz +8 dB
3. Heavy compression
4. Blend 20-30% with original

Result:
- Added attack and presence
- Maintains natural dynamics
- Punchy, excited drums
```

### Multiband EQ Strategies

**Concept:**
- Split signal into frequency bands
- Process each band independently
- Surgical control over spectrum

**Applications:**

**Vocal Polish:**
```
Low Band (80-250 Hz):
- Slight compression
- Small cut to reduce mud
- Mono processing

Mid Band (250 Hz - 5 kHz):
- Main vocal presence
- Light compression
- Careful EQ adjustments

High Band (5-20 kHz):
- De-essing
- Air/brilliance control
- Stereo width (if doubles)

Benefits:
- Independent processing per range
- More control than single EQ
- Can solve multiple issues
```

**Master Bus Enhancement:**
```
Low (20-150 Hz):
- Tight compression
- Mono below 100 Hz
- Small shelf boost if needed

Low-Mid (150 Hz - 1 kHz):
- Gentle compression
- Balance against other bands
- Subtract mud if needed

High-Mid (1-6 kHz):
- Presence control
- De-essing if needed
- Moderate compression

High (6-20 kHz):
- Air and brilliance
- Gentle shelf boost
- Preserve transients

Result:
- Balanced, polished master
- Independent control per range
- Professional sound
```

### Matched EQ Technique

**Process:**
```
1. Capture Reference Spectrum:
   - Load reference track
   - Analyze frequency response
   - Note overall balance

2. Compare Your Mix:
   - Load your mix in analyzer
   - Overlay with reference
   - Identify major differences

3. Apply Corrective EQ:
   - Match overall curves
   - Don't match exactly
   - Use as guide only
   - Trust ears over eyes

4. Refine:
   - A/B between reference and yours
   - Make final adjustments
   - Remove excessive EQ if sounds unnatural
```

**Caution:**
- Every mix is different
- Mastering affects spectrum
- Source material matters
- Use as starting point only
- Don't match blindly

---

## Common Mistakes

### Over-EQing

**Symptoms:**
- Unnatural, processed sound
- Phase issues
- Thin or harsh result
- Lack of cohesion

**Solutions:**
- Less is more
- Use bypass frequently
- Take breaks
- Reference natural recordings
- Aim for 3-6 EQ moves max per track

### Boosting Instead of Cutting

**Problem:**
- Adds noise
- Reduces headroom
- Can sound unnatural
- Phase implications

**Solution:**
- Cut problem frequencies first
- Only boost to enhance
- Subtractive before additive
- If you boost 3 dB somewhere, consider cutting 3 dB elsewhere

### Not Using HPF

**Problem:**
- Muddy low-end
- Wasted headroom
- Frequency masking
- Weak mix translation

**Solution:**
- HPF on almost everything except bass/kick
- Be aggressive (80-150 Hz typical)
- Removes unnecessary information
- Creates clarity and headroom

### Ignoring Phase Issues

**Problem:**
- Thin sound when summed to mono
- Weak low-end
- Unstable stereo image
- Poor mix translation

**Solutions:**
- Check mix in mono frequently
- Use linear phase for critical EQ
- Be aware of phase implications
- Minimize extreme EQ moves

### EQ in Solo

**Problem:**
- Doesn't translate to full mix
- Over-processing
- Missing context
- Can sound good solo but bad in mix

**Solution:**
- EQ in context (full mix)
- Use solo to identify problems only
- Make adjustments with mix playing
- A/B bypass regularly

### Not Referencing

**Problem:**
- Frequency balance off
- Can't judge objectively
- Ear fatigue causes bad decisions
- Mix doesn't translate

**Solutions:**
- Use reference tracks constantly
- Match overall spectrum balance
- Take regular breaks
- Check on multiple systems
- Fresh ears critical

### Using EQ to Fix Arrangement Issues

**Problem:**
- Too many elements in same range
- EQ can't fix fundamental problem
- Everything sounds thin/processed
- Weak mix overall

**Solution:**
- Address arrangement first
- Remove competing elements
- Choose complementary sounds
- EQ enhances, doesn't fix bad arrangements

### Overusing Analog Emulations

**Problem:**
- Too much coloration
- Accumulative distortion
- CPU strain
- Phase issues from stacked plugins

**Solution:**
- Use colored EQs sparingly
- Reserve for important elements
- Mix with clean EQ, add character after
- Not every track needs vintage vibe

---

## Quality Control Checklist

**Before Finalizing EQ:**
```
☐ Check in mono (phase issues?)
☐ Bypass all EQ (is it actually better?)
☐ Compare to reference tracks
☐ Check on multiple systems/headphones
☐ Take a break, return with fresh ears
☐ Verify no excessive CPU usage
☐ Ensure no clipping from EQ boosts
☐ Check spectral balance is even
☐ Verify low-end is tight (not muddy)
☐ Confirm vocals/lead clear and present
☐ Check high-end is bright but not harsh
☐ Verify mix translates to small speakers
☐ Ensure nothing sounds thin or hollow
☐ Confirm surgical cuts aren't too extreme
```

---

## Conclusion

Frequency management is the foundation of professional mixing and mastering. Key takeaways:

**Fundamental Principles:**
- Subtractive EQ before additive
- Less is more - minimal processing preferred
- HPF on almost everything except bass/kick
- Consider context - EQ in full mix, not solo
- Check in mono frequently for phase issues

**Strategic Approach:**
- Identify and remove problem frequencies first
- Enhance existing qualities second
- Use appropriate EQ type for task (surgical vs musical)
- Reference frequently against professional mixes
- Trust your ears over visual analyzers

**Technical Considerations:**
- Understand minimum vs linear phase implications
- Use dynamic EQ for intermittent problems
- Apply parallel processing for extreme moves
- Consider mid-side EQ for stereo control
- Match EQ as guide, not rule

**Common Best Practices:**
- HPF: 80-120 Hz on most elements
- Problem areas: 200-400 Hz (mud), 400-800 Hz (box), 2-4 kHz (harsh)
- Presence: 3-5 kHz boost for clarity
- Air: 10-15 kHz high shelf for brilliance
- De-ess: 6-9 kHz for vocals

**Avoiding Mistakes:**
- Don't over-EQ (3-6 moves per track maximum)
- Don't EQ in solo exclusively
- Don't ignore phase relationships
- Don't boost instead of cutting first
- Don't forget to reference against pro mixes

Mastery of frequency management comes from understanding both the technical aspects and developing critical listening skills. Practice analyzing professional mixes, understanding why certain EQ decisions were made, and applying these principles to your own work. Always serve the music, not the meters.

---

*End of Frequency Management Reference*
