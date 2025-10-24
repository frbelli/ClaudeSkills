#!/usr/bin/env python3
"""
Harmonic Analysis Tool
Analyzes MIDI files to detect:
- Key (root note and major/minor)
- Scale/Mode
- Chord progression
- Suggestions for variations and improvements
"""

import sys
import mido
from collections import Counter, defaultdict
from mido import MidiFile
import os

# ============================================================
# MUSIC THEORY DATA
# ============================================================

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Scale patterns (semitone intervals from root)
SCALES = {
    'Major (Ionian)': [0, 2, 4, 5, 7, 9, 11],
    'Natural Minor (Aeolian)': [0, 2, 3, 5, 7, 8, 10],
    'Harmonic Minor': [0, 2, 3, 5, 7, 8, 11],
    'Melodic Minor': [0, 2, 3, 5, 7, 9, 11],
    'Dorian': [0, 2, 3, 5, 7, 9, 10],
    'Phrygian': [0, 1, 3, 5, 7, 8, 10],
    'Lydian': [0, 2, 4, 6, 7, 9, 11],
    'Mixolydian': [0, 2, 4, 5, 7, 9, 10],
    'Locrian': [0, 1, 3, 5, 6, 8, 10],
    'Blues': [0, 3, 5, 6, 7, 10],
    'Minor Pentatonic': [0, 3, 5, 7, 10],
    'Major Pentatonic': [0, 2, 4, 7, 9],
    'Whole Tone': [0, 2, 4, 6, 8, 10],
    'Phrygian Dominant': [0, 1, 4, 5, 7, 8, 10],
}

# Major and minor profiles for key detection (Krumhansl-Schmuckler)
MAJOR_PROFILE = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
MINOR_PROFILE = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]

# Chord templates (intervals from root)
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
    '7': [0, 4, 7, 10],  # dominant 7
    'maj9': [0, 4, 7, 11, 14],
    'min9': [0, 3, 7, 10, 14],
    'add9': [0, 4, 7, 14],
    '6': [0, 4, 7, 9],
    'min6': [0, 3, 7, 9],
}

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def normalize_pitch_class(midi_note):
    """Convert MIDI note to pitch class (0-11)"""
    return midi_note % 12

def get_note_name(pitch_class):
    """Convert pitch class to note name"""
    return NOTE_NAMES[pitch_class % 12]

def extract_notes_from_midi(midi_file):
    """
    Extract all notes from MIDI file with timing information
    Returns: list of (time, pitch, duration, velocity)
    """
    notes = []
    
    try:
        mid = MidiFile(midi_file)
    except Exception as e:
        print(f"❌ Error reading MIDI file: {e}")
        return []
    
    # Get ticks per beat for timing calculation
    ticks_per_beat = mid.ticks_per_beat
    
    for track_idx, track in enumerate(mid.tracks):
        current_time = 0
        active_notes = {}  # note_number: (start_time, velocity)
        
        for msg in track:
            current_time += msg.time
            
            if msg.type == 'note_on' and msg.velocity > 0:
                active_notes[msg.note] = (current_time, msg.velocity)
            
            elif msg.type == 'note_off' or (msg.type == 'note_on' and msg.velocity == 0):
                if msg.note in active_notes:
                    start_time, velocity = active_notes[msg.note]
                    duration = current_time - start_time
                    
                    # Convert to beats
                    time_in_beats = start_time / ticks_per_beat
                    duration_in_beats = duration / ticks_per_beat
                    
                    notes.append({
                        'time': time_in_beats,
                        'pitch': msg.note,
                        'duration': duration_in_beats,
                        'velocity': velocity,
                        'pitch_class': normalize_pitch_class(msg.note)
                    })
                    
                    del active_notes[msg.note]
    
    # Sort by time
    notes.sort(key=lambda x: x['time'])
    return notes

def calculate_key_correlation(pitch_class_histogram, profile):
    """Calculate correlation between pitch class distribution and key profile"""
    if sum(pitch_class_histogram) == 0:
        return 0
    
    # Normalize histogram
    total = sum(pitch_class_histogram)
    normalized = [count / total for count in pitch_class_histogram]
    
    # Calculate correlation coefficient
    mean_hist = sum(normalized) / len(normalized)
    mean_prof = sum(profile) / len(profile)
    
    numerator = sum((normalized[i] - mean_hist) * (profile[i] - mean_prof) 
                   for i in range(12))
    
    denom_hist = sum((normalized[i] - mean_hist) ** 2 for i in range(12)) ** 0.5
    denom_prof = sum((profile[i] - mean_prof) ** 2 for i in range(12)) ** 0.5
    
    if denom_hist == 0 or denom_prof == 0:
        return 0
    
    return numerator / (denom_hist * denom_prof)

