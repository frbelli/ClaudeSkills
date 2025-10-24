#!/usr/bin/env python3
"""
Mood to Composition Generator
Maps emotional/atmospheric keywords to musical suggestions:
- Scales and modes
- Root key recommendations  
- Chord progressions (3+ variations)
- Orchestration tips
- Optional MIDI generation
"""

import sys
import random
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

# ============================================================
# MOOD DATABASE
# ============================================================

MOOD_DATABASE = {
    "dark": {
        "scales": ["Phrygian", "Locrian", "Harmonic Minor", "Phrygian Dominant"],
        "root_keys": ["D", "E", "F#", "C#", "A"],
        "chord_progressions": [
            {
                "name": "Chromatic Tension",
                "chords": ["i", "bII", "i", "bII"],
                "feel": "Claustrophobic, tense, unsettling"
            },
            {
                "name": "Phrygian Dominant",
                "chords": ["i", "bII", "bVII", "bVI"],
                "feel": "Middle Eastern, exotic, ominous"
            },
            {
                "name": "Dark Descent",
                "chords": ["i", "bVII", "bVI", "V"],
                "feel": "Descending darkness, dramatic"
            }
        ],
        "tips": [
            "Use low-pass filters with slow cutoff sweeps",
            "Add subtle dissonance with minor 2nd intervals",
            "Employ reverb with long decay times",
            "Layer noise textures underneath"
        ]
    },
    
    "atmospheric": {
        "scales": ["Lydian", "Dorian", "Aeolian"],
        "root_keys": ["C", "D", "F", "G", "A"],
        "chord_progressions": [
            {
                "name": "Floating Ambiguity",
                "chords": ["Isus2", "IVsus2", "Vsus2", "IVsus2"],
                "feel": "Spacious, ambiguous, meditative"
            },
            {
                "name": "Ethereal Jazz",
                "chords": ["Imaj9", "VImaj7", "IVmaj9", "IImaj7"],
                "feel": "Lush, sophisticated, dreamy"
            },
            {
                "name": "Ambient Loop",
                "chords": ["vi", "IVmaj7", "I", "V"],
                "feel": "Nostalgic, warm, evolving"
            }
        ],
        "tips": [
            "Use slow attack envelopes (1-2 seconds)",
            "Layer multiple detuned oscillators",
            "Apply heavy reverb and delay",
            "Slow LFO modulation for subtle movement"
        ]
    },
    
    "happy": {
        "scales": ["Major (Ionian)", "Lydian", "Mixolydian"],
        "root_keys": ["C", "G", "D", "F", "A"],
        "chord_progressions": [
            {
                "name": "Pop Anthem",
                "chords": ["I", "V", "vi", "IV"],
                "feel": "Euphoric, sing-along, optimistic"
            },
            {
                "name": "Bouncy Bright",
                "chords": ["I", "IV", "V", "IV"],
                "feel": "Bright, bouncy, classic"
            },
            {
                "name": "Uplifting Build",
                "chords": ["I", "III", "IV", "iv"],
                "feel": "Complex emotions, modern"
            }
        ],
        "tips": [
            "Use bright, harmonic-rich waveforms",
            "Fast attack envelopes for punchy sounds",
            "Add upward pitch sweeps for excitement",
            "Layer with major 7th chords for sophistication"
        ]
    },
    
    "sad": {
        "scales": ["Natural Minor", "Dorian", "Aeolian"],
        "root_keys": ["Am", "Dm", "Em", "Bm", "F#m"],
        "chord_progressions": [
            {
                "name": "Sad Pop",
                "chords": ["i", "VI", "III", "VII"],
                "feel": "Emotional, powerful, modern sad"
            },
            {
                "name": "Descending Sorrow",
                "chords": ["i", "iv", "VII", "VI"],
                "feel": "Melancholic, defeated"
            },
            {
                "name": "Bittersweet Hope",
                "chords": ["i", "III", "VII", "VI"],
                "feel": "Sad but hopeful"
            }
        ],
        "tips": [
            "Use minor triads and seventh chords",
            "Slow tempo (60-90 BPM)",
            "Long release times on pads",
            "Add subtle string-like textures"
        ]
    },
    
    "energetic": {
        "scales": ["Mixolydian", "Dorian", "Major"],
        "root_keys": ["C", "D", "E", "G", "A"],
        "chord_progressions": [
            {
                "name": "Power Drive",
                "chords": ["I", "bVII", "bVI", "bVII"],
                "feel": "Driving, rock, powerful"
            },
            {
                "name": "High Energy Build",
                "chords": ["I", "V/VII", "vi", "IV"],
                "feel": "Building energy, anthemic"
            },
            {
                "name": "Aggressive",
                "chords": ["i", "i", "iv", "v"],
                "feel": "Heavy, blues-rock, groovy"
            }
        ],
        "tips": [
            "Fast tempos (128-150 BPM)",
            "Use compression for punch",
            "Sidechain kick to bass",
            "Layer with syncopated rhythms"
        ]
    },
    
    "epic": {
        "scales": ["Harmonic Minor", "Dorian", "Aeolian"],
        "root_keys": ["Dm", "Am", "Em", "Cm"],
        "chord_progressions": [
            {
                "name": "Heroic Journey",
                "chords": ["i", "bVII", "bVI", "bVII"],
                "feel": "Powerful, determined, heroic"
            },
            {
                "name": "Cinematic Arc",
                "chords": ["Im", "IVm", "VIImaj", "IIImaj"],
                "feel": "Dark to light, dramatic"
            },
            {
                "name": "Rising Action",
                "chords": ["vi", "IV", "I", "V"],
                "feel": "Building, triumphant"
            }
        ],
        "tips": [
            "Layer orchestral sounds with synths",
            "Use crescendos and dynamic builds",
            "Add dramatic percussion fills",
            "Employ tempo changes for impact"
        ]
    },
    
    "dreamy": {
        "scales": ["Lydian", "Major", "Mixolydian"],
        "root_keys": ["C", "F", "G", "D", "A"],
        "chord_progressions": [
            {
                "name": "Lydian Dream",
                "chords": ["Imaj7", "VImaj7", "IImaj7", "Vmaj7"],
                "feel": "Dreamy, magical, otherworldly"
            },
            {
                "name": "Nostalgic Warmth",
                "chords": ["vi", "IVmaj7", "I", "IIIm7"],
                "feel": "Nostalgic, warm, sunset vibes"
            },
            {
                "name": "Jazzy Float",
                "chords": ["IVmaj7", "IIIm7", "VIm7", "IIm7"],
                "feel": "Smooth, sophisticated, jazzy"
            }
        ],
        "tips": [
            "Use maj7 and add9 chords",
            "Slow, gentle arpeggios",
            "Lush reverb and chorus effects",
            "Soft, filtered synth pads"
        ]
    },
    
    "mysterious": {
        "scales": ["Locrian", "Phrygian", "Diminished"],
        "root_keys": ["B", "E", "F#", "C#"],
        "chord_progressions": [
            {
                "name": "Diminished Mystery",
                "chords": ["vii°", "i", "bII", "V"],
                "feel": "Unsettled, dramatic, noir"
            },
            {
                "name": "Exotic Enigma",
                "chords": ["i", "bII", "bVII", "bVI"],
                "feel": "Middle Eastern, mysterious"
            },
            {
                "name": "Suspended Question",
                "chords": ["isus2", "IVsus2", "bVIIsus2", "Vsus4"],
                "feel": "Ambiguous, questioning"
            }
        ],
        "tips": [
            "Use diminished and augmented chords",
            "Add tritone intervals",
            "Sparse, minimal arrangement",
            "Unpredictable rhythm patterns"
        ]
    }
}

