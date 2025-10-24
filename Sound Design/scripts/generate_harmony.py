#!/usr/bin/env python3
"""
Harmony Generator
Generates chord progressions and harmonic content based on:
- Mood
- Genre
- Scale
- Root key

Uses reference database for intelligent suggestions.
Outputs MIDI files with generated harmonies.

Usage:
    python generate_harmony.py --mood dark --genre techno --key Dm --bars 8
    python generate_harmony.py --mood happy --genre house --key C --scale lydian
"""

import sys
import os
import random
import argparse
from typing import List, Dict, Tuple
from mido import MidiFile, MidiTrack, Message, MetaMessage, bpm2tempo

# Import reference parser
try:
    from reference_parser import ReferenceParser
except ImportError:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from reference_parser import ReferenceParser

# ============================================================================
# LOAD REFERENCE DATA
# ============================================================================

parser = ReferenceParser()

SCALES = parser.get_scales()
CHORD_PROGRESSIONS = parser.get_chord_progressions()
GENRES = parser.get_genre_styles()
MOOD_PROFILES = parser.get_mood_profiles()

# ============================================================================
# MUSIC THEORY UTILITIES
# ============================================================================

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def note_to_midi(note_name: str, octave: int = 4) -> int:
    """Convert note name to MIDI number"""
    note_name = note_name.upper().replace('M', '')  # Remove 'm' from minor keys
    base_note = note_name[0]
    
    # Handle sharps/flats
    modifier = 0
    if len(note_name) > 1:
        if '#' in note_name or 's' in note_name.lower():
            modifier = 1
        elif 'b' in note_name.lower():
            modifier = -1
    
    if base_note not in NOTE_NAMES:
        base_note = 'C'
    
    note_index = NOTE_NAMES.index(base_note)
    return (note_index + modifier) + (octave * 12) + 12

def get_scale_notes(root: int, scale_pattern: List[int]) -> List[int]:
    """Get MIDI notes for a scale"""
    return [root + interval for interval in scale_pattern]

def build_chord(root: int, chord_type: str = 'minor', extensions: List[str] = None) -> List[int]:
    """
    Build a chord from root note
    
    Args:
        root: Root MIDI note
        chord_type: 'major', 'minor', 'diminished', 'augmented', etc.
        extensions: List of extensions like '7', '9', 'sus4'
    
    Returns:
        List of MIDI notes for the chord
    """
    # Basic triads
    chord_intervals = {
        'major': [0, 4, 7],
        'minor': [0, 3, 7],
        'diminished': [0, 3, 6],
        'augmented': [0, 4, 8],
        'sus2': [0, 2, 7],
        'sus4': [0, 5, 7],
    }
    
    # Get base chord
    intervals = chord_intervals.get(chord_type, [0, 3, 7])  # Default to minor
    notes = [root + i for i in intervals]
    
    # Add extensions
    if extensions:
        for ext in extensions:
            if ext == '7':
                # Minor 7th for minor, major 7th for major
                seventh = 10 if chord_type == 'minor' else 11
                notes.append(root + seventh)
            elif ext == '9':
                notes.append(root + 14)  # Major 9th
            elif ext == 'maj7':
                notes.append(root + 11)
    
    return notes

def roman_to_chord(numeral: str, scale_notes: List[int], is_minor_key: bool = True) -> Tuple[int, str]:
    """
    Convert Roman numeral to chord root and type
    
    Args:
        numeral: Roman numeral (e.g., 'i', 'IV', 'bVII')
        scale_notes: MIDI notes of the scale
        is_minor_key: Whether we're in a minor key
    
    Returns:
        (root_note, chord_type)
    """
    # Map Roman numerals to scale degrees
    roman_map = {
        'I': 0, 'II': 1, 'III': 2, 'IV': 3, 'V': 4, 'VI': 5, 'VII': 6,
        'i': 0, 'ii': 1, 'iii': 2, 'iv': 3, 'v': 4, 'vi': 5, 'vii': 6
    }
    
    # Handle flat notation
    if numeral.startswith('b'):
        base = numeral[1:]
        degree = roman_map.get(base, 0)
        root = scale_notes[degree] - 1  # Flat
    else:
        degree = roman_map.get(numeral, 0)
        root = scale_notes[degree]
    
    # Determine chord type
    is_minor_chord = numeral.islower()
    chord_type = 'minor' if is_minor_chord else 'major'
    
    # Special cases
    if numeral.lower() == 'vii' or numeral.lower() == 'viio':
        chord_type = 'diminished'
    
    return root, chord_type

# ============================================================================
# HARMONY GENERATION
# ============================================================================