def detect_key(notes):
    """
    Detect key using Krumhansl-Schmuckler key-finding algorithm
    Returns: (root_note, mode, confidence)
    """
    if not notes:
        return None, None, 0
    
    # Count pitch classes weighted by duration and velocity
    pitch_class_counts = [0] * 12
    for note in notes:
        weight = note['duration'] * (note['velocity'] / 127.0)
        pitch_class_counts[note['pitch_class']] += weight
    
    # Try all 24 keys (12 major + 12 minor)
    best_correlation = -1
    best_key = None
    best_mode = None
    
    for root in range(12):
        # Rotate histogram to test this root
        rotated = pitch_class_counts[root:] + pitch_class_counts[:root]
        
        # Test major
        major_corr = calculate_key_correlation(rotated, MAJOR_PROFILE)
        if major_corr > best_correlation:
            best_correlation = major_corr
            best_key = root
            best_mode = 'major'
        
        # Test minor
        minor_corr = calculate_key_correlation(rotated, MINOR_PROFILE)
        if minor_corr > best_correlation:
            best_correlation = minor_corr
            best_key = root
            best_mode = 'minor'
    
    confidence = best_correlation
    return best_key, best_mode, confidence

def detect_scale(notes, root_key):
    """
    Detect which scale best fits the notes
    Returns: (scale_name, match_percentage)
    """
    if not notes:
        return None, 0
    
    # Get unique pitch classes used
    pitch_classes_used = set(note['pitch_class'] for note in notes)
    
    # Normalize to root
    normalized_pcs = set((pc - root_key) % 12 for pc in pitch_classes_used)
    
    best_match = None
    best_percentage = 0
    
    for scale_name, scale_pattern in SCALES.items():
        scale_set = set(scale_pattern)
        
        # Calculate match percentage
        matches = len(normalized_pcs & scale_set)
        total = len(normalized_pcs)
        
        if total > 0:
            percentage = (matches / total) * 100
            
            if percentage > best_percentage:
                best_percentage = percentage
                best_match = scale_name
    
    return best_match, best_percentage

