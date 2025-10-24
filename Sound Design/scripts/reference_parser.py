#!/usr/bin/env python3
"""
Reference Database Parser

Reads and parses markdown reference files from ../references/
Returns structured data for use in generation scripts.

Usage:
    from reference_parser import ReferenceParser
    
    parser = ReferenceParser()
    scales = parser.get_scales()
    progressions = parser.get_chord_progressions()
    moods = parser.get_mood_profiles()
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Any, Optional

class ReferenceParser:
    """Parser for sound-design skill markdown reference files"""
    
    def __init__(self, references_path: str = "../references"):
        """
        Initialize parser with path to references directory
        
        Args:
            references_path: Path to references directory (relative or absolute)
        """
        self.path = Path(__file__).parent / references_path
        if not self.path.exists():
            raise FileNotFoundError(f"References directory not found: {self.path}")
        
        # Cache for parsed data
        self._cache = {}
    
    # ============================================================
    # SCALES & MODES
    # ============================================================
    
    def get_scales(self, use_cache: bool = True) -> Dict[str, Dict[str, Any]]:
        """
        Parse scales-modes.md and return structured scale data
        
        Returns:
            {
                'Ionian': {
                    'full_name': 'Ionian (Major Scale)',
                    'pattern': [0, 2, 4, 5, 7, 9, 11],
                    'formula': '1-2-3-4-5-6-7',
                    'characteristics': 'Bright, happy, optimistic',
                    'moods': ['happy', 'uplifting'],
                    ...
                },
                ...
            }
        """
        if use_cache and 'scales' in self._cache:
            return self._cache['scales']
        
        file_path = self.path / 'scales-modes.md'
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        scales = {}
        
        # Split by scale headers (### N. NAME)
        scale_sections = re.split(r'\n### \d+\. (.+?)\n', content)
        
        for i in range(1, len(scale_sections), 2):
            if i+1 >= len(scale_sections):
                break
                
            name = scale_sections[i].strip()
            section_content = scale_sections[i+1]
            
            # Extract MIDI values
            midi_match = re.search(r'\*\*MIDI\*\*: \[(.+?)\]', section_content)
            if not midi_match:
                continue
            
            midi_values = [int(x.strip()) for x in midi_match.group(1).split(',')]
            
            # Calculate semitone pattern from MIDI values
            semitones = [midi_values[i] - midi_values[0] for i in range(len(midi_values))]
            
            # Extract formula
            formula_match = re.search(r'\*\*Formula\*\*: (.+)', section_content)
            formula = formula_match.group(1).strip() if formula_match else ""
            
            # Extract characteristics
            char_match = re.search(r'\*\*Characteristics\*\*:\n- (.+?)(?:\n\n|\n\*\*)', section_content, re.DOTALL)
            characteristics = char_match.group(1).strip() if char_match else ""
            
            # Clean name (remove parentheses content for key)
            clean_name = re.sub(r'\s*\(.+?\)', '', name).strip()
            
            scales[clean_name] = {
                'full_name': name,
                'pattern': semitones,
                'formula': formula,
                'midi_example': midi_values,
                'characteristics': characteristics,
                'moods': self._extract_moods_from_text(characteristics)
            }
        
        self._cache['scales'] = scales
        return scales
    
    def _extract_moods_from_text(self, text: str) -> List[str]:
        """Extract mood keywords from characteristics text"""
        mood_keywords = {
            'happy': ['happy', 'bright', 'optimistic', 'uplifting', 'joyful', 'cheerful'],
            'sad': ['sad', 'melancholic', 'somber', 'mournful', 'sorrowful'],
            'dark': ['dark', 'ominous', 'evil', 'sinister', 'mysterious', 'brooding'],
            'energetic': ['energetic', 'driving', 'powerful', 'intense', 'aggressive'],
            'calm': ['calm', 'peaceful', 'serene', 'relaxed', 'gentle'],
            'exotic': ['exotic', 'spanish', 'eastern', 'foreign', 'oriental'],
            'atmospheric': ['atmospheric', 'floating', 'ethereal', 'ambient']
        }
        
        text_lower = text.lower()
        moods = []
        
        for mood, keywords in mood_keywords.items():
            if any(kw in text_lower for kw in keywords):
                moods.append(mood)
        
        return moods
    
    # ============================================================
    # CHORD PROGRESSIONS
    # ============================================================
    
    def get_chord_progressions(self, use_cache: bool = True) -> Dict[str, List[Dict]]:
        """
        Parse chord-progressions.md and return progressions by mood
        
        Returns:
            {
                'dark': [
                    {
                        'name': 'i - bII - bVII - bVI',
                        'chords': ['i', 'bII', 'bVII', 'bVI'],
                        'example': 'Em - F - D - C',
                        'feel': 'Dark, exotic',
                        'use': 'Dark techno, horror'
                    },
                    ...
                ],
                ...
            }
        """
        if use_cache and 'progressions' in self._cache:
            return self._cache['progressions']
        
        file_path = self.path / 'chord-progressions.md'
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        progressions = {}
        
        # Split by mood sections (## EMOJI NAME)
        mood_sections = re.split(r'\n## (.+?)\n', content)
        
        for i in range(1, len(mood_sections), 2):
            if i+1 >= len(mood_sections):
                break
                
            mood_header = mood_sections[i]
            mood_content = mood_sections[i+1]
            
            # Extract mood name (remove emoji and extra text)
            mood_name = re.sub(r'[^\w\s/-]', '', mood_header).strip().lower()
            mood_name = mood_name.split('/')[0].strip()  # Take first word if multiple
            mood_name = mood_name.split()[0] if mood_name else 'unknown'  # First word only
            
            # Parse progressions in this mood
            mood_progs = []
            
            # Find all progression blocks
            prog_blocks = re.finditer(
                r'\*\*(.+?)\*\*.*?\nExample: (.+?)\n.*?Feel: (.+?)\nUse: (.+?)(?:\n\n|\n\*\*|\Z)',
                mood_content,
                re.DOTALL
            )
            
            for match in prog_blocks:
                chords_str, example, feel, use = match.groups()
                
                # Parse chord symbols (handle various separators)
                chords = [c.strip() for c in re.split(r'[-–—]', chords_str)]
                chords = [c for c in chords if c and not c.lower() in ['the', 'progression']]
                
                mood_progs.append({
                    'name': chords_str.strip(),
                    'chords': chords,
                    'example': example.strip(),
                    'feel': feel.strip(),
                    'use': use.strip()
                })
            
            if mood_progs:
                progressions[mood_name] = mood_progs
        
        self._cache['progressions'] = progressions
        return progressions
    
    # ============================================================
    # MOOD PROFILES
    # ============================================================
    
    def get_mood_profiles(self, use_cache: bool = True) -> Dict[str, Dict[str, Any]]:
        """
        Parse mood-profiles.md and return melody generation parameters
        
        Returns:
            {
                'happy': {
                    'preferred_intervals': [2, 4, 5, 7],
                    'avoid_intervals': [1, 6, 11],
                    'direction_bias': 0.6,
                    'leap_probability': 0.3,
                    'rest_probability': 0.1,
                    'rhythm_variety': 0.6,
                    'range_preference': 'middle-high',
                    ...
                },
                ...
            }
        """
        if use_cache and 'mood_profiles' in self._cache:
            return self._cache['mood_profiles']
        
        file_path = self.path / 'mood-profiles.md'
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        profiles = {}
        
        # Split by mood sections (## EMOJI NAME)
        mood_sections = re.split(r'\n## (.+?)\n', content)
        
        for i in range(1, len(mood_sections), 2):
            if i+1 >= len(mood_sections):
                break
                
            mood_header = mood_sections[i]
            mood_content = mood_sections[i+1]
            
            # Extract mood name
            mood_name = re.sub(r'[^\w\s]', '', mood_header).strip().lower()
            mood_name = mood_name.split()[0] if mood_name else 'unknown'
            
            profile = {}
            
            # Extract preferred intervals
            pref_match = re.search(r'\*\*Preferred Intervals\*\*:?\n(.+?)(?:\n\n|\*\*Avoid)', mood_content, re.DOTALL)
            if pref_match:
                intervals_text = pref_match.group(1)
                intervals = re.findall(r'- (\d+)', intervals_text)
                profile['preferred_intervals'] = [int(x) for x in intervals]
            
            # Extract avoid intervals
            avoid_match = re.search(r'\*\*Avoid Intervals\*\*:?\n(.+?)(?:\n\n|\n###)', mood_content, re.DOTALL)
            if avoid_match:
                intervals_text = avoid_match.group(1)
                intervals = re.findall(r'- (\d+)', intervals_text)
                profile['avoid_intervals'] = [int(x) for x in intervals]
            
            # Extract movement parameters
            param_patterns = {
                'direction_bias': r'\*\*Direction Bias\*\*: ([\d.]+)',
                'leap_probability': r'\*\*Leap Probability\*\*: ([\d.]+)',
                'step_probability': r'\*\*Step Probability\*\*: ([\d.]+)',
                'rest_probability': r'\*\*Rest Probability\*\*: ([\d.]+)',
                'rhythm_variety': r'\*\*Rhythm Variety\*\*: ([\d.]+)',
                'range_preference': r'\*\*Range Preference\*\*: (.+?)(?:\n|$)',
            }
            
            for param, pattern in param_patterns.items():
                match = re.search(pattern, mood_content)
                if match:
                    value = match.group(1).strip()
                    # Convert to float if numeric
                    try:
                        profile[param] = float(value)
                    except:
                        profile[param] = value
            
            profiles[mood_name] = profile
        
        self._cache['mood_profiles'] = profiles
        return profiles
    
    # ============================================================
    # PRODUCTION TIPS
    # ============================================================
    
    def get_production_tips(self, mood: str = None, use_cache: bool = True) -> Dict[str, Dict[str, List[str]]]:
        """
        Parse production-tips.md and return tips by mood
        
        Args:
            mood: Optional mood to filter by. If None, returns all.
            
        Returns:
            {
                'dark': {
                    'sound_design': ['tip1', 'tip2', ...],
                    'arrangement': [...],
                    'processing': [...],
                    ...
                },
                ...
            }
        """
        if use_cache and 'tips' in self._cache:
            all_tips = self._cache['tips']
        else:
            file_path = self.path / 'production-tips.md'
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            all_tips = {}
            
            # Split by mood sections (## EMOJI NAME)
            mood_sections = re.split(r'\n## (.+?)\n', content)
            
            for i in range(1, len(mood_sections), 2):
                if i+1 >= len(mood_sections):
                    break
                    
                mood_header = mood_sections[i]
                mood_content = mood_sections[i+1]
                
                # Extract mood name
                mood_name = re.sub(r'[^\w\s]', '', mood_header).strip().lower()
                mood_name = mood_name.split()[0] if mood_name else 'unknown'
                
                mood_tips = {}
                
                # Extract different tip categories
                categories = ['sound design', 'arrangement', 'processing']
                
                for category in categories:
                    pattern = rf'### {category.title()} Tips\n((?:- .+?\n)+)'
                    match = re.search(pattern, mood_content, re.IGNORECASE)
                    
                    if match:
                        tips_text = match.group(1)
                        tips = [line.strip('- ').strip() for line in tips_text.split('\n') if line.strip().startswith('-')]
                        mood_tips[category.lower().replace(' ', '_')] = tips
                
                all_tips[mood_name] = mood_tips
            
            self._cache['tips'] = all_tips
        
        if mood:
            return all_tips.get(mood.lower(), {})
        return all_tips
    
    # ============================================================
    # BASS PATTERNS
    # ============================================================
    
    def get_bass_patterns(self, style: str = None, use_cache: bool = True) -> Dict[str, Dict[str, Any]]:
        """
        Parse bass-patterns.md and return pattern data
        
        Args:
            style: Optional style to filter by
            
        Returns:
            {
                'root': {
                    'description': 'Root notes only - minimal',
                    'pattern': ['root'],
                    'rhythm': [16],
                    'octave_variation': False,
                    ...
                },
                ...
            }
        """
        if use_cache and 'bass_patterns' in self._cache:
            all_patterns = self._cache['bass_patterns']
        else:
            file_path = self.path / 'bass-patterns.md'
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            all_patterns = {}
            
            # Find all pattern sections (### Style Name)
            pattern_sections = re.split(r'\n### (.+?)\n', content)
            
            for i in range(1, len(pattern_sections), 2):
                if i+1 >= len(pattern_sections):
                    break
                    
                style_name = pattern_sections[i].strip()
                section_content = pattern_sections[i+1]
                
                # Extract description
                desc_match = re.search(r'\*\*Description\*\*: (.+)', section_content)
                description = desc_match.group(1).strip() if desc_match else ""
                
                # Extract pattern
                pattern_match = re.search(r'\*\*Pattern\*\*: \[(.+?)\]', section_content)
                pattern = []
                if pattern_match:
                    pattern = [x.strip().strip('"').strip("'") for x in pattern_match.group(1).split(',')]
                
                # Extract rhythm
                rhythm_match = re.search(r'\*\*Rhythm\*\*: \[(.+?)\]', section_content)
                rhythm = []
                if rhythm_match:
                    rhythm = [int(x.strip()) for x in rhythm_match.group(1).split(',')]
                
                # Extract octave variation
                octave_match = re.search(r'\*\*Octave Variation\*\*: (Yes|No)', section_content)
                octave_variation = octave_match.group(1) == 'Yes' if octave_match else False
                
                # Create key from style name
                key = style_name.lower().replace(' ', '_').replace('(', '').replace(')', '')
                key = key.split('(')[0].strip('_')  # Remove any parenthetical content
                
                all_patterns[key] = {
                    'description': description,
                    'pattern': pattern,
                    'rhythm': rhythm,
                    'octave_variation': octave_variation
                }
            
            self._cache['bass_patterns'] = all_patterns
        
        if style:
            style_key = style.lower().replace(' ', '_')
            return {k: v for k, v in all_patterns.items() if style_key in k}
        
        return all_patterns
    
    # ============================================================
    # GENRE STYLES
    # ============================================================
    
    def get_genre_styles(self, use_cache: bool = True) -> Dict[str, Dict[str, Any]]:
        """
        Parse genre-styles.md and return genre characteristics with style variations
        
        Returns:
            {
                'techno': {
                    'characteristics': {...},
                    'styles': {
                        'driving': {
                            'bpm': '135-145',
                            'character': 'Relentless, industrial, hypnotic',
                            ...
                        },
                        ...
                    }
                },
                ...
            }
        """
        if use_cache and 'genres' in self._cache:
            return self._cache['genres']
        
        file_path = self.path / 'genre-styles.md'
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        genres = {}
        
        # Split by main genre sections (## Genre Name)
        genre_sections = re.split(r'\n## (.+?)\n', content)
        
        for i in range(1, len(genre_sections), 2):
            if i+1 >= len(genre_sections):
                break
                
            genre_name = genre_sections[i].strip().lower()
            genre_content = genre_sections[i+1]
            
            # Skip special sections
            if 'style variation' in genre_name.lower():
                # This is the style variations section, parse differently
                # Extract style variations for all genres
                style_sections = re.split(r'\n### (.+?) Style Variations\n', genre_content)
                
                for j in range(1, len(style_sections), 2):
                    if j+1 >= len(style_sections):
                        break
                    
                    variation_genre = style_sections[j].strip().lower()
                    variations_content = style_sections[j+1]
                    
                    # Parse individual style variations
                    styles = {}
                    style_blocks = re.split(r'\n#### (.+?)\n', variations_content)
                    
                    for k in range(1, len(style_blocks), 2):
                        if k+1 >= len(style_blocks):
                            break
                        
                        style_name = style_blocks[k].strip()
                        style_content = style_blocks[k+1]
                        
                        # Extract style parameters
                        bpm_match = re.search(r'- \*\*BPM\*\*: (.+)', style_content)
                        char_match = re.search(r'- \*\*Character\*\*: (.+)', style_content)
                        use_match = re.search(r'- \*\*Use\*\*: (.+)', style_content)
                        
                        style_key = style_name.lower().replace(' ', '_').replace('(', '').replace(')', '')
                        style_key = style_key.split('(')[0].strip('_')
                        
                        styles[style_key] = {
                            'name': style_name,
                            'bpm': bpm_match.group(1).strip() if bpm_match else "",
                            'character': char_match.group(1).strip() if char_match else "",
                            'use': use_match.group(1).strip() if use_match else ""
                        }
                    
                    # Add styles to the genre
                    if variation_genre not in genres:
                        genres[variation_genre] = {}
                    genres[variation_genre]['styles'] = styles
                
                continue
            
            # Skip table sections
            if genre_name.startswith('style variation summary'):
                continue
            
            genre_data = {}
            
            # Extract characteristics if present
            if '### General Characteristics' in genre_content:
                genre_data['has_characteristics'] = True
            
            genres[genre_name] = genre_data
        
        self._cache['genres'] = genres
        return genres
    
    # ============================================================
    # CHORD TYPES
    # ============================================================
    
    def get_chord_types(self, use_cache: bool = True) -> Dict[str, List[int]]:
        """
        Parse music-theory.md and return chord interval formulas
        
        Returns:
            {
                'major': [0, 4, 7],
                'minor': [0, 3, 7],
                ...
            }
        """
        if use_cache and 'chord_types' in self._cache:
            return self._cache['chord_types']
        
        file_path = self.path / 'music-theory.md'
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        chord_types = {}
        
        # Parse chord construction section
        # Look for patterns like: "Major triad: ... = [0, 4, 7]"
        chord_pattern = r'(?:^|\n)([A-Z][a-z\s]+(?:triad|chord|seventh)?):.+?=\s*\[(.+?)\]'
        
        for match in re.finditer(chord_pattern, content, re.MULTILINE):
            chord_name = match.group(1).strip().lower()
            chord_name = chord_name.replace(' triad', '').replace(' chord', '').strip()
            intervals = [int(x.strip()) for x in match.group(2).split(',')]
            chord_types[chord_name] = intervals
        
        # Add some common chord types if not found
        if not chord_types:
            chord_types = {
                'major': [0, 4, 7],
                'minor': [0, 3, 7],
                'diminished': [0, 3, 6],
                'augmented': [0, 4, 8],
                'maj7': [0, 4, 7, 11],
                'min7': [0, 3, 7, 10],
                'dom7': [0, 4, 7, 10],
            }
        
        self._cache['chord_types'] = chord_types
        return chord_types
    
    # ============================================================
    # UTILITY METHODS
    # ============================================================
    
    def clear_cache(self):
        """Clear all cached data"""
        self._cache = {}
    
    def get_all_data(self) -> Dict[str, Any]:
        """
        Load all reference data at once
        
        Returns:
            {
                'scales': {...},
                'progressions': {...},
                'mood_profiles': {...},
                'production_tips': {...},
                'bass_patterns': {...},
                'genres': {...},
                'chord_types': {...}
            }
        """
        return {
            'scales': self.get_scales(),
            'progressions': self.get_chord_progressions(),
            'mood_profiles': self.get_mood_profiles(),
            'production_tips': self.get_production_tips(),
            'bass_patterns': self.get_bass_patterns(),
            'genres': self.get_genre_styles(),
            'chord_types': self.get_chord_types()
        }


# ============================================================
# CONVENIENCE FUNCTIONS
# ============================================================

def get_parser(references_path: str = "../references") -> ReferenceParser:
    """Get a ReferenceParser instance"""
    return ReferenceParser(references_path)

def load_scales() -> Dict:
    """Quick function to load scales"""
    return get_parser().get_scales()

def load_chord_progressions() -> Dict:
    """Quick function to load chord progressions"""
    return get_parser().get_chord_progressions()

def load_mood_profiles() -> Dict:
    """Quick function to load mood profiles"""
    return get_parser().get_mood_profiles()


# ============================================================
# TESTING
# ============================================================

if __name__ == "__main__":
    # Test the parser
    print("🧪 Testing ReferenceParser...")
    print("=" * 60)
    
    try:
        parser = ReferenceParser()
        
        print("\n1. Scales:")
        scales = parser.get_scales()
        print(f"   ✅ Loaded {len(scales)} scales")
        if scales:
            first_scale = list(scales.keys())[0]
            print(f"   Example: {first_scale}")
            print(f"   - Pattern: {scales[first_scale]['pattern']}")
            print(f"   - Moods: {scales[first_scale]['moods']}")
        
        print("\n2. Chord Progressions:")
        progs = parser.get_chord_progressions()
        print(f"   ✅ Loaded {len(progs)} mood categories")
        print(f"   Moods: {', '.join(list(progs.keys())[:5])}...")
        if progs:
            first_mood = list(progs.keys())[0]
            print(f"   {first_mood.capitalize()} has {len(progs[first_mood])} progressions")
        
        print("\n3. Mood Profiles:")
        profiles = parser.get_mood_profiles()
        print(f"   ✅ Loaded {len(profiles)} mood profiles")
        if profiles:
            first_profile = list(profiles.keys())[0]
            profile_data = profiles[first_profile]
            print(f"   Example: {first_profile}")
            print(f"   - Preferred intervals: {profile_data.get('preferred_intervals', 'N/A')}")
            print(f"   - Direction bias: {profile_data.get('direction_bias', 'N/A')}")
        
        print("\n4. Production Tips:")
        tips = parser.get_production_tips('dark')
        print(f"   ✅ Dark mood tip categories: {list(tips.keys())}")
        if tips and 'sound_design' in tips:
            print(f"   Example tip: {tips['sound_design'][0][:60]}...")
        
        print("\n5. Bass Patterns:")
        patterns = parser.get_bass_patterns()
        print(f"   ✅ Loaded {len(patterns)} bass patterns")
        print(f"   Patterns: {', '.join(list(patterns.keys())[:5])}...")
        if patterns:
            first_pattern = list(patterns.keys())[0]
            print(f"   {first_pattern}: {patterns[first_pattern]['description'][:50]}...")
        
        print("\n6. Genre Styles:")
        genres = parser.get_genre_styles()
        print(f"   ✅ Loaded {len(genres)} genres")
        print(f"   Genres: {', '.join(list(genres.keys())[:5])}...")
        if genres:
            for genre, data in list(genres.items())[:3]:
                if 'styles' in data:
                    print(f"   {genre.capitalize()}: {len(data['styles'])} styles")
        
        print("\n7. Chord Types:")
        chords = parser.get_chord_types()
        print(f"   ✅ Loaded {len(chords)} chord types")
        print(f"   Types: {', '.join(list(chords.keys())[:5])}...")
        
        print("\n" + "=" * 60)
        print("✅ All tests passed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
