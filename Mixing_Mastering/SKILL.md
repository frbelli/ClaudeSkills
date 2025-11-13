---
name: mixing-and-mastering
description: Comprehensive mixing and mastering guidance for electronic music production. Use when the user needs advice on mixing or mastering a track, especially when they have MIDI files, sound design specifications, or a song document from the sound-design skill. Provides track-by-track mixing suggestions (EQ, compression, effects), mix bus processing advice, and final mastering chain recommendations. Covers all electronic music genres including techno, house, drum & bass, dubstep, trap, and more. Also use when the user asks about frequency ranges, compression settings, kick-bass relationships, loudness targets (LUFS), or mastering for streaming platforms.
---

# Mixing and Mastering Skill

This skill provides comprehensive mixing and mastering guidance for electronic music production, with seamless integration with the sound-design skill.

## Core Capabilities

1. **Track Analysis** - Analyze MIDI files and sound design specifications
2. **Mixing Suggestions** - Provide detailed EQ, compression, and effects advice per track
3. **Low-End Management** - Specialized guidance for kick-bass interaction
4. **Mix Bus Processing** - Bus compression and glue recommendations
5. **Mastering Chain** - Complete mastering workflow with loudness targets
6. **Genre-Specific Advice** - Tailored approaches for electronic subgenres
7. **Platform Optimization** - Streaming platform delivery standards

---

## Workflow Overview

### The Complete Pipeline

```
Sound Design (sound-design skill)
    ↓
    - MIDI files (individual tracks)
    - Song document (genre, BPM, key, mood, chords)
    - Sound design specs (synthesis parameters per track)
    ↓
Mixing & Mastering (THIS skill)
    ↓
    - Track-by-track mixing advice
    - Mix bus processing
    - Mastering chain
    - Export specifications
```

---

## Step 1: Input Recognition and Analysis

### Recognize Input from sound-design Skill

When the user provides materials from sound-design, you'll typically see:

**MIDI Files**:
- Individual tracks (kick, bass, lead, pad, hi-hat, etc.)
- Named descriptively (e.g., "techno_kick.mid", "reese_bass.mid")