# ============================================================
# SCALE DEFINITIONS (MIDI note offsets from root)
# ============================================================

SCALES = {
    "Major (Ionian)": [0, 2, 4, 5, 7, 9, 11],
    "Natural Minor (Aeolian)": [0, 2, 3, 5, 7, 8, 10],
    "Harmonic Minor": [0, 2, 3, 5, 7, 8, 11],
    "Dorian": [0, 2, 3, 5, 7, 9, 10],
    "Phrygian": [0, 1, 3, 5, 7, 8, 10],
    "Lydian": [0, 2, 4, 6, 7, 9, 11],
    "Mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "Locrian": [0, 1, 3, 5, 6, 8, 10],
    "Phrygian Dominant": [0, 1, 4, 5, 7, 8, 10]
}

# Note names
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# ============================================================
# CHORD CONSTRUCTION
# ============================================================

def get_chord_midi_notes(root_midi, chord_type, scale_notes):
    """
    Returns MIDI notes for a chord based on root and type
    """
    # Basic chord formulas (scale degrees from 0)
    chord_formulas = {
        "I": [0, 2, 4],          # Major triad
        "i": [0, 2, 4],          # Minor triad (handled by scale)
        "IV": [3, 5, 0],         # Fourth degree
        "iv": [3, 5, 0],
        "V": [4, 6, 1],          # Fifth degree
        "v": [4, 6, 1],
        "VI": [5, 0, 2],         # Sixth degree
        "vi": [5, 0, 2],
        "VII": [6, 1, 3],        # Seventh degree
        "bII": [1, 3, 5],        # Flat second
        "bVII": [5, 0, 2],       # Flat seventh
        "bVI": [4, 6, 1],        # Flat sixth
        "III": [2, 4, 6],        # Third
        "iii": [2, 4, 6],
        "Imaj7": [0, 2, 4, 6],   # Major seventh
        "Imaj9": [0, 2, 4, 6, 1],# Major ninth
        "Isus2": [0, 1, 4],      # Suspended second
        "Isus4": [0, 3, 4],      # Suspended fourth
        "IVsus2": [3, 4, 0],
        "Vsus2": [4, 5, 1],
        "IVmaj7": [3, 5, 0, 2],
        "VImaj7": [5, 0, 2, 4],
    }
    
    # Get formula or default to triad
    formula = chord_formulas.get(chord_type, [0, 2, 4])
    
    # Map to actual MIDI notes using scale
    notes = []
    for degree in formula:
        if degree < len(scale_notes):
            notes.append(scale_notes[degree])
    
    return notes

