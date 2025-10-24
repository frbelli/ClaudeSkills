# Sound Archetypes Database

Complete reference for common sound types in electronic music production. This database defines characteristics, synthesis approaches, and parameter recommendations for each sound archetype.

---

## BASS SOUNDS

### Sub Bass

**Characteristics**:
- Pure low frequency (20-60Hz)
- Minimal harmonics
- Felt more than heard
- Foundation of the track

**Frequency Range**: 20-60Hz (fundamental)

**Synthesis Approach**:
- Single sine or triangle wave oscillator
- No or minimal filtering
- No or very subtle modulation
- Pure, clean tone

**Key Parameters**:
- **Oscillator**: Sine or triangle wave
- **Pitch**: Usually C1-C2 (MIDI 36-48)
- **Filter**: None or LP with very high cutoff
- **Envelope**: Medium attack (20-50ms), long sustain, medium release
- **Effects**: Light saturation, no reverb
- **Mono**: Always mono for maximum power

**Best Synths**: Any synth with sine/triangle waves
**Genre Use**: All electronic genres, hip-hop, trap

**Tips**:
- Keep it simple - complexity is the enemy
- Check on multiple speakers/headphones
- Use spectrum analyzer to ensure clean low end
- Avoid doubling in octaves (causes phase issues)

---

### Reese Bass

**Characteristics**:
- Rich, growling, wide
- Detuned oscillators creating movement
- Evolving timbre
- Fills the low-mid spectrum

**Frequency Range**: 40-250Hz (fundamental + harmonics)

**Synthesis Approach**:
- 2-3 detuned saw waves
- Heavy unison (7-16 voices)
- Lowpass filter with moderate resonance
- Slight filter modulation

**Key Parameters**:
- **Oscillators**: 2-3 saw waves, detune 5-15 cents
- **Unison**: 7-16 voices, stereo spread 30-50%
- **Filter**: LP 24dB, cutoff 30-50%, resonance 20-40%
- **Filter Envelope**: Medium attack, medium decay, medium sustain
- **LFO → Filter**: Slow rate (1/4 - 1/8), subtle depth
- **Envelope**: Fast attack (5-10ms), medium decay, full sustain

**Best Synths**: Serum, Vital, Massive X, any wavetable synth
**Genre Use**: DnB, dubstep, neurofunk, liquid

**Tips**:
- Detune is key - too much = out of tune, too little = thin
- Use spectrum analyzer to check harmonic spread
- Automation on detune amount creates movement
- Pair with sub bass for complete low end

---

### Acid Bass (303-Style)

**Characteristics**:
- Squelchy, resonant
- Filter sweeps creating melody
- Plucky attack
- Iconic character

**Frequency Range**: 60-400Hz

**Synthesis Approach**:
- Single saw wave oscillator
- Lowpass filter with HIGH resonance (70-90%)
- Fast envelope → filter cutoff
- Accent on key notes

**Key Parameters**:
- **Oscillator**: Saw wave
- **Filter**: LP 24dB (ladder filter best), resonance 70-90%
- **Filter Envelope**: Fast attack (0-5ms), fast decay (50-200ms), zero sustain
- **Envelope Depth → Filter**: Maximum (100%)
- **VCA Envelope**: Fast attack, short decay, zero sustain, short release
- **Accent**: Increases envelope amount on specific notes
- **Slide**: Portamento/glide between notes

**Best Synths**: Crave (TB-303 clone), Serum, Vital, Diva
**Genre Use**: Acid house, acid techno, psytrance

**Tips**:
- Resonance is everything - push it high
- Zero sustain on both envelopes
- Use sequencer accents for groove
- Slight distortion/overdrive adds character
- Experiment with filter cutoff position

---

### Growl Bass (Dubstep/Bass Music)

**Characteristics**:
- Aggressive, modulated
- Complex harmonic movement
- Rhythmic modulation
- "Talking" quality

**Frequency Range**: 60-500Hz

**Synthesis Approach**:
- FM, wavetable, or resampled oscillators
- Multiple LFOs modulating various parameters
- Formant filtering or vowel filters
- Heavy distortion/saturation

