# Synthesizer Database

Complete reference for all supported hardware and software synthesizers. This database includes technical specifications, programming approaches, and sound design tips for each instrument.

---

## HARDWARE SYNTHESIZERS

### Elektron Digitone II

**📖 Complete Documentation**: See [synths/digitone-ii.md](synths/digitone-ii.md)

**Quick Reference**:
- **Type**: Digital 8-voice FM synthesizer with subtractive filtering
- **Operators**: 4 operators (Groups: C, A, B1, B2)
- **Algorithms**: 8 routing configurations with X/Y outputs
- **Voices**: 8-voice polyphony across 4 tracks
- **Filter**: Analog-modeled multimode (multiple filter machines available)
- **Sequencer**: 64-step with parameter locks, micro-timing
- **Effects**: Per-track (Chorus, Delay, Reverb, Overdrive) + Master

**Key Features**:
- Unique FM + Subtractive hybrid architecture
- Parameter locks for per-step sound design (most powerful feature)
- 8 algorithms with dual carrier outputs (X/Y crossfade)
- Bipolar HARM parameter (wavetable-like harmonic control)
- Operator envelopes: ADE (triggered) or ASDE (gated)
- Overbridge integration for DAW control

**Best For**:
- Dark techno (aggressive FM bass and leads)
- Percussive sounds (kicks, snares, bells via FM)
- Evolving pads (parameter locks + effects)
- Complex sequenced patterns
- Live performance (pattern chaining, scenes)

**Quick Start Tips**:
- **Start simple**: Algorithm 1 (series) with 2 operators
- **Use the filter**: LP 24dB to tame harsh FM
- **Parameter locks**: Evolve static sounds over time
- **Integer ratios**: 1, 2, 3, 4 for harmonic sounds
- **Decimal ratios**: 1.37, 2.51 for metallic timbres
- **Feedback**: Adds aggression and harmonics
- **MIX parameter**: Crossfade between X/Y outputs

**Common Patches**:
- **Techno Kick**: Algorithm 1, Ratio C=1.0, Fast pitch envelope, LP filter
- **Reese Bass**: Algorithm 5 (parallel), Detuning, High resonance
- **FM Lead**: Algorithm 3 or 7, Feedback ON, Ratio 3-7, BP filter
- **Pad**: Algorithm 5, Slow attacks, Chorus + Reverb
- **Bell**: Algorithm 2, Integer ratios, Fast decay

**Documentation Note**: The complete reference includes:
- Detailed algorithm diagrams (all 8 configurations)
- Operator envelope types and behaviors
- Ratio system (including B1/B2 "clock" behavior)
- Harmonics parameter deep dive
- Filter machines comparison
- Sound design strategies by genre
- All information verified from official Digitone II manual (OS 1.00A)

---

### Moog Matriarch

- **Type**: Semi-modular 4-VCO analog paraphonic synthesizer
- **Oscillators**: 4 analog VCOs (saw, triangle, square, PWM)
- **Filter**: 2x Moog ladder filters (24dB/octave, LP) with series/parallel routing
- **Voices**: Paraphonic (all oscillators share filter/VCA, but can be split)
- **Envelopes**: 2x ADSR (filter and VCA)
- **LFO**: 1 LFO with multiple waveforms (triangle, square, ramp, sample & hold)
- **Modulation**: 90 patch points for modular routing
- **Effects**: Analog delay, stereo output, built-in spring reverb tank
- **Arpeggiator/Sequencer**: 256-step sequencer/arpeggiator with ratcheting
- **Keyboard**: 49 keys with velocity and aftertouch
- **Patchbay**: 90 patch points (CV/Gate/Audio)
- **Specialties**:
  - 4 VCOs for massive unison sounds
  - Dual filters for complex timbres
  - Semi-modular for creative patching
  - Analog warmth and character
  - Built-in analog delay
  - Stereo output path

**Programming Interface**:
- Knob-per-function (immediate access)
- Patch bay requires patch cables
- Very hands-on and intuitive
- No menu diving

**Best For**:
- Massive bass (4 VCOs in unison)
- Thick leads (detuned oscillators)
- Lush pads (slow attack, long release, stereo delay)
- Drones (paraphonic voicing)
- Modular experimentation (patch bay)
- Analog warmth and character
- Live performance (immediate control)

**Programming Tips - Basic Patches**:

**Massive Bass**:
1. All 4 VCOs ON, tune to same note
2. VCO1: Saw, VCO2: Saw (detune +2 cents)
3. VCO3: Square, VCO4: Triangle (sub bass)
4. Both filters: LP mode, series routing
5. Filter 1 cutoff: 30-40%, resonance: 50%
6. Filter EG: Fast attack, medium decay, low sustain
7. VCA EG: Fast attack, short decay, full sustain
8. Patch: Filter EG → Filter 1 Cutoff (moderate amount)

**Ethereal Pad**:
1. VCO1+2: Saw waves, slight detune
2. VCO3+4: Triangle waves, octave up (+12 semitones)
3. Both filters: LP, parallel routing
4. Filter 1: Open (80%), low resonance
5. Filter 2: Mid (50%), medium resonance
6. Filter EG: Slow attack (1-2 sec), long decay, high sustain
7. VCA EG: Slow attack (1-2 sec), long release (3+ sec)
8. LFO → Filter 2 Cutoff (slow, subtle movement)
9. Delay ON, mix 30-40%, time medium

**Acid Lead**:
1. VCO1: Saw wave
2. VCO2: Square wave, detune +5 cents
3. VCO3+4: OFF
4. Filter 1: LP, cutoff 40%, resonance 70%
5. Filter EG: Fast attack, fast decay, zero sustain, short release
6. Filter EG → Filter 1 Cutoff (maximum amount)
7. VCA EG: Fast attack, medium decay, full sustain
8. Optional: Patch LFO → Filter Cutoff for wobble

**Modular Patching Ideas**:
- Patch LFO → VCO1 FM for vibrato
- Patch VCO1 out → VCO2 FM for complex timbres
- Patch Keyboard CV → Delay Time for pitch-tracked delay
- Patch Filter 1 out → external effects → Stereo In (for parallel processing)
- Patch Noise → VCO1 FM for wind/breath sounds

**Limitations**:
- Paraphonic (not fully polyphonic - all notes share same filter/VCA)
- Can be CPU-heavy with all 4 VCOs running
- Patch cables required for advanced routing
- No built-in effects beyond delay and reverb

---

### Moog DFAM (Drummer From Another Mother)

- **Type**: Analog percussion synthesizer (semi-modular)
- **Oscillators**: 2 analog VCOs (saw, square)
- **Filter**: Moog ladder filter (24dB/octave, LP)
- **Voices**: Monophonic (designed for percussion)
- **Envelopes**: 2x AD envelopes (decay-only, for percussion)
- **Sequencer**: 8-step sequencer with velocity per step
- **Modulation**: 24 patch points
- **Noise**: White/pink noise generator
- **VCA**: Velocity-sensitive VCA
- **Patchbay**: 24 patch points for modular integration
- **Specialties**:
  - Designed specifically for percussion/drums
  - Analog character for kicks, snares, hi-hats
  - Patch bay for modular integration
  - Internal sequencer with per-step velocity

**Programming Interface**:
- Knob-per-function
- Intuitive for percussion programming
- Patch bay for creative routing

**Best For**:
- Kick drums (punchy, sub-heavy)
- Snare drums (noise + pitch)
- Hi-hats (noise-based)
- Toms and percussion
- Industrial/experimental drums
- Modular drum setups

**Programming Tips**:

**Kick Drum**:
1. VCO1: Saw wave, tune to ~60Hz (C1 or lower)
2. VCO2: OFF or very low level
3. Filter: LP, cutoff 40%, resonance 30%
4. Envelope 1 → VCO1 Pitch (fast decay for pitch drop)
5. Envelope 2 → VCA (fast decay)
6. Velocity: High (100)

**Snare Drum**:
1. VCO1: Square wave, tune to ~200Hz
2. Noise: High level, white noise
3. Filter: HP or BP mode, cutoff 50%
4. Envelope 1 → Filter Cutoff (medium decay)
5. Envelope 2 → VCA (fast decay, ~100ms)
6. Patch Noise → Filter for snap

**Hi-Hat**:
1. VCO1: OFF
2. VCO2: Square wave, high pitch
3. Noise: Maximum level
4. Filter: HP mode, high cutoff
5. Both envelopes: Very fast decay
6. Velocity variations per step for groove

**Limitations**:
- Monophonic (one sound at a time)
- No polyphony or chords
- Limited to percussion sounds primarily
- No effects (external required)

---

### Moog Subharmonicon