# ============================================================
# MAIN GENERATOR
# ============================================================

def generate_composition_from_mood(mood_keyword, root_note="C", generate_midi=True):
    """
    Main function to generate composition suggestions from mood
    """
    
    # Find matching mood (case-insensitive, partial match)
    mood_keyword = mood_keyword.lower()
    matched_mood = None
    
    for mood_key in MOOD_DATABASE.keys():
        if mood_keyword in mood_key or mood_key in mood_keyword:
            matched_mood = mood_key
            break
    
    if not matched_mood:
        # Try to find related moods
        mood_suggestions = list(MOOD_DATABASE.keys())
        print(f"\n❌ Mood '{mood_keyword}' not found in database.")
        print(f"\n💡 Available moods: {', '.join(mood_suggestions)}")
        return
    
    mood_data = MOOD_DATABASE[matched_mood]
    
    # Select scale
    selected_scale = random.choice(mood_data["scales"])
    
    # Select root key (or use provided)
    if root_note not in NOTE_NAMES:
        root_note = random.choice(mood_data["root_keys"])[0]
    
    # Get root MIDI note (middle C = 60)
    root_midi = 60 + NOTE_NAMES.index(root_note)
    
    # Generate scale notes
    scale_offsets = SCALES[selected_scale]
    scale_notes = [root_midi + offset for offset in scale_offsets]
    
    # Print results
    print("\n" + "=" * 70)
    print(f"🎹 COMPOSITION SUGGESTIONS FOR: {matched_mood.upper()}")
    print("=" * 70)
    
    print(f"\n🎼 SCALE: {root_note} {selected_scale}")
    scale_note_names = [NOTE_NAMES[(note - 60) % 12] for note in scale_notes]
    print(f"   Notes: {' - '.join(scale_note_names)}")
    print(f"   MIDI: {scale_notes}")
    
    print(f"\n🎵 ROOT KEY: {root_note}")
    
    print(f"\n🎹 CHORD PROGRESSIONS:\n")
    
    # Generate all progressions
    for i, prog in enumerate(mood_data["chord_progressions"], 1):
        print(f"   Progression {i}: \"{prog['name']}\"")
        print(f"   Chords: {' → '.join(prog['chords'])}")
        print(f"   Feel: {prog['feel']}")
        
        # Show chord names
        chord_names = []
        for chord_symbol in prog['chords']:
            # Simple conversion (you can make this more sophisticated)
            if chord_symbol.startswith('I'):
                chord_names.append(f"{root_note}{chord_symbol.replace('I', '')}")
            elif chord_symbol.startswith('i'):
                chord_names.append(f"{root_note}m{chord_symbol.replace('i', '')}")
            else:
                chord_names.append(f"{root_note}{chord_symbol}")
        
        print(f"   Example: {' - '.join(chord_names)}")
        print()
    
    print(f"💡 PRODUCTION TIPS:")
    for tip in mood_data["tips"]:
        print(f"   • {tip}")
    
    # Generate MIDI if requested
    if generate_midi:
        print(f"\n🎼 Generating MIDI files...")
        
        for i, prog in enumerate(mood_data["chord_progressions"], 1):
            filename = f"progression_{i}_{matched_mood}_{root_note}.mid"
            create_progression_midi(
                prog['chords'], 
                scale_notes, 
                root_midi,
                filename,
                bpm=100
            )
            print(f"   ✅ Created: {filename}")
    
    print("\n" + "=" * 70)
    print("🎛️ Ready to create! Use these suggestions as starting points.")
    print("=" * 70 + "\n")

