# Stereo Imaging Reference

## Overview
Comprehensive guide to stereo imaging, width control, panning techniques, and spatial placement in mixing and mastering. This reference covers mid-side processing, stereo enhancement, mono compatibility, and advanced spatial techniques.

---

## Table of Contents
1. [Stereo Fundamentals](#stereo-fundamentals)
2. [Panning Techniques](#panning-techniques)
3. [Mid-Side Processing](#mid-side-processing)
4. [Stereo Width Control](#stereo-width-control)
5. [Mono Compatibility](#mono-compatibility)
6. [Advanced Stereo Techniques](#advanced-stereo-techniques)
7. [Genre-Specific Approaches](#genre-specific-approaches)
8. [Common Problems & Solutions](#common-problems--solutions)

---

## Stereo Fundamentals

### Understanding Stereo Audio

**Stereo Basics:**
- Two-channel audio (Left + Right)
- Creates illusion of width and space
- Provides spatial information
- More immersive than mono
- Standard since 1960s

**Stereo Field:**
```
Left ←---------------Center---------------→ Right
 100%      50%         0%        50%       100%
 
Terminology:
- Center: Both channels equal
- Hard Left: 100% left, 0% right
- Hard Right: 0% left, 100% right
- Phantom Center: Equal in both speakers
```

**Why Stereo Matters:**
- Separation of elements
- Width and depth perception
- More engaging listening
- Professional standard
- Creative possibilities

### Mid-Side Explained

**Mid-Side Concept:**
```
Traditional Stereo (L/R):
- Left channel
- Right channel

Mid-Side (M/S):
- Mid: L + R (center/mono content)
- Side: L - R (stereo/width content)

Conversion:
L/R → M/S:
- Mid = (L + R) / 2
- Side = (L - R) / 2

M/S → L/R:
- Left = Mid + Side
- Right = Mid - Side
```

**Why Use Mid-Side:**
- Independent control of center vs width
- Surgical stereo adjustments
- Better mono compatibility
- Professional mastering tool
- Creative stereo enhancement

**Mid Channel Contains:**
- Lead vocals
- Kick drum
- Bass
- Snare (mostly)
- Center-panned elements

**Side Channels Contain:**
- Panned instruments
- Stereo width
- Ambience and reverb
- Doubled elements
- Spatial information

### Phase Relationships

**Phase Basics:**
```
In-Phase:
- Waveforms aligned
- Additive (louder in mono)
- Solid, powerful
- Stable image

Out-of-Phase:
- Waveforms inverted
- Cancellation (quieter in mono)
- Weak, unstable
- Can disappear in mono
```

**Phase Issues:**
```
Symptoms:
- Thin sound in mono
- Weak low-end
- Unstable stereo image
- Elements disappear when mono

Causes:
- Microphone placement
- Stereo effects
- Phase-altering processors
- Incorrect stereo widening
- Polarity reversal

Solutions:
- Check in mono constantly
- Use correlation meter
- Fix at source when possible
- Careful with stereo widening
- Use linear-phase EQ when critical
```

**Correlation Meter:**
```
Reading:
+1.0 = Perfect mono (fully correlated)
 0.0 = Full stereo (uncorrelated)
-1.0 = Inverted phase (anti-correlated)

Target Range:
+0.5 to +1.0 = Safe, solid
 0.0 to +0.5 = Good stereo, check mono
-0.5 to  0.0 = Caution, check mono carefully
Below -0.5 = Problem, likely phase issues

Ideal Mix:
+0.3 to +0.7 = Good balance
```

### Stereo vs Mono Sources

**Mono Sources:**
- Single microphone recording
- Synth mono output
- Samples (often mono)
- DI bass/guitar
- Can be panned anywhere

**Advantages:**
- Phase coherent
- Solid low-end
- Easy to place
- Mono compatible
- Predictable

**Stereo Sources:**
- Two microphones (XY, AB, etc.)
- Stereo synth patches
- Recorded ambience
- Piano (two mics)
- Drum overheads

**Advantages:**
- Width and space
- More immersive
- Natural ambience
- Depth information

**Considerations:**
- Check mono compatibility
- Watch for phase issues
- Be careful with processing
- Consider mid-side balance

---

## Panning Techniques

### Basic Panning Strategies

**Pan Law:**
```
Center Attenuation:
-3 dB: Most common (ITU standard)
-4.5 dB: Pro Tools default
-6 dB: Mathematical equal power

Why It Matters:
- Center-panned sounds may seem louder
- Pan law compensates
- Maintains consistent perceived level
- Check your DAW settings
```

**Panning Positions:**
```
Center (C):
- Lead vocal
- Kick
- Bass
- Snare
- Most important elements

Near-Center (20-30%):
- Lead doubles
- Secondary vocals
- Guitars (rhythm)
- Supporting elements

Mid-Pan (40-60%):
- Guitars
- Keys
- Percussion
- Fills and effects

Wide-Pan (70-90%):
- Doubled guitars
- Wide synths
- Percussion
- Stereo effects

Hard-Pan (100%):
- Overheads
- Room mics
- Special effects
- Ear candy
```

### Frequency-Based Panning

**Low Frequency Guidelines:**
```
Keep Centered (Below 150 Hz):
- Kick drum
- Bass (all types)
- Sub frequencies
- Low synths

Reason:
- Mono = more powerful
- Phase coherent
- Better translation
- More focused energy
- Subwoofers are often mono
```

**Mid-High Frequency Panning:**
```
More Freedom (Above 150 Hz):
- Can pan wider
- Less phase-sensitive
- Creates width
- Better separation

Strategy:
- Keep fundamental centered
- Pan harmonics wider
- Use mid-side to control
```

### LCR Panning (Hard Panning)

**Concept:**
- Only Left, Center, Right
- No in-between positions
- Cleaner separation
- Vintage approach
- Modern revival

**Benefits:**
```
Clarity:
- Less phase confusion
- Clear element separation
- Decisive placement
- Strong stereo image

Power:
- More impact per element
- Less masking
- Defined positions
```

**Typical LCR Setup:**
```
Center:
- Lead vocal
- Kick
- Bass
- Snare

Hard Left:
- Rhythm guitar 1
- Tom 1
- Hi-hat (if not center)
- Percussion 1

Hard Right:
- Rhythm guitar 2
- Tom 2
- Cymbals
- Percussion 2

Result:
- Wide, powerful mix
- Clear separation
- Strong image
- Vintage character
```

### Complementary Panning

**Concept:**
- Balance left and right
- Maintain stereo equilibrium
- Avoid lopsided mix
- Professional standard

**Strategies:**

**Mirrored Elements:**
```
Guitar Example:
- Guitar 1: Panned 70% left
- Guitar 2: Panned 70% right
- Balanced weight
- Wide stereo image

Percussion Example:
- Shaker: 80% left
- Tambourine: 80% right
- Symmetrical feel
```

**Frequency Balance:**
```
Balance by Frequency Content:
- Bright element left? → Bright element right
- Dark element left? → Dark element right
- Maintains tonal balance
- Prevents frequency bias

Example:
- Hi-hat left (bright)
- Ride cymbal right (bright)
- Balanced high-end
```

**Dynamic Balance:**
```
Balance by Level:
- Loud element left? → Loud element right
- Or: Quiet element left, loud right
- Then: Loud left, quiet right next section

Creates:
- Movement
- Interest
- Balance over time
```

### Stereo Panning Techniques

**Width Adjustment:**
```
Narrowing Stereo Source:
- Reduce L/R difference
- Closer to mono
- More focused
- Better mono compatibility

Widening Stereo Source:
- Increase L/R difference
- More spacious
- Immersive
- Check mono!

Tools:
- Stereo width plugin
- Mid-side adjustment
- Manually adjust L/R levels
```

**Haas Effect Panning:**
```
Concept:
- Delay one side 5-30 ms
- Creates width and positioning
- Based on precedence effect
- Powerful but risky

Settings:
- Delay: 10-25 ms typical
- Can pan delayed signal
- Adjust level balance
- Creates space

Caution:
- Can cause phase issues
- Check mono carefully
- Can sound weak in mono
- Use sparingly
```

---

## Mid-Side Processing

### M/S EQ

**Concept:**
- Different EQ for mid vs side
- Surgical stereo control
- Professional technique
- Essential mastering tool

**Applications:**

**Tighten Low-End:**
```
Problem: Bass spread too wide

Solution:
Mid:
- No change or slight boost 60-100 Hz
- Maintain power

Side:
- HPF at 150-200 Hz (aggressive)
- Remove low-end from sides
- Mono below 150 Hz

Result:
- Tight, focused bass
- Powerful mono low-end
- Clean stereo image
- Better translation
```

**Enhance Stereo Width:**
```
Goal: Wider mix

Mid:
- Reduce high-end slightly (2-4 kHz, -1 to -2 dB)
- Or leave unchanged

Side:
- Boost high-end (8-12 kHz, +2 to +4 dB)
- High shelf works well

Result:
- Wider perceived image
- More spacious
- Enhanced stereo field
- Still mono compatible
```

**Vocal Clarity:**
```
Problem: Vocal buried in stereo mix

Solution:
Mid:
- Boost vocal presence (3-5 kHz, +2 to +4 dB)
- Enhance center

Side:
- Cut vocal range (3-5 kHz, -2 to -3 dB)
- Reduce competition

Result:
- Vocal more prominent
- Clear center image
- Background sits back
- Professional separation
```

**Clean Up Sides:**
```
Problem: Muddy stereo field

Solution:
Mid:
- Leave natural

Side:
- Cut low-mids (200-400 Hz, -2 to -4 dB)
- Remove mud from sides
- Clean stereo image

Result:
- Clearer mix
- Focused stereo information
- Maintained mono power
```

### M/S Compression

**Concept:**
- Independent compression of mid and side
- Control center vs width dynamics
- Advanced technique
- Mastering application

**Applications:**

**Enhance Width Dynamically:**
```
Setup:
Mid:
- Light compression (2:1)
- Slow attack (30 ms)
- Maintain center dynamics
- GR: 1-2 dB

Side:
- Heavier compression (4:1)
- Medium attack (15 ms)
- Bring up quieter stereo elements
- GR: 3-4 dB

Result:
- More consistent width
- Sides brought forward
- Maintained center power
- Enhanced stereo image
```

**Control Excessive Width:**
```
Setup:
Mid:
- Very light compression (1.5:1)
- Or no compression
- Preserve center

Side:
- Moderate to heavy compression (6:1)
- Reduces extreme width
- Controls wild sides
- GR: 4-6 dB

Result:
- Controlled stereo field
- Better mono compatibility
- Focused image
- Professional sound
```

**Vocal-Focused Mix:**
```
Problem: Vocal inconsistent against stereo backing

Solution:
Mid:
- Compression for vocal (4:1)
- Control center dynamics
- GR: 3-5 dB

Side:
- Light compression (2:1)
- Preserve stereo dynamics
- GR: 1-2 dB

Result:
- Consistent vocal level
- Natural backing dynamics
- Balanced mix
```

### M/S Stereo Width

**Width Adjustment:**
```
Narrower:
- Reduce side level
- More mono content
- Focused image
- Better mono compatibility

Wider:
- Increase side level
- More stereo content
- Spacious image
- Check mono!

Technique:
Mid: 0 dB (reference)
Side: -3 to +3 dB (adjust)
  -3 dB = Narrower
  +3 dB = Wider
```

**Genre Guidelines:**
```
Narrow (Side -2 to -1 dB):
- Mono-focused genres
- Bass-heavy music
- Old school hip-hop
- Vintage styles

Balanced (Side ±0 dB):
- Most modern music
- Pop, rock
- Standard width
- Versatile

Wide (Side +1 to +3 dB):
- Electronic music
- Ambient, cinematic
- Modern pop
- Spacious productions

Caution:
- Never exceed +3 dB side boost
- Always check mono
- Can sound weak if too wide
- Reference against professional tracks
```

### M/S Saturation

**Concept:**
- Different saturation on mid vs side
- Add character to specific spatial zones
- Creative technique

**Applications:**

**Warm Center:**
```
Mid:
- Tube/tape saturation
- Adds warmth to lead elements
- Slight even harmonics

Side:
- Clean or minimal saturation
- Preserves stereo clarity

Result:
- Warm, present center
- Clear stereo field
```

**Exciting Sides:**
```
Mid:
- Clean

Side:
- Exciter/saturation
- Adds air and width
- Enhances stereo content

Result:
- Wide, exciting mix
- Focused center
- Dimensional sound
```

---

## Stereo Width Control

### Stereo Enhancement Techniques

**Chorus/Unison:**
```
Method:
- Slight pitch variation
- Stereo spread
- Creates width from mono

Settings:
- Rate: 0.2-0.5 Hz (slow)
- Depth: 5-15% (subtle)
- Mix: 20-40%

Use On:
- Synths
- Guitars
- Pads
- Backing vocals

Result:
- Wider stereo image
- Fuller sound
- Chorus character
```

**Micro-Timing:**
```
Technique:
- Delay L or R by 1-10 ms
- Creates width perception
- Haas effect

Settings:
- Delay: 5-15 ms typical
- Level: Equal or adjust
- Pan: Optional additional pan

Caution:
- Can cause mono issues
- Check phase carefully
- Use sparingly
- Not for bass/kick
```

**Double-Tracking:**
```
Natural Width:
- Record same part twice
- Pan hard left and right
- Natural variation creates width

Digital Double:
- Duplicate track
- Slight pitch/timing shift
- Pan L/R

Settings:
- Pitch: ±5-10 cents
- Timing: 5-15 ms delay
- Pan: Hard L/R or 80% L/R

Result:
- Natural, wide sound
- Full, rich tone
- Professional technique
```

**Stereo Imaging Plugins:**
```
Types:
- Pseudo-stereo from mono
- Width enhancement
- Specific algorithms

Common Plugins:
- Waves S1
- iZotope Ozone Imager
- Brainworx bx_stereomaker
- Voxengo MSED (free)

Parameters:
- Width: 0-200% typical
- Frequency-dependent width
- Mono bass option
- Correlation metering

Guidelines:
- Keep bass mono (below 150 Hz)
- Moderate width (100-130%)
- Check mono constantly
- Use preset as starting point
```

### Frequency-Dependent Width

**Concept:**
- Different width per frequency range
- Low = narrow, high = wide
- Professional standard
- Better mono compatibility

**Strategy:**
```
Low (20-150 Hz):
- 0% width (mono)
- Tight, powerful
- Phase coherent
- Essential

Low-Mid (150-500 Hz):
- 50% width (moderate)
- Some stereo
- Controlled

Mid (500 Hz - 5 kHz):
- 100% width (natural)
- Full stereo
- Standard width

High (5-20 kHz):
- 120-150% width (enhanced)
- Extra spacious
- Air and shimmer
- Check mono!
```

**Implementation:**
```
Method 1: Multiband Stereo Tool
- Split into bands
- Adjust width per band
- Professional result

Method 2: Parallel Processing
- Duplicate track
- HPF at 5 kHz
- Widen high-passed version
- Blend with original

Method 3: M/S EQ
- Filter side channel low-end
- Boost side channel high-end
- Effective and simple
```

### Stereo Delay Effects

**Ping-Pong Delay:**
```
Settings:
- Delay time: Tempo-synced
- Feedback: 30-50%
- Pan: Alternating L/R

Effect:
- Wide stereo movement
- Rhythmic interest
- Spacious

Use On:
- Vocals (throws)
- Synths
- Guitar solos
- Effects
```

**Stereo Delay Offset:**
```
Settings:
- Left: 1/4 note
- Right: Dotted 1/8 note
- Different times create width

Effect:
- Complex stereo rhythm
- Wide image
- Movement

Applications:
- Vocals
- Leads
- Atmospheric effects
```

**Haas Effect Delay:**
```
Settings:
- One side delayed 10-30 ms
- No feedback
- Creates position and width

Caution:
- Check mono
- Can be problematic
- Use carefully
```

---

## Mono Compatibility

### Why Mono Matters

**Real-World Mono Situations:**
- Smartphones (often mono)
- Bluetooth speakers (many mono)
- Club systems (summed to mono)
- TV speakers
- Podcast/radio
- Some streaming situations

**Problems with Poor Mono:**
- Weak sound
- Elements disappear
- Thin bass
- Unprofessional
- Bad translation

### Checking Mono Compatibility

**Testing Process:**
```
1. Reference in Stereo:
   - Know how it sounds full stereo
   - Note key elements

2. Switch to Mono:
   - Use DAW mono button
   - Or mono utility plugin
   - Listen critically

3. Check for Issues:
   - Volume drops?
   - Elements disappear?
   - Thin sound?
   - Phase problems?

4. Adjust and Retest:
   - Fix problems at source
   - Recheck in mono
   - Verify improvement

5. Final Stereo Check:
   - Ensure fixes didn't hurt stereo
   - Balance is key
```

**Correlation Metering:**
```
Use Plugin with Correlation Meter:
- Watches phase relationship
- Visual feedback
- Real-time monitoring

Safe Range:
+0.5 to +1.0 = Very safe
+0.3 to +0.5 = Safe, good stereo
 0.0 to +0.3 = Caution, check mono
Below 0.0 = Problem, fix immediately

Throughout Mix:
- Monitor constantly
- Watch during stereo widening
- Check individual tracks
- Verify final mix
```

### Mono Compatibility Techniques

**Keep Bass Mono:**
```
Essential Rule:
- Everything below 150 Hz mono
- Bass, kick, sub synths
- Non-negotiable

Implementation:
Method 1: M/S Processing
- Aggressive HPF on side channel
- 150-200 Hz cutoff
- Simple, effective

Method 2: Mono Plugin
- Insert on bass/kick
- Mono below 150 Hz
- Stereo above

Method 3: Manual
- Ensure bass tracks mono
- Check panning (center)
- Verify with correlation meter
```

**Fix Phase Issues:**
```
At Source:
- Better mic placement
- Check polarity (phase button)
- Fix during recording

In Mix:
- Flip polarity on one side
- Time-align tracks
- Use linear phase EQ
- Reduce stereo width

Advanced:
- Phase rotation plugins
- Corrective processing
- Surgical EQ
```

**Test Throughout Process:**
```
Regular Mono Checks:
- Every 15-20 minutes
- After adding stereo effects
- Before and after widening
- Final mix verification

Listen For:
- Overall level (should be similar to stereo)
- Bass power (should be strong)
- Lead elements (should be clear)
- No disappearing parts
- Solid, punchy sound
```

### Mixing for Both Stereo and Mono

**Balanced Approach:**
```
Strategy:
1. Mix primarily in stereo
2. Check mono every 15-20 min
3. Fix major mono issues
4. Don't sacrifice stereo for mono
5. Find balance

Goal:
- Great stereo experience
- Acceptable mono experience
- Professional standard
```

**Priority Elements:**
```
Must Work in Mono:
- Lead vocal
- Bass
- Kick
- Snare
- Main melody

Can Lose Impact in Mono:
- Wide pads
- Stereo effects
- Ear candy
- Ambience
- Room mics

Strategy:
- Critical elements: Mono-safe
- Supporting elements: Can be wider
- Effects: Can be stereo-only
```

---

## Advanced Stereo Techniques

### Stereo Ambience Creation

**Reverb Panning:**
```
Technique:
- Mono reverb send
- Stereo reverb return
- Pan reverb separately from source

Example:
- Vocal: Center
- Reverb: Wide stereo (100%)
- Creates depth and width

Advanced:
- Different reverb L/R
- Asymmetrical decay
- Creative spatial effects
```

**Stereo Room Mics:**
```
Setup:
- Wide stereo pair (AB, ORTF)
- Captures room ambience
- Blend with close mics

Mix Technique:
- Low level (subtle)
- Wide panned (70-100%)
- HPF heavily (400-600 Hz)
- Adds space and dimension

Result:
- Natural ambience
- Professional depth
- Cohesive sound
```

### Binaural and 3D Audio

**Binaural Basics:**
```
Concept:
- Head-related transfer function (HRTF)
- 3D spatial positioning
- Headphone-optimized
- Immersive experience

Applications:
- Headphone mixes
- VR/AR audio
- ASMR content
- Spatial audio

Caution:
- Only works on headphones
- Can sound strange on speakers
- Specialized tools needed
```

**Dolby Atmos / Spatial Audio:**
```
Modern Format:
- Object-based audio
- 3D positioning
- Height channels
- Future of music

Considerations:
- Requires specific tools
- Stereo downmix still important
- Growing platform support
- Professional opportunity
```

### Stereo Width Automation

**Dynamic Width:**
```
Concept:
- Automate stereo width
- Create movement and interest
- Emphasize sections

Examples:
Verse:
- Narrower (90-100%)
- Intimate feel

Chorus:
- Wider (110-130%)
- Big, expansive

Bridge:
- Very narrow (70-80%)
- Creates contrast

Post-Chorus:
- Maximum width (130-150%)
- Huge, epic feel

Tools:
- Stereo width plugin automation
- M/S side level automation
- Creative panning automation
```

**Element-Specific Automation:**
```
Synth Pad:
- Start narrow in intro
- Gradually widen to chorus
- Smooth automation curve

Guitars:
- Narrow during verse
- Wide in chorus
- Dynamic arrangement support

Effects:
- Delay width automation
- Reverb width changes
- Creative spatial movement
```

### Asymmetrical Stereo

**Concept:**
- Different content L vs R
- Not mirrored
- Creative technique
- Unique sound

**Applications:**

**Complementary Elements:**
```
Example 1:
- Left: Acoustic guitar
- Right: Electric guitar
- Different but balanced

Example 2:
- Left: Piano low notes
- Right: Piano high notes
- Frequency-split stereo

Result:
- Unique stereo field
- Interesting soundstage
- Creative approach
```

**Call and Response:**
```
Technique:
- Element plays left
- Response plays right
- Back and forth

Example:
- Guitar lick left
- Synth answer right
- Creates dialogue

Effect:
- Engaging stereo movement
- Musical conversation
- Active listening experience
```

---

## Genre-Specific Approaches

### Electronic/EDM

**Philosophy:**
- Wide, spacious mixes
- Mono bass, wide everything else
- Stereo enhancement common
- Immersive experience

**Strategy:**
```
Bass/Kick:
- Completely mono below 150 Hz
- Sub frequencies mono
- Power and focus

Leads:
- Moderate to wide (100-120%)
- Present but controlled
- Center-focused

Pads/Synths:
- Very wide (120-150%)
- Create space
- Immersive bed

FX/Ear Candy:
- Extreme width possible
- Can be mono-unfriendly
- Creative freedom

Result:
- Powerful center
- Wide, immersive sides
- Modern EDM sound
```

### Rock/Pop

**Philosophy:**
- Balanced, wide but solid
- Traditional panning
- Vocals centered
- Band arrangement

**Typical Setup:**
```
Center:
- Lead vocal
- Kick
- Bass
- Snare

Near-Center (20-40%):
- Vocal doubles
- Toms (panned between)
- Supporting elements

Wide (60-80%):
- Guitars (L/R)
- Keys
- Backing vocals

Hard-Pan (100%):
- Overheads
- Room mics (optional)
- Special effects

Result:
- Clear center
- Wide but natural stereo
- Balanced, professional
```

### Hip-Hop/Trap

**Philosophy:**
- Mono-focused low-end
- Stereo high-end and effects
- Vocal front and center
- Space for 808s

**Strategy:**
```
808/Bass:
- Completely mono
- No stereo width
- Maximum power

Kick:
- Mono
- Often minimal

Vocal:
- Center (lead)
- Wider (doubles, ad-libs)
- Stereo delay throws

Hi-Hats:
- Stereo (can be wide)
- Panned slightly or wide
- Rhythmic stereo movement

FX:
- Stereo, creative
- Ping-pong delays
- Wide reverbs

Result:
- Powerful mono low-end
- Stereo interest in mid/high
- Vocal clarity
```

### Acoustic/Jazz

**Philosophy:**
- Natural stereo image
- Realistic positioning
- Subtle width
- Organic sound

**Approach:**
```
Realistic Panning:
- Mimic live stage positions
- Instruments where they'd sit
- Natural balance

Example Stage:
Left:        Center:      Right:
Piano        Vocals       Bass
Guitar       Drums        Saxophone
Percussion   (Kit spread) Trumpet

Width:
- Natural (85-100%)
- Not enhanced
- Room mics wide
- Organic stereo

Result:
- Realistic soundstage
- Natural listening
- Intimate, organic
```

---

## Common Problems & Solutions

### Problem: Weak Mono Bass

**Cause:**
- Bass too wide
- Phase cancellation
- Stereo sub information

**Solution:**
```
1. Check Phase:
   - Listen in mono
   - Check correlation meter
   - Fix polarity if needed

2. Make Bass Mono:
   - M/S processing: Cut sides below 150 Hz
   - Or use mono plugin
   - Or ensure single-mic recording

3. Verify Improvement:
   - Check in mono
   - Should be powerful
   - Equal to stereo level

Result:
- Powerful mono bass
- Solid foundation
- Professional translation
```

### Problem: Mix Too Wide

**Symptoms:**
- Weak in mono
- Sounds thin
- Unfocused
- Correlation meter low

**Solution:**
```
1. Identify Culprit:
   - Solo tracks in mono
   - Find widened elements
   - Check correlation

2. Reduce Width:
   - Lower stereo enhancement
   - Reduce side channel (M/S)
   - Narrow width plugins

3. Focus Low-End:
   - Mono below 150 Hz everywhere
   - Check bass/kick

4. Balance:
   - Aim for +0.3 to +0.7 correlation
   - Test in mono frequently
   - Professional balance

Result:
- Better mono compatibility
- Still wide in stereo
- Professional standard
```

### Problem: Unbalanced Stereo Image

**Symptoms:**
- Lopsided left or right
- Too much one side
- Uncomfortable listening
- Unprofessional

**Solution:**
```
1. Visual Check:
   - Stereo meter/scope
   - Look for imbalance
   - Which side heavier?

2. Balance Elements:
   - Count panned elements L vs R
   - Adjust panning
   - Mirror important elements

3. Frequency Balance:
   - EQ matching L/R
   - Similar tonal balance both sides
   - Check with pink noise

4. Level Check:
   - Ensure L/R similar RMS
   - Use metering
   - Trust meters + ears

Result:
- Centered stereo image
- Balanced, professional
- Comfortable listening
```

### Problem: Vocal Buried in Stereo Mix

**Cause:**
- Too many wide elements
- Vocal fighting stereo field
- Lack of center focus

**Solution:**
```
1. M/S EQ:
   - Boost vocal range in mid (3-5 kHz)
   - Cut vocal range in side (3-5 kHz)
   - Creates space for vocal

2. Pan Adjustment:
   - Ensure vocal truly center
   - Check for stereo widening on vocal
   - Keep vocal mono or narrow

3. Reduce Competing Width:
   - Narrow instruments in vocal range
   - Create center pocket
   - Less stereo in midrange

4. Automation:
   - Duck sides when vocal present
   - Or narrow stereo width in vocal sections

Result:
- Clear, present vocal
- Wide mix maintained
- Professional separation
```

### Problem: Harsh Stereo Field

**Symptoms:**
- Fatiguing to listen
- Harsh high-end in stereo
- More comfortable in mono

**Solution:**
```
1. M/S EQ:
   - Check side channel
   - Cut harsh frequencies sides (6-8 kHz)
   - Leave mid channel natural

2. Width Reduction:
   - Narrow high-frequency width slightly
   - Still stereo but less extreme

3. Check Sources:
   - Overly bright elements?
   - Harsh cymbals/hi-hats?
   - Stereo-enhanced harshness?

4. De-Ess:
   - Can apply to side channel
   - Reduces harsh stereo sibilance

Result:
- Smooth, pleasant stereo
- Not fatiguing
- Professional quality
```

### Problem: Phase Issues from Processing

**Cause:**
- Stereo effects
- Multiple processors
- EQ phase shift
- Delay-based effects

**Solution:**
```
1. Identify Source:
   - Bypass plugins one by one
   - Find offending processor
   - Check in mono

2. Use Linear Phase:
   - Linear phase EQ
   - Especially on stereo bus
   - Prevents phase shift

3. Alternative Processing:
   - Different plugin
   - Different settings
   - Simpler approach

4. Accept Trade-off:
   - Some effects cause phase issues
   - Decide if worth it
   - Balance stereo vs mono

Prevention:
- Check mono throughout process
- Use correlation meter
- Be aware of phase-altering effects
```

---

## Best Practices Summary

### Essential Guidelines

**Mono Bass Rule:**
```
Always:
- Everything below 150 Hz mono
- Bass, kick, sub-bass
- No exceptions
- Check with correlation meter
```

**Check Mono Frequently:**
```
Every 15-20 Minutes:
- Toggle mono
- Listen critically
- Fix issues immediately
- Don't wait until end
```

**Balanced Panning:**
```
Mirror Important Elements:
- Guitar L → Guitar R
- Percussion L → Percussion R
- Vocal double L → Vocal double R
- Maintain equilibrium
```

**Width by Frequency:**
```
Low: Mono (20-150 Hz)
Low-Mid: Narrow (150-500 Hz)
Mid: Natural (500 Hz - 5 kHz)
High: Wide (5-20 kHz)

Adjust to taste but follow principle
```

### Quality Control Checklist

**Before Finalizing Stereo Image:**
```
☐ Check in mono (sounds solid?)
☐ Verify correlation meter (+0.3 to +0.7?)
☐ Bass mono below 150 Hz?
☐ No phase cancellation issues?
☐ Balanced left/right weight?
☐ Vocals clear in stereo and mono?
☐ Width appropriate for genre?
☐ No elements disappear in mono?
☐ Stereo enhancement not excessive?
☐ Compare to professional reference tracks
☐ Test on multiple systems
☐ Comfortable, not fatiguing?
```

### Professional Standards

**Target Correlation:**
```
Aim For:
+0.3 to +0.7 = Good stereo, mono-compatible

Avoid:
Below +0.2 = Too wide, mono problems
Above +0.8 = Too narrow, lacking stereo

Exceptions:
- Some electronic music wider
- Some acoustic music narrower
- Always check references
```

**Width Recommendations:**
```
Conservative (Safe):
- 100% stereo width
- Natural sound
- Mono compatible

Moderate (Modern):
- 100-120% width
- Enhanced stereo
- Check mono

Aggressive (Electronic):
- 120-150% width
- Very wide
- Mono compromised but acceptable for genre

Never:
- Exceed 150% width
- Ignore mono completely
- Widen below 150 Hz
```

---

## Conclusion

Stereo imaging is crucial for professional, engaging mixes. Key takeaways:

**Fundamental Principles:**
- Keep bass mono below 150 Hz always
- Check mono compatibility frequently
- Balance left and right elements
- Use correlation metering
- Understand mid-side processing

**Essential Techniques:**
- Mid-side EQ for surgical stereo control
- Frequency-dependent width (narrow low, wide high)
- Complementary panning for balance
- Mono bass, stereo everything else
- Regular mono checking throughout process

**Advanced Applications:**
- M/S compression for dynamic width control
- Stereo width automation for movement
- Asymmetrical panning for creativity
- Genre-specific width strategies
- Binaural and spatial audio awareness

**Problem Prevention:**
- Monitor correlation constantly
- Test in mono every 15-20 minutes
- Keep critical elements mono-compatible
- Balance stereo width with mono power
- Reference professional mixes

**Professional Standards:**
- Correlation: +0.3 to +0.7 target
- Width: Appropriate to genre
- Mono: Solid, powerful, clear
- Balance: Left/right equilibrium
- Translation: Works on all systems

Mastery of stereo imaging creates professional, immersive mixes that translate well to all playback systems. Always serve the music while maintaining technical excellence and mono compatibility.

---

*End of Stereo Imaging Reference*
