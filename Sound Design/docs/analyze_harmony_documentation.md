# 🎼 Harmonic Analysis Tool - Documentation

## Overview

The **Harmonic Analysis Tool** (`analyze_harmony.py`) is a comprehensive MIDI analysis script that detects key, scale, chord progressions, and provides musical suggestions.

---

## 🎯 What It Does

### Core Analysis Features:

1. **Key Detection**
   - Identifies root note (C, D, E, etc.)
   - Determines major or minor mode
   - Provides confidence percentage
   - Uses Krumhansl-Schmuckler algorithm

2. **Scale Detection**
   - Matches notes to 14+ scale types
   - Includes: Major modes, minor scales, pentatonic, blues, exotic
   - Shows match percentage
   - Lists all notes in detected scale

3. **Chord Progression Analysis**
   - Detects individual chords throughout the piece
   - Identifies chord types (major, minor, 7th, 9th, sus, etc.)
   - Shows Roman numeral analysis
   - Provides simplified progression

4. **Statistical Analysis**
   - Pitch class distribution
   - Note usage percentages
   - Duration and measure count
   - Most-used notes visualization

5. **Musical Suggestions**
   - Related keys (relative, parallel)
   - Scale variations
   - Chord substitution ideas
   - Compositional improvements

---

## 📋 Usage

### Basic Usage

```bash
python analyze_harmony.py <midi_file>
```

**Example**:
```bash
python analyze_harmony.py my_song.mid
```

### Advanced Usage

```bash
python analyze_harmony.py <midi_file> <beats_per_measure> <beats_per_chord>
```

**Examples**:
```bash
# Standard 4/4 time, chords every 4 beats
python analyze_harmony.py song.mid 4 4

# 3/4 waltz time, chords every 6 beats
python analyze_harmony.py waltz.mid 3 6

# 6/8 time, chords every 2 beats
python analyze_harmony.py ballad.mid 6 2

# Fast chord changes (every 2 beats)
python analyze_harmony.py jazz.mid 4 2
```

---

## 📊 Output Format

### Example Output:

```
======================================================================
🎼 HARMONIC ANALYSIS
======================================================================

File: my_progression.mid
Analyzing...
✅ Found 48 notes
Duration: 32.0 beats (9 measures at 4/4)

----------------------------------------------------------------------
🎹 KEY DETECTION
----------------------------------------------------------------------

✅ Detected Key: C major
   Confidence: 87.45%

----------------------------------------------------------------------
🎵 SCALE DETECTION
----------------------------------------------------------------------

✅ Best matching scale: C Major (Ionian)
   Match: 100.0%
   Notes: C - D - E - F - G - A - B

----------------------------------------------------------------------
📊 PITCH CLASS DISTRIBUTION
----------------------------------------------------------------------

Most used notes:
   C  : ████████████ 25.0%
   E  : ████████ 16.7%
   G  : ████████ 16.7%
   F  : ██████ 12.5%
   A  : ██████ 12.5%
   D  : ████ 8.3%
   B  : ████ 8.3%

----------------------------------------------------------------------
🎸 CHORD PROGRESSION
----------------------------------------------------------------------

✅ Detected 8 chords:

   Bar  1: Cmajor   (I)
   Bar  2: Fmajor   (IV)
   Bar  3: Gmajor   (V)
   Bar  4: Cmajor   (I)
   Bar  5: Aminor   (vi)
   Bar  6: Fmajor   (IV)
   Bar  7: Gmajor   (V)
   Bar  8: Cmajor   (I)

📝 Simplified progression:
   Cmajor → Fmajor → Gmajor → Cmajor → Aminor → Fmajor → Gmajor → Cmajor

🎼 Roman numeral progression:
   I - IV - V - I - vi - IV - V - I

----------------------------------------------------------------------
💡 SUGGESTIONS
----------------------------------------------------------------------

💡 RELATED KEYS:
   • Relative minor: A
   • Parallel minor: C

💡 SCALE VARIATIONS:
   • Try C Lydian for brighter sound
   • Try C Mixolydian for bluesy feel

💡 CHORD SUBSTITUTIONS:
   • Replace major chords with maj7 for sophistication
   • Try sus2/sus4 chords for ambiguous feel
   • Add passing chords between main chords

======================================================================
📋 SUMMARY
======================================================================

Key: C major
Scale: C Major (Ionian)
Measures: 9
Chords detected: 8
Notes analyzed: 48

======================================================================
✅ Analysis complete!
======================================================================
```

---

## 🎹 Supported Scales

The tool can detect these scales:

### Major Modes:
- Major (Ionian)
- Dorian
- Phrygian
- Lydian
- Mixolydian
- Aeolian (Natural Minor)
- Locrian

### Minor Scales:
- Natural Minor
- Harmonic Minor
- Melodic Minor

### Pentatonic Scales:
- Major Pentatonic
- Minor Pentatonic
- Blues Scale

