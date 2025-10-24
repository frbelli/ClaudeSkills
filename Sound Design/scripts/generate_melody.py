#!/usr/bin/env python3
"""
Melody Generator
Generates MIDI melodies based on scale, mood, and musical rules

Usage:
    python generate_melody.py <scale> <root_note> <mood> [options]
    
Examples:
    python generate_melody.py "C Major" C happy
    python generate_melody.py "D Minor" D sad --length 16 --bpm 120
    python generate_melody.py "E Phrygian" E dark --octave 4 --rhythm varied
"""

import random
import argparse
from typing import List, Tuple, Dict

# Try to import mido for MIDI generation
try:
    from mido import MidiFile, MidiTrack, Message
    MIDO_AVAILABLE = True
except ImportError:
    MIDO_AVAILABLE = False
    print("⚠️  Warning: mido not installed. Install with: pip install mido")
    print("   MIDI files will not be generated, but notation will be shown.\n")


# ============================================================================
# SCALE DATABASE
# ============================================================================

SCALES = {
    # Major Scale and Modes
    "Major": [0, 2, 4, 5, 7, 9, 11],
    "Ionian": [0, 2, 4, 5, 7, 9, 11],
    "Dorian": [0, 2, 3, 5, 7, 9, 10],
    "Phrygian": [0, 1, 3, 5, 7, 8, 10],
    "Lydian": [0, 2, 4, 6, 7, 9, 11],
    "Mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "Aeolian": [0, 2, 3, 5, 7, 8, 10],
    "Minor": [0, 2, 3, 5, 7, 8, 10],  # Natural Minor = Aeolian
    "Locrian": [0, 1, 3, 5, 6, 8, 10],
    
    # Other Important Scales
    "Harmonic Minor": [0, 2, 3, 5, 7, 8, 11],
    "Melodic Minor": [0, 2, 3, 5, 7, 9, 11],
    "Major Pentatonic": [0, 2, 4, 7, 9],
    "Minor Pentatonic": [0, 3, 5, 7, 10],
    "Blues": [0, 3, 5, 6, 7, 10],
    "Whole Tone": [0, 2, 4, 6, 8, 10],
    
    # Exotic Scales
    "Phrygian Dominant": [0, 1, 4, 5, 7, 8, 10],
    "Hungarian Minor": [0, 2, 3, 6, 7, 8, 11],
    "Japanese": [0, 1, 5, 7, 8],
    "Arabic": [0, 1, 4, 5, 7, 8, 11],
}

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# ============================================================================
# MELODY GENERATION RULES
# ============================================================================

MOOD_PROFILES = {
    "happy": {
        "preferred_intervals": [2, 4, 5, 7],  # Major 2nd, Major 3rd, Perfect 4th, Perfect 5th
        "avoid_intervals": [1, 6, 11],  # Minor 2nd, Tritone
        "direction_bias": 0.6,  # Slight upward bias
        "leap_probability": 0.3,  # Moderate leaps
        "rest_probability": 0.1,  # Few rests
        "rhythm_variety": 0.6,  # Moderate rhythm variation
        "range_preference": "middle-high",
    },
    "sad": {
        "preferred_intervals": [1, 2, 3, 5],  # Minor intervals, descending
        "avoid_intervals": [4, 7],  # Avoid major intervals
        "direction_bias": 0.3,  # Downward bias
        "leap_probability": 0.2,  # Fewer leaps
        "rest_probability": 0.25,  # More pauses
        "rhythm_variety": 0.4,  # Less rhythm variation
        "range_preference": "low-middle",
    },
    "dark": {
        "preferred_intervals": [1, 3, 6, 8],  # Minor 2nd, Minor 3rd, Tritone
        "avoid_intervals": [4, 7],  # Avoid perfect intervals
        "direction_bias": 0.35,  # Downward bias
        "leap_probability": 0.4,  # More dramatic leaps
        "rest_probability": 0.2,  # Some pauses
        "rhythm_variety": 0.5,  # Moderate variation
        "range_preference": "low",
    },
    "energetic": {
        "preferred_intervals": [2, 4, 5, 7, 9],  # Large intervals
        "avoid_intervals": [1],  # Avoid chromatic steps
        "direction_bias": 0.5,  # No bias
        "leap_probability": 0.5,  # Many leaps
        "rest_probability": 0.05,  # Very few rests
        "rhythm_variety": 0.8,  # High rhythm variation
        "range_preference": "full",
    },
    "calm": {
        "preferred_intervals": [2, 3, 5],  # Stepwise motion
        "avoid_intervals": [6, 11],  # Avoid dissonance
        "direction_bias": 0.5,  # No bias
        "leap_probability": 0.15,  # Very few leaps
        "rest_probability": 0.2,  # Some pauses
        "rhythm_variety": 0.3,  # Low rhythm variation
        "range_preference": "middle",
    },
    "mysterious": {
        "preferred_intervals": [1, 3, 6, 10],  # Chromatic, tritone
        "avoid_intervals": [4, 7],  # Avoid stable intervals
        "direction_bias": 0.5,  # No bias
        "leap_probability": 0.35,  # Some leaps
        "rest_probability": 0.3,  # Many pauses
        "rhythm_variety": 0.6,  # Varied rhythm
        "range_preference": "wide",
    },
}

