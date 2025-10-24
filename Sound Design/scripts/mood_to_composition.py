#!/usr/bin/env python3
"""
Mood to Composition Generator
Maps emotional/atmospheric keywords to musical suggestions:
- Scales and modes
- Root key recommendations  
- Chord progressions (3+ variations)
- Production tips
- Optional MIDI generation

REFACTORED: Now uses reference_parser.py to load data from MD files
"""

import sys
import random
from pathlib import Path
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

# Import reference parser
try:
    from reference_parser import ReferenceParser
except ImportError:
    # Fallback if not in same directory
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from reference_parser import ReferenceParser

# ============================================================
# LOAD DATA FROM REFERENCE FILES
# ============================================================

# Initialize parser (loads from ../references/)
parser = ReferenceParser()

# Load all reference data
SCALES = parser.get_scales()
CHORD_PROGRESSIONS = parser.get_chord_progressions()
PRODUCTION_TIPS = parser.get_production_tips()

# ============================================================
# MOOD DATABASE BUILDER
# ============================================================

def get_mood_data(mood_name: str) -> dict:
    """
    Build mood data from reference files
    
    Args:
        mood_name: Name of the mood (e.g., 'dark', 'happy')
        
    Returns:
        Dictionary with scales, progressions, tips, and keys for the mood
    """
    mood_lower = mood_name.lower()
    
    # Get scales suitable for this mood
    suitable_scales = []
    for scale_name, scale_data in SCALES.items():
        if mood_lower in scale_data.get('moods', []):
            suitable_scales.append(scale_data['full_name'])
    
    # Fallback: if no scales found, use common defaults
    if not suitable_scales:
        default_scales = {
            'dark': ['Phrygian', 'Locrian', 'Harmonic Minor'],
            'happy': ['Ionian', 'Lydian', 'Mixolydian'],
            'sad': ['Aeolian', 'Dorian', 'Phrygian'],
            'energetic': ['Mixolydian', 'Dorian', 'Ionian'],
            'calm': ['Ionian', 'Lydian'],
            'atmospheric': ['Lydian', 'Dorian', 'Aeolian'],
            'dreamy': ['Lydian', 'Ionian'],
            'mysterious': ['Locrian', 'Phrygian Dominant', 'Diminished']
        }
        suitable_scales = default_scales.get(mood_lower, ['Ionian'])
    
    # Get chord progressions for this mood
    progressions = CHORD_PROGRESSIONS.get(mood_lower, [])
    
    # Limit to top 3 progressions
    if len(progressions) > 3:
        progressions = progressions[:3]
    
    # Get production tips
    tips = PRODUCTION_TIPS.get(mood_lower, {})
    
    # Combine all tips into a single list
    all_tips = []
    if tips:
        for category in ['sound_design', 'arrangement', 'processing']:
            all_tips.extend(tips.get(category, []))
    
    # Recommended root keys by mood
    root_keys = {
        'dark': ['D', 'E', 'F#', 'C#', 'A'],
        'atmospheric': ['C', 'D', 'F', 'G', 'A'],
        'happy': ['C', 'G', 'D', 'F', 'A'],
        'sad': ['Am', 'Dm', 'Em', 'Bm', 'F#m'],
        'energetic': ['C', 'D', 'E', 'G', 'A'],
        'epic': ['Cm', 'Dm', 'Em', 'Am'],
        'dreamy': ['C', 'G', 'F', 'D', 'A'],
        'mysterious': ['C#', 'D#', 'F#', 'G#']
    }
    
    return {
        'scales': suitable_scales,
        'root_keys': root_keys.get(mood_lower, ['C', 'D', 'G', 'A']),
        'chord_progressions': progressions,
        'tips': all_tips[:4] if all_tips else []  # Top 4 tips
    }

# ============================================================
# NOTE/CHORD UTILITIES
# ============================================================

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def note_name_to_midi(note: str, octave: int = 4) -> int:
    """Convert note name to MIDI number"""
    note = note.upper().replace('B', 'A#')  # Handle flats
    if note not in NOTE_NAMES:
        # Try to extract just the note letter
        note_letter = note[0]
        if note_letter in NOTE_NAMES:
            note = note_letter
        else:
            return 60  # Default to C4
    
    note_index = NOTE_NAMES.index(note)
    return note_index + (octave * 12) + 12

def parse_roman_numeral(numeral: str, root_midi: int, is_minor: bool = True) -> list:
    """
    Parse Roman numeral chord to MIDI notes
    
    Args:
        numeral: Roman numeral (e.g., 'i', 'IV', 'bVII')
        root_midi: MIDI number of the root note
        is_minor: Whether we're in a minor key
        
    Returns:
        List of MIDI notes for the chord
    """
    # Scale intervals (semitones from root)
    if is_minor:
        scale = [0, 2, 3, 5, 7, 8, 10]  # Natural minor
    else:
        scale = [0, 2, 4, 5, 7, 9, 11]  # Major
    
    # Roman numeral to scale degree
    roman_map = {
        'I': 0, 'II': 1, 'III': 2, 'IV': 3, 'V': 4, 'VI': 5, 'VII': 6,
        'i': 0, 'ii': 1, 'iii': 2, 'iv': 3, 'v': 4, 'vi': 5, 'vii': 6
    }
    
    # Handle flat notation
    if numeral.startswith('b'):
        base_numeral = numeral[1:]
        degree = roman_map.get(base_numeral, 0)
        chord_root = root_midi + scale[degree] - 1  # Flat = -1 semitone
    else:
        degree = roman_map.get(numeral, 0)
        chord_root = root_midi + scale[degree]
    
    # Build triad (root, third, fifth)
    is_minor_chord = numeral.islower()
    if is_minor_chord:
        return [chord_root, chord_root + 3, chord_root + 7]  # Minor triad
    else:
        return [chord_root, chord_root + 4, chord_root + 7]  # Major triad

