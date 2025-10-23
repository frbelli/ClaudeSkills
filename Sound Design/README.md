# 🎹 Sound Design Skill - README

## Contenuto della Cartella

Questa cartella contiene la tua **Sound Design Skill** completa e funzionante, pronta per essere importata in Claude.

### 📦 File Principali

| File | Descrizione |
|------|-------------|
| **sound-design.skill** | ⭐ La skill completa (da importare in Claude) |
| **Sound_Design_Skill_Guida.md** | 📖 Guida completa in italiano |
| **Esempi_Pratici.md** | 💡 Esempi d'uso dettagliati |

### 🎛️ File di Esempio (Dimostrativi)

| File | Descrizione |
|------|-------------|
| **esempio_bass_techno.json** | Specifica per generare preset bass |
| **esempio_signal_flow.json** | Specifica per diagramma routing |
| **Dark_Techno_Bass.vital** | Preset Vital generato (esempio) |
| **esempio_signal_flow_diagram.svg** | Diagramma SVG del segnale |
| **pattern_techno_techno_128bpm.mid** | File MIDI pattern techno |

## 🚀 Quick Start

### 1. Importa la Skill in Claude

1. Apri Claude
2. Vai su **Menu → Skills**
3. Clicca **Import Skill**
4. Seleziona **sound-design.skill**
5. ✅ La skill è attiva!

### 2. Inizia ad Usarla

Prova queste query:

```
"Crea un bass techno per Vital"
"Come programmo un pad sulla Matriarch?"
"Analizza questo suono e dimmi come ricrearlo"
"Genera un pattern trap a 140 BPM"
```

## 📚 Documentazione

### Leggi Prima:
1. **Sound_Design_Skill_Guida.md** - Guida completa con tutte le funzionalità
2. **Esempi_Pratici.md** - Esempi concreti di conversazioni con Claude

### Synth Supportati:

**Hardware:**
- Elektron Digitone II
- Moog Matriarch, DFAM, Subharmonicon
- Behringer Crave
- Make Noise 0-Coast

**Software:**
- Vital (con generazione preset!)
- Serum, Massive X, Diva, Pigments 6

## ⚙️ Dipendenze Opzionali

Per usare tutte le funzionalità degli script Python:

```bash
# Per analisi audio
pip install librosa --break-system-packages

# Per generazione MIDI
pip install mido --break-system-packages
```

**Nota**: La skill funziona anche senza queste librerie, con funzionalità ridotte.

## 🎯 Cosa Può Fare

✅ Creare patch per synth (hardware e software)  
✅ Generare preset Vital pronti all'uso (.vital)  
✅ Analizzare file audio esistenti  
✅ Generare pattern MIDI ritmici  
✅ Creare diagrammi SVG del routing del segnale  
✅ Guide step-by-step per programmare synth  
✅ Supporto per synth modulari (patch routing)  
✅ Adattamento per genere musicale  
✅ Gestione voci (mono/poly/unison)  

## 📖 Contenuto della Skill

### Reference Files (Conoscenza)
- **synth-parameters.md** - Tutti i parametri dei synth
- **sound-archetypes.md** - Caratteristiche per tipo di suono
- **genre-styles.md** - Approcci per genere musicale
- **synth-database.md** - Database dei tuoi synth specifici

### Scripts (Automazione)
- **analyze_audio.py** - Analisi file audio
- **generate_rhythm.py** - Generazione pattern MIDI
- **generate_vital_preset.py** - Generazione preset Vital
- **generate_signal_diagram.py** - Diagrammi SVG routing

## 💡 Tips

### Per Risultati Ottimali:

1. **Sii specifico** nella richiesta
   - ❌ "voglio un bass"
   - ✅ "voglio un reese bass per drum and bass sul Digitone II"

2. **Specifica sempre il synth**
   - Claude adatterà le istruzioni al tuo hardware/software

3. **Chiedi file quando possibile**
   - "genera anche il preset Vital"
   - "crea il diagramma del routing"
   - "dammi il file MIDI"