**Key Parameters**:
- **Oscillators**: Wavetable or FM (complex waveforms)
- **Modulation**: Multiple LFOs (1/16 - 1/4 rate)
- **LFO Targets**: Filter cutoff, wavetable position, FM amount
- **Filter**: Formant, bandpass, or comb filter
- **Distortion**: Heavy (soft clip or multiband)
- **Unison**: 5-9 voices for thickness

**Best Synths**: Serum, Vital, Massive X, FM8
**Genre Use**: Dubstep, brostep, riddim, bass music

**Tips**:
- Layer multiple modulation sources
- Use different LFO rates for complexity
- Resample and manipulate the result
- Automate parameters for variation
- Less is NOT more - push it extreme

---

### Rolling Bass (DnB Style)

**Characteristics**:
- Rhythmic, bouncing
- Filter movement in rhythm
- Mid-range punch
- Drives the groove

**Frequency Range**: 80-400Hz

**Synthesis Approach**:
- Saw or square waves
- Rhythmic filter modulation (LFO or sequencer)
- Moderate distortion
- Sidechained to kick

**Key Parameters**:
- **Oscillators**: Saw + square, slight detune
- **Filter**: LP or BP, moderate resonance
- **LFO → Filter**: Synced to tempo (1/16, 1/8), high depth
- **Envelope**: Medium attack (10-20ms), short decay, medium sustain
- **Distortion**: Moderate (for grit)
- **Sidechain**: Ducking with kick

**Best Synths**: Any synth with tempo-synced LFO
**Genre Use**: Drum & Bass, jungle, neurofunk

**Tips**:
- Sync LFO to song tempo
- Try different LFO waveforms (saw, square)
- Layer with sub bass
- Sidechain compression is essential
- Use swing/groove quantization

---

## LEAD SOUNDS

### Synth Lead (Classic)

**Characteristics**:
- Bright, cutting through mix
- Sustained or plucky
- Melodic focus
- Clear harmonic content

**Frequency Range**: 200-4000Hz

**Synthesis Approach**:
- Saw waves with unison
- Highpass filtering to remove low end
- Moderate filter envelope modulation
- Chorus or unison for width

**Key Parameters**:
- **Oscillators**: 1-2 saw waves, detune 5-10 cents
- **Unison**: 3-7 voices
- **Filter**: LP 12-24dB, cutoff 50-70%, low resonance
- **Filter Envelope**: Medium attack, medium decay, high sustain
- **LFO → Pitch**: Vibrato (slow rate, subtle depth)
- **Effects**: Chorus, stereo widening

**Best Synths**: Any analog or virtual analog synth
**Genre Use**: Synthwave, EDM, pop, house

**Tips**:
- Remove low frequencies (HP filter at 200Hz)
- Unison for width, not too much detune
- Add subtle vibrato for expression
- Layer octaves for thickness

---

### Pluck/Key Sound

**Characteristics**:
- Fast attack, fast decay
- Percussive quality
- Harmonic and musical
- Often used for melodies

**Frequency Range**: 200-3000Hz

**Synthesis Approach**:
- Bright oscillators (saw, square, FM)
- Fast filter envelope with decay
- Zero sustain
- Reverb and delay for space

**Key Parameters**:
- **Oscillators**: Saw, square, or FM operators
- **Filter**: LP with moderate cutoff
- **Filter Envelope**: Fast attack (0-5ms), fast decay (100-400ms), zero sustain
- **Amp Envelope**: Fast attack (0-5ms), medium decay (200-600ms), zero sustain
- **Effects**: Short reverb, ping-pong delay

**Best Synths**: Any synth, FM synths excel here
**Genre Use**: All genres, especially house, trance, pop

**Tips**:
- Zero sustain on both envelopes
- Longer decay times = more musical
- Shorter decay times = more percussive
- Reverb and delay add space
- Layer multiple octaves for richness

---

### Supersaw Lead

**Characteristics**:
- Massive, epic, wide
- Wall of sound
- Bright and uplifting
- Fills entire stereo field

**Frequency Range**: 150-8000Hz

**Synthesis Approach**:
- Multiple detuned saw waves (7-16 voices)
- Wide stereo spread
- Highpass filter to remove mud
- Heavy unison