# ============================================================
# MIDI GENERATION
# ============================================================

def create_progression_midi(progression: dict, root_note: str, output_file: str, 
                            bpm: int = 120):
    """
    Create a MIDI file with the chord progression
    
    Args:
        progression: Progression dictionary with 'chords' list
        root_note: Root note (e.g., 'D', 'Am')
        output_file: Path to save MIDI file
        bpm: Tempo in beats per minute
    """
    # Determine if minor key
    is_minor = 'm' in root_note or root_note.lower() == root_note
    
    # Remove 'm' from note name for MIDI conversion
    clean_note = root_note.replace('m', '').replace('M', '')
    root_midi = note_name_to_midi(clean_note, octave=3)
    
    # Create MIDI file
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    
    # Set tempo
    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm)))
    
    # Add each chord
    ticks_per_beat = mid.ticks_per_beat
    chord_duration = ticks_per_beat * 4  # 4 beats per chord
    
    for chord_numeral in progression['chords']:
        # Parse chord
        chord_notes = parse_roman_numeral(chord_numeral, root_midi, is_minor)
        
        # Note on
        for note in chord_notes:
            track.append(Message('note_on', note=note, velocity=80, time=0))
        
        # Note off (after duration)
        for i, note in enumerate(chord_notes):
            time = chord_duration if i == 0 else 0
            track.append(Message('note_off', note=note, velocity=0, time=time))
    
    # Save MIDI file
    mid.save(output_file)
    print(f"💾 MIDI file saved: {output_file}")

# ============================================================
# MAIN INTERFACE
# ============================================================

def display_mood_suggestions(mood: str, root_key: str = None, 
                             generate_midi: bool = False):
    """
    Display composition suggestions for a given mood
    
    Args:
        mood: Mood name (e.g., 'dark', 'happy')
        root_key: Optional root key (e.g., 'D', 'Am')
        generate_midi: Whether to generate MIDI files
    """
    print("=" * 70)
    print(f"🎵 MOOD TO COMPOSITION: {mood.upper()}")
    print("=" * 70)
    
    # Get mood data
    mood_data = get_mood_data(mood)
    
    if not mood_data['scales'] and not mood_data['chord_progressions']:
        print(f"\n❌ Mood '{mood}' not found in database.")
        print(f"Available moods: {', '.join(CHORD_PROGRESSIONS.keys())}")
        return
    
    # Select or suggest root key
    if not root_key:
        root_key = random.choice(mood_data['root_keys'])
        print(f"\n🎹 Suggested Root Key: {root_key}")
    else:
        print(f"\n🎹 Root Key: {root_key}")
    
    # Display scales
    print(f"\n📊 RECOMMENDED SCALES:")
    for i, scale in enumerate(mood_data['scales'], 1):
        print(f"   {i}. {scale}")
    
    # Display chord progressions
    if mood_data['chord_progressions']:
        print(f"\n🎼 CHORD PROGRESSIONS:")
        for i, prog in enumerate(mood_data['chord_progressions'], 1):
            print(f"\n   {i}. {prog.get('name', 'Progression ' + str(i))}")
            print(f"      Chords: {' - '.join(prog['chords'])}")
            if 'example' in prog:
                print(f"      Example: {prog['example']}")
            print(f"      Feel: {prog.get('feel', 'N/A')}")
            
            # Generate MIDI if requested
            if generate_midi:
                filename = f"progression_{i}_{mood}_{root_key}.mid"
                create_progression_midi(prog, root_key, filename)
    
    # Display production tips
    if mood_data['tips']:
        print(f"\n💡 PRODUCTION TIPS:")
        for i, tip in enumerate(mood_data['tips'], 1):
            print(f"   {i}. {tip}")
    
    print("\n" + "=" * 70)

# ============================================================
# CLI INTERFACE
# ============================================================

def main():
    """Main CLI interface"""
    if len(sys.argv) < 2:
        print("Usage: python mood_to_composition.py <mood> [root_key] [--midi]")
        print("\nAvailable moods:")
        for mood in sorted(CHORD_PROGRESSIONS.keys()):
            print(f"  - {mood}")
        print("\nExample: python mood_to_composition.py dark D --midi")
        sys.exit(1)
    
    mood = sys.argv[1].lower()
    root_key = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].startswith('--') else None
    generate_midi = '--midi' in sys.argv
    
    display_mood_suggestions(mood, root_key, generate_midi)

if __name__ == "__main__":
    main()
