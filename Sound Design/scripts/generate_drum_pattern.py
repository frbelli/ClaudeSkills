#!/usr/bin/env python3
"""
Drum Pattern Generator
Generates drum patterns based on:
- Genre
- Mood/Energy level
- Complexity
- BPM

Uses reference database for genre-specific patterns.
Outputs MIDI files with generated drum patterns.

Usage:
    python generate_drum_pattern.py --genre techno --energy high --bars 8
    python generate_drum_pattern.py --genre house --mood happy --complexity medium
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

GENRES = parser.get_genre_styles()
MOOD_PROFILES = parser.get_mood_profiles()

# ============================================================================
# DRUM MAPPING (GM Standard)
# ============================================================================

DRUM_MAP = {
    'kick': 36,
    'snare': 38,
    'clap': 39,
    'rim': 37,
    'closed_hat': 42,
    'open_hat': 46,
    'crash': 49,
    'ride': 51,
    'tom_low': 45,
    'tom_mid': 47,
    'tom_high': 50,
    'perc_high': 56,  # Cowbell
    'perc_low': 54,   # Tambourine
    'shaker': 82,
}

# ============================================================================
# GENRE-SPECIFIC PATTERNS
# ============================================================================

GENRE_PATTERNS = {
    'techno': {
        'bpm_range': (125, 145),
        'time_signature': '4/4',
        'kick_pattern': [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # 4-on-floor
        'snare_pattern': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 2 and 4
        'hat_pattern': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],    # Eighth notes
        'open_hat_pattern': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # Sparse
        'perc_pattern': [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],   # Syncopated
        'complexity_modifiers': {
            'low': 0.5,
            'medium': 1.0,
            'high': 1.5
        }
    },
    
    'house': {
        'bpm_range': (120, 130),
        'time_signature': '4/4',
        'kick_pattern': [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # 4-on-floor
        'snare_pattern': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 2 and 4
        'clap_pattern': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],   # With snare
        'hat_pattern': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],    # Straight 8ths
        'open_hat_pattern': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],  # Offbeat
        'shaker_pattern': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # 16ths
        'complexity_modifiers': {
            'low': 0.5,
            'medium': 1.0,
            'high': 1.3
        }
    },
    
    'dubstep': {
        'bpm_range': (138, 142),
        'time_signature': '4/4',
        'kick_pattern': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # Sparse, syncopated
        'snare_pattern': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # Half-time feel
        'rim_pattern': [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],    # Syncopated
        'hat_pattern': [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0],    # Skippy
        'perc_pattern': [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],   # Complex
        'complexity_modifiers': {
            'low': 0.7,
            'medium': 1.0,
            'high': 1.4
        }
    },
    
    'dnb': {
        'bpm_range': (170, 180),
        'time_signature': '4/4',
        'kick_pattern': [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Syncopated
        'snare_pattern': [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],  # Fast breaks
        'hat_pattern': [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0],    # Fast, skippy
        'ride_pattern': [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],   # Quarter notes
        'perc_pattern': [0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],   # 16th rolls
        'complexity_modifiers': {
            'low': 0.6,
            'medium': 1.0,
            'high': 1.6
        }
    },
    
    'trap': {
        'bpm_range': (130, 170),
        'time_signature': '4/4',
        'kick_pattern': [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # Syncopated
        'snare_pattern': [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 2 and 4
        'rim_pattern': [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],    # 16th rolls
        'hat_pattern': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],    # Constant 16ths
        'open_hat_pattern': [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],  # Triplet feel
        'perc_pattern': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],   # Sparse snaps
        'complexity_modifiers': {
            'low': 0.5,
            'medium': 1.0,
            'high': 1.8
        }
    },
    
    'ambient': {
        'bpm_range': (60, 100),
        'time_signature': '4/4',
        'kick_pattern': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Very sparse
        'perc_high_pattern': [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # Minimal
        'shaker_pattern': [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],  # Gentle
        'rim_pattern': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],    # Very sparse
        'complexity_modifiers': {
            'low': 0.3,
            'medium': 0.5,
            'high': 0.8
        }
    },
}

# ============================================================================
# PATTERN GENERATION
# ============================================================================

def apply_velocity_variation(pattern: List[int], variation: float = 0.2) -> List[Tuple[int, int]]:
    """
    Apply velocity variation to pattern
    
    Args:
        pattern: List of 0s and 1s
        variation: Amount of velocity variation (0.0-1.0)
    
    Returns:
        List of (hit, velocity) tuples
    """
    result = []
    base_velocity = 100
    
    for hit in pattern:
        if hit == 1:
            # Add random variation
            vel_variation = int(base_velocity * variation * random.uniform(-1, 1))
            velocity = max(60, min(127, base_velocity + vel_variation))
            result.append((1, velocity))
        else:
            result.append((0, 0))
    
    return result

def apply_swing(pattern: List[int], swing_amount: float = 0.1) -> List[Tuple[int, int]]:
    """
    Apply swing timing to pattern
    
    Args:
        pattern: List of hits
        swing_amount: Amount of swing (0.0-0.3)
    
    Returns:
        List of (hit, timing_offset) tuples
    """
    result = []
    
    for i, hit in enumerate(pattern):
        if i % 2 == 1:  # Off-beat
            timing_offset = int(swing_amount * 50)  # Delay in ticks
        else:
            timing_offset = 0
        
        result.append((hit, timing_offset))
    
    return result

def apply_humanization(pattern: List[int], amount: float = 0.05) -> List[Tuple[int, int]]:
    """
    Apply timing humanization to pattern
    
    Args:
        pattern: List of hits
        amount: Amount of humanization (0.0-0.2)
    
    Returns:
        List of (hit, timing_offset) tuples
    """
    result = []
    
    for hit in pattern:
        if hit == 1:
            # Random timing offset
            offset = int(random.uniform(-1, 1) * amount * 30)
            result.append((hit, offset))
        else:
            result.append((hit, 0))
    
    return result

def modify_pattern_complexity(pattern: List[int], complexity: str, genre: str) -> List[int]:
    """
    Modify pattern based on complexity level
    
    Args:
        pattern: Original pattern
        complexity: 'low', 'medium', 'high'
        genre: Genre name
    
    Returns:
        Modified pattern
    """
    if complexity == 'low':
        # Simplify: remove some hits
        return [hit if random.random() > 0.3 else 0 for hit in pattern]
    
    elif complexity == 'high':
        # Add fills and variations
        modified = pattern.copy()
        # Add ghost notes (every 4th hit has a chance)
        for i in range(len(modified)):
            if i % 4 == 3 and modified[i] == 0:
                if random.random() < 0.3:
                    modified[i] = 1
        return modified
    
    else:  # medium
        return pattern

def get_energy_from_mood(mood: str) -> str:
    """Map mood to energy level"""
    energy_map = {
        'dark': 'medium',
        'happy': 'high',
        'sad': 'low',
        'energetic': 'high',
        'calm': 'low',
        'atmospheric': 'low',
        'mysterious': 'medium',
        'epic': 'high',
    }
    return energy_map.get(mood.lower(), 'medium')

def generate_drum_midi(
    genre: str,
    energy: str = 'medium',
    complexity: str = 'medium',
    bars: int = 8,
    bpm: int = None,
    output_file: str = 'drums.mid',
    humanize: bool = True,
    swing: float = 0.0
) -> str:
    """
    Generate drum pattern MIDI file
    
    Args:
        genre: Genre name
        energy: Energy level ('low', 'medium', 'high')
        complexity: Pattern complexity
        bars: Number of bars
        bpm: Tempo (None = auto from genre)
        output_file: Output filename
        humanize: Apply humanization
        swing: Swing amount (0.0-0.3)
    
    Returns:
        Path to generated file
    """
    # Get genre pattern
    genre_lower = genre.lower()
    genre_pattern = None
    
    for key in GENRE_PATTERNS:
        if key in genre_lower:
            genre_pattern = GENRE_PATTERNS[key]
            break
    
    if not genre_pattern:
        # Default to house
        genre_pattern = GENRE_PATTERNS['house']
    
    # Get BPM
    if bpm is None:
        bpm_min, bpm_max = genre_pattern['bpm_range']
        bpm = random.randint(bpm_min, bpm_max)
    
    # Create MIDI file
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)
    
    # Set tempo and track name
    track.append(MetaMessage('set_tempo', tempo=bpm2tempo(bpm)))
    track.append(MetaMessage('track_name', name=f'{genre.title()} Drums - {energy.title()} Energy'))
    
    # Calculate timing
    ticks_per_beat = mid.ticks_per_beat
    sixteenth_note = ticks_per_beat // 4
    
    # Get patterns for each drum element
    patterns = {}
    for drum_name, drum_midi in DRUM_MAP.items():
        pattern_key = f'{drum_name}_pattern'
        if pattern_key in genre_pattern:
            base_pattern = genre_pattern[pattern_key]
            # Modify based on complexity
            modified_pattern = modify_pattern_complexity(base_pattern, complexity, genre)
            patterns[drum_name] = modified_pattern
    
    # Generate pattern for specified number of bars
    pattern_length = 16  # 16th notes per bar
    total_steps = pattern_length * bars
    
    # Generate MIDI events
    for bar in range(bars):
        for step in range(pattern_length):
            current_step = bar * pattern_length + step
            time_offset = 0
            
            # Check each drum element
            for drum_name, pattern in patterns.items():
                if pattern[step] == 1:
                    drum_note = DRUM_MAP[drum_name]
                    
                    # Velocity based on energy
                    if energy == 'low':
                        velocity = random.randint(60, 85)
                    elif energy == 'high':
                        velocity = random.randint(95, 120)
                    else:  # medium
                        velocity = random.randint(80, 105)
                    
                    # Apply humanization
                    if humanize:
                        time_offset = random.randint(-5, 5)
                        velocity += random.randint(-10, 10)
                    
                    # Apply swing (only on off-beats)
                    if swing > 0 and step % 2 == 1:
                        time_offset += int(swing * sixteenth_note)
                    
                    # Clamp velocity
                    velocity = max(40, min(127, velocity))
                    
                    # Add note
                    track.append(Message('note_on', note=drum_note, velocity=velocity, 
                                       time=sixteenth_note + time_offset if step == 0 and bar == 0 else 0))
                    track.append(Message('note_off', note=drum_note, velocity=0, 
                                       time=sixteenth_note // 4))  # Short notes
            
            # Move time forward for next step
            if step < pattern_length - 1 or bar < bars - 1:
                track.append(Message('note_on', note=DRUM_MAP['kick'], velocity=0, 
                                   time=sixteenth_note - (sixteenth_note // 4)))
    
    # Save file
    mid.save(output_file)
    return output_file

# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    """Main CLI interface"""
    parser_cli = argparse.ArgumentParser(
        description='Generate drum patterns based on genre, mood, and energy',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_drum_pattern.py --genre techno --energy high --bars 8
  python generate_drum_pattern.py --genre house --mood happy --complexity medium
  python generate_drum_pattern.py --genre dubstep --energy medium --bpm 140 --swing 0.1
  python generate_drum_pattern.py --genre trap --complexity high --bars 16
  
Available genres: techno, house, dubstep, dnb, trap, ambient
Energy levels: low, medium, high
Complexity: low, medium, high
        """
    )
    
    parser_cli.add_argument('--genre', type=str, required=True,
                           help='Genre (techno, house, dubstep, dnb, trap, ambient)')
    parser_cli.add_argument('--mood', type=str, default=None,
                           help='Mood (overrides energy if specified)')
    parser_cli.add_argument('--energy', type=str, default='medium',
                           choices=['low', 'medium', 'high'],
                           help='Energy level [default: medium]')
    parser_cli.add_argument('--complexity', type=str, default='medium',
                           choices=['low', 'medium', 'high'],
                           help='Pattern complexity [default: medium]')
    parser_cli.add_argument('--bars', type=int, default=8,
                           help='Number of bars [default: 8]')
    parser_cli.add_argument('--bpm', type=int, default=None,
                           help='Tempo in BPM [default: auto from genre]')
    parser_cli.add_argument('--swing', type=float, default=0.0,
                           help='Swing amount 0.0-0.3 [default: 0.0]')
    parser_cli.add_argument('--humanize', action='store_true',
                           help='Apply timing humanization')
    parser_cli.add_argument('--output', type=str, default=None,
                           help='Output filename [default: auto-generated]')
    
    args = parser_cli.parse_args()
    
    # Determine energy from mood if specified
    if args.mood:
        energy = get_energy_from_mood(args.mood)
        print(f"🎭 Mood '{args.mood}' → Energy level: {energy}")
    else:
        energy = args.energy
    
    print("=" * 70)
    print("🥁 DRUM PATTERN GENERATOR")
    print("=" * 70)
    
    # Get genre pattern info
    genre_lower = args.genre.lower()
    genre_info = None
    for key in GENRE_PATTERNS:
        if key in genre_lower:
            genre_info = GENRE_PATTERNS[key]
            break
    
    if not genre_info:
        print(f"⚠️  Genre '{args.genre}' not found, using House as default")
        genre_info = GENRE_PATTERNS['house']
    
    # Determine BPM
    if args.bpm:
        bpm = args.bpm
    else:
        bpm_min, bpm_max = genre_info['bpm_range']
        bpm = (bpm_min + bpm_max) // 2  # Use middle of range
    
    print(f"\n📊 PARAMETERS:")
    print(f"   Genre: {args.genre.title()}")
    print(f"   Energy: {energy.title()}")
    print(f"   Complexity: {args.complexity.title()}")
    print(f"   Bars: {args.bars}")
    print(f"   BPM: {bpm}")
    print(f"   Time Sig: {genre_info['time_signature']}")
    if args.swing > 0:
        print(f"   Swing: {args.swing:.1%}")
    if args.humanize:
        print(f"   Humanization: Enabled")
    
    print(f"\n🎵 DRUM ELEMENTS:")
    element_count = 0
    for key in genre_info.keys():
        if key.endswith('_pattern'):
            element_name = key.replace('_pattern', '').replace('_', ' ').title()
            print(f"   - {element_name}")
            element_count += 1
    
    # Generate output filename
    if args.output:
        output_file = args.output
    else:
        output_file = f"drums_{args.genre}_{energy}_{args.complexity}.mid"
    
    # Generate MIDI
    print(f"\n🎵 Generating drum pattern...")
    generated_file = generate_drum_midi(
        args.genre,
        energy,
        args.complexity,
        args.bars,
        bpm,
        output_file,
        args.humanize,
        args.swing
    )
    
    print(f"✅ Generated: {generated_file}")
    print("\n" + "=" * 70)
    print("💡 TIPS:")
    print("   - Import into your DAW on a drum rack/sampler")
    print("   - Adjust velocities for more dynamics")
    print("   - Layer with your own samples")
    print("   - Try different complexity levels for variations")
    print("=" * 70)

if __name__ == "__main__":
    main()
