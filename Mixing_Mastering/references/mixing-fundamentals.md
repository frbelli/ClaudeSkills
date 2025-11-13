# Mixing Fundamentals Reference

This reference contains essential theoretical and practical foundations for audio mixing in a DAW environment, with particular focus on electronic music production.

---

## 1. Sound Physics: Time and Frequency Domains

Every sound can be analyzed from two complementary perspectives, both essential for mastering mixing tools.

### 1.1 Frequency Domain

Sound is analyzed as a combination of simple sine waves, each with specific frequency and amplitude. The human audible spectrum ranges from approximately 20 Hz to 20,000 Hz (20 kHz).

#### Frequency Ranges and Psychoacoustic Impact

| Frequency Range | Description | Psychoacoustic Impact |
|-----------------|-------------|----------------------|
| **20-40 Hz** (Sub-bass) | At the extreme limits of human hearing, these frequencies are more _felt_ than _heard_. Most speakers cannot reproduce them accurately. Require very high volumes to be perceived. | Can induce powerful physical and mental effects: chest pressure, discomfort, disorientation. Often used in horror films to create fear. |
| **40-80 Hz** (Bass) | The fundamental frequencies of bass instruments and kick drums. Critical for groove and rhythmic power. | Provides physical impact and power. Defines the foundation of the mix. |
| **80-300 Hz** (Low-Mid) | Contains the body of many instruments. Excessive energy here creates "mud" or "boxiness." | Can make mixes sound unclear and congested if not properly managed. |
| **300-1,000 Hz** (Lower Midrange) | Relatively neutral character. Acts as an anchor and stabilizer for other frequency bands. | A mix lacking these frequencies will sound "thin" and unbalanced. |
| **1,000-8,000 Hz** (Upper Midrange) | Naturally attracts attention. The human ear is extremely sensitive in this area. Defines _presence_, _clarity_, and _punch_. | Absence makes music dull and lifeless; excess makes it piercing, overwhelming, and fatiguing. |
| **8,000-20,000 Hz** (Treble/Air) | Defines _detail_, _sparkle_, and _sizzle_. | Absence makes music muffled and dull; excess makes it harsh and unpleasant. Their presence makes music exciting (as in dance music); absence makes it more relaxing. |

#### Key Concepts

- **Logarithmic Perception**: Humans perceive frequencies logarithmically. The perceived difference between 40 Hz and 80 Hz is comparable to that between 2,000 Hz and 4,000 Hz. This frequency doubling is called an **octave**.
- **Masking**: When two sounds occupy the same frequency range, the louder one masks (hides) the quieter one, making it difficult or impossible to hear.

### 1.2 Time Domain

Sound is analyzed as a waveform whose **amplitude** (intensity) varies over time. When combining multiple tracks in a mix, their instantaneous amplitudes are mathematically summed. This process, known as **"summing"**, is literally the addition of all individual channel waveforms into a single master channel.

#### Volume Perception (Loudness)

Sound volume can be measured in two primary ways:

- **Peak Volume**: Measures the maximum instantaneous amplitude of the waveform. Essential for avoiding digital distortion (clipping), but does not accurately reflect our volume perception.
- **Average Volume (RMS)**: Measures the overall average amplitude level over time. The human ear is much more sensitive to average volume, which corresponds more faithfully to our sensation of "how loud" a sound is.

---

## 2. Digital Audio Fundamentals

In the digital world, sound is represented by a series of numbers (samples). This introduces fundamental rules and limitations every producer must know.

### 2.1 Clipping

Digital systems have an absolute maximum amplitude limit, defined as **0 dBFS** (Decibels Full Scale). Any signal exceeding this level is "clipped," flattening the top of the waveform. This generates extremely unpleasant digital distortion and must be avoided at all costs in most cases.

### 2.2 Bit Depth (Sample Resolution)

Bit depth defines the precision with which the amplitude of each sample is measured. Lower resolution introduces an artifact called **quantization noise**, a low-level hiss that can mask subtle details.