**Key Parameters**:
- **Oscillators**: Multiple saw waves (7-16 voices)
- **Detune**: 10-20 cents
- **Stereo Spread**: 60-100%
- **Filter**: HP at 150-200Hz + LP at 8-10kHz
- **Unison**: Maximum voices available
- **Effects**: Chorus, reverb, stereo widening

**Best Synths**: Serum, Vital, Diva (JP-8000 model), Sylenth1
**Genre Use**: Trance, big room house, progressive house

**Tips**:
- More voices = bigger sound
- Remove low end with HP filter
- Tame harshness with LP filter
- Layer with pad for fullness
- Use sparingly (very dense sound)

---

### Arpeggio Lead

**Characteristics**:
- Sequenced, rhythmic
- Melodic pattern
- Drives energy
- Repetitive but evolving

**Frequency Range**: 300-4000Hz

**Synthesis Approach**:
- Plucky sound + arpeggiator
- Filter modulation for movement
- Synchronized to tempo
- Various arpeggio patterns

**Key Parameters**:
- **Oscillators**: Saw or square waves
- **Filter**: LP with moderate cutoff and resonance
- **Envelope**: Fast attack, medium decay, low sustain
- **Arpeggiator**: Various patterns (up, down, random)
- **LFO → Filter**: Synced to tempo
- **Gate**: Optional (creates rhythm)

**Best Synths**: Any synth with built-in arpeggiator
**Genre Use**: Synthwave, techno, trance, house

**Tips**:
- Sync arpeggiator to song tempo
- Experiment with patterns and ranges
- Automate filter cutoff over time
- Layer multiple arpeggios in different octaves
- Use sidechain for groove

---

## PAD SOUNDS

### Ambient Pad

**Characteristics**:
- Soft, warm, evolving
- Slow attack and release
- Fills space without dominating
- Atmospheric

**Frequency Range**: 100-6000Hz (wide spectrum)

**Synthesis Approach**:
- Multiple oscillators (saw, triangle, or wavetables)
- Slow filter modulation
- Long attack and release envelopes
- Heavy reverb and delay

**Key Parameters**:
- **Oscillators**: 2-3 oscillators, different waveforms, slight detune
- **Filter**: LP with open cutoff (60-80%), low resonance
- **Filter Envelope**: Very slow attack (1-3s), long decay, high sustain
- **Amp Envelope**: Very slow attack (1-3s), long release (3-5s)
- **LFO → Filter/Pitch**: Very slow rate (0.1-0.5Hz), subtle depth
- **Effects**: Large reverb (3-5s), long delay

**Best Synths**: Any polyphonic synth, especially analog modeling
**Genre Use**: Ambient, chillout, cinematic, atmospheric

**Tips**:
- Layer multiple pads with different timbres
- Slow modulation creates movement
- Use lots of reverb
- Remove harsh frequencies (EQ notch 2-4kHz)
- Automate filter cutoff slowly over time

---

### String Pad

**Characteristics**:
- Rich, orchestral
- Warm and lush
- Fills harmonic space
- Sustained and flowing

**Frequency Range**: 150-5000Hz

**Synthesis Approach**:
- Saw waves with chorus
- Slow attack
- Moderate filtering
- Stereo spread

**Key Parameters**:
- **Oscillators**: 2 saw waves, slight detune (3-7 cents)
- **Filter**: LP 12dB, cutoff 60-70%
- **Envelope**: Slow attack (200-500ms), long release (1-2s)
- **Chorus**: Moderate depth and rate
- **Unison**: 3-5 voices
- **Effects**: Room reverb, subtle delay

**Best Synths**: Diva, analog modeling synths
**Genre Use**: All genres for background harmony

**Tips**:
- Chorus is essential for authentic string sound
- Slow attack prevents abrupt entries
- EQ to fit with other instruments
- Layer with real strings for realism
- Use expression/mod wheel for dynamics

---

### Drone Pad

**Characteristics**:
- Static, unchanging
- Sustained indefinitely
- Creates tension or atmosphere
- Minimal movement

**Frequency Range**: 50-2000Hz

**Synthesis Approach**:
- Simple waveforms (sine, triangle)
- No or minimal modulation
- Very long or infinite sustain
- Reverb for space

