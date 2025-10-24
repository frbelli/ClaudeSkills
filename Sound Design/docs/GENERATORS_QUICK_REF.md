# 🚀 QUICK REFERENCE - GENERATORI MUSICALI

## 🎹 generate_harmony.py

### Comando Base
```bash
python generate_harmony.py --mood MOOD --genre GENRE --key KEY
```

### Esempi Rapidi
```bash
# Dark techno
python generate_harmony.py --mood dark --genre techno --key Dm

# Happy house
python generate_harmony.py --mood happy --genre house --key C --bars 16

# Atmospheric ambient
python generate_harmony.py --mood atmospheric --genre ambient --key F --scale lydian
```

### Parametri Principali

| Parametro | Valori | Default |
|-----------|--------|---------|
| --mood | dark, happy, sad, calm, energetic | required |
| --genre | techno, house, ambient, trance, dubstep | required |
| --key | C, Dm, F#, etc. | Am |
| --bars | 1-64 | 8 |
| --bpm | 60-200 | 120 |

---

## 🥁 generate_drum_pattern.py

### Comando Base
```bash
python generate_drum_pattern.py --genre GENRE --energy LEVEL
```

### Esempi Rapidi
```bash
# Techno driving
python generate_drum_pattern.py --genre techno --energy high --bars 8

# House groovy
python generate_drum_pattern.py --genre house --energy medium --swing 0.1 --humanize

# Trap aggressive
python generate_drum_pattern.py --genre trap --complexity high --bpm 150
```

### Parametri Principali

| Parametro | Valori | Default |
|-----------|--------|---------|
| --genre | techno, house, dubstep, dnb, trap, ambient | required |
| --energy | low, medium, high | medium |
| --complexity | low, medium, high | medium |
| --bars | 1-64 | 8 |
| --swing | 0.0-0.3 | 0.0 |
| --humanize | flag | False |

---

## 🎼 COMBINAZIONI CONSIGLIATE

### Dark Techno
```bash
python generate_harmony.py --mood dark --genre techno --key Dm --bpm 138
python generate_drum_pattern.py --genre techno --energy high --bpm 138 --humanize
```

### Uplifting House
```bash
python generate_harmony.py --mood happy --genre house --key C --bars 16
python generate_drum_pattern.py --genre house --mood happy --swing 0.08 --humanize
```

### Deep Dubstep
```bash
python generate_harmony.py --mood dark --genre dubstep --key D --bpm 140
python generate_drum_pattern.py --genre dubstep --energy medium --complexity high --bpm 140
```

### Liquid DnB
```bash
python generate_harmony.py --mood atmospheric --genre dnb --key Am --scale dorian
python generate_drum_pattern.py --genre dnb --energy medium --complexity high --humanize
```

### Chill Ambient
```bash
python generate_harmony.py --mood calm --genre ambient --key F --scale lydian --bpm 80 --bars 32
python generate_drum_pattern.py --genre ambient --energy low --complexity low --bpm 80 --bars 32
```

---

## 💡 TIPS RAPIDI

### Harmony
- **Phrygian** → dark/industrial
- **Lydian** → atmospheric/dreamy
- **Mixolydian** → energetic/driving
- Usa `--progression` per custom chords

### Drums
- `--humanize` → sempre ON per realismo
- `--swing 0.08-0.12` → house/funk feel
- `--complexity high` → fills e breaks
- `--energy` progressivo: low → high

---

## 📥 OUTPUT FILES

**Harmony**: `harmony_{mood}_{genre}_{key}.mid`  
**Drums**: `drums_{genre}_{energy}_{complexity}.mid`

Import nella DAW e assegna ai synth!

---

**Files**: 
- [generate_harmony.py](computer:///mnt/user-data/outputs/generate_harmony.py)
- [generate_drum_pattern.py](computer:///mnt/user-data/outputs/generate_drum_pattern.py)
- [Documentazione completa](computer:///mnt/user-data/outputs/NEW_GENERATORS_DOCUMENTATION.md)
