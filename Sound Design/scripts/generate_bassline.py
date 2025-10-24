#!/usr/bin/env python3
"""
Bass Line Generator
Generates MIDI bass lines that follow chord progressions

Usage:
    python generate_bassline.py <progression> <key> <genre> [options]
    
Examples:
    python generate_bassline.py "i-VI-III-VII" Am techno
    python generate_bassline.py "I-V-vi-IV" C house --bpm 125 --style rolling
    python generate_bassline.py "i-iv-VII-VI" Dm dubstep --octave 1
"""

import random
import argparse
from typing import List, Tuple, Dict, Optional

# Try to import mido for MIDI generation
try:
    from mido import MidiFile, MidiTrack, Message
    MIDO_AVAILABLE = True
except ImportError:
    MIDO_AVAILABLE = False
    print("⚠️  Warning: mido not installed. Install with: pip install mido")
    print("   MIDI files will not be generated, but notation will be shown.\n")

# ============================================================================
# MUSIC THEORY DATABASE
# ============================================================================

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

SCALES = {
    "Major": [0, 2, 4, 5, 7, 9, 11],
    "Minor": [0, 2, 3, 5, 7, 8, 10],
    "Dorian": [0, 2, 3, 5, 7, 9, 10],
    "Phrygian": [0, 1, 3, 5, 7, 8, 10],
    "Harmonic Minor": [0, 2, 3, 5, 7, 8, 11],
}

# Roman numeral to scale degree mapping
ROMAN_TO_DEGREE = {
    # Major key
    "I": 0, "II": 1, "III": 2, "IV": 3, "V": 4, "VI": 5, "VII": 6,
    # Minor key (lowercase)
    "i": 0, "ii": 1, "iii": 2, "iv": 3, "v": 4, "vi": 5, "vii": 6,
    # Flat variants
    "bII": 1, "bIII": 2, "bVI": 5, "bVII": 6,
}

# ============================================================================
# BASS STYLE PATTERNS
# ============================================================================

BASS_STYLES = {
    "root": {
        "description": "Root notes only (minimal)",
        "pattern": ["root"],
        "rhythm": [16],  # Whole note
        "octave_variation": False,
    },
    "root_fifth": {
        "description": "Root and fifth alternating",
        "pattern": ["root", "fifth", "root", "fifth"],
        "rhythm": [4, 4, 4, 4],  # Quarter notes
        "octave_variation": False,
    },
    "walking": {
        "description": "Walking bass (quarter notes, stepwise)",
        "pattern": ["root", "step", "step", "approach"],
        "rhythm": [4, 4, 4, 4],
        "octave_variation": False,
    },
    "rolling": {
        "description": "Rolling bass (constant eighth notes)",
        "pattern": ["root", "root", "fifth", "root", "octave", "fifth", "root", "fifth"],
        "rhythm": [2, 2, 2, 2, 2, 2, 2, 2],  # Eighth notes
        "octave_variation": True,
    },
    "syncopated": {
        "description": "Syncopated groove",
        "pattern": ["root", "rest", "fifth", "root", "rest", "third", "fifth", "root"],
        "rhythm": [2, 2, 2, 2, 2, 2, 2, 2],
        "octave_variation": False,
    },
    "funky": {
        "description": "Funky groove with rests and octaves",
        "pattern": ["root", "rest", "octave", "rest", "fifth", "root", "rest", "third"],
        "rhythm": [2, 2, 2, 2, 2, 2, 2, 2],
        "octave_variation": True,
    },
    "dubstep": {
        "description": "Dubstep wobble (long notes with movement)",
        "pattern": ["root", "root", "root", "fifth"],
        "rhythm": [4, 4, 4, 4],
        "octave_variation": False,
        "wobble": True,  # Special flag for wobble bass
    },
    "dnb": {
        "description": "Drum & Bass rolling (fast)",
        "pattern": ["root", "fifth", "root", "octave", "fifth", "root", "fifth", "third"],
        "rhythm": [2, 2, 2, 2, 2, 2, 2, 2],
        "octave_variation": True,
    },
    "trap": {
        "description": "Trap 808 (long sub notes)",
        "pattern": ["root", "root", "fifth", "third"],
        "rhythm": [8, 4, 2, 2],  # Varied lengths
        "octave_variation": False,
        "glide": True,  # Pitch glide between notes
    },
}