def create_progression_midi(chord_symbols, scale_notes, root_midi, filename, bpm=100):
    """
    Creates a MIDI file with the chord progression
    """
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    
    # Set tempo
    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm)))
    
    # Timing
    ticks_per_beat = 480
    whole_note = ticks_per_beat * 4
    
    # Generate chords
    time_elapsed = 0
    
    for chord_symbol in chord_symbols:
        # Get MIDI notes for chord
        chord_notes = get_chord_midi_notes(root_midi, chord_symbol, scale_notes)
        
        # Note on events
        for i, note in enumerate(chord_notes):
            delta = 0 if i > 0 else 0
            track.append(Message('note_on', note=note, velocity=80, time=delta))
        
        # Hold for whole note
        time_elapsed += whole_note
        
        # Note off events
        for i, note in enumerate(chord_notes):
            delta = whole_note if i == 0 else 0
            track.append(Message('note_off', note=note, velocity=0, time=delta))
    
    # Save
    mid.save(filename)

# ============================================================
# CLI INTERFACE
# ============================================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n🎹 MOOD TO COMPOSITION GENERATOR")
        print("=" * 70)
        print("\nUsage: python mood_to_composition.py <mood> [root_note]")
        print("\nExamples:")
        print("  python mood_to_composition.py dark")
        print("  python mood_to_composition.py atmospheric D")
        print("  python mood_to_composition.py 'dark atmospheric' C#")
        print("\nAvailable moods:")
        for mood in MOOD_DATABASE.keys():
            print(f"  • {mood}")
        print("\nCombine moods with spaces: 'dark atmospheric', 'sad dreamy', etc.")
        print("=" * 70 + "\n")
        sys.exit(0)
    
    # Parse arguments
    mood = sys.argv[1]
    root = sys.argv[2] if len(sys.argv) > 2 else "C"
    
    # Generate
    generate_composition_from_mood(mood, root, generate_midi=True)