RHYTHM_PATTERNS = {
    "steady": [4, 4, 4, 4],  # Quarter notes
    "varied": [4, 4, 2, 2, 4],  # Mixed
    "flowing": [2, 2, 2, 2, 4, 4],  # Eighth notes with quarters
    "syncopated": [2, 4, 2, 4, 2, 2],  # Syncopation
    "triplet": [3, 3, 3, 3],  # Triplets (approximate)
    "sparse": [4, 8, 4, 8],  # With rests
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def note_name_to_midi(note_name: str, octave: int = 4) -> int:
    """Convert note name (e.g., 'C#') to MIDI number"""
    try:
        note_index = NOTE_NAMES.index(note_name.upper())
        return note_index + (octave * 12) + 12  # MIDI C0 = 12
    except ValueError:
        print(f"⚠️  Unknown note name: {note_name}, using C")
        return 60  # Default to middle C

def midi_to_note_name(midi: int) -> str:
    """Convert MIDI number to note name with octave"""
    octave = (midi - 12) // 12
    note_index = (midi - 12) % 12
    return f"{NOTE_NAMES[note_index]}{octave}"

def get_scale_notes(root_note: str, scale_name: str, octave: int = 4, num_octaves: int = 2) -> List[int]:
    """Get all MIDI notes in a scale across multiple octaves"""
    if scale_name not in SCALES:
        print(f"⚠️  Unknown scale: {scale_name}, using Major")
        scale_name = "Major"
    
    root_midi = note_name_to_midi(root_note, octave)
    scale_intervals = SCALES[scale_name]
    
    notes = []
    for oct_offset in range(num_octaves):
        for interval in scale_intervals:
            notes.append(root_midi + interval + (oct_offset * 12))
    
    return sorted(notes)

def is_good_interval(interval: int, mood_profile: Dict) -> bool:
    """Check if interval fits the mood"""
    abs_interval = abs(interval) % 12
    preferred = mood_profile["preferred_intervals"]
    avoided = mood_profile["avoid_intervals"]
    
    if abs_interval in avoided:
        return False
    if abs_interval in preferred:
        return True
    return random.random() > 0.5  # 50% chance for neutral intervals

def apply_rhythm_pattern(melody_length: int, pattern_name: str) -> List[int]:
    """Generate rhythm durations based on pattern"""
    if pattern_name not in RHYTHM_PATTERNS:
        pattern_name = "varied"
    
    pattern = RHYTHM_PATTERNS[pattern_name]
    rhythm = []
    total_beats = 0
    target_beats = melody_length * 4  # Assuming 4/4 time
    
    while total_beats < target_beats:
        note_duration = random.choice(pattern)
        rhythm.append(note_duration)
        total_beats += note_duration
    
    return rhythm

# ============================================================================
# MELODY GENERATION
# ============================================================================

def generate_melody(
    scale_notes: List[int],
    mood: str,
    length: int = 16,
    rhythm_pattern: str = "varied"
) -> List[Tuple[int, int, int]]:  # (MIDI note, duration, velocity)
    """
    Generate a melody using musical rules and mood constraints
    
    Returns:
        List of (midi_note, duration_ticks, velocity) tuples
    """
    
    if mood not in MOOD_PROFILES:
        print(f"⚠️  Unknown mood: {mood}, using 'happy'")
        mood = "happy"
    
    mood_profile = MOOD_PROFILES[mood]
    
    # Generate rhythm
    rhythm = apply_rhythm_pattern(length, rhythm_pattern)
    
    # Initialize melody
    melody = []
    
    # Start on tonic (root note) or fifth
    current_note = scale_notes[0] if random.random() > 0.3 else scale_notes[4 % len(scale_notes)]
    
    for i, duration in enumerate(rhythm):
        # Add rest?
        if random.random() < mood_profile["rest_probability"]:
            melody.append((0, duration, 0))  # Rest (MIDI note 0)
            continue
        
        # Determine next note
        if i == 0:
            # First note
            next_note = current_note
        else:
            # Get possible next notes (stepwise and leaps)
            current_index = scale_notes.index(current_note) if current_note in scale_notes else 0
            
            # Leap or step?
            if random.random() < mood_profile["leap_probability"]:
                # Leap (3-7 scale degrees)
                leap_size = random.choice([3, 4, 5, 7])
                direction = 1 if random.random() < mood_profile["direction_bias"] else -1
                next_index = current_index + (leap_size * direction)
            else:
                # Step (1-2 scale degrees)
                step_size = random.choice([1, 2])
                direction = 1 if random.random() < mood_profile["direction_bias"] else -1
                next_index = current_index + (step_size * direction)
            
            # Wrap within scale range
            next_index = max(0, min(next_index, len(scale_notes) - 1))
            next_note = scale_notes[next_index]
            
            # Check interval validity
            interval = next_note - current_note
            attempts = 0
            while not is_good_interval(interval, mood_profile) and attempts < 5:
                # Try again with different note
                next_index = random.randint(max(0, current_index - 5), 
                                           min(len(scale_notes) - 1, current_index + 5))
                next_note = scale_notes[next_index]
                interval = next_note - current_note
                attempts += 1
        
        # Velocity (dynamics)
        if i == 0 or i == len(rhythm) - 1:
            velocity = random.randint(80, 100)  # Stronger on first/last
        else:
            velocity = random.randint(60, 90)
        
        melody.append((next_note, duration, velocity))
        current_note = next_note
    
    # End on tonic (resolve)
    if melody and melody[-1][0] != scale_notes[0]:
        melody[-1] = (scale_notes[0], melody[-1][1], 100)  # Strong ending
    
    return melody

# ============================================================================
# MIDI FILE GENERATION
# ============================================================================

def create_midi_file(
    melody: List[Tuple[int, int, int]],
    filename: str,
    bpm: int = 120
) -> bool:
    """Create MIDI file from melody"""
    
    if not MIDO_AVAILABLE:
        print("⚠️  Cannot create MIDI file (mido not installed)")
        return False
    
    try:
        mid = MidiFile()
        track = MidiTrack()
        mid.tracks.append(track)
        
        # Set tempo
        tempo = int(60000000 / bpm)  # microseconds per beat
        track.append(Message('program_change', program=0, time=0))  # Piano
        
        # Add notes
        ticks_per_beat = mid.ticks_per_beat
        current_time = 0
        
        for note, duration, velocity in melody:
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
# NOTATION DISPLAY
# ============================================================================

def display_melody_notation(melody: List[Tuple[int, int, int]], scale_name: str, root_note: str):
    """Display melody in text notation"""
    
    print(f"\n🎼 MELODY NOTATION")
    print(f"   Scale: {root_note} {scale_name}")
    print(f"   Length: {len([m for m in melody if m[0] != 0])} notes")
    print(f"\n   Notes (Note - Duration - Velocity):")
    print("   " + "-" * 50)
    
    for i, (note, duration, velocity) in enumerate(melody, 1):
        if note == 0:
            print(f"   {i:2d}. REST        - {duration:2d} ticks")
        else:
            note_name = midi_to_note_name(note)
            duration_name = {
                1: "16th", 2: "8th", 3: "8th triplet", 
                4: "Quarter", 8: "Half", 16: "Whole"
            }.get(duration, f"{duration} ticks")
            
            velocity_desc = "ff" if velocity > 90 else "f" if velocity > 75 else "mf" if velocity > 60 else "mp"
            
            print(f"   {i:2d}. {note_name:5s} (MIDI {note:3d}) - {duration_name:12s} - {velocity_desc}")

def display_melody_ascii(melody: List[Tuple[int, int, int]]):
    """Display melody as ASCII piano roll"""
    
    # Filter out rests
    notes = [(n, d) for n, d, v in melody if n != 0]
    if not notes:
        return
    
    min_note = min(n for n, d in notes)
    max_note = max(n for n, d in notes)
    
    print(f"\n🎹 PIANO ROLL (ASCII):")
    print("   " + "-" * 60)
    
    # Display each pitch row
    for pitch in range(max_note, min_note - 1, -1):
        note_name = midi_to_note_name(pitch)
        line = f"   {note_name:5s} |"
        
        for i, (note, duration) in enumerate(notes):
            if note == pitch:
                line += "█" * min(duration, 4)  # Limit visual length
            else:
                line += " " * min(duration, 4)
        
        print(line)
    
    print("   " + "-" * 60)

# ============================================================================
# MAIN FUNCTION
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Generate MIDI melodies based on scale and mood",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_melody.py "C Major" C happy
  python generate_melody.py "D Minor" D sad --length 16 --bpm 120
  python generate_melody.py "E Phrygian" E dark --octave 4 --rhythm syncopated
  
Available Scales:
  Major, Minor, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian
  Harmonic Minor, Melodic Minor, Major Pentatonic, Minor Pentatonic
  Blues, Whole Tone, Phrygian Dominant, Hungarian Minor, Japanese, Arabic
  
Available Moods:
  happy, sad, dark, energetic, calm, mysterious
  
Available Rhythms:
  steady, varied, flowing, syncopated, triplet, sparse
        """
    )
    
    parser.add_argument("scale", help="Scale name (e.g., 'C Major', 'D Minor')")
    parser.add_argument("root", help="Root note (C, C#, D, etc.)")
    parser.add_argument("mood", help="Mood (happy, sad, dark, energetic, calm, mysterious)")
    parser.add_argument("--length", type=int, default=16, help="Melody length in bars (default: 16)")
    parser.add_argument("--bpm", type=int, default=120, help="Tempo in BPM (default: 120)")
    parser.add_argument("--octave", type=int, default=4, help="Starting octave (default: 4)")
    parser.add_argument("--rhythm", default="varied", help="Rhythm pattern (default: varied)")
    parser.add_argument("--output", default=None, help="Output MIDI filename (default: auto-generated)")
    parser.add_argument("--no-ascii", action="store_true", help="Skip ASCII piano roll display")
    
    args = parser.parse_args()
    
    # Parse scale name
    scale_parts = args.scale.split()
    if len(scale_parts) > 1:
        scale_name = " ".join(scale_parts)
    else:
        scale_name = args.scale
    
    print(f"\n🎵 MELODY GENERATOR")
    print(f"   Scale: {args.root} {scale_name}")
    print(f"   Mood: {args.mood}")
    print(f"   Length: {args.length} bars")
    print(f"   BPM: {args.bpm}")
    print(f"   Rhythm: {args.rhythm}")
    
    # Get scale notes
    scale_notes = get_scale_notes(args.root, scale_name, args.octave, num_octaves=2)
    
    print(f"\n✅ Scale notes: {[midi_to_note_name(n) for n in scale_notes[:7]]}")
    
    # Generate melody
    print(f"\n🎼 Generating melody...")
    melody = generate_melody(scale_notes, args.mood, args.length, args.rhythm)
    
    # Display notation
    display_melody_notation(melody, scale_name, args.root)
    
    # Display ASCII piano roll
    if not args.no_ascii:
        display_melody_ascii(melody)
    
    # Create MIDI file
    if args.output:
        filename = args.output
    else:
        filename = f"melody_{args.root}_{scale_name.replace(' ', '_')}_{args.mood}_{args.bpm}bpm.mid"
    
    print(f"\n💾 Creating MIDI file: {filename}")
    
    if create_midi_file(melody, filename, args.bpm):
        print(f"✅ MIDI file created successfully!")
        print(f"   Location: {filename}")
    else:
        print(f"❌ Failed to create MIDI file")
    
    print(f"\n🎹 Melody generation complete!\n")

if __name__ == "__main__":
    main()