# Genre to style mapping
GENRE_STYLES = {
    "house": ["root_fifth", "rolling"],
    "techno": ["rolling", "root_fifth"],
    "deep house": ["root_fifth", "syncopated"],
    "tech house": ["syncopated", "funky"],
    "dubstep": ["dubstep", "root"],
    "dnb": ["dnb", "rolling"],
    "drum and bass": ["dnb", "rolling"],
    "trap": ["trap", "root"],
    "hip hop": ["root", "walking"],
    "funk": ["funky", "walking"],
    "disco": ["root_fifth", "funky"],
    "trance": ["root_fifth", "rolling"],
    "ambient": ["root", "root_fifth"],
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def note_name_to_midi(note_name: str, octave: int = 2) -> int:
    """Convert note name to MIDI (default octave 2 for bass)"""
    try:
        note_index = NOTE_NAMES.index(note_name.upper())
        return note_index + (octave * 12) + 12
    except ValueError:
        print(f"⚠️  Unknown note: {note_name}, using C")
        return 48  # C2

def midi_to_note_name(midi: int) -> str:
    """Convert MIDI to note name with octave"""
    octave = (midi - 12) // 12
    note_index = (midi - 12) % 12
    return f"{NOTE_NAMES[note_index]}{octave}"

def parse_chord_progression(progression: str, key: str, scale_type: str = "Minor") -> List[int]:
    """
    Parse chord progression (Roman numerals) into root notes
    
    Examples:
        "i-VI-III-VII" in Am -> [A, F, C, G]
        "I-V-vi-IV" in C -> [C, G, Am, F]
    """
    # Determine if major or minor key
    if progression[0].islower():
        scale_type = "Minor"
    else:
        scale_type = "Major"
    
    scale = SCALES[scale_type]
    root_midi = note_name_to_midi(key, octave=2)
    
    chords = progression.split("-")
    root_notes = []
    
    for chord in chords:
        chord = chord.strip()
        
        # Handle flat notation (bII, bIII, etc.)
        if chord.startswith("b"):
            base_chord = chord[1:]
            degree = ROMAN_TO_DEGREE.get(base_chord, 0)
            # Flat means lower by semitone
            note = root_midi + scale[degree] - 1
        else:
            degree = ROMAN_TO_DEGREE.get(chord, 0)
            note = root_midi + scale[degree]
        
        root_notes.append(note)
    
    return root_notes

def get_chord_tones(root: int, chord_type: str = "minor") -> Dict[str, int]:
    """Get chord tones (root, third, fifth, octave) for a chord"""
    if chord_type.lower() == "major":
        third = root + 4  # Major third
    else:
        third = root + 3  # Minor third
    
    return {
        "root": root,
        "third": third,
        "fifth": root + 7,
        "octave": root + 12,
        "octave_down": root - 12,
    }

def get_scale_notes_around(root: int, scale_type: str, range_semitones: int = 12) -> List[int]:
    """Get scale notes around a root note"""
    scale = SCALES.get(scale_type, SCALES["Minor"])
    notes = []
    
    # Get notes in range
    for octave_offset in range(-1, 2):
        for interval in scale:
            note = root + interval + (octave_offset * 12)
            if abs(note - root) <= range_semitones:
                notes.append(note)
    
    return sorted(set(notes))

# ============================================================================
# BASS LINE GENERATION
# ============================================================================

def generate_bass_note(
    chord_root: int,
    pattern_element: str,
    chord_tones: Dict[str, int],
    scale_notes: List[int],
    previous_note: Optional[int] = None
) -> int:
    """Generate a single bass note based on pattern element"""
    
    if pattern_element == "root":
        return chord_root
    
    elif pattern_element == "fifth":
        return chord_tones["fifth"]
    
    elif pattern_element == "third":
        return chord_tones["third"]
    
    elif pattern_element == "octave":
        # Random octave variation
        return chord_tones["octave"] if random.random() > 0.5 else chord_root
    
    elif pattern_element == "step":
        # Stepwise motion in scale
        if previous_note:
            available = [n for n in scale_notes if abs(n - previous_note) <= 2]
            if available:
                return random.choice(available)
        return chord_root
    
    elif pattern_element == "approach":
        # Approach next chord root (chromatic or stepwise)
        # This would need next chord info, for now return fifth
        return chord_tones["fifth"]
    
    elif pattern_element == "rest":
        return 0  # Rest (MIDI note 0)
    
    else:
        return chord_root

def generate_bassline(
    chord_roots: List[int],
    style: str,
    key: str,
    scale_type: str = "Minor",
    bars_per_chord: int = 1
) -> List[Tuple[int, int, int]]:  # (MIDI note, duration, velocity)
    """
    Generate complete bass line following chord progression
    
    Returns:
        List of (midi_note, duration_ticks, velocity) tuples
    """
    
    if style not in BASS_STYLES:
        print(f"⚠️  Unknown style: {style}, using 'root_fifth'")
        style = "root_fifth"
    
    style_info = BASS_STYLES[style]
    pattern = style_info["pattern"]
    rhythm = style_info["rhythm"]
    
    bassline = []
    
    # Get scale notes for passing tones
    root_midi = note_name_to_midi(key, octave=2)
    scale_notes = get_scale_notes_around(root_midi, scale_type, range_semitones=12)
    
    previous_note = None
    
    for chord_root in chord_roots:
        chord_tones = get_chord_tones(chord_root, chord_type="minor")
        
        # Repeat pattern for bars_per_chord
        for bar in range(bars_per_chord):
            for i, pattern_element in enumerate(pattern):
                note = generate_bass_note(
                    chord_root,
                    pattern_element,
                    chord_tones,
                    scale_notes,
                    previous_note
                )
                
                duration = rhythm[i % len(rhythm)]
                
                # Velocity variations
                if pattern_element == "root" or i == 0:
                    velocity = random.randint(100, 120)  # Strong
                elif pattern_element == "rest":
                    velocity = 0
                else:
                    velocity = random.randint(80, 100)  # Medium
                
                bassline.append((note, duration, velocity))
                
                if note != 0:
                    previous_note = note
    
    return bassline

# ============================================================================
# MIDI FILE GENERATION
# ============================================================================

def create_midi_file(
    bassline: List[Tuple[int, int, int]],
    filename: str,
    bpm: int = 120
) -> bool:
    """Create MIDI file from bass line"""
    
    if not MIDO_AVAILABLE:
        print("⚠️  Cannot create MIDI file (mido not installed)")
        return False
    
    try:
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
        
        # Set tempo
        tempo = int(60000000 / bpm)
        track.append(Message('program_change', program=33, time=0))  # Finger Bass
        
        # Add notes
        ticks_per_beat = mid.ticks_per_beat
        current_time = 0
        
        for note, duration, velocity in bassline:
            if note == 0:  # Rest
                current_time += int((duration / 4.0) * ticks_per_beat)
            else:
                # Note on
                track.append(Message('note_on', note=note, velocity=velocity, time=current_time))
                # Note off
                note_length = int((duration / 4.0) * ticks_per_beat)
                track.append(Message('note_off', note=note, velocity=0, time=note_length))
                current_time = 0
        
        mid.save(filename)
        return True
    
    except Exception as e:
        print(f"⚠️  Error creating MIDI file: {e}")
        return False

# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_bassline_notation(
    bassline: List[Tuple[int, int, int]],
    chord_roots: List[int],
    style: str
):
    """Display bass line in text notation"""
    
    print(f"\n🎸 BASS LINE NOTATION")
    print(f"   Style: {style}")
    print(f"   Total notes: {len([b for b in bassline if b[0] != 0])}")
    print(f"   Chord progression: {' - '.join([midi_to_note_name(c) for c in chord_roots])}")
    print(f"\n   Notes (Note - Duration - Velocity):")
    print("   " + "-" * 50)
    
    for i, (note, duration, velocity) in enumerate(bassline[:32], 1):  # Show first 32 notes
        if note == 0:
            print(f"   {i:2d}. REST        - {duration:2d} ticks")
        else:
            note_name = midi_to_note_name(note)
            duration_name = {
                1: "16th", 2: "8th", 3: "8th triplet",
                4: "Quarter", 8: "Half", 16: "Whole"
            }.get(duration, f"{duration} ticks")
            
            velocity_desc = "ff" if velocity > 100 else "f" if velocity > 85 else "mf"
            
            print(f"   {i:2d}. {note_name:5s} (MIDI {note:3d}) - {duration_name:12s} - {velocity_desc}")
    
    if len(bassline) > 32:
        print(f"   ... ({len(bassline) - 32} more notes)")

