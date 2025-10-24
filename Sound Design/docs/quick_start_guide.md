# 🚀 QUICK START: Usa Subito la Skill Espansa

Guida rapida per iniziare immediatamente a usare teoria musicale e composizione nella tua skill sound-design.

---

## ⚡ 3 PASSI PER INIZIARE ORA

### PASSO 1: Chiedi a Claude una composizione basata su mood

**Esempio 1**:
```
"Voglio creare un brano dark ambient, suggerisci scala e progressioni"
```

**Claude farà**:
- Leggerà automaticamente i file di teoria musicale
- Ti suggerirà scala (es. D Phrygian)
- Ti darà 3 progressioni con MIDI
- Ti darà tips per produzione

---

### PASSO 2: Combina con synth programming

**Esempio 2**:
```
"Crea un pad per questo mood e programmalo sulla Matriarch"
```

**Claude farà**:
- Suggerirà patch synth appropriato
- Lo programmerà nella scala giusta
- Ti darà il file completo

---

### PASSO 3: Aggiungi ritmo

**Esempio 3**:
```
"Aggiungi un pattern ritmico per questo brano"
```

**Claude farà**:
- Genererà pattern drum appropriato
- Creerà MIDI
- Suggerirà BPM adatto al mood

---

## 🎯 ESEMPI DI RICHIESTE CHE PUOI FARE SUBITO

### Composizione da Mood

**"Voglio un brano energetic, dammi progressioni e scala"**
- Output: Scala Mixolydian, 3 progressioni, MIDI files

**"Ho bisogno di chord progression sad ma con un po' di speranza"**
- Output: Progressioni bittersweet con esempi MIDI

**"Quali scale usi per musica dark mysterious?"**
- Output: Lista scale con caratteristiche e MIDI

---

### Synth Programming con Teoria

**"Crea un bass synth in D minor per techno"**
- Output: Patch bass + note MIDI corrette per D minor

**"Programma un pad ambientale in F Lydian sulla Matriarch"**
- Output: Patch completo ottimizzato per F Lydian

**"Voglio un lead synth che suoni happy e bright"**
- Output: Patch in scala major con sound design appropriato

---

### Workflow Completo

**"Crea un track completo dark techno in Em"**

Claude ti darà:
1. ✅ Scala: E Phrygian
2. ✅ Progressioni: 3 varianti con MIDI
3. ✅ Bass patch: Sound design specifico
4. ✅ Pattern drum: 128 BPM, 16 bars, IDM style
5. ✅ Arrangement tips: Struttura del brano

**"Voglio fare un ambient soundtrack style Blade Runner"**

Claude ti darà:
1. ✅ Mood analysis: Dark, atmospheric, nostalgic
2. ✅ Scale: C# Locrian o D Phrygian
3. ✅ Progressioni: Suspended, ambiguous chords
4. ✅ Synth patches: Multiple layers (pad, bass, texture)
5. ✅ Production tips: Reverb, space, movement

---

## 🎹 FILE CHE HAI A DISPOSIZIONE

### 1. Music Theory Reference
**File**: `music-theory.md`

**Contiene**:
- Tutti gli intervalli
- Scale e modi completi
- Costruzione accordi
- Voice leading
- Database MIDI per ogni scala

**Quando usarlo**:
- Capire teoria dietro alle progressioni
- Trovare note MIDI per scale
- Costruire accordi custom

---

### 2. Chord Progressions Database
**File**: `chord-progressions.md`

**Contiene**:
- Progressioni per ogni mood
- Progressioni per genere
- Esempi con MIDI
- Tecniche di variazione

**Quando usarlo**:
- Cercare progressioni per mood specifico
- Trovare alternative a progressioni esistenti
- Imparare progressioni classiche

---

### 3. Scales & Modes Database
**File**: `scales-modes.md`

**Contiene**:
- Tutte le scale importanti
- Caratteristiche di ogni scala
- MIDI values
- Uso per mood/genere

**Quando usarlo**:
- Scegliere scala per mood
- Capire differenze tra modi
- Trovare scale esotiche

---

### 4. Mood → Composition Script
**Script**: `mood_to_composition.py`

**Fa**:
- Genera suggerimenti automatici
- Crea MIDI delle progressioni
- Suggerisce production tips

**Come usarlo**:
```bash
python scripts/mood_to_composition.py dark
python scripts/mood_to_composition.py happy G
python scripts/mood_to_composition.py "sad atmospheric" Dm
```

---

## 💡 ESEMPI PRATICI STEP-BY-STEP

### ESEMPIO 1: Creare un Sad Pop Brano

**Prompt**:
```
"Voglio creare un brano sad pop type The Weeknd. Aiutami con composizione e sound design."
```

**Claude risponde con**:

**1. COMPOSIZIONE**
```
🎼 MOOD: Sad Pop
🎹 SCALA: A Minor (Natural Minor)
📝 PROGRESSIONE PRINCIPALE: Am - F - C - G
   (i - VI - III - VII)

Alternative:
1. Am - Dm - G - F (più scuro)
2. Am - C - G - F (più uplifting)
```

**2. SOUND DESIGN**
```
🎛️ SYNTH PATCHES:

Bass:
- Sub bass in A minor pentatonic
- Reese bass detuned per width

Lead:
- Synth lead con vibrato delayed
- Scala: A minor
- Add reverb e delay

Pad:
- String pad in Am
- Use Matriarch patch in A Aeolian
```

**3. RHYTHM**
```
🥁 DRUM PATTERN:
- Trap-style beat
- 140 BPM half-time (70 feel)
- Sparse kick pattern
- Rolling hi-hats
```

**4. MIDI FILES**
Claude genera e ti dà:
- `progression_sad_Am.mid`
- `bass_line_Am.mid`
- `drum_pattern_trap_140.mid`