### Exotic/Other:
- Whole Tone
- Phrygian Dominant
- (More can be added easily)

---

## 🎸 Supported Chord Types

The tool can identify these chord types:

### Triads:
- Major (e.g., C, G, F)
- Minor (e.g., Am, Dm, Em)
- Diminished (e.g., Bdim)
- Augmented (e.g., Caug)

### Suspended:
- Sus2 (e.g., Csus2)
- Sus4 (e.g., Gsus4)

### Seventh Chords:
- Major 7th (e.g., Cmaj7)
- Minor 7th (e.g., Am7)
- Dominant 7th (e.g., G7)

### Extended:
- Major 9th (e.g., Cmaj9)
- Minor 9th (e.g., Am9)
- Add9 (e.g., Cadd9)
- 6th chords (e.g., C6, Am6)

---

## 🔬 How It Works

### 1. Key Detection Algorithm

Uses the **Krumhansl-Schmuckler key-finding algorithm**:

1. Counts pitch classes in the MIDI file
2. Weights by duration and velocity
3. Compares distribution to known major/minor profiles
4. Calculates correlation coefficient for all 24 keys
5. Selects key with highest correlation

**Confidence levels**:
- **>80%**: Very confident
- **60-80%**: Confident
- **40-60%**: Uncertain (may be modal or ambiguous)
- **<40%**: Low confidence (may be atonal or chromatic)

### 2. Scale Detection

1. Normalizes all pitch classes to detected root
2. Compares against 14+ scale templates
3. Calculates match percentage
4. Selects best-fitting scale

### 3. Chord Detection

1. Segments MIDI into time windows (customizable)
2. Extracts simultaneous notes in each window
3. Tests all possible chord roots
4. Matches against chord templates
5. Prioritizes more specific chord types

### 4. Roman Numeral Analysis

1. Calculates scale degree of each chord root
2. Converts to Roman numeral based on mode
3. Shows harmonic function (I, IV, V, etc.)

---

## 💡 Use Cases

### For Producers:

**Analyzing reference tracks**:
```bash
python analyze_harmony.py reference_track.mid
```
Learn the key, scale, and progression of tracks you like.

**Understanding your own work**:
```bash
python analyze_harmony.py my_work_in_progress.mid
```
See what key/scale you're actually using (might surprise you!).

**Finding variations**:
The tool suggests related keys and scales to try.

### For Composers:

**Theory analysis**:
Use to verify your chord progressions follow theory rules.

**Learning progressions**:
Analyze famous songs to understand their harmonic structure.

**Chord substitution ideas**:
Get suggestions for variations and improvements.

### For Educators:

**Teaching tool**:
Demonstrate key detection and harmonic analysis.

**Student feedback**:
Analyze student compositions and provide detailed feedback.

**Theory verification**:
Check if students are using correct scales/keys.

---

## 🎓 Understanding the Output

### Key Detection Confidence

- **High (>70%)**: Clear tonal center, confident result
- **Medium (50-70%)**: Somewhat ambiguous, but likely correct
- **Low (<50%)**: Very ambiguous or atonal; may not have a clear key

### Scale Match Percentage

- **100%**: All notes perfectly fit the scale
- **85-99%**: Very close, possible passing tones or chromatic notes
- **70-84%**: Good fit, some notes outside scale (common)
- **<70%**: Poor fit; may be using multiple scales or chromatic

### Roman Numeral Analysis

**In major key** (C major example):
- **I** = C major (tonic, home)
- **ii** = D minor (supertonic)
- **iii** = E minor (mediant)
- **IV** = F major (subdominant, movement away)
- **V** = G major (dominant, tension)
- **vi** = A minor (submediant)
- **vii°** = B diminished (leading tone)

**In minor key** (A minor example):
- **i** = A minor (tonic)
- **ii°** = B diminished
- **III** = C major (relative major)
- **iv** = D minor
- **v** = E minor
- **VI** = F major
- **VII** = G major

---

## 🛠️ Customization

### Adding New Scales

Edit the `SCALES` dictionary in the script:

```python
SCALES = {
    'Your Scale Name': [0, 2, 3, 5, 7, 9, 10],  # semitone intervals
    # ... existing scales
}
```

### Adding New Chord Types

Edit the `CHORD_TYPES` dictionary:

```python
CHORD_TYPES = {
    'your_chord': [0, 4, 7, 10, 14],  # intervals from root
    # ... existing chords
}
```

### Adjusting Chord Detection Window

Change `beats_per_chord` parameter:

```bash
# Detect chords every 2 beats (faster changes)
python analyze_harmony.py song.mid 4 2

# Detect chords every 8 beats (slower changes)
python analyze_harmony.py song.mid 4 8
```

---

## ⚠️ Limitations

### What it CAN'T do:

1. **Analyze audio files**
   - Only works with MIDI files
   - Audio must be converted to MIDI first (use tools like AnthemScore, Melodyne)