**General rule**: Each bit adds approximately **6 dB of dynamic range** (the difference between the quietest and loudest representable sound).

- **16-bit**: Standard for CD audio, offers approximately 96 dB dynamic range
- **24-bit**: Production standard, offers approximately 144 dB dynamic range (exceeds human hearing capability)

### 2.3 Sample Rate

The number of "snapshots" (samples) captured per second to represent the waveform. Sample rate determines the maximum audio frequency that can be digitally represented, known as the **Nyquist frequency**, which is exactly half the sample rate.

Example: 44.1 kHz sample rate (CD standard) can represent frequencies up to 22.05 kHz.

### 2.4 dBFS Scale

- **0 dBFS**: The absolute digital ceiling (clipping point)
- **Negative values** (e.g., -6 dBFS, -18 dBFS): Indicate how far below the ceiling the signal is
- **No positive values exist** in dBFS (unlike analog dBu scale)

---

## 3. Signal Flow and Gain Staging

### 3.1 The -18 dBFS Standard

Proper gain staging is the fundamental prerequisite for sound quality in a DAW environment, especially when using plugins modeled on analog hardware.

**Core principle**: The standard reference level for average signal (RMS) at plugin inputs and during processing should target **-18 dBFS**.

- This level corresponds approximately to **+4 dBu** in the analog domain
- Represents the optimal operating point (sweet spot) where analog simulators work with expected dynamics and noise levels
- Ensures compressors and console emulators operate in their linear region, avoiding unintended harmonic distortion or overly aggressive dynamic response

### 3.2 Gain Staging Table

| Measurement Point | Target RMS/Average Level | Maximum Peak Level | Function/Goal |
|-------------------|--------------------------|-------------------|---------------|
| DAW Input (Recording) | -18 dBFS | -10 dBFS | Ensure optimal headroom |
| Mix Levels (Post-Plugin) | -18 dBFS | -6 dBFS | Dynamic uniformity |
| Channel Faders | Unity (0 dB / 50% travel) | — | Automation precision |

### 3.3 Signal Flow Architecture

Effective mixing depends largely on correct signal flow structuring. Define a standard flowchart where the insert chain on each track follows sequential logic:

**Typical Insert Order**:
1. Filter (High-pass/Low-pass)
2. Corrective EQ
3. Compressor
4. Saturation/Creative Effects
5. Timbral EQ
6. Volume Fader

**Routing Hierarchy**:
- Individual tracks → Summing Groups (Buses) → Mix Bus
- Example groups: Drums Bus, Bass Bus, Vocal Bus, FX Bus
- VCAs (Voltage Controlled Amplifiers) used for logical, non-destructive control

### 3.4 Practical Tips

- Use a **VU Meter plugin** in the first slot, set to 0VU = -18 dBFS
- Watch the **average first**, not the peaks
- Any processor introducing gain (e.g., compressor makeup gain, EQ boosts) must be balanced by subsequent output adjustment
- Keep faders near unity gain (0 dB) initially, reserving 6-10 dB of movement for balancing and automation

---

## 4. Phase and Polarity Management

### 4.1 Definitions

- **Out of Polarity**: One waveform inverted relative to another (peaks become troughs)
- **Out of Phase**: Time delay between two signals
- Both can cause destructive cancellation

### 4.2 Phase Issues in Recording

When using multiple microphones on the same source (common for drums), temporal differences in signal arrival create phase cancellation, nullifying crucial frequencies.

**First corrective step**: Polarity inversion (the "phase" button)
- Example: The microphone positioned under the snare is almost always out of phase with the top mic
- Listen to determine which polarity produces the fuller, denser sound

**Second corrective step**: Time alignment
- If polarity inversion is insufficient, add delay (in samples or milliseconds) to perfectly align transients
- Critical operation for kick and snare drums
- Micro-delays of **0.1-1.5 ms** can make a dramatic difference

### 4.3 Comb Filtering

When a direct sound and its delayed reflection combine, they create **comb filtering**: a series of peaks and notches in the frequency spectrum.