---

### ESEMPIO 2: Dark Techno Track

**Prompt**:
```
"Crea un dark techno track completo in D minor, 130 BPM"
```

**Claude workflow**:

**Step 1**: Analizza mood → "dark", "energetic", "techno"

**Step 2**: Composizione
```
🎼 SCALA: D Phrygian (D-Eb-F-G-A-Bb-C)
📝 PROGRESSIONE: Dm - Eb - F - Dm (i - bII - bIII - i)
```

**Step 3**: Sound Design
```
🎛️ PATCHES NECESSARI:

1. KICK: Punchy, sub-heavy (60Hz)
2. BASS: Reese in D, filter automation
3. LEAD: FM stabs su Digitone, Phrygian scale
4. PAD: Dark ambient pad, D Phrygian root
5. PERCUSSION: Industrial hits, metallic
```

**Step 4**: Rhythm
```
python scripts/generate_rhythm.py techno 130 16
```

**Step 5**: Arrangement
```
STRUCTURE:
Bars 1-16:   Intro (kick + bass)
Bars 17-32:  Build (add percussion)
Bars 33-48:  Drop (full elements)
Bars 49-64:  Breakdown
Bars 65-80:  Final drop
Bars 81-96:  Outro
```

**Output**: Tutti i file MIDI + guida dettagliata

---

## 🎓 TRUCCHI & TIPS

### Tip 1: Combina Mood per Risultati Unici

Invece di:
```
"dark"
```

Prova:
```
"dark atmospheric with a touch of hope"
"energetic but melancholic"
"dreamy and mysterious"
```

Claude combinerà suggerimenti da mood multipli!

---

### Tip 2: Specifica Root Key

Invece di:
```
"voglio progressioni sad"
```

Prova:
```
"voglio progressioni sad in E minor"
```

Otterrai tutto già nella tonalità giusta!

---

### Tip 3: Chiedi Variazioni

Dopo aver ricevuto una progressione:
```
"dammi altre 3 variazioni più complesse"
"aggiungi extended chords (9th, 11th)"
"rendi questa progressione più jazzy"
```

---

### Tip 4: Integra con Synth Esistenti

```
"usa questa progressione [Am-F-C-G] e programmala come pad sulla Matriarch"
"crea un bass patch per il Digitone che segua questi accordi"
```

---

### Tip 5: Chiedi Spiegazioni

```
"perché questa scala funziona per mood dark?"
"spiegami la teoria dietro questa progressione"
"come posso variare questa progressione rimanendo nello stesso mood?"
```

---

## 🎬 ESEMPI DI GENERI SPECIFICI

### House
```
"Crea progressioni per deep house in G minor"
```
→ Claude usa chord-progressions.md sezione House

### Trance
```
"Uplifting trance in C major, progressioni emotionali"
```
→ Progressioni euphoric, major key

### Ambient
```
"Soundscape ambientale, minimalista, in F Lydian"
```
→ Suspended chords, sparse progressions

### Drum & Bass
```
"Liquid DnB in A minor, progressioni smooth"
```
→ Jazzy chords, maj7 sounds, 170 BPM

---

## 📊 CHEAT SHEET RAPIDO

### Mood → Scala

| Mood | Scale Consigliate |
|------|------------------|
| Dark | Phrygian, Locrian, Harmonic Minor |
| Happy | Major, Lydian, Major Pentatonic |
| Sad | Minor, Dorian, Minor Pentatonic |
| Mysterious | Phrygian Dominant, Whole Tone |
| Energetic | Mixolydian, Dorian |
| Dreamy | Lydian, Major 7th chords |
| Epic | Harmonic Minor, Dorian |

### BPM per Genere

| Genere | BPM Range |
|--------|-----------|
| House | 120-130 |
| Techno | 125-135 |
| Trance | 130-145 |
| Dubstep | 140 (half-time 70) |
| Drum & Bass | 160-180 |
| Ambient | 60-90 |
| Trap | 140-160 |

---

## ✅ CHECKLIST: Prima Sessione di Produzione

Prima di iniziare un brano:

- [ ] Definisci il mood/atmosfera
- [ ] Chiedi a Claude scala e progressioni
- [ ] Genera MIDI delle progressioni per testare
- [ ] Scegli synth appropriati per il mood
- [ ] Genera pattern drum nel giusto stile
- [ ] Crea struttura/arrangement
- [ ] Inizia la produzione!

---

## 🎯 PROSSIMI STEP

Ora che hai tutto:

1. **Testa il sistema**: Chiedi una composizione semplice
2. **Esplora i file**: Leggi music-theory.md per approfondire
3. **Combina funzionalità**: Mood + Synth + Rhythm in un workflow
4. **Crea brani completi**: Usa tutti gli strumenti insieme
5. **Espandi**: Aggiungi nuovi mood, synth, scale

---

## 🆘 RISOLUZIONE PROBLEMI

**Q**: Claude non usa i nuovi file?
**A**: Ricordagli: "Usa i file di teoria musicale per questa richiesta"

**Q**: Voglio più dettagli teorici?
**A**: Chiedi: "Spiegami la teoria dietro questo"

**Q**: I MIDI files non si aprono?
**A**: Controlla formato (.mid) e prova con DAW diversa

**Q**: Come aggiungo nuovi mood?
**A**: Vedi `skill_expansion_guide.md` sezione "Aggiungere Altri Mood"

---

## 🎉 SEI PRONTO!

Hai ora:
✅ Teoria musicale completa
✅ Database di progressioni
✅ Generatore automatico
✅ Integrazione con synth programming
✅ Workflow produzione completi

**Inizia ora con**:
```
"Claude, crea un brano [MOOD] in [KEY] con synth e drums"
```

🎛️ **Happy music making!** ✨