**Key Parameters**:
- **Oscillators**: 1-2 simple waveforms (sine, triangle)
- **Filter**: Wide open or none
- **Envelope**: No attack, infinite sustain, long release
- **Modulation**: Minimal or none
- **Effects**: Large reverb, subtle chorus

**Best Synths**: Any synth, modular synths excel
**Genre Use**: Ambient, drone, dark ambient, experimental

**Tips**:
- Less is more
- Use very subtle modulation if any
- Layer multiple drones in different registers
- Automate volume for breathing effect
- Perfect for background atmosphere

---

### Evolving Pad

**Characteristics**:
- Constantly changing
- Complex modulation
- Never static
- Creates interest over time

**Frequency Range**: 100-8000Hz (wide)

**Synthesis Approach**:
- Wavetable or multiple oscillators
- Multiple LFOs at different rates
- Slow filter modulation
- Parameter automation

**Key Parameters**:
- **Oscillators**: Wavetable or multiple oscillators
- **LFO 1 → Wavetable Position**: Slow rate (0.1-0.3Hz)
- **LFO 2 → Filter Cutoff**: Different rate (0.15-0.4Hz)
- **LFO 3 → Pitch/Detune**: Very slow (0.05-0.1Hz)
- **Envelope**: Slow attack, long release
- **Effects**: Reverb, modulated delay

**Best Synths**: Serum, Vital, Massive X, Pigments
**Genre Use**: Ambient, cinematic, progressive electronic

**Tips**:
- Use different LFO rates for complexity
- Automate parameters over long time spans
- Layer multiple evolving pads
- Use random/sample-and-hold LFOs
- Record long takes and edit sections

---

## KEYS & MALLETS

### Electric Piano

**Characteristics**:
- Bell-like attack
- Warm sustain
- Velocity sensitive
- Natural decay

**Frequency Range**: 100-5000Hz

**Synthesis Approach**:
- FM synthesis (best for EP sounds)
- Bell-like operators
- Velocity → amplitude/brightness
- Subtle chorus or tremolo

**Key Parameters**:
- **Oscillators**: FM operators (sine waves)
- **FM Algorithm**: Bell-like (2-3 operators)
- **Envelope**: Fast attack, medium decay, medium sustain, long release
- **Filter**: Optional LP for tone shaping
- **Velocity**: Modulates amplitude and brightness
- **Effects**: Chorus, tremolo, room reverb

**Best Synths**: Digitone II (FM), FM8, DX7 emulations
**Genre Use**: Jazz, soul, R&B, lo-fi hip-hop

**Tips**:
- Velocity sensitivity is crucial
- Slight detuning adds warmth
- Chorus creates classic EP sound
- Layer with strings for fullness
- Use compression for consistency

---

### Bells/Chimes

**Characteristics**:
- Bright, metallic attack
- Long sustain with decay
- Harmonic complexity
- Shimmer and sparkle

**Frequency Range**: 500-12000Hz

**Synthesis Approach**:
- FM synthesis (inharmonic ratios)
- Fast attack, long decay
- High frequencies
- Reverb for space

**Key Parameters**:
- **Oscillators**: FM operators with inharmonic ratios
- **FM Amount**: High for metallic quality
- **Envelope**: Instant attack, very long decay (3-10s), zero sustain
- **Filter**: HP to remove mud
- **Effects**: Long reverb (5-10s), subtle delay

**Best Synths**: Digitone II, FM8, Operator (Ableton)
**Genre Use**: Ambient, cinematic, meditation, orchestral

**Tips**:
- Use inharmonic ratios (1.3, 2.7, 4.1, etc.)
- Very long decay times
- High-frequency content is essential
- Reverb creates shimmer
- Layer multiple bells at different pitches

---

### Marimba/Xylophone

**Characteristics**:
- Woody, percussive
- Clear pitch
- Fast attack, medium decay
- Natural resonance

**Frequency Range**: 200-4000Hz

**Synthesis Approach**:
- Filtered noise + tonal oscillator
- Fast attack, medium decay
- Bandpass or formant filter
- Physical modeling if available