- **Type**: Semi-modular subharmonic synthesizer
- **Oscillators**: 2 analog VCOs with 4 subharmonic generators (6 tones total)
- **Subharmonics**: Each VCO has 2 subharmonic generators (1/2, 1/3, 1/4 divisions)
- **Filter**: Moog ladder filter (24dB/octave, LP)
- **Voices**: Paraphonic (6 tones, shared filter)
- **Envelopes**: 2x AD envelopes
- **Sequencer**: 2x 4-step sequencers (polyrhythmic)
- **Rhythm**: 4-step rhythm generator
- **Patchbay**: 32 patch points
- **Specialties**:
  - Subharmonic synthesis (generates lower harmonics)
  - Polyrhythmic sequencers
  - Drones and evolving textures
  - Unique harmonic relationships

**Programming Interface**:
- Knob-per-function
- Two independent sequencers
- Patch bay for modular routing

**Best For**:
- Sub bass (deep subharmonic fundamentals)
- Drones (long evolving tones)
- Experimental harmony (unconventional intervals)
- Polyrhythmic sequences
- Ambient textures
- Bass music (subharmonics add weight)

**Programming Tips**:

**Deep Sub Bass**:
1. VCO1: ON, tune to root note
2. Sub1: 1/2 division (octave down)
3. Sub2: 1/4 division (two octaves down)
4. VCO2: OFF
5. Filter: LP, open cutoff, low resonance
6. Envelope: Fast attack, long decay

**Polyrhythmic Drone**:
1. Both VCOs ON with subharmonics
2. Sequencer 1: 4 steps
3. Sequencer 2: 3 steps (polyrhythm: 4 against 3)
4. Filter: Slow LFO modulation
5. Long envelope decay times

**Limitations**:
- Unconventional tuning system (not chromatic)
- Limited to specific harmonic relationships
- Can be challenging to play "in tune"
- Not for traditional melodies

---

### Behringer Crave

- **Type**: Semi-modular analog monophonic synthesizer
- **Oscillators**: 1 analog VCO (saw, triangle, square, PWM)
- **Filter**: 24dB Moog-style ladder filter (LP)
- **Voices**: Monophonic
- **Envelopes**: 1x ADSR
- **LFO**: 1 LFO with multiple waveforms
- **Sequencer**: 32-step sequencer
- **Patchbay**: 18 patch points (3.5mm mini-jacks)
- **Arpeggiator**: Built-in arpeggiator
- **MIDI**: Full MIDI implementation
- **Specialties**:
  - Affordable semi-modular
  - Moog-style ladder filter
  - Compact size
  - Patch bay for modular integration

**Programming Interface**:
- Knob-per-function for main parameters
- Mini-jack patch bay (3.5mm)
- External keyboard/sequencer needed

**Best For**:
- Mono bass lines
- Acid basslines (TB-303 style)
- Lead lines
- Modular integration (Eurorack compatible with adapters)
- Budget analog sound

**Programming Tips**:

**TB-303 Style Acid Bass**:
1. VCO: Saw wave
2. Filter: LP, cutoff 30%, resonance 80%
3. Envelope → Filter Cutoff (maximum amount)
4. Envelope: Fast attack, fast decay, zero sustain, short release
5. Sequencer: 16 steps with accent on key notes

**Mono Lead**:
1. VCO: Square wave with PWM
2. Filter: Cutoff 50%, resonance 40%
3. LFO → PWM for movement
4. Envelope: Medium attack, medium decay, half sustain

