# Sound Design Skill

## Description
Professional skill for sound design on hardware and software synthesizers. Supports sound design, audio analysis, preset generation, and MIDI pattern creation for music production.

## Core Capabilities

1. **Guided Sound Design** - Parameter suggestions based on sound type and genre
2. **Preset Generation** - Creates ready-to-use .vital files
3. **Audio Analysis** - Extracts features from existing audio files
4. **MIDI Patterns** - Generates rhythms for various genres (techno, house, trap, dnb, etc.)
5. **Signal Flow Diagrams** - Visualizes routing and modulations
6. **Music Theory & Composition** - Suggests scales, keys, and chord progressions based on mood
7. **Harmonic Analysis** - Analyzes and generates chord progressions with MIDI output

## Supported Synthesizers

### Hardware
- **Elektron Digitone II** [📖 Complete Guide](references/synths/digitone-ii.md)
- Moog Matriarch, DFAM, Subharmonicon
- Behringer Crave
- Make Noise 0-Coast

### Software
- Vital, Serum, Massive X, Diva, Arturia Pigments 6

**Note**: Detailed synth documentation available in `references/synths/` directory. Currently available:
- `digitone-ii.md` - Complete reference from official manual (OS 1.00A)

## Supported Genres
Techno, IDM, Ambient/Drone, Synthwave, Dubstep, Trap/Hip-Hop, Psytrance, Industrial/EBM, House, Vintage/Analog

## Sound Types
Bass, Lead, Pad, Keys/Mallets, Texture, Percussion

## Documentation
- [Complete Guide](Sound_Design_Skill_Guida.md) - Detailed tutorial
- [Practical Examples](Esempi_Pratici.md) - Usage examples
- [Skill Expansion Guide](skill_expansion_guide.md) - How to expand functionality
- [Quick Start Guide](quick_start_guide.md) - Get started immediately
- [Integration Instructions](integration_instructions.md) - Step-by-step integration

## Available Scripts
- `analyze_audio.py` - Spectral analysis and suggestions
- `generate_rhythm.py` - MIDI pattern generation
- `generate_vital_preset.py` - Vital preset creation
- `generate_signal_diagram.py` - SVG routing diagrams
- `mood_to_composition.py` - Mood-based composition generation

## Basic Usage

```
"Create a reese bass for DnB on Digitone II"
"Analyze this kick and tell me how to recreate it"
"Generate a techno pattern at 128 BPM"
"I want an ambient pad on the Matriarch"
"Suggest a dark atmospheric progression in D"
```

## Music Theory & Composition Workflow

### When User Wants Composition from Mood

When user requests musical suggestions based on mood/atmosphere:

**Step 1: Identify Mood**
Ask what emotional/atmospheric quality they want:
- Dark, mysterious, ominous
- Happy, uplifting, bright
- Sad, melancholic, emotional
- Energetic, aggressive, driving
- Dreamy, nostalgic, floating
- Epic, cinematic, heroic
- Atmospheric, ambient, ethereal

**Step 2: Read Music Theory References**
```
view references/music-theory.md
view references/chord-progressions.md
view references/scales-modes.md
```

**Step 3: Generate Composition Suggestions**
```bash
python scripts/mood_to_composition.py "dark atmospheric" D
```

This will output:
- Suggested scale/mode
- Root key recommendation  
- 3 chord progression variations with MIDI
- Production/orchestration tips

**Step 4: Provide to User**
Give complete breakdown:
- Scale with note names and MIDI values
- Each progression with Roman numerals and actual chords
- Musical feeling/character of each progression
- Production tips for achieving the mood
- MIDI files for testing

### Integration with Synth Programming

Combine composition with synth programming:

**Example Workflow**:
1. User: "I want a dark ambient track"
2. Generate composition suggestions (scale, progressions)
3. Suggest synth patches (e.g., Matriarch pad in D Phrygian)
4. Provide rhythm pattern (minimal, sparse)
5. Offer arrangement structure

**Code Example**:
```bash
# Generate composition
python scripts/mood_to_composition.py "dark ambient" D

# Generate rhythm (sparse)
python scripts/generate_rhythm.py ambient 90 8

# Suggest using existing pad patch
# "Use the Matriarch Ethereal Drift pad, tuned to D Phrygian"
```

## Optional Dependencies
```bash
pip install librosa mido --break-system-packages
```

## Included Resources
- `Dark_Techno_Bass.vital` - Example preset
- `pattern_techno_techno_128bpm.mid` - Example MIDI pattern
- Example JSON configuration files
- SVG signal flow diagrams

## Music Theory Reference Quick Access

When suggesting compositions:
- Consult `references/music-theory.md` for scale theory, intervals, chord construction
- Consult `references/chord-progressions.md` for mood-specific progressions
- Consult `references/scales-modes.md` for complete scales database with MIDI values
- Use `scripts/mood_to_composition.py` to generate complete suggestions with MIDI
- Combine music theory with synth programming for complete production workflows

## Workflow Guidelines

### Sound Design Workflow
1. Identify the synthesizer
2. Specify sound type and genre
3. Get detailed patch parameters
4. Optional: Generate preset files
5. Follow step-by-step programming guide

### Composition Workflow
1. Define mood/atmosphere
2. Get scale and key suggestions
3. Receive chord progressions with MIDI
4. Apply to synth programming
5. Generate rhythm patterns
6. Complete arrangement structure

## Remember
- Always identify the synth being used
- Adapt suggestions to hardware/software capabilities
- Provide step-by-step programming guides
- Generate files when possible (presets, MIDI, diagrams)
- Combine sound design with music theory for complete productions
- Read theory references before suggesting compositions
- Create MIDI files to help users test ideas quickly