**Key Parameters**:
- **Oscillator 1**: Sine or triangle (tonal)
- **Oscillator 2**: Filtered noise (attack)
- **Filter**: BP or formant filter
- **Envelope**: Instant attack, medium decay (300-800ms), zero sustain
- **Mix**: Balance between tone and noise
- **Effects**: Short room reverb

**Best Synths**: Physical modeling synths, Pigments, Modal synthesis
**Genre Use**: World music, orchestral, experimental

**Tips**:
- Noise in attack creates "mallet hit"
- Tune filter to fundamental frequency
- Velocity affects noise level
- Layer different timbres
- Use variations in velocity for realism

---

## TEXTURE & ATMOSPHERE

### Granular Texture

**Characteristics**:
- Complex, evolving
- Microscopic grains of sound
- Unpredictable movement
- Abstract quality

**Frequency Range**: Full spectrum (20-20000Hz)

**Synthesis Approach**:
- Granular synthesis engine
- Sample playback in tiny grains
- Random or sequential grain playback
- Heavy processing

**Key Parameters**:
- **Grain Size**: 20-200ms
- **Grain Density**: Number of simultaneous grains
- **Playback Position**: Modulated or random
- **Pitch**: Can be shifted per grain
- **Effects**: Reverb, delay, filtering

**Best Synths**: Pigments, Granulator (Ableton), Quanta
**Genre Use**: Ambient, experimental, IDM, sound design

**Tips**:
- Smaller grains = more abstract
- Modulate playback position
- Use field recordings as source
- Layer with traditional instruments
- Automate grain parameters

---

### Noise Sweep

**Characteristics**:
- Filtered white/pink noise
- Build-up or transition effect
- Creates energy and anticipation
- Sweeping frequency content

**Frequency Range**: Variable (sweeps across spectrum)

**Synthesis Approach**:
- White or pink noise generator
- Automated filter sweep
- Rising or falling
- Volume automation

**Key Parameters**:
- **Noise**: White (bright) or pink (darker)
- **Filter**: HP or LP
- **Automation**: Sweep cutoff frequency over time
- **Envelope**: Rising volume (for build-ups)
- **Resonance**: Add emphasis to sweep
- **Effects**: Reverb, distortion

**Best Synths**: Any synth with noise generator
**Genre Use**: All electronic genres (transitions, build-ups)

**Tips**:
- Automate filter cutoff from low to high (build-up)
- Or high to low (drop/release)
- Add resonance for emphasis
- Layer with kick/snare rolls
- Use sidechain for rhythmic pumping

---

### Atmospheric Wash

**Characteristics**:
- Ambient, spacious
- Fills background
- Non-intrusive
- Creates mood and depth

**Frequency Range**: 100-10000Hz (wide)

**Synthesis Approach**:
- Reverb on long sustained tones
- Heavy processing
- Slow modulation
- Layered textures

**Key Parameters**:
- **Oscillators**: Simple waveforms or field recordings
- **Reverb**: 100% wet, very long decay (10-20s)
- **Filter**: Optional LP to darken
- **Modulation**: Very slow LFOs
- **Volume**: Background level
- **Effects**: Chorus, delay, granular

**Best Synths**: Any synth + heavy reverb
**Genre Use**: Ambient, cinematic, meditation, background

**Tips**:
- Start with simple source (sine wave, chord)
- Process heavily with reverb
- Automate slowly over long periods
- Layer multiple washes
- Use EQ to carve space for other elements

---

## PERCUSSION (SYNTHESIZED)

### Synthesized Kick

**Characteristics**:
- Punchy transient
- Low frequency body
- Clean or distorted
- Defines rhythm

**Frequency Range**: 30-150Hz (fundamental + harmonics)

**Synthesis Approach**:
- Sine wave with pitch envelope
- Transient layer (click/punch)
- Fast decay
- Optional distortion

**Key Parameters**:
- **Oscillator**: Sine wave tuned to 40-60Hz
- **Pitch Envelope**: Fast decay (30-100ms), drops from high pitch
- **Amp Envelope**: Instant attack, fast decay (100-300ms), zero sustain
- **Transient**: Short noise burst or high-frequency oscillator
- **Distortion**: Optional (soft clip or saturation)

**Best Synths**: DFAM, Digitone II, any synth with pitch envelope
**Genre Use**: All electronic genres