4. **Usa l'analisi per sound design inverso**
   - Carica audio di riferimento
   - Claude estrarrà le caratteristiche
   - Riceverai i parametri per ricreare il suono

## 🎵 Generi Musicali Supportati

- Vintage/Analog (70s-80s)
- Techno
- House (Deep/Tech)
- IDM
- Ambient/Drone
- Synthwave/Retrowave
- Dubstep/Bass Music
- Trap/Hip-Hop
- Psytrance
- Industrial/EBM
- Drum & Bass
- Breakbeat

## 🔧 Tipologie di Suono

**Bass:** Sub Bass, Reese, Acid, 808  
**Lead:** Synth Lead, Pluck, Supersaw  
**Pad:** Ambient, String, Drone  
**Keys:** Electric Piano, Bells, Marimba  
**Texture:** Granular, Noise Sweep, Evolving  
**Percussion:** Kick, Snare, Hi-Hat  

## 🎛️ Workflow Tipico

```
1. Tu: "Voglio creare un [tipo suono] per [genere] su [synth]"
   
2. Claude: 
   - Legge i reference files
   - Identifica caratteristiche necessarie
   - Prepara la configurazione
   
3. Claude ti fornisce:
   - Parametri dettagliati
   - File generati (preset/MIDI/diagrammi)
   - Guide step-by-step
   - Tips di programmazione
   
4. Tu: "Perfetto! Ora fammi una variazione più [caratteristica]"
   
5. Claude: Crea variazioni basate su feedback
```

## 📞 Supporto

### Hai Problemi?

**La skill non si importa:**
- Verifica che il file .skill non sia corrotto
- Riprova l'import
- Controlla la versione di Claude

**Gli script non funzionano:**
- Verifica di aver installato le dipendenze Python
- Controlla i permessi di esecuzione
- Gli script funzionano anche senza librerie (con funzionalità ridotte)

**I preset non si caricano nel synth:**
- Verifica la compatibilità della versione
- Controlla il formato del file
- Vital: file .vital dovrebbe essere JSON valido

## 🎓 Risorse Aggiuntive

### Impara di Più:

1. **Synthesis Basics**: La skill spiega tutti i concetti
2. **Modular Patching**: Guide complete per synth semi-modulari
3. **Sound Design Theory**: Integrato nei reference files
4. **Genre-Specific Techniques**: Per ogni stile musicale

### Estendere la Skill:

Puoi aggiungere:
- Nuovi synth nel database
- Pattern ritmici personalizzati
- Template di preset per altri formati
- Analisi MIDI esistenti

## ✨ Caratteristiche Uniche

🎯 **Supporto Multi-Synth**: 11 synth diversi  
🎵 **10+ Generi**: Da ambient a techno  
🤖 **Generazione Automatica**: Preset, MIDI, diagrammi  
📊 **Analisi Audio**: Reverse engineering di suoni  
🎛️ **Modular Support**: Routing completo per semi-modulari  
📖 **Step-by-Step**: Guide dettagliate per ogni synth  

## 🙏 Crediti

Skill creata per supportare il workflow di sound design professionale.

**Tecnologie utilizzate:**
- Python (scripts)
- JSON (preset Vital)
- SVG (diagrammi)
- MIDI (pattern ritmici)

**Librerie Python:**
- librosa (analisi audio)
- mido (generazione MIDI)

## 📄 Licenza

Questa skill è stata creata su richiesta e può essere usata liberamente per scopi personali e professionali.

---

## 🎉 Pronto per Iniziare!

1. ✅ Importa **sound-design.skill** in Claude
2. 📖 Leggi **Sound_Design_Skill_Guida.md** per capire tutte le funzionalità
3. 💡 Consulta **Esempi_Pratici.md** per vedere casi d'uso concreti
4. 🎹 Inizia a creare suoni fantastici!

**Buon sound design!** 🎵🎛️🎹

---

*Per domande o feedback, usa la skill conversando direttamente con Claude!*