2. **Detect complex jazz voicings**
   - May simplify very complex chords
   - Upper extensions (11th, 13th) may not be detected

3. **Understand context**
   - Doesn't know musical form (verse, chorus, etc.)
   - Treats all sections equally

4. **Detect modulations**
   - Analyzes entire piece as single key
   - Won't catch mid-song key changes

5. **Monophonic analysis**
   - Works best with harmonic content (multiple notes)
   - Single-note melodies may give uncertain results

---

## 🐛 Troubleshooting

### Issue: "No notes found in MIDI file"

**Solutions**:
- Check MIDI file is not empty
- Ensure MIDI file is not corrupted
- Try opening in DAW to verify it contains notes

### Issue: Low confidence key detection

**Reasons**:
- Piece may be atonal or chromatic
- Very short piece (not enough data)
- Piece uses multiple keys (modulation)
- Heavy use of non-scale tones

**Solutions**:
- Try analyzing longer section
- Check if piece is intentionally atonal
- Analyze sections separately if it modulates

### Issue: No chords detected

**Reasons**:
- MIDI is monophonic (single notes)
- Notes never overlap
- Very sparse arrangement

**Solutions**:
- Use `beats_per_chord` to adjust detection window
- Check if MIDI is melody-only

### Issue: Wrong key detected

**Reasons**:
- Piece may be modal (not major/minor)
- Heavy chromatic passages
- Short excerpt

**Solutions**:
- Check the suggested scale (might be a mode)
- Analyze longer section
- Verify by ear

---

## 📚 Integration with Sound-Design Skill

This tool integrates perfectly with the mood-to-composition workflow:

### Workflow Example:

1. **Analyze reference track**:
   ```bash
   python analyze_harmony.py reference.mid
   # Output: Key = D minor, Scale = Phrygian
   ```

2. **Generate composition in same key/mood**:
   ```bash
   python mood_to_composition.py dark D
   # Creates progressions in D Phrygian
   ```

3. **Program synth in correct scale**:
   ```
   "Program Matriarch pad in D Phrygian with dark character"
   ```

4. **Add drums matching the vibe**:
   ```bash
   python generate_rhythm.py techno 128 16
   ```

---

## 🎯 Best Practices

### For Best Results:

1. **Use clear harmonic content**
   - Works best with chords, not single-note melodies
   - Include bass notes for better root detection

2. **Analyze complete sections**
   - At least 4-8 measures for accurate key detection
   - Longer = more accurate

3. **Clean up MIDI first**
   - Quantize if timing is messy
   - Remove non-musical noise notes

4. **Adjust parameters for style**:
   - **Jazz**: `beats_per_chord 2` (faster changes)
   - **Ambient**: `beats_per_chord 8` (slower changes)
   - **Classical**: Use actual time signature

5. **Cross-reference with ear**
   - Trust your ears if results seem wrong
   - Tool is a guide, not absolute truth

---

## 🔮 Future Enhancements

Planned features:

- [ ] Modulation detection (key changes)
- [ ] Tempo/BPM analysis
- [ ] Rhythmic analysis
- [ ] MIDI export of cleaned-up progression
- [ ] Web interface
- [ ] Audio file support (via audio-to-MIDI)
- [ ] Batch analysis of multiple files
- [ ] PDF report generation
- [ ] Integration with DAWs

---

## 📖 References

### Algorithms Used:

- **Krumhansl-Schmuckler Key-Finding Algorithm**
  - Krumhansl, C. L., & Schmuckler, M. A. (1986)
  - "Key-finding algorithm based on listener judgments"

### Music Theory:

- Standard Western music theory (scales, chords, Roman numerals)
- Jazz theory (extended chords, substitutions)

---

## 🎵 Example Analyses

### Pop Progression (I-V-vi-IV)

```
Key: C major
Progression: C - G - Am - F
Roman: I - V - vi - IV
Mood: Uplifting, pop, anthemic
```

### Jazz ii-V-I

```
Key: C major  
Progression: Dm7 - G7 - Cmaj7
Roman: ii7 - V7 - Imaj7
Mood: Sophisticated, jazzy, smooth
```

### Minor Epic

```
Key: D minor
Progression: Dm - C - Bb - C
Roman: i - VII - VI - VII
Mood: Epic, cinematic, powerful
```

---

## 💻 Dependencies

Required Python libraries:
- `mido` - MIDI file reading

Install with:
```bash
pip install mido --break-system-packages
```

---

## ✅ Quick Reference

```bash
# Basic analysis
python analyze_harmony.py song.mid

# Custom time signature
python analyze_harmony.py song.mid 3 6  # 3/4 time

# Faster chord detection
python analyze_harmony.py song.mid 4 2  # Every 2 beats

# Help
python analyze_harmony.py
```

---

**Created for the Sound-Design Skill**  
Version 1.0  
Part of the complete music production workflow toolkit