**Causes**:
- Early room reflections combining with direct sound
- Misaligned multi-mic setups
- Speaker positioning issues

**Solution**:
- Acoustic treatment for room reflections
- Proper time alignment for multi-mic recordings
- Correct speaker positioning and symmetry

### 4.4 Critical Rule

**Align phase BEFORE equalizing or compressing!**

If phase cancellation eliminates energy at a specific frequency (e.g., 400 Hz on snare), subsequent attempts to cut or boost that region won't restore the lost signal. Phase correction must be prioritized before any dynamic or timbral processing.

---

## 5. Monitoring Environment: Your Window Into the Mix

Reliable mixing is impossible without accurate monitoring. The listening environment is the lens through which every decision is made. A flawed lens guarantees a flawed mix.

**Core principle**: THE ROOM IS AT LEAST AS IMPORTANT AS THE SPEAKERS!

### 5.1 Primary Studio Monitors

**Speakers (Monitors)**:
- Essential for accurate stereo imaging
- Allow perception of how sound interacts in physical space
- Must be thoroughly learned through comparison with reference recordings

**Cabinet Design Considerations**:
- **Ported designs**: Extend low-frequency response but can create skewed sub-bass relationships in small rooms, and may introduce resonant ringing
- **Unported (closed-box) designs**: More truthful, if less extended, bass response (e.g., Yamaha NS10, Auratone 5C)

**Positioning Principles** (non-negotiable):
1. **Equilateral Triangle**: Distance between speakers = distance from each speaker to your head
2. **On-Axis Listening**: Aim speakers directly at your ears for accurate frequency response (especially high frequencies)
3. **Symmetrical Placement**: Entire monitoring setup must be symmetrical within room to prevent unbalanced reflections
4. **Correct Width**: Too far apart destabilizes center image; better to err slightly too close together

**Headphones**:
- Supplementary tool
- Isolate from room acoustics
- Reveal low-volume details (noises, clicks) that might escape speakers

### 5.2 Room Acoustics Problems (Small Studios)

Three dominant acoustic problems compromise monitoring reliability:

#### A. Early Reflections (Primary Reflections)

Direct sound from monitors combines with first reflections from nearby surfaces (desk, walls, ceiling), creating **comb filtering** that causes unnatural peaks and cancellations in the frequency spectrum.

**Solution**: Place absorbent panels (acoustic foam) at key reflection points
**Important**: Don't overdo it! Excessive absorption creates an unnatural monitoring environment

**Mirror Trick**: Have an assistant move a mirror along walls and ceiling while you sit in listening position. Every point where you see a monitor's reflection is a primary reflection point requiring treatment.

#### B. Boundary Effect

Monitor proximity to a wall (especially corners) causes unnatural increase in low frequencies. This reinforcement can reach up to 6 dB if monitors are in corners, leading to mixes with insufficient bass.

#### C. Room Modes (Low-Frequency Resonances)

Room dimensions create standing waves at low frequencies, resulting in dramatic peaks and dips in frequency response, making bass balancing extremely unreliable.

**Formula**: First modal frequency = `172 / distance in meters`
**Impact**: A single room mode can easily push its resonant frequency 20 dB out of balance

**Solution**: Broadband absorption (**bass traps**)
- Most effective when placed in room corners (where bass builds up)
- Spaced off the wall with air gap to increase low-frequency absorption
- DIY option: 10cm-thick slabs of dense mineral fiber (50-100 kg/m³)

**Important**: Avoid listening position exactly halfway between two parallel walls (where modal problems are most pronounced)

### 5.3 Supplementary Monitoring

To ensure mix translation across diverse playback systems, use supplementary monitoring systems:

#### A. Single-Driver Midrange Monitor (Auratone-type)

- Limited frequency response is a **strength**, not weakness
- Focuses on midrange: the part that survives playback on laptops, phones, cheap radios
- Highly resistant to room mode problems due to limited low-frequency output
- **Principle**: "If your mix doesn't stand up on an Auratone, you haven't done your job properly!"