def display_bassline_ascii(bassline: List[Tuple[int, int, int]], width: int = 64):
    """Display bass line as ASCII visualization"""
    
    notes = [(n, d) for n, d, v in bassline if n != 0]
    if not notes:
        return
    
    min_note = min(n for n, d in notes)
    max_note = max(n for n, d in notes)
    
    print(f"\n🎸 BASS LINE VISUALIZATION:")
    print("   " + "-" * width)
    
    # Display each pitch row
    for pitch in range(max_note, min_note - 1, -1):
        note_name = midi_to_note_name(pitch)
        line = f"   {note_name:5s} |"
        
        note_count = 0
        for i, (note, duration) in enumerate(notes):
            if note_count >= width - 10:
                break
            if note == pitch:
                bar_length = min(duration // 2, 4)  # Visualize duration
                line += "█" * bar_length
                note_count += bar_length
            else:
                line += " "
                note_count += 1
        
        print(line)
    
    print("   " + "-" * width)

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Generate MIDI bass lines following chord progressions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_bassline.py "i-VI-III-VII" Am techno
  python generate_bassline.py "I-V-vi-IV" C house --bpm 125 --style rolling
  python generate_bassline.py "i-iv-VII-VI" Dm dubstep --octave 1
  python generate_bassline.py "I-IV-V-IV" G funk --style funky
  
Progression Format:
  Use Roman numerals separated by dashes: "I-V-vi-IV"
  Lowercase for minor key: "i-VI-III-VII"
  Flat notation: "i-bVII-bVI-V"
  
Available Styles:
  root, root_fifth, walking, rolling, syncopated, funky, dubstep, dnb, trap
  
Supported Genres:
  house, techno, deep house, tech house, dubstep, dnb, trap, hip hop, funk, disco, trance, ambient
        """
    )
    
    parser.add_argument("progression", help="Chord progression (e.g., 'i-VI-III-VII')")
    parser.add_argument("key", help="Key (e.g., Am, C, Dm)")
    parser.add_argument("genre", help="Genre (house, techno, dubstep, etc.)")
    parser.add_argument("--style", default=None, help="Bass style (overrides genre default)")
    parser.add_argument("--bpm", type=int, default=120, help="Tempo in BPM (default: 120)")
    parser.add_argument("--octave", type=int, default=2, help="Bass octave (default: 2)")
    parser.add_argument("--bars", type=int, default=1, help="Bars per chord (default: 1)")
    parser.add_argument("--output", default=None, help="Output MIDI filename")
    parser.add_argument("--no-ascii", action="store_true", help="Skip ASCII visualization")
    
    args = parser.parse_args()
    
    # Determine style from genre if not specified
    if args.style:
        style = args.style
    else:
        genre_lower = args.genre.lower()
        if genre_lower in GENRE_STYLES:
            style = random.choice(GENRE_STYLES[genre_lower])
        else:
            style = "root_fifth"
            print(f"⚠️  Unknown genre: {args.genre}, using default style: {style}")
    
    print(f"\n🎸 BASS LINE GENERATOR")
    print(f"   Progression: {args.progression}")
    print(f"   Key: {args.key}")
    print(f"   Genre: {args.genre}")
    print(f"   Style: {style} - {BASS_STYLES[style]['description']}")
    print(f"   BPM: {args.bpm}")
    print(f"   Octave: {args.octave}")
    
    # Parse chord progression
    print(f"\n🎼 Parsing chord progression...")
    chord_roots = parse_chord_progression(args.progression, args.key)
    
    print(f"✅ Chord roots: {' - '.join([midi_to_note_name(c) for c in chord_roots])}")
    
    # Generate bass line
    print(f"\n🎸 Generating bass line...")
    bassline = generate_bassline(
        chord_roots,
        style,
        args.key,
        scale_type="Minor" if args.progression[0].islower() else "Major",
        bars_per_chord=args.bars
    )
    
    # Display notation
    display_bassline_notation(bassline, chord_roots, style)
    
    # Display ASCII visualization
    if not args.no_ascii:
        display_bassline_ascii(bassline)
    
    # Create MIDI file
    if args.output:
        filename = args.output
    else:
        filename = f"bassline_{args.key}_{args.genre}_{style}_{args.bpm}bpm.mid"
    
    print(f"\n💾 Creating MIDI file: {filename}")
    
    if create_midi_file(bassline, filename, args.bpm):
        print(f"✅ MIDI file created successfully!")
        print(f"   Location: {filename}")
    else:
        print(f"❌ Failed to create MIDI file")
    
    print(f"\n🎸 Bass line generation complete!\n")

if __name__ == "__main__":
    main()