**Song Document** (typically markdown):
- **Genre/Subgenre**: Techno, House, Drum & Bass, etc.
- **BPM**: Tempo of the track
- **Key**: Musical key (e.g., Am, F#m)
- **Mood**: Dark, uplifting, aggressive, etc.
- **Chord Progression**: Used in the track
- **Structure**: Intro, verse, chorus, breakdown, etc.

**Sound Design Specifications** (per track):
- Synthesis type (e.g., FM, wavetable, analog)
- Waveforms used
- Filter settings
- Modulation routings
- Effects applied in synthesis

### Initial Questions to Ask

If any information is missing, ask:

1. **What genre/subgenre is this track?** (Critical for appropriate advice)
2. **What's the BPM?** (Affects compression release times)
3. **What's the intended platform?** (Streaming, club, DJ sets)
4. **Do you have a reference track?** (Important for context)
5. **What's the current issue or goal?** (Clarity, loudness, balance, etc.)

---

## Step 2: Read Appropriate Reference Files

**CRITICAL**: Always read the relevant reference files BEFORE providing advice. The references contain detailed parameters and best practices.

### When to Read Each Reference

#### Always Read First:
**`references/mixing-fundamentals.md`**
- Read when: Starting ANY mixing or mastering task
- Contains: Gain staging, phase management, monitoring, fundamental concepts
- Essential for: Understanding the technical foundation

#### Read Based on User Need:

**`references/low-end-treatment.md`**
- Read when: User asks about kick, bass, sub-bass, or low-end interaction
- Read when: Track has both kick and bass (almost always in electronic music)
- Contains: Kick compression, bass saturation, Dynamic EQ sidechain, kick-bass interaction techniques
- Essential for: Electronic music low-end power and clarity

**`references/frequency-ranges.md`**
- Read when: User asks about EQ, frequency balance, or specific instruments
- Read when: Providing mixing advice for any track element
- Contains: Complete frequency breakdown for all instruments, EQ starting points, genre-specific targets
- Essential for: Track-by-track EQ recommendations

**`references/compression-guide.md`**
- Read when: User asks about dynamics, compression, or transient control
- Read when: Providing mixing advice requiring compression
- Contains: Compression parameters for all instruments, parallel compression, vocal staging, mix bus compression
- Essential for: Dynamic control and "glue"

**`references/mastering-chain.md`**
- Read when: User asks about mastering, loudness, LUFS targets, or final mix processing
- Read when: Track is mixed and ready for mastering phase
- Contains: Mastering chain order, EQ in mastering, limiting, platform targets, dithering
- Essential for: Final mastering and delivery

**`references/spatial-effects.md`** (when created)
- Read when: User asks about reverb, delay, stereo width, or spatial effects
- Contains: Reverb/delay strategies, send/return setup, effect EQ
- Essential for: Creating depth and space in mix

### Reading Strategy

**For mixing advice**: Read fundamentals + frequency-ranges + compression-guide + low-end-treatment
**For mastering advice**: Read fundamentals + mastering-chain
**For specific problem**: Read fundamentals + relevant specific reference

---

## Step 3: Analyze Track Elements

Based on the input, categorize tracks into:

### Rhythm Section
- **Kick Drum**: Foundation of low-end and rhythm
- **Bass/Sub-Bass**: Harmonic and tonal foundation
- **Percussion**: Hi-hats, claps, snares, shakers, etc.

### Harmonic Elements
- **Leads**: Main melodic elements
- **Pads**: Ambient, atmospheric background
- **Chords**: Harmonic support
- **Arps**: Rhythmic melodic patterns

### Effects and Atmosphere
- **FX Sweeps**: Risers, impacts, transitions
- **Ambient Textures**: Noise, field recordings, atmosphere

### Vocals (if present)
- **Lead Vocals**: Primary vocal performance
- **Backing Vocals**: Harmonies, doubles, ad-libs

---

## Step 4: Provide Track-by-Track Mixing Advice

For each track, provide a structured recommendation following this format:

### Track Mixing Template

```markdown
## [TRACK NAME] (e.g., Kick Drum, Reese Bass, Synth Lead)

**Function in Mix**: [What role does this element play?]

### High-Pass Filter (HPF)
- **Frequency**: [XX Hz]
- **Slope**: [12/18/24 dB/octave]
- **Rationale**: [Why this frequency?]

### EQ Recommendations
Based on `frequency-ranges.md`:

1. **[Frequency Range 1]**
   - Action: [Boost/Cut]
   - Amount: [±X dB]
   - Q: [Wide/Medium/Narrow]
   - Purpose: [Why this move?]

2. **[Frequency Range 2]**
   - [Continue as needed...]

### Compression
Based on `compression-guide.md`:

- **Attack**: [X ms]
- **Release**: [X ms]
- **Ratio**: [X:1]
- **Threshold**: [Set for X dB reduction]
- **Purpose**: [Why compressing?]

### Additional Processing (if needed)
- **Saturation**: [If needed for bass/harmonics]
- **Transient Designer**: [If needed for drums]
- **Stereo Width**: [Mono/Stereo/Width amount]

### Special Considerations
[Genre-specific or context-specific advice]
```

### Priority Order for Mixing Advice

Provide advice in this order:

1. **Kick Drum** (foundation)
2. **Bass/Sub-Bass** (harmonic foundation)
3. **Kick-Bass Interaction** (using `low-end-treatment.md` Dynamic EQ technique)
4. **Snare/Clap** (rhythmic counterpoint)
5. **Hi-Hats/Percussion** (high-end rhythm)
6. **Leads** (main melodic elements)
7. **Pads/Chords** (harmonic support)
8. **Arps/Plucks** (rhythmic melody)
9. **FX/Atmosphere** (space and transitions)
10. **Vocals** (if present)

---

## Step 5: Mix Bus Processing Recommendations

After individual track advice, provide mix bus guidance:

### Mix Bus Chain

Based on `compression-guide.md` and `mastering-chain.md`:

```markdown
## Mix Bus Processing

### 1. Mix Bus Compression (Glue)
- **Type**: [VCA/Opto/FET - usually VCA for electronic]
- **Ratio**: 2:1 (gentle)
- **Attack**: 30 ms (preserve transients)
- **Release**: 100 ms (auto if available)
- **Target**: 1-2 dB gain reduction MAX
- **Purpose**: Cohesion and "glue"

### 2. Optional: Mix Bus EQ
[Only if needed for broad tonal adjustments]

### 3. Target Levels for Mastering
- **Peak Level**: -6 dBFS
- **RMS Average**: -18 dBFS
- **NO limiter** on mix bus
- **Leave headroom** for mastering
```

---

## Step 6: Mastering Chain Recommendations

Based on `mastering-chain.md`:

### Mastering Workflow

```markdown
## Mastering Chain

### Genre: [User's Genre]
### Target Platform: [Streaming/Club/DJ]
### Target LUFS: [Based on genre and platform]

### Processing Chain:

1. **Gain Staging/Trim**
   - Verify input at -18 dBFS RMS average

2. **Corrective EQ** (Minimum Phase)
   - HPF at 20-30 Hz
   - [Specific corrective moves if needed]

3. **Glue Compression**
   - Type: [SSL VCA for electronic]
   - Ratio: 1.5:1 - 2:1
   - Attack: 30 ms
   - Release: 100-200 ms
   - Target: 1-2 dB GR

4. **Sweetening EQ** (Linear Phase)
   - [Broad tonal enhancements]
   - Presence: +1 to +2 dB at 2-4 kHz
   - Air: +1 to +2 dB at 10-16 kHz

5. **M-S Processing**
   - HPF on Side: 100-200 Hz (mono low-end)
   - Optional: Boost Side at 8-16 kHz (stereo width)

6. **Limiter** (True Peak)
   - Ceiling: -1.0 dBTP
   - Lookahead: ON
   - Oversampling: ON
   - Adjust threshold for target LUFS

7. **Dithering** (ONLY if exporting to 16-bit)
   - POW-r Type 2 for electronic music

### Loudness Targets by Genre:
[Based on mastering-chain.md genre-specific section]

- **Techno/Minimal**: -8 to -10 LUFS
- **House/Deep House**: -10 to -12 LUFS
- **Drum & Bass/Dubstep**: -8 to -10 LUFS
- **Trap/Hip-Hop**: -10 to -12 LUFS

### Export Specifications:

**For Streaming** (Recommended):
- Format: 24-bit WAV
- Sample Rate: 44.1 kHz or 48 kHz
- NO dither

**For CD**:
- Format: 16-bit WAV
- Sample Rate: 44.1 kHz
- YES dither (POW-r Type 2)
```

---

## Step 7: Provide Contextual Guidance

### Genre-Specific Considerations

Based on the genre identified, emphasize specific aspects:

**Techno/Minimal**:
- Very controlled dynamics (tight compression)
- Sub-bass dominance (30-60 Hz)
- Aggressive limiting (-8 to -10 LUFS)
- Minimal mid-range content
- Bright, crispy hi-hats

**House/Deep House**:
- More dynamic than techno
- Warmer overall tone
- Musical bass (not just sub)
- Balanced spectrum
- Moderate limiting (-10 to -12 LUFS)

**Drum & Bass/Dubstep**:
- Bass-focused (often loudest element)
- Very bright, aggressive high-end
- Tight, aggressive drums
- Heavy multiband compression
- Aggressive limiting (-8 to -10 LUFS)

**Trap/Hip-Hop**:
- 808 kick/bass as foundation
- Extreme high-end air (10-16 kHz)
- Vocal clarity critical
- Moderate dynamics
- Moderate limiting (-10 to -12 LUFS)

### Common Issues and Solutions

Reference the appropriate files for solutions:

- **Muddy low-end** → `frequency-ranges.md` (HPF strategies, 200-500 Hz cuts)
- **Kick and bass fighting** → `low-end-treatment.md` (Dynamic EQ sidechain)
- **Lack of punch** → `compression-guide.md` (Slow attack compression)
- **Too loud/squashed** → `mastering-chain.md` (Proper LUFS targets)
- **Poor translation** → `mixing-fundamentals.md` (Monitoring, reference tracks)

---

## Output Format Guidelines

### Structure Your Response Clearly

1. **Introduction**
   - Acknowledge the track/project
   - Confirm genre and context
   - State your approach

2. **Track-by-Track Recommendations**
   - Organized by priority (kick → bass → etc.)
   - Clear section headers
   - Specific, actionable parameters

3. **Mix Bus Processing**
   - Separate section
   - Clear chain order

4. **Mastering Chain**
   - Complete workflow
   - Genre-appropriate targets
   - Export specifications

5. **Summary/Next Steps**
   - Key priorities
   - Workflow order
   - Reference track recommendations

### Tone and Style

- **Be specific**: Give exact parameters, not vague advice
- **Be practical**: Focus on actionable steps
- **Be educational**: Explain WHY, not just WHAT
- **Be genre-aware**: Tailor advice to the specific style
- **Be realistic**: Don't over-process; preserve musicality

### Use Tables When Appropriate

Tables are excellent for:
- Parameter summaries
- Frequency breakdowns
- Compression settings
- Platform targets

---

## Example Interaction

### User Input:
> "I've just finished sound design for a techno track at 128 BPM in Am. I have MIDI for kick, bass (sub sine), lead (saw), pad, hi-hat, and clap. Can you help me with mixing and mastering advice?"

### Your Response Approach:

1. **Read references**:
   - `references/mixing-fundamentals.md` (always)
   - `references/low-end-treatment.md` (kick + bass)
   - `references/frequency-ranges.md` (all elements)
   - `references/compression-guide.md` (dynamics)
   - `references/mastering-chain.md` (final processing)

2. **Confirm details**:
   - "Great! Techno at 128 BPM in Am. Is this for club play, streaming, or both?"
   - "Do you have a reference track in mind?"

3. **Provide structured advice**:
   - Start with kick (foundation)
   - Move to bass and kick-bass interaction
   - Continue through all elements
   - Provide mix bus processing
   - Provide mastering chain with -8 to -10 LUFS target

4. **Emphasize techno-specific approaches**:
   - Tight, controlled dynamics
   - Sub-heavy kick
   - Aggressive limiting acceptable
   - Minimal mid-range
   - Bright high-end

---

## Integration with sound-design Skill

### Seamless Workflow

The **sound-design** skill produces:
- MIDI files with synthesis specifications
- Song document with musical context

This **mixing-and-mastering** skill takes that output and provides:
- Processing recommendations per track
- Mix bus treatment
- Mastering chain
- Export specifications

### When User References sound-design Output

If user says: "I used your sound-design skill to create these sounds..."

**Your response**:
1. Acknowledge the integration
2. Review the sound design specs (if provided)
3. Tailor mixing advice to the specific sounds created
4. Consider synthesis characteristics (e.g., bright sawtooth lead needs less high boost)

---

## Critical Reminders

### Always Reference Files

**Do not guess parameters** - always read the appropriate reference file and provide advice based on documented best practices.

### Prioritize Low-End

For electronic music, kick-bass relationship is **critical**. Always address this using techniques from `low-end-treatment.md`, particularly:
- Dynamic EQ sidechain (most effective)
- Complementary EQ
- Sound selection advice

### Match Genre Expectations

Different electronic subgenres have different standards:
- Techno: Aggressive, loud, tight
- House: Musical, groovy, balanced
- DnB: Bass-focused, aggressive
- Trap: 808-focused, airy

Consult `mastering-chain.md` for genre-specific approaches.

### Explain the Why

Don't just say "boost 2 kHz by 3 dB" - explain WHY:
- "Boost 2-4 kHz by 2 dB to add presence and help the lead cut through the dense mix"

### Preserve Musicality

Mixing and mastering should enhance the music, not destroy it:
- Less is more
- Preserve dynamics when appropriate
- Serve the song, not the meters

### Check Understanding

Ask if user needs clarification on:
- Specific techniques (parallel compression, M-S processing, etc.)
- Plugin selections
- Workflow order
- Listening environment considerations

---

## Advanced Scenarios

### When Mix Has Problems

If the user's mix has fundamental issues:

1. **Identify the problem clearly**
2. **Explain why it should be fixed in mixing, not mastering**
3. **Provide specific mixing fixes**
4. **Reference `mixing-fundamentals.md` philosophy: "Mastering enhances, doesn't fix"**

### When User Asks for Platform-Specific Masters

Reference `mastering-chain.md` platform targets:
- Spotify: -14 LUFS
- Apple Music: -16 LUFS
- YouTube: -13 to -14 LUFS
- Universal target: -14 LUFS + -1.0 dBTP (works everywhere)

### When User Wants Multiple Genre Approaches

Provide separate recommendations for each genre, clearly labeled.

### When Technical Terms Need Explanation

Always be ready to explain:
- LUFS vs dBFS
- True Peak vs Peak
- Attack/Release times
- Q values
- Phase vs Polarity
- Linear Phase vs Minimum Phase
- Dithering

Reference `mixing-fundamentals.md` for detailed explanations.

---

## Troubleshooting Guide

### User Says Mix Sounds "Muddy"

1. Read `frequency-ranges.md`
2. Recommend HPF on all non-bass elements
3. Check 200-500 Hz range (most common mud)
4. Suggest reference tracks

### User Says Mix Sounds "Harsh"

1. Read `frequency-ranges.md`
2. Check 2-6 kHz range
3. Suggest de-essing if vocals present
4. Consider compression settings (fast attack can emphasize harshness)

### User Says Mix Sounds "Weak" or "Quiet"

1. Read `mastering-chain.md` loudness section
2. Explain LUFS vs perceived loudness
3. Check individual track compression
4. Verify mix bus headroom (-6 dBFS peak)
5. Provide appropriate limiting settings

### User Says "Kick and Bass Fighting"

1. Read `low-end-treatment.md` IMMEDIATELY
2. Provide Dynamic EQ sidechain setup (most effective)
3. Consider complementary EQ
4. Check sound selection

---

## Final Workflow Summary

**Complete mixing and mastering process:**

1. **Preparation**
   - Gather all materials (MIDI, song doc, specs)
   - Read `references/mixing-fundamentals.md`
   - Identify genre and context

2. **Individual Track Mixing**
   - Read `references/frequency-ranges.md` and `references/compression-guide.md`
   - Provide track-by-track advice
   - Prioritize: Kick → Bass → Interaction → Rest

3. **Low-End Management**
   - Read `references/low-end-treatment.md`
   - Implement Dynamic EQ sidechain
   - Verify mono compatibility

4. **Mix Bus Processing**
   - Read `references/compression-guide.md` mix bus section
   - Light glue compression (1-2 dB GR)
   - Leave headroom for mastering

5. **Mastering**
   - Read `references/mastering-chain.md`
   - Provide complete processing chain
   - Genre-appropriate LUFS target
   - Export specifications

6. **Verification**
   - Reference track comparison
   - Multi-system listening
   - LUFS and True Peak metering

---

## Remember

- **Always read references first** - Don't guess parameters
- **Be specific and actionable** - Exact numbers, clear steps
- **Explain the why** - Educational approach
- **Adapt to genre** - One size doesn't fit all
- **Preserve musicality** - Serve the song, not the meters
- **Integration matters** - Seamless workflow from sound-design to final master

This skill transforms sound design output into professional, release-ready mixes and masters through systematic, genre-aware processing.