#### B. Mono Listening

Summing mix to mono forces clarity and separation without relying on stereo panning.
- Immediately highlights masking between instruments
- Exposes phase/polarity issues causing mix elements to weaken or disappear
- **Quote (Geoff Emerick)**: "Mixing in stereo [is] the easy way out."
- **Principle**: A mix that sounds solid in mono will sound even bigger in stereo

#### C. "Grotboxes" (Consumer Speakers)

Cheap, mass-market speakers reveal how mix holds up to distortion and resonance artifacts of lo-fi playback.

### 5.4 Reference Tracks for Objective Comparison

Human ears fatigue and adapt quickly, losing objectivity. Constant comparison with high-quality commercial tracks in the same genre is the most effective technique to "recalibrate ears" and maintain proper perspective.

**Methodology**:
1. Choose appropriate reference track (matching genre/style)
2. **Lower reference track volume** to match your mix level (references are already mastered and much louder)
3. Make rapid, frequent A/B comparisons
4. Evaluate key elements:
   - **Tonal balance**: Too much bass or treble compared to reference?
   - **Lead/vocal level**: Too forward or too far back?
   - **Stereo width**: Mix sounds narrow or diffuse in comparison?
   - **Dynamics**: Mix too "squashed" or too "weak"?

**Critical mistake**: Not matching perceived volume. A mastered track will always sound "better" because it's louder. Lower reference by 6-10 dB until perceived volume matches your mix. Only then is A/B comparison valid.

---

## 6. Session Preparation and Organization

Professional mixing doesn't begin with EQs and compressors, but with meticulous preparation. Sound selection, logical organization, and clean editing form the foundation of a great mix.

### 6.1 Sound Selection: The Mix's Foundation

**Core principle**: Sound selection isn't a step before mixing—**it IS the first step of mixing**.

The single most important factor for achieving a good mix is selecting sounds that work well together from the start. Especially in electronic music, think like a sculptor: each new sound must occupy complementary space, reducing the need to aggressively "chisel" with EQ later.

This proactive approach:
- Minimizes **masking** (one sound hiding another)
- Drastically reduces need for corrective processing
- Creates clearer, more powerful mixes

### 6.2 DAW Session Organization

A well-organized project is easy to navigate, minimizes errors, and frees the mind for creativity.

#### A. Bouncing MIDI to Audio

Converting MIDI tracks to audio files ("bouncing" or "rendering") offers significant advantages:
- **Reduces CPU load**: Frees computer resources for mixing plugins
- **Sound stability**: Fixes the sound, preventing accidental preset changes mid-workflow
- **Editing flexibility**: Audio files offer manipulation options (reverse, advanced time-stretching) not always available with MIDI

#### B. Visual Navigation

Implement consistent visual organization system:
- **Colors**: Assign specific colors to instrument groups (e.g., blue for drums, green for bass, red for vocals)
- **Track names**: Use clear, concise names (e.g., "Kick In", "Bass Sub", "Vocal Lead Verse")
- **Section markers**: Use DAW markers to define song sections (Intro, Verse 1, Chorus, etc.) for rapid navigation

#### C. Track Layout Standardization

Adopt a standardized track order and use it consistently across all projects:
- Common order: Drums → Percussion → Bass → Guitars → Keys → Vocals
- **Benefit**: Creates instinctive workflow (Chris Lord-Alge: "If everything is parked in the same place, all you have to worry about is the song")

#### D. Multing

"Multing" involves splitting a single audio performance across several tracks to allow unique mix settings in different song sections.

**Example**: Acoustic guitar fingerpicked in verse vs. strummed heavily in chorus
- Requires very different EQ and compression
- By multing verse and chorus to separate tracks, dial in perfect settings for each without complex automation

**Use cases**:
- Lead vocal needing different brightness/compression in verse vs. chorus
- Instrument requiring different processing in different song sections

### 6.3 Corrective Editing: Timing and Tuning