**Tips**:
- Pitch envelope creates body
- Transient creates punch
- Distortion adds harmonics
- Sidechain other elements to kick
- Layer multiple kicks for thickness

---

### Synthesized Snare

**Characteristics**:
- Tonal body + noise
- Short, snappy
- Defines backbeat
- Bright and cutting

**Frequency Range**: 150-8000Hz

**Synthesis Approach**:
- Tonal oscillator (body)
- Filtered noise (snare buzz)
- Fast decay
- Optional pitch envelope

**Key Parameters**:
- **Oscillator**: Triangle or saw, tuned 150-250Hz
- **Noise**: White noise, HP filtered at 1-2kHz
- **Envelope**: Instant attack, fast decay (100-200ms), zero sustain
- **Mix**: Balance tone and noise (50/50 to 30/70)
- **Pitch Envelope**: Optional slight drop
- **Effects**: Short reverb, compression

**Best Synths**: DFAM, Digitone II, modular synths
**Genre Use**: All electronic genres

**Tips**:
- Noise creates "snare" character
- Tune tonal body to song key
- Fast decay is essential
- Layer acoustic snare samples
- Compress for punch

---

### Synthesized Hi-Hat

**Characteristics**:
- High-frequency noise
- Short or sustained
- Creates groove
- Rhythmic element

**Frequency Range**: 5000-16000Hz

**Synthesis Approach**:
- Filtered white noise
- BP or HP filter
- Very fast decay (closed) or longer (open)
- Optional metallic oscillators

**Key Parameters**:
- **Noise**: White noise
- **Filter**: BP 8-12kHz or HP 6kHz+
- **Envelope**: Instant attack, very fast decay (20-50ms closed, 200-500ms open)
- **Resonance**: Add metallic quality
- **Optional**: Add square wave oscillators at high frequency
- **Effects**: None or subtle reverb

**Best Synths**: DFAM, any synth with noise generator
**Genre Use**: All electronic genres

**Tips**:
- Closed = short decay, Open = longer decay
- Filter resonance adds character
- Velocity variations create groove
- Layer multiple hi-hats
- Use for rhythmic patterns (1/8, 1/16 notes)

---

## SOUND DESIGN BY GENRE

### Techno
**Priority Sounds**:
- Kick (sub-heavy, punchy)
- Rolling bass (rhythmic)
- Hi-hats (varied)
- Minimal pads (dark)
- Percussion (industrial)

### Ambient
**Priority Sounds**:
- Evolving pads (multiple layers)
- Drones (tonal center)
- Granular textures
- Atmospheric washes
- Field recordings processed

### Dubstep
**Priority Sounds**:
- Growl bass (aggressive)
- Sub bass (clean)
- Wobble bass (rhythmic LFO)
- Drums (punchy, compressed)
- Leads (bright, cutting)

### House
**Priority Sounds**:
- Kick (punchy, 909-style)
- Bass (rolling, filtered)
- Synth stabs (plucky)
- Pads (warm chords)
- Hi-hats (groovy)

### Synthwave
**Priority Sounds**:
- Supersaw lead (epic)
- Analog bass (warm)
- Synth lead (bright)
- Pads (lush strings)
- Gated reverb drums

---

## QUICK REFERENCE: SYNTHESIS TECHNIQUES BY SOUND TYPE

| Sound Type | Primary Synthesis | Filter Type | Modulation Focus |
|------------|------------------|-------------|------------------|
| Sub Bass | Subtractive (sine) | None/LP high cutoff | Minimal |
| Reese Bass | Subtractive (saws) | LP 24dB | Detune, filter |
| Acid Bass | Subtractive (saw) | LP high res | Filter envelope |
| Synth Lead | Subtractive | LP/BP | Unison, chorus |
| Pluck | Subtractive/FM | LP fast decay | Envelope |
| Ambient Pad | Subtractive/Wavetable | LP slow mod | Multiple LFOs |
| Bells | FM (inharmonic) | HP | Long decay |
| Granular | Granular synthesis | Various | Grain parameters |
| Kick | Pitch envelope | None | Pitch envelope |
| Hi-Hat | Noise + filter | BP/HP | Fast envelope |

---

**End of Sound Archetypes Database**