**Limitations**:
- Monophonic only
- Single oscillator (limited thickness)
- No built-in effects
- Small patch bay (18 points vs Matriarch's 90)

---

### Make Noise 0-Coast

- **Type**: Single-voice patchable synthesizer (West Coast philosophy)
- **Oscillator**: 1 digital/analog hybrid oscillator
- **Waveshaper**: Overtone generator for additive/subtractive synthesis
- **Filter**: No traditional filter (uses wavefolding/timbre)
- **Voices**: Monophonic
- **Envelopes**: Contour generator (loopable)
- **LFO**: Contour can function as LFO
- **Modulation**: Multiply section for complex modulation
- **Patchbay**: Banana jack patchbay
- **CV/Gate**: 1V/oct input, gate input
- **Specialties**:
  - West Coast synthesis (wavefolding, not filtering)
  - No keyboard (CV/Gate controlled)
  - Experimental/noise-friendly
  - Unique sound character

**Programming Interface**:
- Knob-based with banana jack patching
- No traditional keyboard
- Experimental workflow

**Best For**:
- Experimental sounds
- Noise and texture
- West Coast synthesis exploration
- Modular integration
- Sound design (not traditional musical playing)
- Drones and evolving timbres

**Programming Tips**:
- Explore wavefolding (Balance control)
- Use Multiply section for complex modulation
- Patch Contour to multiple destinations
- Self-patching creates feedback loops

**Limitations**:
- Monophonic
- No keyboard
- Steep learning curve
- Not for traditional playing
- Banana jacks (not standard 3.5mm)

---

## SOFTWARE SYNTHESIZERS

### Vital

- **Type**: Wavetable synthesizer with spectral processing
- **Oscillators**: 3 wavetable oscillators with spectral warping
- **Wavetables**: 100+ included, user wavetable import
- **Spectral Processing**: Spectral morph, warp, unison spread
- **Filter**: 4 filter types with multiple modes (LP/HP/BP/Notch/Formant/Comb/Phaser)
- **Voices**: Unlimited polyphony (CPU dependent)
- **Envelopes**: 3 envelopes with complex shapes
- **LFO**: 2 LFOs with multiple shapes and grid mode
- **Modulation**: Full modulation matrix (drag and drop)
- **Effects**: 9 effect types (distortion, chorus, flanger, phaser, reverb, delay, compressor, EQ, filter)
- **Arpeggiator**: None built-in
- **File Format**: .vital (JSON-based, human-readable)
- **Presets**: 500+ included presets
- **UI**: Modern, visual with oscilloscope
- **Specialties**:
  - Spectral warping (unique to Vital)
  - Visual modulation routing
  - Free and open-source
  - Very CPU-efficient
  - High-quality sound

**Programming Interface**:
- Visual drag-and-drop modulation
- Real-time waveform/spectrum display
- Intuitive layout
- Easy to learn, deep to master

**Best For**:
- Modern EDM sounds
- Bass (dubstep, future bass, house)
- Leads (bright, evolving)
- Pads (wavetable smoothness)
- Plucks and keys
- Sound design (extensive modulation)
- CPU-friendly production

**Programming Tips**:

**Dubstep Wobble Bass**:
1. Oscillator 1: Wavetable (Basic Shapes → Saw)
2. Spectral Warp: High amount
3. Filter 1: Formant filter
4. LFO 1 → Filter Cutoff (rate 1/4, depth 100%)
5. Unison: 7 voices, detune spread
6. Distortion effect: Soft clip, drive 50%

**Future Bass Lead**:
1. Oscillator 1+2: Detuned wavetables (EDM category)
2. Spectral Morph: Animate between frames
3. Filter: LP 24dB, cutoff modulated by envelope
4. Envelope 2 → Spectral Morph (slow attack)
5. Unison: 5 voices, wide stereo spread
6. Chorus + Reverb effects

**Ambient Pad**:
1. Oscillator 1+2+3: Different wavetables, stacked
2. Spectral Warp: Subtle movement
3. Filter: LP 12dB, open cutoff
4. LFO → Wavetable Position (very slow)
5. Envelope: Slow attack (2s), long release (5s)
6. Reverb: 100% wet mix, long decay

**Limitations**:
- No arpeggiator built-in
- Wavetable-focused (not analog modeling)
- Can be CPU-heavy with many voices

**Preset Generation**: 
Use `scripts/generate_vital_preset.py` to create .vital files programmatically.

---

### Serum

- **Type**: Wavetable synthesizer
- **Oscillators**: 2 wavetable oscillators + sub oscillator + noise
- **Wavetables**: 450+ included, user wavetable import (supports images, audio)
- **Filter**: 2 filters, 20+ types per filter
- **Voices**: Up to 16 voices polyphony
- **Envelopes**: 2 ADSR envelopes + mod envelope
- **LFO**: 2 LFOs with custom shape drawing
- **Modulation**: Full modulation matrix
- **Effects**: 10 effect types (hyper/dimension, chorus, phaser, flanger, reverb, delay, distortion, compressor, EQ, multiband compressor)
- **Arpeggiator**: Built-in with note pattern
- **File Format**: .fxp (VST preset format)
- **Presets**: 450+ factory presets
- **UI**: Visual with real-time waveform display
- **Specialties**:
  - Wavetable editor (create from audio, images)
  - Ultra-clean sound quality
  - Industry standard for EDM
  - Extensive preset library

**Programming Interface**:
- Visual wavetable editor
- Drag-and-drop modulation
- Real-time spectrum analyzer
- Intuitive workflow

**Best For**:
- EDM production (house, dubstep, future bass, trap)
- Bass sounds (clean, powerful)
- Leads (bright, cutting)
- Pads (evolving, lush)
- Sound design (wavetable manipulation)

**Programming Tips**:
- Import audio to create custom wavetables
- Use warp modes for movement (Bend, PWM, Sync, etc.)
- Layer two different wavetables per voice
- LFO shape drawing for custom modulation
- High-quality effects (don't skip them)

**Limitations**:
- Commercial plugin (not free)
- Can be CPU-intensive
- Learning curve for wavetable editing

---

### Massive X

- **Type**: Semi-modular wavetable/hybrid synthesizer
- **Oscillators**: 2 oscillators with 170+ wavetables and modes
- **Audio Routing**: Flexible routing (oscillators → filters → effects)
- **Filter**: 2 filters with 18 filter types
- **Voices**: Up to 32 voices polyphony
- **Envelopes**: 4 envelopes with multiple shapes
- **LFO**: 2 LFOs + 2 Performers (complex modulation sources)
- **Modulation**: Full modulation routing (drag-and-drop)
- **Effects**: 3 effect slots with 13 effect types
- **Arpeggiator**: None built-in
- **Noise**: 2 noise generators with filtering
- **File Format**: .nmsv (Native Instruments format)
- **Presets**: 500+ factory presets
- **Specialties**:
  - Semi-modular routing (flexible signal path)
  - Performers (complex modulation sequencers)
  - Phase modulation synthesis
  - Tracker mode (rhythmic gating)

**Programming Interface**:
- Drag-and-drop routing
- Visual modulation system
- Complex but powerful

**Best For**:
- Modern electronic music
- Complex bass sounds
- Evolving pads
- Experimental sound design
- Modulated textures

**Programming Tips**:
- Use Performers for rhythmic modulation
- Experiment with audio routing
- Phase modulation creates FM-like sounds
- Combine multiple modulation sources

**Limitations**:
- Steep learning curve
- Can be CPU-heavy
- Requires Native Access for authorization

---

### u-he Diva

- **Type**: Virtual analog synthesizer (analog modeling)
- **Oscillators**: Multiple oscillator models (Minimoog, Jupiter, Juno, etc.)
- **Filters**: Multiple filter models (Moog ladder, Roland cascade, etc.)
- **Architecture**: Modular (mix and match oscillators/filters/envelopes)
- **Voices**: Up to 32 voices polyphony
- **Envelopes**: Multiple envelope types
- **LFO**: 2 LFOs
- **Modulation**: Flexible modulation routing
- **Effects**: Chorus, phaser, rotary, reverb, delay, plate
- **File Format**: .h2p (u-he preset format)
- **Presets**: 1200+ factory presets
- **Quality Modes**: Draft, Good, Great, Divine (CPU vs quality trade-off)
- **Specialties**:
  - Best-in-class analog modeling
  - Authentic vintage sound
  - Mix different oscillator/filter models
  - Very warm, analog character

**Programming Interface**:
- Modular architecture (choose your components)
- Visual and intuitive
- Vintage-style layout

**Best For**:
- Vintage analog sounds
- Warm bass and leads
- Classic pads and strings
- 70s/80s style sounds
- Analog emulation

**Programming Tips**:
- Match oscillator and filter models for authentic vintage sounds
- Divine mode for best sound (CPU heavy)
- Use unison mode for thick sounds
- Chorus effect adds 80s character

**Limitations**:
- Very CPU-intensive (especially in Divine mode)
- Not for modern digital sounds
- Slower workflow than modern synths

---

### Arturia Pigments 6

- **Type**: Hybrid multi-engine synthesizer
- **Engines**: 4 sound engines (Wavetable, Virtual Analog, Sample, Harmonic, Utility)
- **Oscillators**: 2 engines per voice (mix wavetable + analog, sample + harmonic, etc.)
- **Filter**: 2 multimode filters (24 types)
- **Voices**: Unlimited polyphony (CPU dependent)
- **Envelopes**: 3 function generators
- **LFO**: 3 LFOs with extensive modulation options
- **Modulation**: Full modulation matrix with visual feedback
- **Sequencer**: 3 sequencers/arpeggiators
- **Effects**: 17 effect types (multi-effect section)
- **File Format**: .pigments (Arturia format)
- **Presets**: 1400+ factory presets
- **Specialties**:
  - Hybrid architecture (combine different engines)
  - Sample engine (granular playback)
  - Visual modulation feedback
  - Extensive effect section

**Programming Interface**:
- Tabbed interface (Synth, Sequencer, Effects)
- Visual modulation matrix
- Modern, colorful UI

**Best For**:
- Hybrid sounds (analog + digital)
- Complex textures
- Granular synthesis
- Modern electronic music
- Sound design experiments
- Combining multiple synthesis types

**Programming Tips**:
- Combine different engines (e.g., wavetable + analog)
- Use sample engine for unique textures
- Modulation matrix is very powerful
- Sequencers can create evolving patterns

**Limitations**:
- Can be overwhelming (many features)
- CPU-intensive with multiple engines
- Requires Arturia Software Center

---

## SYNTHESIS APPROACH BY SYNTH TYPE

### For Analog Synths (Moog, Behringer)
1. Start with oscillator tuning and waveform selection
2. Use detuning for width and thickness
3. Shape with filter (cutoff + resonance)
4. Add envelope modulation (filter and amp)
5. Keep effects minimal (analog character is the sound)
6. Explore modular patching if available

### For FM Synths (Digitone II)
1. Start with simple algorithms (2 operators)
2. Adjust operator ratios (integer = harmonic, decimal = inharmonic)
3. Use modulation index for brightness/complexity
4. Add subtractive filter to tame harshness
5. Parameter lock evolving parameters
6. Keep envelopes tight for percussive sounds

### For Wavetable Synths (Vital, Serum, Massive X)
1. Choose appropriate wavetable for sound type
2. Modulate wavetable position for movement
3. Use spectral processing for character
4. Add unison for width
5. Filter for tone shaping
6. Effects are crucial (reverb, delay, distortion)

### For Analog Modeling (Diva)
1. Choose oscillator and filter models that match era
2. Use unison and detune for vintage thickness
3. Keep modulation simple (vintage synths were limited)
4. Add chorus/phaser for 80s character
5. Don't over-process (analog warmth is the goal)

### For Hybrid Synths (Pigments, Minilogue XD)
1. Combine different engines for unique character
2. Use digital engines for brightness, analog for warmth
3. Layer textures (sample + wavetable)
4. Extensive modulation for complexity
5. Experiment with unusual combinations

---

## PRESET FILE FORMATS REFERENCE

| Synth | Format | Extension | Programmable |
|-------|--------|-----------|--------------|
| Vital | JSON | .vital | ✅ Yes (script available) |
| Serum | VST Preset | .fxp | ⚠️ Possible (binary) |
| Massive X | Native | .nmsv | ⚠️ Difficult (proprietary) |
| Diva | u-he | .h2p | ⚠️ Difficult (proprietary) |
| Pigments | Arturia | .pigments | ⚠️ Difficult (proprietary) |
| Digitone II | Sysex | .syx | ⚠️ Complex (MIDI Sysex) |

---

## MIDI NOTE REFERENCE

**Standard Tuning (A4 = 440Hz)**:
- C0 = MIDI 12
- C1 = MIDI 24
- C2 = MIDI 36 (sub bass territory)
- C3 = MIDI 48 (bass range)
- C4 = MIDI 60 (middle C)
- C5 = MIDI 72 (lead range)
- C6 = MIDI 84 (high lead/pluck)

**Common Bass Notes**:
- E1 = MIDI 40 (deep bass)
- A1 = MIDI 45 (common bass root)
- D2 = MIDI 50 (mid bass)
- G2 = MIDI 55 (higher bass)

---

## WHEN TO USE WHICH SYNTH

**For Dark Techno Bass**: Matriarch, Digitone II, Vital, Serum  
**For Ambient Pads**: Matriarch, Pigments, Diva, Massive X  
**For Acid Lines**: Crave, Matriarch  
**For FM Sounds**: Digitone II, Massive X (phase mod)  
**For Experimental**: 0-Coast, Subharmonicon, Pigments  
**For Vintage 80s**: Diva, Matriarch  
**For Modern EDM**: Vital, Serum, Massive X  
**For Drums/Percussion**: DFAM, Digitone II  

---

**End of Database**