def get_genre_characteristics(genre: str) -> Dict:
    """Get harmonic characteristics for a genre"""
    genre_lower = genre.lower()
    
    # Genre-specific harmonic characteristics
    characteristics = {
        'techno': {
            'chord_density': 'low',  # Sparse chords
            'voicing': 'wide',       # Wide voicings
            'extensions': ['7'],     # Minor 7ths
            'rhythm': 'sustained',   # Long chords
            'complexity': 'simple',
        },
        'house': {
            'chord_density': 'medium',
            'voicing': 'medium',
            'extensions': ['7', '9'],
            'rhythm': 'syncopated',
            'complexity': 'medium',
        },
        'trance': {
            'chord_density': 'high',
            'voicing': 'wide',
            'extensions': ['7', '9', 'maj7'],
            'rhythm': 'sustained',
            'complexity': 'medium',
        },
        'dubstep': {
            'chord_density': 'low',
            'voicing': 'wide',
            'extensions': [],
            'rhythm': 'sparse',
            'complexity': 'simple',
        },
        'ambient': {
            'chord_density': 'low',
            'voicing': 'wide',
            'extensions': ['7', '9', 'maj7'],
            'rhythm': 'very_sustained',
            'complexity': 'complex',
        },
        'dnb': {
            'chord_density': 'medium',
            'voicing': 'tight',
            'extensions': ['7'],
            'rhythm': 'sustained',
            'complexity': 'medium',
        },
    }
    
    # Check for matching genre
    for key in characteristics:
        if key in genre_lower:
            return characteristics[key]
    
    # Default
    return characteristics['house']

def apply_voicing(chord_notes: List[int], voicing_type: str = 'medium') -> List[int]:
    """
    Apply voicing to chord notes
    
    Args:
        chord_notes: Base chord notes
        voicing_type: 'tight', 'medium', 'wide'
    
    Returns:
        Voiced chord notes
    """
    if voicing_type == 'tight':
        # Keep all notes in same octave
        return chord_notes
    
    elif voicing_type == 'wide':
        # Spread notes across octaves
        voiced = []
        for i, note in enumerate(chord_notes):
            octave_shift = i * 12  # Each note up one octave
            voiced.append(note + octave_shift)
        return voiced
    
    else:  # medium
        # Moderate spreading
        voiced = []
        for i, note in enumerate(chord_notes):
            if i > 0 and i % 2 == 0:
                voiced.append(note + 12)  # Every other note up octave
            else:
                voiced.append(note)
        return voiced