def segment_into_measures(notes, beats_per_measure=4):
    """Segment notes into measures"""
    if not notes:
        return []
    
    measures = []
    current_measure = []
    current_measure_num = 0
    
    for note in notes:
        measure_num = int(note['time'] // beats_per_measure)
        
        if measure_num > current_measure_num:
            if current_measure:
                measures.append(current_measure)
            current_measure = []
            current_measure_num = measure_num
        
        current_measure.append(note)
    
    if current_measure:
        measures.append(current_measure)
    
    return measures

def detect_chord(notes_in_window, root_key):
    """
    Detect chord from simultaneous notes
    Returns: (root, chord_type, notes)
    """
    if not notes_in_window:
        return None, None, []
    
    # Get unique pitch classes
    pitch_classes = list(set(note['pitch_class'] for note in notes_in_window))
    
    if len(pitch_classes) < 2:
        return None, None, pitch_classes
    
    # Try each note as potential root
    best_match = None
    best_root = None
    best_chord_type = None
    
    for potential_root in pitch_classes:
        # Normalize other notes relative to this root
        intervals = sorted(set((pc - potential_root) % 12 for pc in pitch_classes))
        
        # Check against chord templates
        for chord_type, template in CHORD_TYPES.items():
            # Check if intervals match template
            if set(template).issubset(set(intervals)):
                # Prefer more specific chord types (more notes matched)
                if best_match is None or len(template) > len(best_match):
                    best_match = template
                    best_root = potential_root
                    best_chord_type = chord_type
    
    return best_root, best_chord_type, pitch_classes

def analyze_chord_progression(notes, beats_per_chord=4):
    """
    Detect chord progression from MIDI notes
    Returns: list of (time, root, chord_type)
    """
    if not notes:
        return []
    
    progression = []
    
    # Group notes by time windows
    max_time = max(note['time'] for note in notes)
    num_windows = int(max_time / beats_per_chord) + 1
    
    for window_idx in range(num_windows):
        window_start = window_idx * beats_per_chord
        window_end = window_start + beats_per_chord
        
        # Get notes in this window (that overlap with window)
        notes_in_window = [
            note for note in notes 
            if note['time'] < window_end and 
               (note['time'] + note['duration']) > window_start
        ]
        
        if notes_in_window:
            root, chord_type, pcs = detect_chord(notes_in_window, None)
            
            if root is not None:
                progression.append({
                    'time': window_start,
                    'root': root,
                    'root_name': get_note_name(root),
                    'chord_type': chord_type,
                    'notes': [get_note_name(pc) for pc in pcs]
                })
    
    return progression

def roman_numeral_from_degree(degree, mode):
    """Convert scale degree to Roman numeral"""
    if mode == 'major':
        numerals = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii°']
    else:  # minor
        numerals = ['i', 'ii°', 'III', 'iv', 'v', 'VI', 'VII']
    
    if 0 <= degree < len(numerals):
        return numerals[degree]
    return str(degree + 1)

def get_suggestions(key_root, mode, scale_name, progression):
    """Generate suggestions based on analysis"""
    suggestions = []
    
    # Suggest related keys
    suggestions.append(f"💡 RELATED KEYS:")
    relative_key = (key_root + 3) % 12 if mode == 'major' else (key_root - 3) % 12
    relative_mode = 'minor' if mode == 'major' else 'major'
    suggestions.append(f"   • Relative {relative_mode}: {get_note_name(relative_key)}")
    
    parallel_mode = 'minor' if mode == 'major' else 'major'
    suggestions.append(f"   • Parallel {parallel_mode}: {get_note_name(key_root)}")
    
    # Suggest scale variations
    suggestions.append(f"\n💡 SCALE VARIATIONS:")
    if mode == 'major':
        suggestions.append(f"   • Try {get_note_name(key_root)} Lydian for brighter sound")
        suggestions.append(f"   • Try {get_note_name(key_root)} Mixolydian for bluesy feel")
    else:
        suggestions.append(f"   • Try {get_note_name(key_root)} Dorian for jazzier sound")
        suggestions.append(f"   • Try {get_note_name(key_root)} Harmonic Minor for dramatic feel")
    
    # Suggest chord substitutions
    if progression:
        suggestions.append(f"\n💡 CHORD SUBSTITUTIONS:")
        suggestions.append(f"   • Replace major chords with maj7 for sophistication")
        suggestions.append(f"   • Try sus2/sus4 chords for ambiguous feel")
        suggestions.append(f"   • Add passing chords between main chords")
    
    return '\n'.join(suggestions)

# ============================================================
# MAIN ANALYSIS FUNCTION
# ============================================================

def analyze_harmony(midi_file, beats_per_measure=4, beats_per_chord=4):
    """
    Comprehensive harmonic analysis of MIDI file
    """
    print("\n" + "=" * 70)
    print("🎼 HARMONIC ANALYSIS")
    print("=" * 70)
    print(f"\nFile: {os.path.basename(midi_file)}")
    print(f"Analyzing...")
    
    # Extract notes
    notes = extract_notes_from_midi(midi_file)
    
    if not notes:
        print("\n❌ No notes found in MIDI file!")
        return
    
    print(f"✅ Found {len(notes)} notes")
    
    # Calculate basic statistics
    duration = max(note['time'] + note['duration'] for note in notes)
    measures = int(duration / beats_per_measure) + 1
    
    print(f"Duration: {duration:.1f} beats ({measures} measures at {beats_per_measure}/4)")
    
    # Detect key
    print(f"\n" + "-" * 70)
    print("🎹 KEY DETECTION")
    print("-" * 70)
    
    key_root, mode, confidence = detect_key(notes)
    
    if key_root is not None:
        key_name = get_note_name(key_root)
        print(f"\n✅ Detected Key: {key_name} {mode}")
        print(f"   Confidence: {confidence:.2%}")
    else:
        print("\n❌ Could not detect key")
        return
    
    # Detect scale
    print(f"\n" + "-" * 70)
    print("🎵 SCALE DETECTION")
    print("-" * 70)
    
    scale_name, match_percentage = detect_scale(notes, key_root)
    
    if scale_name:
        print(f"\n✅ Best matching scale: {key_name} {scale_name}")
        print(f"   Match: {match_percentage:.1f}%")
        
        # Show scale notes
        scale_pattern = SCALES[scale_name]
        scale_notes = [get_note_name((key_root + interval) % 12) for interval in scale_pattern]
        print(f"   Notes: {' - '.join(scale_notes)}")
    
    # Analyze pitch class distribution
    print(f"\n" + "-" * 70)
    print("📊 PITCH CLASS DISTRIBUTION")
    print("-" * 70)
    
    pitch_class_counts = Counter(note['pitch_class'] for note in notes)
    sorted_pcs = sorted(pitch_class_counts.items(), key=lambda x: x[1], reverse=True)
    
    print("\nMost used notes:")
    for pc, count in sorted_pcs[:8]:
        note_name = get_note_name(pc)
        percentage = (count / len(notes)) * 100
        bar = '█' * int(percentage / 2)
        print(f"   {note_name:3s}: {bar} {percentage:.1f}%")
    
    # Detect chord progression
    print(f"\n" + "-" * 70)
    print("🎸 CHORD PROGRESSION")
    print("-" * 70)
    
    progression = analyze_chord_progression(notes, beats_per_chord)
    
    if progression:
        print(f"\n✅ Detected {len(progression)} chords:\n")
        
        # Group consecutive same chords
        simplified_prog = []
        last_chord = None
        
        for chord in progression:
            chord_name = f"{chord['root_name']}{chord['chord_type']}"
            if chord_name != last_chord:
                # Calculate scale degree
                degree = (chord['root'] - key_root) % 12
                # Find closest scale degree
                scale_pattern = SCALES.get(scale_name, SCALES['Major (Ionian)'])
                closest_degree = min(range(len(scale_pattern)), 
                                   key=lambda i: abs(scale_pattern[i] - degree))
                roman = roman_numeral_from_degree(closest_degree, mode)
                
                simplified_prog.append(chord_name)
                measure_num = int(chord['time'] / beats_per_measure) + 1
                print(f"   Bar {measure_num:2d}: {chord_name:8s} ({roman})")
                last_chord = chord_name
        
        # Show simplified progression
        print(f"\n📝 Simplified progression:")
        print(f"   {' → '.join(simplified_prog)}")
        
        # Roman numeral progression
        roman_progression = []
        for chord in progression:
            chord_name = f"{chord['root_name']}{chord['chord_type']}"
            degree = (chord['root'] - key_root) % 12
            scale_pattern = SCALES.get(scale_name, SCALES['Major (Ionian)'])
            closest_degree = min(range(len(scale_pattern)), 
                               key=lambda i: abs(scale_pattern[i] - degree))
            roman = roman_numeral_from_degree(closest_degree, mode)
            if roman not in [r for r in roman_progression]:
                roman_progression.append(roman)
        
        print(f"\n🎼 Roman numeral progression:")
        print(f"   {' - '.join(roman_progression)}")
    
    else:
        print("\n⚠️  No clear chord progression detected")
        print("    (File may be monophonic or very sparse)")
    
    # Suggestions
    print(f"\n" + "-" * 70)
    print("💡 SUGGESTIONS")
    print("-" * 70)
    
    suggestions = get_suggestions(key_root, mode, scale_name, progression)
    print(f"\n{suggestions}")
    
    # Summary
    print(f"\n" + "=" * 70)
    print("📋 SUMMARY")
    print("=" * 70)
    print(f"""
Key: {get_note_name(key_root)} {mode}
Scale: {key_name} {scale_name}
Measures: {measures}
Chords detected: {len(progression) if progression else 0}
Notes analyzed: {len(notes)}
    """)
    
    print("=" * 70)
    print("✅ Analysis complete!")
    print("=" * 70 + "\n")

# ============================================================
# CLI INTERFACE
# ============================================================

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n🎼 HARMONIC ANALYSIS TOOL")
        print("=" * 70)
        print("\nAnalyzes MIDI files to detect:")
        print("  • Key (root note and major/minor)")
        print("  • Scale/Mode")
        print("  • Chord progression")
        print("  • Suggestions for variations")
        print("\nUsage: python analyze_harmony.py <midi_file> [beats_per_measure] [beats_per_chord]")
        print("\nExamples:")
        print("  python analyze_harmony.py song.mid")
        print("  python analyze_harmony.py song.mid 4 4")
        print("  python analyze_harmony.py song.mid 3 6  # for 3/4 time")
        print("\nDefault: 4 beats per measure, 4 beats per chord")
        print("=" * 70 + "\n")
        sys.exit(0)
    
    midi_file = sys.argv[1]
    
    if not os.path.exists(midi_file):
        print(f"\n❌ Error: File '{midi_file}' not found!")
        sys.exit(1)
    
    # Parse optional parameters
    beats_per_measure = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    beats_per_chord = int(sys.argv[3]) if len(sys.argv) > 3 else 4
    
    # Run analysis
    analyze_harmony(midi_file, beats_per_measure, beats_per_chord)