In modern commercial music, tight timing and tuning are not aesthetic choices—they are **requirements** for competitive mixes.

#### A. Timing Correction

**Strategy**: Establish a "groove reference"
1. Identify the single instrument best embodying the song's rhythmic feel (often drums)
2. If necessary, perfect the timing of this reference instrument while soloed
3. Rebuild arrangement around it, introducing other instruments one by one
4. Tighten their timing to lock with the reference

**Editing techniques to hide edit points**:
- Position edits in silence
- Hide within noisy sounds (breath, cymbal crash)
- Mask with transient of another sound (e.g., edit bass exactly where kick hits)

#### B. Tuning Correction

Poorly tuned instruments/vocals:
- Do not blend well with each other
- Consume unnecessary frequency space
- Are notoriously difficult to balance

**Best practices**:
- Avoid fully automatic modes (can create unnatural artifacts)
- Manually guide pitch correction to correct notes
- Use slowest and gentlest correction speed achieving desired result
- Take frequent breaks to maintain objectivity and avoid over-correction

#### C. Comping (Composite Take Creation)

Process of assembling the ideal performance by combining the best parts from multiple recorded takes.
- Listen to all takes
- Select best phrases or individual words
- Create a single, impeccable "master" track

**Method**: Create a "comp sheet" listing each musical phrase and rating each take, to systematically assemble the best possible version.

---

## 7. Key Mixing Principles

### 7.1 The 80/20 Rule

Be prepared to dedicate 80% of your time to achieve the last 20% of quality. Small details and micro-adjustments separate good mixes from excellent mixes.

### 7.2 Trust Your Ears

If it sounds good, it IS good. Rules and techniques are guides, not dogma. Critical listening is the final judge.

### 7.3 Take Regular Breaks

Auditory fatigue is the worst enemy of a mixing engineer. After a couple hours of work, your perception of bass and treble will be compromised. Take regular breaks and, if possible, listen to the mix the next day with fresh ears.

### 7.4 Don't Fix Arrangement Problems with Mixing

If two parts clash musically, the best solution isn't surgical EQ—it's muting one or rewriting it. Mixing cannot save a poor arrangement.

### 7.5 Jack Joseph Puig's Rule of Three

"The ear can process only three things at once."

At any given moment in the song:
1. Identify the three most important elements
2. Mute everything else
3. If the song still works, every other part is a candidate for removal or reduction

This isn't just about cleaning up mud—it's about directing the listener's focus.

### 7.6 Create Light and Shade

Static arrangements become boring quickly. Vary instrumentation between sections to create dynamics.

**Example**: Dropping out rhythm guitar in verse makes its return in chorus feel bigger and more impactful.

**Advanced technique - Drop Chorus**: Build into final chorus, then "drop" to just vocal and minimal rhythm section. Creates surprise and focus, making subsequent full arrangement return feel even more explosive.

---

## 8. Workflow Philosophy: Fader Instability as Diagnosis

**Core methodology**: Build the mix one track at a time, in order of musical importance.

**Guiding principle**: Let "fader instability" guide you. If a track's fader cannot be set to a single, stable level where it works throughout a section, that instability is a **diagnosis**.

It tells you that some form of processing is required to solve a problem with the track's dynamics or tone.

**Ultimate goal**: Process each track just enough so it can sit at a static fader level, perfectly balanced against everything else.

---

## Summary

These fundamental concepts form the bedrock of professional mixing:

1. **Sound exists in both time and frequency domains** - understanding both is essential
2. **Digital audio has specific rules and limits** that must be respected
3. **Proper gain staging (-18 dBFS standard)** ensures optimal plugin operation
4. **Phase and polarity** must be corrected before any other processing
5. **Monitoring environment** is as critical as the speakers themselves
6. **Sound selection and preparation** are the first steps of mixing
7. **Organization and workflow** prevent errors and enable creativity
8. **Trust your ears** while understanding the technical foundations

Master these fundamentals before diving into specific processing techniques. They are the lens through which all mixing decisions are made.