def generate_progression_midi(
    progression: List[str],
    root_key: str,
    scale_name: str,
    genre: str,
    mood: str,
    bars: int = 8,
    bpm: int = 120,
    output_file: str = 'harmony.mid'
) -> str:
    """
    Generate MIDI file with chord progression
    
    Args:
        progression: List of Roman numerals
        root_key: Root key (e.g., 'C', 'Dm')
        scale_name: Scale name
        genre: Genre name
        mood: Mood name
        bars: Number of bars
        bpm: Tempo
        output_file: Output filename
    
    Returns:
        Path to generated MIDI file
    """
    # Determine if minor key
    is_minor = 'm' in root_key.lower() or root_key.islower()
    
    # Get root note
    clean_key = root_key.replace('m', '').replace('M', '')
    root_midi = note_to_midi(clean_key, octave=3)
    
    # Get scale pattern
    scale_pattern = None
    for scale_key, scale_data in SCALES.items():
        if scale_name.lower() in scale_key.lower():
            scale_pattern = scale_data.get('pattern', [])
            break
    
    if not scale_pattern:
        # Default to natural minor or major
        scale_pattern = [0, 2, 3, 5, 7, 8, 10] if is_minor else [0, 2, 4, 5, 7, 9, 11]
    
    scale_notes = get_scale_notes(root_midi, scale_pattern)
    
    # Get genre characteristics
    genre_char = get_genre_characteristics(genre)
    
    # Create MIDI file
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    
    # Set tempo
    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm)))
    track.append(MetaMessage('track_name', name=f'{mood.title()} {genre.title()} - {root_key} {scale_name}'))
    
    # Calculate timing
    ticks_per_beat = mid.ticks_per_beat
    beats_per_bar = 4
    beats_per_chord = 4  # One chord per bar
    
    # Adjust chord duration based on genre rhythm
    if genre_char['rhythm'] == 'very_sustained':
        beats_per_chord = 8  # Two bars per chord
    elif genre_char['rhythm'] == 'sparse':
        beats_per_chord = 4
    elif genre_char['rhythm'] == 'syncopated':
        beats_per_chord = 2  # Half bar per chord
    
    chord_duration = ticks_per_beat * beats_per_chord
    
    # Generate chords
    total_chords_needed = bars // (beats_per_chord // beats_per_bar)
    if total_chords_needed == 0:
        total_chords_needed = bars
    
    # Loop progression to fill bars
    extended_progression = progression * (total_chords_needed // len(progression) + 1)
    extended_progression = extended_progression[:total_chords_needed]
    
    for chord_numeral in extended_progression:
        # Get chord root and type
        chord_root, chord_type = roman_to_chord(chord_numeral, scale_notes, is_minor)
        
        # Build chord with extensions
        extensions = genre_char.get('extensions', [])
        chord_notes = build_chord(chord_root, chord_type, extensions)
        
        # Apply voicing
        voiced_notes = apply_voicing(chord_notes, genre_char['voicing'])
        
        # Add to MIDI
        for note in voiced_notes:
            track.append(Message('note_on', note=note, velocity=80, time=0))
        
        for i, note in enumerate(voiced_notes):
            time = chord_duration if i == 0 else 0
            track.append(Message('note_off', note=note, velocity=0, time=time))
    
    # Save file
    mid.save(output_file)
    return output_file

def suggest_progression(mood: str, genre: str) -> Dict:
    """
    Suggest chord progression based on mood and genre
    
    Returns:
        Dict with progression and metadata
    """
    # Get progressions for mood
    mood_progs = CHORD_PROGRESSIONS.get(mood.lower(), [])
    
    if not mood_progs:
        # Fallback to common progressions
        mood_progs = [
            {
                'name': 'Classic Minor',
                'chords': ['i', 'bVII', 'bVI', 'bVII'],
                'feel': 'Versatile, works for most genres'
            }
        ]
    
    # Pick a progression (prefer first one, which is usually most characteristic)
    progression = mood_progs[0] if mood_progs else {
        'chords': ['i', 'bVII', 'bVI', 'bVII'],
        'name': 'Default'
    }
    
    return progression

# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    """Main CLI interface"""
    parser_cli = argparse.ArgumentParser(
        description='Generate harmonic progressions based on mood, genre, and scale',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_harmony.py --mood dark --genre techno --key Dm
  python generate_harmony.py --mood happy --genre house --key C --scale lydian --bars 16
  python generate_harmony.py --mood atmospheric --genre ambient --key F --bpm 90
  
Available moods: dark, happy, sad, energetic, calm, atmospheric, mysterious
Available genres: techno, house, trance, dubstep, ambient, dnb
        """
    )
    
    parser_cli.add_argument('--mood', type=str, required=True,
                           help='Mood (e.g., dark, happy, sad)')
    parser_cli.add_argument('--genre', type=str, required=True,
                           help='Genre (e.g., techno, house, ambient)')
    parser_cli.add_argument('--key', type=str, default='Am',
                           help='Root key (e.g., C, Dm, F#) [default: Am]')
    parser_cli.add_argument('--scale', type=str, default=None,
                           help='Scale name (e.g., aeolian, phrygian) [default: auto]')
    parser_cli.add_argument('--bars', type=int, default=8,
                           help='Number of bars [default: 8]')
    parser_cli.add_argument('--bpm', type=int, default=120,
                           help='Tempo in BPM [default: 120]')
    parser_cli.add_argument('--output', type=str, default=None,
                           help='Output filename [default: auto-generated]')
    parser_cli.add_argument('--progression', type=str, default=None,
                           help='Custom progression (e.g., "i-bVII-bVI-V") [default: auto]')
    
    args = parser_cli.parse_args()
    
    print("=" * 70)
    print("🎹 HARMONY GENERATOR")
    print("=" * 70)
    
    # Get progression
    if args.progression:
        # Parse custom progression
        chords = args.progression.split('-')
        progression = {
            'chords': chords,
            'name': 'Custom',
            'feel': 'User-defined'
        }
    else:
        # Suggest based on mood/genre
        progression = suggest_progression(args.mood, args.genre)
    
    print(f"\n📊 PARAMETERS:")
    print(f"   Mood: {args.mood}")
    print(f"   Genre: {args.genre}")
    print(f"   Key: {args.key}")
    print(f"   Bars: {args.bars}")
    print(f"   BPM: {args.bpm}")
    
    # Determine scale
    if args.scale:
        scale_name = args.scale
    else:
        # Auto-select scale based on mood
        mood_scales = {
            'dark': 'Phrygian',
            'happy': 'Ionian',
            'sad': 'Aeolian',
            'energetic': 'Mixolydian',
            'calm': 'Lydian',
            'atmospheric': 'Dorian',
            'mysterious': 'Locrian'
        }
        scale_name = mood_scales.get(args.mood.lower(), 'Aeolian')
    
    print(f"   Scale: {scale_name}")
    
    print(f"\n🎼 PROGRESSION: {progression['name']}")
    print(f"   Chords: {' - '.join(progression['chords'])}")
    print(f"   Feel: {progression.get('feel', 'N/A')}")
    
    # Generate output filename
    if args.output:
        output_file = args.output
    else:
        output_file = f"harmony_{args.mood}_{args.genre}_{args.key}.mid"
    
    # Get genre characteristics
    genre_char = get_genre_characteristics(args.genre)
    print(f"\n🎛️  GENRE CHARACTERISTICS:")
    print(f"   Density: {genre_char['chord_density']}")
    print(f"   Voicing: {genre_char['voicing']}")
    print(f"   Extensions: {', '.join(genre_char['extensions']) if genre_char['extensions'] else 'none'}")
    print(f"   Rhythm: {genre_char['rhythm']}")
    
    # Generate MIDI
    print(f"\n🎵 Generating MIDI file...")
    generated_file = generate_progression_midi(
        progression['chords'],
        args.key,
        scale_name,
        args.genre,
        args.mood,
        args.bars,
        args.bpm,
        output_file
    )
    
    print(f"✅ Generated: {generated_file}")
    print("\n" + "=" * 70)
    print("💡 TIP: Import this MIDI into your DAW and assign it to a pad/chord synth!")
    print("=" * 70)

if __name__ == "__main__":
    main()
