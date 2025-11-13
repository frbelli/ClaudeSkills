# Spatial Effects Reference

## Overview
Comprehensive guide to reverb, delay, and spatial processing techniques for creating depth, dimension, and space in mixes. This reference covers both technical parameters and creative applications.

---

## Table of Contents
1. [Reverb Fundamentals](#reverb-fundamentals)
2. [Reverb Types & Algorithms](#reverb-types--algorithms)
3. [Reverb Parameters](#reverb-parameters)
4. [Delay Fundamentals](#delay-fundamentals)
5. [Delay Types & Techniques](#delay-types--techniques)
6. [Creating Depth & Dimension](#creating-depth--dimension)
7. [Advanced Spatial Techniques](#advanced-spatial-techniques)
8. [Genre-Specific Applications](#genre-specific-applications)
9. [Common Issues & Solutions](#common-issues--solutions)

---

## Reverb Fundamentals

### Natural Reverberation Physics

**Acoustic Behavior:**
- Early reflections (0-80ms): First discrete echoes from nearby surfaces
- Pre-delay gap: Time between direct sound and first reflections
- Early decay: Initial density buildup (80-200ms)
- Late reflections: Dense reverberant tail
- Decay time (RT60): Time for reverb to drop 60dB

**Room Acoustics:**
- Small rooms: 0.2-0.6s decay, prominent early reflections
- Medium rooms: 0.6-1.5s decay, balanced character
- Large halls: 1.5-4s+ decay, smooth long tail
- Surface materials affect frequency-dependent absorption

### Psychoacoustic Principles

**Spatial Perception:**
- Early reflections define perceived room size and geometry
- Reverb tail provides ambient context and emotional character
- Pre-delay separates direct sound from reverb (clarity preservation)
- Frequency balance affects perceived distance and environment

**Distance Cues:**
- Direct-to-reverberant ratio (D/R ratio)
- High frequency rolloff (air absorption simulation)
- Pre-delay amount
- Early reflection pattern

---

## Reverb Types & Algorithms

### Algorithmic Reverb Types

#### **1. Room Reverb**
```
Characteristics:
- Decay time: 0.2-0.8 seconds
- Prominent early reflections
- Intimate, present character
- Clear articulation

Applications:
- Vocals (intimate feel)
- Acoustic instruments
- Dialogue/speech
- Tight rhythm sections

Parameter Ranges:
- Size: 10-50 m²
- Pre-delay: 0-20ms
- Decay: 0.2-0.8s
- ER/Tail balance: Favor early reflections
```

**Best Practices:**
- Use for sources that need to stay upfront
- Keep decay times short to maintain clarity
- Adjust early reflections to simulate specific room types
- Consider room reverb for "in the room with you" feel

#### **2. Hall Reverb**
```
Characteristics:
- Decay time: 1.5-4+ seconds
- Smooth, lush tail
- Gradual density buildup
- Spacious, elegant character

Applications:
- Orchestral music
- Ballads and emotional pieces
- Pad sounds and synths
- Cinematic soundtracks

Parameter Ranges:
- Size: 500-3000 m²
- Pre-delay: 20-60ms
- Decay: 1.5-4.0s
- High damping: 3-8kHz
```

**Best Practices:**
- Ideal for creating grandeur and emotion
- Use longer pre-delays to maintain separation
- Apply high-frequency damping to avoid harshness
- Consider stereo width for immersive experience

#### **3. Chamber Reverb**
```
Characteristics:
- Decay time: 0.8-1.8 seconds
- Rich early reflections
- Warm, enveloping character
- Dense midrange

Applications:
- Vocals (classic sound)
- Drum rooms
- Vintage recordings
- Rock and indie productions

Parameter Ranges:
- Size: 50-200 m²
- Pre-delay: 10-30ms
- Decay: 0.8-1.8s
- Moderate diffusion
```

**Vintage Emulations:**
- Capitol Studios echo chambers
- Abbey Road chambers
- Columbia Records 30th Street Studio

#### **4. Plate Reverb**
```
Characteristics:
- Bright, dense character
- Quick buildup
- Smooth decay
- Distinctive metallic quality

Applications:
- Vocals (radio/pop production)
- Snare drums
- Percussion
- Any source needing presence + space

Classic Models:
- EMT 140 (2.7s decay)
- EMT 240 (compact version)
- Various plugin emulations

Parameter Focus:
- Pre-delay: 0-40ms
- Decay: 1-5s (typically 2-3s)
- High frequency damping
- Low-cut to avoid muddiness
```

#### **5. Spring Reverb**
```
Characteristics:
- Boingy, mechanical character
- Non-linear frequency response
- Vintage texture
- Quick attack

Applications:
- Guitar amplifiers
- Surf music
- Vintage keyboards
- Lo-fi/retro productions

Typical Implementations:
- Fender spring tanks (guitar amps)
- Hammond organs
- Dub reggae
- Rockabilly recordings
```

#### **6. Convolution Reverb**
```
Technology:
- Uses impulse responses (IR) of real spaces
- Exact acoustic reproduction
- High CPU usage
- Static spatial characteristics

Applications:
- Realistic room placement
- Matching production environments
- Sound design (creative IRs)
- Post-production dialogue

IR Sources:
- Concert halls
- Churches and cathedrals
- Studios and rooms
- Creative/unusual spaces
```

**Considerations:**
- Choose IR length carefully (CPU impact)
- Pre-process IRs (EQ, trim) for better results
- Use for realistic acoustic environments
- Combine with algorithmic reverbs for movement

### Advanced Algorithm Types

#### **Shimmer Reverb**
- Pitch-shifted reflections (octave up)
- Ethereal, ambient character
- Popular in post-rock, ambient, cinematic

#### **Gated Reverb**
- Abrupt tail cutoff via noise gate
- 1980s drum sound (Phil Collins)
- Controlled by threshold and hold time

#### **Reverse Reverb**
- Builds up before source hits
- Dramatic effect for transitions
- Requires pre-planning/bouncing

#### **Non-Linear Reverb**
- Unconventional decay envelopes
- Can increase in volume over time
- Used for special effects

---

## Reverb Parameters

### Core Parameters

#### **1. Pre-Delay**
```
Range: 0-120ms (typical)
Function: Gap between dry signal and reverb onset

Settings by Purpose:
- 0-5ms: Tight integration
- 10-20ms: Subtle separation (vocals)
- 30-50ms: Clear articulation
- 60-100ms: Dramatic separation
- 100ms+: Special effects

Technical Note:
Pre-delay = Distance / Speed_of_sound
~1ms per foot from source to wall
```

**Application Guidelines:**
- Vocals: 20-40ms (maintains clarity)
- Snare: 0-10ms (blended sound)
- Strings: 30-60ms (preserves attack)
- Percussion: Variable (rhythmic considerations)

#### **2. Decay Time (RT60)**
```
Definition: Time for reverb to decay 60dB

Ranges by Type:
- Small room: 0.2-0.8s
- Medium room: 0.8-1.5s
- Large hall: 1.5-3.0s
- Cathedral: 3.0-8.0s+

Mixing Considerations:
- Tempo-sync to avoid rhythmic clutter
- Shorter for busy mixes
- Longer for sparse arrangements
- Different decay times for different sources
```

**Tempo Synchronization:**
```
Decay ≈ Note_value × 1.5-2.0

Examples (120 BPM = 500ms per beat):
- Quarter note: 750-1000ms
- Dotted quarter: 1125-1500ms
- Half note: 1500-2000ms
```

#### **3. Size/Room Size**
```
Parameter Type: Physical modeling dimension
Affects: Early reflection spacing and reverb character

Ranges:
- Tiny: <20 m² (vocal booth)
- Small: 20-50 m² (control room)
- Medium: 50-200 m² (studio live room)
- Large: 200-1000 m² (concert hall)
- Huge: 1000+ m² (cathedral)

Relationship to Other Parameters:
- Larger size → Longer pre-delay naturally
- Larger size → More diffuse reflections
- Size affects early reflection pattern
```

#### **4. Damping/High Frequency Absorption**
```
Function: Simulates frequency-dependent absorption

Physical Basis:
- Air absorbs high frequencies over distance
- Soft materials absorb highs preferentially
- Creates warmth and realism

Typical Settings:
- Low damping (3-5kHz): Bright, open spaces
- Medium damping (5-8kHz): Natural rooms
- High damping (8-12kHz): Warm, intimate
- Extreme damping (12kHz+): Dark, dead spaces

Mixing Applications:
- Bright sources → More damping
- Dark sources → Less damping
- Create distance illusion via HF rolloff
```

#### **5. Diffusion**
```
Definition: Density and smoothness of reflections

Settings:
- Low diffusion (0-30%):
  • Discrete, audible reflections
  • Flutter echoes possible
  • Rhythmic character
  
- Medium diffusion (30-70%):
  • Balanced reflection density
  • Natural room character
  • Versatile for most sources
  
- High diffusion (70-100%):
  • Smooth, dense tail
  • No discrete reflections
  • Pad-like character
```

#### **6. Early Reflections Level**
```
Function: Balance between ER and reverb tail

Relationships:
- High ER level: Defined space, upfront
- Low ER level: Distant, ambient
- ER pattern defines room geometry

Separate ER Control:
Some reverbs offer independent:
- ER level
- ER delay
- ER pattern selection
```

### Advanced Parameters

#### **Modulation**
```
Purpose: Adds movement and prevents metallic artifacts

Parameters:
- Rate: 0.1-5 Hz (typical)
- Depth: Subtle to obvious pitch variation

Applications:
- Smooths out algorithm artifacts
- Creates chorus-like width
- Adds organic quality

Caution:
- Too much = seasick feeling
- Keep subtle for realism
```

#### **Density**
```
Function: Reflection build-up speed

Settings:
- Low: Gradual buildup, spacious
- High: Instant dense tail, tight

Use Cases:
- Low density: Large halls, slow music
- High density: Drums, rhythmic material
```

#### **Mix/Wet-Dry Balance**
```
Critical Mixing Parameter:

Send/Return Method (Preferred):
- 100% wet on reverb return
- Control via send level
- Parallel processing advantages

Insert Method:
- Adjust wet/dry mix parameter
- Useful for quick setup
- Less flexible for complex mixes

Typical Mix Levels:
- Subtle ambience: 10-20% wet
- Present reverb: 20-40% wet
- Obvious effect: 40-60% wet
- Special effects: 60-100% wet
```

#### **Width/Stereo Spread**
```
Controls spatial distribution of reverb

Settings:
- 0% (mono): Center-focused, vintage
- 50%: Natural stereo
- 100%: Wide, modern
- >100%: Exaggerated width

Considerations:
- Too wide can lack impact
- Mono compatibility check
- Match to source width
```

---

## Delay Fundamentals

### Basic Delay Concepts

**Core Principle:**
```
Delayed signal = Original signal + Time_offset

Parameters:
1. Delay time (ms or note values)
2. Feedback (number of repeats)
3. Mix level (blend with dry)
4. Filtering (tone of repeats)
```

**Temporal Perception:**
```
<20ms: Perceived as thickening/coloration
20-40ms: Doubling/slapback effect
40-100ms: Discrete echo audible
>100ms: Clear rhythmic delay
```

### Delay Types Overview

#### **Digital Delay**
- Clean, precise repeats
- Consistent timing
- Modern sound
- Flexible modulation

#### **Analog Delay**
- Warm, degraded repeats
- Slight pitch/timing drift
- Darker tone each repeat
- Vintage character

#### **Tape Delay**
- Natural wow/flutter
- High-frequency rolloff
- Compression artifacts
- Organic degradation

---

## Delay Types & Techniques

### Standard Delay Types

#### **1. Slapback Delay**
```
Definition: Single, fast repeat (40-120ms)

Classic Settings:
- Time: 60-120ms
- Feedback: 0% (one repeat only)
- Mix: 20-40%
- Filter: Optional high-cut

Origins: Rockabilly, early rock & roll
Famous Use: Elvis Presley vocals

Applications:
- Vocals (energy and presence)
- Guitars (rockabilly)
- Snare (fatness without reverb)
```

**Implementation Tips:**
- Use mono delay for vintage vibe
- Adjust time to avoid comb filtering
- Can replace/augment short reverb
- Great for adding life to dry sources

#### **2. Ping-Pong Delay**
```
Definition: Alternating left-right repeats

Settings:
- Time: Typically tempo-synced
- Feedback: 30-70%
- Stereo width: 100%
- Pan law: Hard L/R alternation

Applications:
- Synth leads
- Guitar solos
- Spacious vocals
- Electronic production

Variations:
- Equal level bounces
- Volume-reduced alternates
- Filtered bounces
- Modulated ping-pong
```

#### **3. Dotted Eighth Delay**
```
Timing: 3/16 note (dotted eighth)

Musical Effect:
- Creates polyrhythmic texture
- Very popular in modern production
- Works well with sustained notes

Famous Examples:
- The Edge (U2) - "Where the Streets Have No Name"
- Countless modern worship music

Settings:
- Time: Dotted eighth note
- Feedback: 2-4 repeats typical
- Mix: 15-35%
- Often combined with reverb
```

**Calculation:**
```
At 120 BPM:
- Quarter note = 500ms
- Dotted eighth = 375ms

Formula: (60,000 / BPM) × 0.75
```

#### **4. Dual/Multi-Tap Delay**
```
Definition: Multiple independent delay taps

Applications:
- Complex rhythmic patterns
- Stereo widening
- Simulating multiple rooms
- Sound design

Configuration:
Tap 1: 180ms, -3dB, L
Tap 2: 240ms, -6dB, R
Tap 3: 360ms, -9dB, C
(Example only - infinitely variable)
```

### Vintage Delay Emulations

#### **Tape Echo Machines**

**Watkins Copicat**
```
Characteristics:
- Tape loop mechanism
- Multiple playback heads
- Natural saturation
- Warm, degraded repeats

Settings:
- Delay time: Fixed heads positions
- Repeat rate: Feedback control
- Tone: Often dark, murky
```

**Roland Space Echo (RE-201)**
```
Legendary Features:
- Tape + spring reverb combination
- Multiple playback heads (3 delays)
- Built-in preamp/saturation
- Adjustable tape speed

Iconic Settings:
- "Long" mode: 600ms max
- "Short" mode: 200ms
- Reverb: Bright spring character
- Wow/flutter adds movement

Famous Users:
- Dub reggae (Lee "Scratch" Perry)
- Pink Floyd
- Radiohead
```

**Maestro Echoplex (EP-3)**
```
Characteristics:
- Clean tape echo
- Sound-on-sound capability
- Feedback oscillation
- Excellent for ambient

Applications:
- Guitar (David Gilmour)
- Ambient loops
- Sound effects
```

#### **Analog Delay Units**

**Boss DM-2 Delay**
- Bucket brigade (BBD) circuit
- Warm, slightly degraded repeats
- 300ms max delay time
- Classic guitar pedal

**Electro-Harmonix Deluxe Memory Man**
- Analog BBD delay
- Built-in modulation
- Up to 550ms delay
- Warm, musical character

**MXR Carbon Copy**
- Modern BBD design
- Modulation switch
- 600ms max
- Pedalboard-friendly

### Advanced Delay Techniques

#### **Reverse Delay**
```
Effect: Each repeat plays backwards

Applications:
- Experimental/psychedelic
- Lead-ins to events
- Sound design
- Ambient textures

Implementation:
- Some plugins offer native reverse
- Or: bounce delay track and reverse
```

#### **Filtered/Ducked Delay**
```
Ducking:
- Delay level drops when signal present
- Prevents clutter
- Maintains clarity

Filtering:
- High-pass delay repeats
- Low-pass for dark trails
- Bandpass for telephone effect

Use Cases:
- Dense mixes
- Rhythmic material
- Clarity preservation
```

#### **Feedback Loop Processing**
```
Technique: Insert effects in delay feedback path

Possibilities:
- Filter sweep on repeats
- Pitch shift (shimmer effect)
- Distortion (degradation)
- Reverb (spatial evolution)

Setup:
Requires delay with feedback send/return
or plugin with feedback processing
```

#### **Throw Delay**
```
Application: Momentary delay effect

Technique:
- Route to delay send
- Automate send level
- Single word/note gets delayed
- Creates emphasis

Common Uses:
- Vocal ad-libs
- Last word of phrase
- Snare fills
- Transition effects
```

---

## Creating Depth & Dimension

### The Depth Pyramid

**Front to Back Layering:**
```
FRONT (Dry, present):
├─ Lead vocal (minimal reverb)
├─ Bass (DI, direct)
└─ Kick (dry, punchy)

MIDDLE (Moderate space):
├─ Rhythm guitars (room reverb)
├─ Snare (small room)
└─ Lead instruments (balanced)

BACK (Spacious):
├─ Pads/strings (long reverb)
├─ Cymbals (plate reverb)
└─ Ambient elements (hall)
```

### Reverb Techniques for Depth

#### **1. Multiple Reverb Strategy**
```
Approach: Different reverbs for different depths

Example Setup:
Reverb 1 (Close): Small room, 0.6s
- Rhythm section
- Lead vocals
- Upfront instruments

Reverb 2 (Mid): Medium hall, 1.4s
- Guitars
- Keys
- Backing vocals

Reverb 3 (Far): Large hall, 3.0s
- Pads
- Cymbals
- Ambient elements

Benefits:
- Clear depth separation
- CPU efficient vs. individual reverbs
- Coherent spatial image
```

#### **2. Pre-Delay for Distance Control**
```
Distance Simulation:

Near (intimate):
- Pre-delay: 0-10ms
- Reverb: Short, bright
- Direct/reverb ratio: High direct

Medium:
- Pre-delay: 20-40ms
- Reverb: Medium decay
- D/R ratio: Balanced

Far (distant):
- Pre-delay: 50-80ms
- Reverb: Long, dark
- D/R ratio: Favor reverb
```

#### **3. Frequency-Dependent Reverb**
```
Concept: Different reverb amount per frequency

Implementation:
1. Send source to reverb
2. EQ reverb return:
   - High-pass: 200-400Hz (reduce mud)
   - Low-pass: 6-10kHz (warmth)
   - Presence boost: 3-5kHz (air)

Advanced:
- Multiband send to reverb
- Only reverb specific frequency ranges
- Parallel compression on reverb
```

### Width and Depth Integration

**Combined Stereo/Reverb Strategy:**
```
Vocal Example:

Lead Vocal:
├─ Mono, center
├─ Pre-delay: 30ms
├─ Room reverb: 0.8s
└─ Subtle ambience

Backing Vocals:
├─ Wide stereo (L/R panned)
├─ Pre-delay: 40ms
├─ Hall reverb: 1.8s
└─ More spatial presence

Result: Depth AND width separation
```

### Early Reflections for Realism

**ER Patterns by Environment:**
```
Small Room:
- First reflection: 5-10ms
- Dense pattern
- Irregular spacing

Concert Hall:
- First reflection: 30-50ms
- Sparse initial pattern
- Gradual density increase

Cathedral:
- First reflection: 80-120ms
- Very sparse
- Long build-up time
```

**Separate ER Processing:**
Some reverbs allow independent ER control:
- Use ER only for subtle space
- Add tail separately as needed
- More flexible than combined reverb

---

## Advanced Spatial Techniques

### Side-Chain Processing

#### **Ducked Reverb**
```
Setup:
1. Send vocal to reverb (100% wet)
2. Side-chain compress reverb from vocal
3. Reverb ducks when vocal present

Parameters:
- Ratio: 4:1 to 6:1
- Attack: Fast (1-5ms)
- Release: Medium (50-150ms)
- Threshold: Adjust for desired ducking

Benefits:
- Clear vocal during performance
- Reverb swells between phrases
- Reduces mud and clutter
```

#### **Ducked Delay**
```
Similar Principle:
- Delay quieter during direct sound
- Swells in gaps

Applications:
- Dense mixes
- Rhythmic material
- Maintaining intelligibility
```

### Parallel Spatial Processing

**Concept: Blend dry and wet independently**

#### **Parallel Reverb**
```
Method 1: Aux/Send Track
- Send to reverb (100% wet)
- Control blend via send level
- Compress reverb separately
- EQ reverb return independently

Method 2: Duplicate Track
- Duplicate source track
- Apply reverb 100% to duplicate
- Process wet track (EQ, compression)
- Balance with original
```

**Benefits:**
- Heavy processing without losing direct sound
- Independent dynamic control
- Creative processing options
- Better gain structure

#### **The "Reverb Swell" Technique**
```
Application: Ambient pads between events

Setup:
1. Long reverb (3-5s) on aux
2. Heavy compression on reverb return
3. Send short notes to reverb
4. Compression creates reverb swell

Use in:
- Ambient music
- Post-rock
- Cinematic underscore
```

### Reverb Automation

**Dynamic Reverb Amount:**
```
Vocal Example:

Verse:
- Less reverb (intimate)
- Send level: -20dB

Chorus:
- More reverb (big)
- Send level: -12dB

Bridge:
- Minimal (dry, raw)
- Send level: -30dB

Post-Chorus:
- Maximum space
- Send level: -8dB
```

**Parameter Automation:**
- Decay time (build/release)
- Pre-delay (distance shifts)
- High damping (tone changes)
- Width (expansion/contraction)

### Creative Spatial Chains

#### **Reverb into Delay**
```
Signal Flow:
Source → Reverb → Delay → Output

Effect:
- Reverb tail gets repeated
- Rhythmic spatial movement
- Complex, evolving texture

Applications:
- Lead guitars
- Synth pads
- Ambient vocals
```

#### **Delay into Reverb**
```
Signal Flow:
Source → Delay → Reverb → Output

Effect:
- Distinct delays enter reverb
- Each repeat has own space
- More natural, less robotic

Applications:
- Most common routing
- Acoustic instruments
- Realistic spatial placement
```

#### **Parallel Delay + Reverb**
```
Signal Flow:
        ┌→ Delay → Output
Source →┤
        └→ Reverb → Output

Benefits:
- Independent control
- Different settings possible
- Maximum flexibility
```

### Modulated Reverb/Delay

**Chorus in Reverb:**
```
Parameters:
- Rate: 0.2-0.8 Hz
- Depth: Subtle
- Mix: 10-30%

Effect:
- Smoother tail
- Reduced metallic artifacts
- Width enhancement
- Organic movement
```

**Modulated Delay:**
```
Classic: Tape Wow/Flutter

Settings:
- Rate: 0.5-2 Hz
- Depth: Light to moderate
- Type: Random or sine wave

Results:
- Analog character
- Movement in repeats
- Less static feel
```

---

## Genre-Specific Applications

### Pop/R&B Production

**Vocal Treatment:**
```
Lead Vocal:
- Pre-delay: 25-35ms
- Room/Chamber: 1.0-1.5s
- Damping: 6-8kHz
- Mix: 15-25%

Doubles/Ad-libs:
- Slap delay: 80-100ms (one repeat)
- Plate reverb: 2.0s
- Wider stereo spread
- Higher mix level (30-40%)

Backing Vocals:
- Hall reverb: 2.0-3.0s
- Less direct sound
- Heavily filtered (HPF 500Hz)
```

**Drums:**
```
Kick: Minimal/none (tightness)
Snare:
- Gated reverb (1980s) or
- Tight room (0.4-0.8s) modern
Toms: Room ambience
Cymbals: Plate or hall (long)
```

### Rock/Alternative Production

**Guitar Spatial Treatment:**
```
Rhythm Guitars:
- Room reverb: 0.8-1.2s
- Slight delay: Quarter note
- Keep tight for groove

Lead Guitars:
- Longer reverb: 1.5-2.5s
- Dotted eighth delay
- Stereo spread
- More presence

Ambient/Textural:
- Long hall: 3-4s
- Reverse reverb
- Heavy modulation
```

**Drums:**
```
Snare:
- Big room: 1.2-1.8s
- Natural ambience
- Can be prominent

Toms:
- Similar to snare
- Pitch-dependent decay

Overheads:
- Plate or hall
- Blend for cohesion
```

### Electronic/EDM Production

**Synth Processing:**
```
Leads:
- Ping-pong delay
- Short plate reverb
- Keep upfront but spacious

Pads:
- Long hall: 4-6s
- Heavy reverb mix (40-60%)
- Creates wash/bed

Plucks:
- Dotted eighth delay
- Minimal reverb
- Rhythmic movement

Bass:
- Usually minimal spatial processing
- Possible short room for realism
```

**Drums:**
```
Kick: Dry (club system consideration)
Snare:
- Short reverb
- Often heavily processed
- Can be synthetic
Claps: Room for natural feel
Hats/Cymbals: Varied by subgenre
```

### Orchestral/Cinematic

**Depth Layering:**
```
Close (Soloists):
- Small hall: 1.2-1.8s
- Clear early reflections
- High detail

Mid (Sections):
- Medium hall: 1.8-2.5s
- Balanced D/R ratio

Far (Ambience):
- Large hall/cathedral: 3.0-6.0s
- Lush, long decay
```

**Technique:**
```
Convolution Reverb Preferred:
- Real hall IRs
- Authentic acoustics
- Multiple mic positions

Considerations:
- Match reverb to perceived distance
- Use pre-delay for depth
- Different reverb amounts per section
- Maintain clarity in climaxes
```

### Jazz/Acoustic

**Natural Space Philosophy:**
```
Approach:
- Emulate live performance space
- Consistent reverb across elements
- Subtle, supportive spatial treatment

Room/Chamber Preferred:
- Decay: 1.0-1.8s
- Natural early reflections
- Warm character
```

**Per-Element Treatment:**
```
Vocals: Light room (presence)
Acoustic instruments:
- Natural ambience
- Room or small hall
- Preserve acoustic character

Drums:
- Kit-wide room treatment
- Natural blend
- Avoid artificial separation

Bass:
- Minimal space
- Direct sound priority
```

### Hip-Hop/Trap Production

**Vocal Treatment:**
```
Modern Aesthetic:
- Lead: Minimal reverb, upfront
- Slap delay common (60-80ms)
- Short plate if reverb used

Doubles:
- Short reverb
- Wider panning
- Delay throw effects

Ad-libs:
- Ping-pong delay
- Short reverb
- Heavy effects acceptable
```

**Drums:**
```
808/Bass: Completely dry
Snare:
- Often minimal
- Short room if any
- Sometimes reverse reverb

Hi-hats: Dry or subtle room
Claps: Short reverb possible
```

**Creative Effects:**
```
Reverse reverb on ad-libs
Delay throws on vocal phrases
Heavy reverb on melodic elements
Minimal on rhythmic elements
```

---

## Common Issues & Solutions

### Problem: Muddy Mix

**Causes:**
- Too much reverb in low frequencies
- Long decay times in busy mix
- Multiple reverbs without high-pass filtering

**Solutions:**
```
1. High-Pass Filter Reverb Returns:
   - 200-400Hz typical
   - Prevents bass buildup in reverb

2. Reduce Low-Frequency Reverb Decay:
   - Many reverbs have bass multiplier
   - Set to 0.5-0.7x of main decay

3. Use Shorter Decay Times:
   - Tempo-appropriate lengths
   - Faster songs = shorter reverbs

4. Side-Chain Reverb:
   - Duck reverb when source plays
   - Swells between notes/phrases
```

### Problem: Loss of Clarity

**Causes:**
- Insufficient pre-delay
- Too much reverb mix
- Early reflections masking direct sound

**Solutions:**
```
1. Increase Pre-Delay:
   - Start at 20-30ms
   - Adjust upward until clarity returns

2. Reduce Reverb Mix Level:
   - Often less is more
   - Try 10-20% for subtle space

3. Filter Reverb:
   - High-pass at 300-500Hz
   - Low-pass at 8-10kHz
   - Carve room for direct sound

4. Use Shorter Decay:
   - Prevents overlapping tails
   - Maintains rhythmic definition
```

### Problem: Delay Clutter

**Causes:**
- Too many feedback repeats
- Wrong delay time for tempo
- Multiple delays conflicting

**Solutions:**
```
1. Tempo-Sync Delays:
   - Match BPM exactly
   - Use musical divisions
   - Dotted notes often work best

2. Reduce Feedback:
   - 2-3 repeats usually sufficient
   - More can cloud mix

3. Filter Delay Repeats:
   - High-pass to reduce low-end buildup
   - Low-pass for darker trails

4. Duck Delay:
   - Side-chain from source
   - Repeats quieter during performance
```

### Problem: Reverb Sounds Artificial

**Causes:**
- Poor algorithm/preset selection
- Insufficient diffusion
- Too much modulation
- Unrealistic parameter combinations

**Solutions:**
```
1. Choose Better Algorithm:
   - Convolution for realism
   - Quality algorithmic reverbs
   - Match reverb type to source

2. Adjust Diffusion:
   - Increase for smoother tail
   - Reduce flutter echoes

3. Subtle Modulation:
   - 0.2-0.5 Hz rate
   - Light depth
   - Can smooth artifacts

4. Natural Parameters:
   - Match decay to room size
   - Appropriate damping
   - Realistic early reflections
```

### Problem: Stereo Image Collapse

**Causes:**
- Mono reverb on stereo sources
- Phase issues in reverb
- Over-widened reverb

**Solutions:**
```
1. Use Stereo Reverb:
   - Maintain or enhance width
   - Match source stereo field

2. Check Phase:
   - Mono compatibility test
   - Avoid excessive width
   - Mid-side processing if needed

3. Balance Width:
   - Not everything needs 100% width
   - Vary reverb widths for depth
   - Center elements can stay narrow
```

### Problem: Reverb Sounds Harsh

**Causes:**
- Insufficient high-frequency damping
- Bright source + bright reverb
- Excessive early reflections

**Solutions:**
```
1. Increase Damping:
   - Start at 5-7kHz
   - Adjust to taste
   - Emulates air absorption

2. Low-Pass Filter Reverb:
   - 8-12kHz typical
   - Subtle rolloff
   - Smooth without dulling

3. Reduce Early Reflections:
   - Balance with tail
   - Less discrete reflections
   - Smoother buildups

4. Choose Warmer Algorithm:
   - Vintage plates
   - Chambers
   - Avoid bright halls
```

### Problem: Delay Feedback Oscillation

**Causes:**
- Feedback set too high (>100%)
- Additional gain in feedback path
- Resonant filtering in feedback

**Solutions:**
```
1. Reduce Feedback Amount:
   - Keep below 100%
   - Watch for buildup

2. Check Signal Path:
   - Remove gain plugins
   - Avoid feedback loop through mixer

3. Filter Feedback:
   - High-pass to prevent low buildup
   - Low-pass to dampen oscillation
   - Gentle slopes preferred

4. Use Feedback Limiter:
   - Some delays have built-in limiting
   - Prevents runaway feedback
```

### Problem: Vocal Buried by Reverb

**Causes:**
- Too much reverb mix
- Wrong reverb type
- Insufficient pre-delay
- Reverb competing in vocal frequency range

**Solutions:**
```
1. Reduce Reverb Level:
   - 15-25% typical for lead vocals
   - Less can often work better

2. Increase Pre-Delay:
   - 30-40ms for clear separation
   - Allows consonants to speak

3. EQ Reverb Return:
   - High-pass at 300-500Hz
   - Notch out 2-4kHz (vocal presence)
   - Low-pass at 8-10kHz

4. Use Appropriate Reverb:
   - Plate or chamber for vocals
   - Shorter decay (1-2s)
   - Avoid long halls

5. Automate Reverb:
   - Less during verses
   - More during sustained notes
   - Pull back on consonants
```

---

## Technical Tips & Best Practices

### Signal Flow Optimization

**Reverb Send Strategy:**
```
Preferred Method: Aux Send/Return

Advantages:
- 100% wet reverb
- Multiple sources to one reverb
- Parallel processing options
- Better gain structure
- CPU efficiency

Setup:
1. Create aux track with reverb (100% wet)
2. Send sources to aux via send knobs
3. Return aux to main mix
4. Control blend via send level
```

**Reverb Insert Method:**
```
When to Use:
- Quick setup for single source
- Creative processing needed
- Source-specific reverb character

Limitations:
- Less flexible blending
- CPU less efficient
- Harder to share processing
```

### CPU Management

**Efficiency Strategies:**
```
1. Share Reverbs:
   - 2-4 reverb types typically sufficient
   - Send multiple sources to each
   - More CPU-friendly

2. Use Lower Quality During Composition:
   - Switch to high quality for mixdown
   - Saves CPU during editing

3. Freeze/Bounce Reverb Tracks:
   - Commit to reverb choices
   - Free up CPU
   - Can always revert

4. Convolution IR Length:
   - Shorter IRs use less CPU
   - Trim unnecessary IR length
   - 2-3 seconds often sufficient
```

### Mono Compatibility

**Testing:**
```
1. Check Mix in Mono:
   - Use mono button on interface
   - Check for phase issues
   - Ensure reverb doesn't disappear

2. Reverb Width Considerations:
   - 100% width not always necessary
   - Some mono reverb for center focus
   - Balance stereo and mono elements

3. Problem Solving:
   - If reverb cancels in mono
   - Reduce stereo width slightly
   - Use mid-side processing
   - Check for phase-inverted returns
```

### Reverb in Mastering

**Subtle Enhancement:**
```
Applications:
- Gluing mix together
- Adding cohesive ambience
- Filling empty frequencies

Settings:
- Very short decay (0.2-0.5s)
- Low mix (5-15%)
- Wide stereo field
- Heavily filtered (HPF + LPF)

Caution:
- Can reduce impact
- Check mono compatibility
- Easy to overdo
```

### Delay Timing Calculations

**BPM to Milliseconds:**
```
Formula: (60,000 / BPM) = Quarter note duration (ms)

Examples at 120 BPM:
- Whole note: 2000ms
- Half note: 1000ms
- Quarter note: 500ms
- Eighth note: 250ms
- Sixteenth note: 125ms
- Dotted quarter: 750ms
- Dotted eighth: 375ms
- Triplet eighth: 166.67ms

Quick Reference:
60 BPM → 1000ms quarter note
90 BPM → 666.67ms
100 BPM → 600ms
120 BPM → 500ms
140 BPM → 428.57ms
160 BPM → 375ms
180 BPM → 333.33ms
```

### Automation Best Practices

**What to Automate:**
```
Send Levels:
- Most common
- Change reverb amount dynamically
- Build excitement in chorus

Reverb Parameters:
- Decay time (expansion/contraction)
- Pre-delay (distance shifts)
- Mix level (subtle to obvious)

Delay Parameters:
- Feedback (buildup effects)
- Filter frequency (tone evolution)
- Time (special effects - use carefully)
```

**Automation Tips:**
```
1. Write Smooth Curves:
   - Avoid abrupt changes (unless intentional)
   - Use appropriate curve types
   - Listen for audible jumps

2. Automate Returns, Not Sends:
   - Control overall effect level
   - Affects all sources equally
   - Useful for mix sections

3. Snapshot Important Settings:
   - Document automation moves
   - Create presets for recalls
   - Note parameters automated
```

### Quality Control Checklist

**Before Finalizing Spatial Effects:**
```
☐ Check mono compatibility
☐ Verify no excessive low-frequency reverb
☐ Confirm delays are tempo-synced (if intended)
☐ Test reverb decay times against tempo
☐ Check for masking of lead elements
☐ Verify appropriate pre-delays
☐ Confirm spatial depth hierarchy is clear
☐ Test on multiple playback systems
☐ Check for phase issues
☐ Verify no feedback oscillations
☐ Confirm appropriate damping/filtering
☐ Check CPU usage is manageable
```

---

## Conclusion

Spatial effects are fundamental tools for creating professional, three-dimensional mixes. Key takeaways:

**Reverb Fundamentals:**
- Choose appropriate algorithm for source and genre
- Use pre-delay for clarity and depth control
- Match decay time to tempo and arrangement density
- Apply frequency-dependent processing (filtering/damping)
- Employ multiple reverbs for clear depth layering

**Delay Techniques:**
- Tempo-sync for musical coherence
- Filter repeats to prevent clutter
- Use slapback for presence without long tails
- Employ ping-pong for width and movement
- Consider ducked delay for clarity in dense mixes

**Creating Depth:**
- Establish front-to-back hierarchy
- Use send/return routing for flexibility
- Employ pre-delay as distance control
- Balance direct-to-reverberant ratios
- Layer multiple spatial treatments strategically

**Advanced Techniques:**
- Side-chain processing for clarity
- Parallel spatial chains for heavy effects without mud
- Automate spatial parameters for dynamics
- Chain effects creatively (reverb→delay, delay→reverb)
- Use modulation to smooth artificial artifacts

**Problem Solving:**
- High-pass filter reverb returns (200-400Hz)
- Keep decay times appropriate to tempo
- Use pre-delay to prevent masking
- Filter delay repeats to reduce clutter
- Check mono compatibility regularly

**Best Practices:**
- Use aux sends for shared reverbs (CPU efficiency)
- Match reverb character to source and genre
- Automate spatial effects for dynamic interest
- Test in mono and on various playback systems
- Less is often more - maintain clarity

Mastery of spatial effects requires both technical knowledge and musical sensitivity. Understanding the physics and psychoacoustics helps make informed decisions, while artistic judgment determines what serves the song. Practice applying these principles across various genres and production styles to develop your spatial processing expertise.

---

*End of Spatial Effects Reference*
