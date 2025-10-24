#!/usr/bin/env python3
"""
Harmonic Analysis Tool
Analyzes MIDI files to detect:
- Key (root note and major/minor)
- Scale/Mode
- Chord progression
- Suggestions for variations and improvements

REFACTORED: Now uses reference_parser.py to load scales and chord types
"""

import sys
import mido
from collections import Counter, defaultdict
from mido import MidiFile
import os

# Import reference parser
try:
    from reference_parser import ReferenceParser
except ImportError:
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from reference_parser import ReferenceParser

# ============================================================
# LOAD DATA FROM REFERENCE FILES
# ============================================================

# Initialize parser
parser = ReferenceParser()

# Load scales from MD files
SCALES_DATA = parser.get_scales()

# Convert to format needed by analysis algorithm
SCALES = {}
for scale_name, scale_data in SCALES_DATA.items():
    full_name = scale_data.get('full_name', scale_name)
    pattern = scale_data.get('pattern', [])
    SCALES[full_name] = pattern

# Add some common scales if missing
if 'Blues' not in SCALES:
    SCALES['Blues'] = [0, 3, 5, 6, 7, 10]
if 'Minor Pentatonic' not in SCALES:
    SCALES['Minor Pentatonic'] = [0, 3, 5, 7, 10]
if 'Major Pentatonic' not in SCALES:
    SCALES['Major Pentatonic'] = [0, 2, 4, 7, 9]
if 'Whole Tone' not in SCALES:
    SCALES['Whole Tone'] = [0, 2, 4, 6, 8, 10]

# Load chord types
CHORD_TYPES = parser.get_chord_types()
if not CHORD_TYPES or len(CHORD_TYPES) < 5:
    CHORD_TYPES = {
        'major': [0, 4, 7],
        'minor': [0, 3, 7],
        'diminished': [0, 3, 6],
        'augmented': [0, 4, 8],
        'sus2': [0, 2, 7],
        'sus4': [0, 5, 7],
        'maj7': [0, 4, 7, 11],
        'min7': [0, 3, 7, 10],
        'dom7': [0, 4, 7, 10],
    }

# ============================================================
# CONSTANTS
# ============================================================

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
MAJOR_PROFILE = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
MINOR_PROFILE = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def normalize_pitch_class(midi_note):
    return midi_note % 12

def get_note_name(pitch_class):
    return NOTE_NAMES[pitch_class % 12]

def extract_notes_from_midi(midi_file):
    notes = []
    try:
        mid = MidiFile(midi_file)
    except Exception as e:
        print(f"❌ Error: {e}")
        return []
    
    ticks_per_beat = mid.ticks_per_beat
    for track in mid.tracks:
        current_time = 0
        active_notes = {}
        for msg in track:
            current_time += msg.time
            if msg.type == 'note_on' and msg.velocity > 0:
                active_notes[msg.note] = (current_time, msg.velocity)
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                if msg.note in active_notes:
                    start_time, velocity = active_notes[msg.note]
                    duration = current_time - start_time
                    notes.append({
                        'time': start_time / ticks_per_beat,
                        'pitch': msg.note,
                        'duration': duration / ticks_per_beat,
                        'velocity': velocity,
                        'pitch_class': normalize_pitch_class(msg.note)
                    })
                    del active_notes[msg.note]
    notes.sort(key=lambda x: x['time'])
    return notes

def calculate_key_correlation(histogram, profile):
    if sum(histogram) == 0:
        return 0
    total = sum(histogram)
    normalized = [count / total for count in histogram]
    mean_hist = sum(normalized) / 12
    mean_prof = sum(profile) / 12
    numerator = sum((normalized[i] - mean_hist) * (profile[i] - mean_prof) for i in range(12))
    denom_hist = sum((normalized[i] - mean_hist) ** 2 for i in range(12)) ** 0.5
    denom_prof = sum((profile[i] - mean_prof) ** 2 for i in range(12)) ** 0.5
    if denom_hist == 0 or denom_prof == 0:
        return 0
    return numerator / (denom_hist * denom_prof)

def detect_key(notes):
    if not notes:
        return None, None, 0
    histogram = [0] * 12
    for note in notes:
        weight = note['duration'] * (note['velocity'] / 127.0)
        histogram[note['pitch_class']] += weight
    best_corr = -1
    best_key = None
    best_mode = None
    for root in range(12):
        rotated = histogram[root:] + histogram[:root]
        major_corr = calculate_key_correlation(rotated, MAJOR_PROFILE)
        if major_corr > best_corr:
            best_corr = major_corr
            best_key = root
            best_mode = 'Major'
        minor_corr = calculate_key_correlation(rotated, MINOR_PROFILE)
        if minor_corr > best_corr:
            best_corr = minor_corr
            best_key = root
            best_mode = 'Minor'
    return best_key, best_mode, best_corr

def detect_scale(notes, key_root):
    if not notes:
        return None, 0
    pitch_classes = set(note['pitch_class'] for note in notes)
    normalized = {(pc - key_root) % 12 for pc in pitch_classes}
    best_match = None
    best_score = 0
    for scale_name, pattern in SCALES.items():
        scale_set = set(pattern)
        matches = len(normalized & scale_set)
        total = len(normalized)
        if total == 0:
            continue
        score = matches / total
        coverage = matches / len(scale_set) if scale_set else 0
        combined = (score + coverage) / 2
        if combined > best_score:
            best_score = combined
            best_match = scale_name
    return best_match, best_score

def analyze_midi_file(midi_file, verbose=True):
    if verbose:
        print("=" * 70)
        print(f"🎼 ANALYZING: {os.path.basename(midi_file)}")
        print("=" * 70)
    
    notes = extract_notes_from_midi(midi_file)
    if not notes:
        print("❌ No notes found")
        return None
    
    if verbose:
        print(f"\n📊 Found {len(notes)} notes")
    
    key_root, key_mode, key_conf = detect_key(notes)
    if key_root is not None:
        key_name = get_note_name(key_root)
        if verbose:
            print(f"\n🎹 Key: {key_name} {key_mode} ({key_conf:.2%} confidence)")
    else:
        if verbose:
            print("\n❌ Could not detect key")
        return None
    
    scale_name, scale_conf = detect_scale(notes, key_root)
    if scale_name and verbose:
        print(f"\n📊 Scale: {scale_name} ({scale_conf:.2%} confidence)")
    
    if verbose:
        print("\n" + "=" * 70)
    
    return {
        'key_root': key_name,
        'key_mode': key_mode,
        'key_confidence': key_conf,
        'scale': scale_name,
        'scale_confidence': scale_conf,
        'note_count': len(notes)
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_harmony.py <midi_file>")
        sys.exit(1)
    
    midi_file = sys.argv[1]
    if not os.path.exists(midi_file):
        print(f"❌ File not found: {midi_file}")
        sys.exit(1)
    
    analyze_midi_file(midi_file)

if __name__ == "__main__":
    main()
