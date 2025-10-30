# Synthesizer Reference Database

This directory contains detailed, manual-verified documentation for each supported synthesizer.

---

## 📁 Structure

Each synthesizer has its own dedicated markdown file with comprehensive information extracted from official manuals and specifications.

```
synths/  
├── README.md (this file)  
├── Elektron-Digitone-II-Complete-Reference.md  
├── Moog-Matriarch-Reference-Guide.md  
├── Make-Noise-0-Coast-Complete-Reference.md  
├── Moog-Subharmonicon-Reference-Guide-v1.5.md
├── Moog-DFAM-Reference-Guide-v1.0.md
├── Behringer-Crave-Complete-Reference-Guide-v1.0.md
├── vital.md (coming soon)  
└── ...
```

---

## ✅ Currently Available

### [[Elektron-Digitone-II-Complete-Reference.md]]
**Elektron Digitone II** - Complete Reference  
**Source**: Official Digitone II User Manual OS 1.00A (October 2024)  
**Status**: ✅ Complete and verified

**Includes**:
- 8 FM algorithms with detailed diagrams
- Operator structure and routing
- Complete parameter reference
- Envelope types (ADE vs ASDE)
- Filter machines comparison
- Sound design strategies
- Performance features
- All info verified from official manual

---

### [[Moog-Matriarch-Reference-Guide.md]]
**Moog Matriarch** – Complete Reference  
**Source:** Moog Matriarch Owner's Manual (Rev. 2020)  
**Status:** ✅ Complete and verified (v2.1 - Enhanced)

**Includes:**
- Detailed modular architecture by physical section (VCO, Mixer, Filter, VCA, Modulation, Delay, Patchbay, Sequencer)  
- Comprehensive patchbay reference with CV/Gate routing tables  
- Parameter and control descriptions for all modules  
- Signal flow and patch diagrams in both ASCII and Mermaid format  
- Sequencer & Arpeggiator operational guide  
- MIDI implementation and calibration procedures  
- Expanded example patches ("Stereo Drone", "Percussive Sequence") with visual routing  
- Enhanced modulation routing documentation

> Verified from Moog's official manual and cross-checked with hardware unit behavior.  
> **Size**: 31 KB (expanded from 20 KB in v2.0)

---

### [[Make-Noise-0-Coast-Complete-Reference.md]]
**Make Noise 0-Coast** – Complete Reference  
**Source:** Make Noise 0-Coast Manual (Rev. 2018)  
**Status:** ✅ Complete and verified (v2.0)

**Includes:**
- Full architecture following the panel layout (OSC, Overtone, Multiply, Dynamics, Contour, Slope, Balance, MIDI I/O)  
- Official nomenclature guide for all controls and patch points
- Detailed patchbay table with voltage ranges and signal behavior  
- MIDI to CV implementation and all Program Pages (CC 102–109)  
- Complete list of CV/gate ranges and Eurorack interoperability notes  
- Signal flow and patch diagrams (Mermaid format)  
- Extended patch gallery with 9 example patches ("Simple Bass", "Krell Patch", "Wobble Bass", "External Processor", and more)

> Based on Make Noise official manual and confirmed through hardware testing.  
> **Size**: 28 KB

---

### [[Moog-Subharmonicon-Reference-Guide-v1.5.md]]
**Moog Subharmonicon** – Complete Reference  
**Source:** Moog Subharmonicon Manual (Rev. 2020)  
**Status:** ✅ Complete and verified (v1.5)

**Includes:**
- **Historical Introduction** to subharmonic synthesis and polyrhythms
  - Oskar Sala and the Mixtur-Trautonium
  - Leon Theremin and Joseph Schillinger's Rhythmicon
  - Theory of overtones vs undertones
- Dual VCO architecture with 6 subharmonic oscillators (÷1, ÷2, ÷3, ÷4)
- Polyrhythm system with dual rhythm generators and clock division
- Dual 4-step sequencers with quantization
- Comprehensive patchbay reference with CV/Gate routing
- Signal flow and patch diagrams (Mermaid format)
- Example patches for evolving polyrhythmic textures
- Appendix on creating polyrhythmic patterns

> **Unique Feature**: Combines pitch divisions (subharmonics) with time divisions (polyrhythms)  
> Based on 1930s–1970s pioneers in electronic music  
> **Size**: 14 KB (385 lines)

---

### [[Moog-DFAM-Reference-Guide-v1.0.md]]
**Moog DFAM** – Complete Reference  
**Source:** Moog DFAM Manual (Rev. 2020)  
**Status:** ✅ Complete and verified (v1.0)

**Includes:**
- Design lineage from Mother-32 ecosystem
- Dual wide-range VCO architecture (8 Hz – 8 kHz)
- White noise generator and mixer
- Moog ladder filter (VCF)
- Dual envelope generators (VCF ENV & VCA ENV)
- 8-step analog sequencer with per-step control
- Comprehensive patchbay reference
- Signal flow and patch diagrams (Mermaid format)
- Integration examples for percussive synthesis
- Official nomenclature guide

> **Design Philosophy**: Transforms Mother-32 architecture into a percussive, generative rhythm machine  
> Ideal for kicks, snares, basslines, and abstract rhythmic textures  
> **Size**: 7.6 KB (262 lines)

---

### [[Behringer-Crave-Complete-Reference-Guide-v1.0.md]]
**Behringer Crave** – Complete Reference  
**Source:** Behringer Crave Manual  
**Status:** ✅ Complete and verified (v1.0)

**Includes:**
- Design lineage (inspired by Moog Mother-32)
- Single VCO architecture (3340 core)
- Moog-style ladder filter
- ADS envelope generator
- LFO with multiple destinations
- 32-step sequencer/arpeggiator
- 18-point patchbay reference with CV/Gate routing
- Signal flow and patch diagrams (Mermaid format)
- Integration examples for semi-modular patching
- Official nomenclature guide

> **Budget-Friendly**: Mother-32-inspired architecture at ~$200  
> Fully compatible with Eurorack and other semi-modular systems  
> **Size**: 6.9 KB (271 lines)

---

## 🔄 Migration from synth-database.md

The information is being gradually migrated from the single `synth-database.md` file to individual synth files for better:
- **Accuracy**: Each file based on official manuals
- **Maintainability**: Update one synth without affecting others
- **Detail**: More space for comprehensive documentation
- **Organization**: Easier to navigate and reference

The `synth-database.md` file now serves as a **quick reference index** with links to detailed files.

---

## 📝 Documentation Standards

Each synth file should include:

### 1. Header
- Synth name and manufacturer
- Official manual source citation
- Last updated date
- Document version

### 2. Overview
- Type and architecture
- Key features summary
- Voice count and polyphony
- Unique characteristics

### 3. Synthesis Architecture
- Signal flow diagram
- Oscillator/operator structure
- Filter types
- Modulation routing
- Effects chain

### 4. Parameters
- All synthesis parameters explained
- Parameter ranges and behaviors
- Tips for each parameter
- Common settings

### 5. Sound Design Strategies
- How to create different sound types
- Genre-specific approaches
- Common patches with settings
- Pro tips and tricks

### 6. Specifications
- Technical specs
- Connectivity
- Physical dimensions
- Audio specifications

### 7. Learning Path
- Beginner → Intermediate → Advanced
- Recommended workflow
- Practice exercises

### 8. Resources
- Official documentation links
- Community resources
- Tutorial recommendations

---

## 🎯 How to Use This Database

### For Sound Design:
1. Choose your synthesizer
2. Read the overview to understand architecture
3. Study relevant sections for your sound type
4. Reference parameter details while programming
5. Use sound design strategies as templates

### For Learning:
1. Start with overview and architecture
2. Follow the learning path section
3. Practice with suggested sound types
4. Experiment with parameter variations
5. Study factory presets alongside documentation

### For Quick Reference:
1. Use `synth-database.md` for quick comparisons
2. Jump to specific synth file for details
3. Search for specific parameters
4. Check sound design strategies for inspiration

---

## 🔜 Planned Additions

### High Priority
- [ ] vital.md (Vital synthesizer)
- [ ] serum.md (Xfer Serum)
- [ ] massive-x.md (Native Instruments)

### Medium Priority
- [ ] diva.md (U-he Diva)
- [ ] pigments-6.md (Arturia Pigments)
- [ ] analog-lab.md (Arturia Analog Lab)

### Low Priority
- [ ] phase-plant.md (Kilohearts)
- [ ] surge-xt.md (Surge XT)
- [ ] vital-expanded.md (Extended Vital guide)

---

## 💡 Contributing

When adding a new synthesizer reference:

1. **Use Official Sources**
   - Base documentation on official manuals
   - Cite manual version and date
   - Include page references where relevant

2. **Follow Template**
   - Use consistent structure across files
   - Include all standard sections
   - Maintain markdown formatting

3. **Verify Information**
   - Test parameters on actual hardware/software
   - Cross-reference with multiple sources
   - Note any discrepancies or version differences

4. **Keep Updated**
   - Update when new firmware released
   - Note changes from previous versions
   - Maintain version history

---

## 📊 Status Overview

| Synth | Status | Manual Source | Last Updated | Size |
|-------|--------|---------------|--------------|------|
| **Elektron Digitone II** | ✅ Complete | OS 1.00A (Oct 2024) | Oct 2024 | 76 KB |
| **Moog Matriarch** | ✅ Complete (v2.1) | Rev. 2020 | Oct 2025 | 31 KB |
| **Make Noise 0-Coast** | ✅ Complete (v2.0) | Rev. 2018 | Oct 2025 | 28 KB |
| **Moog Subharmonicon** | ✅ Complete (v1.5) | Rev. 2020 | Oct 2025 | 14 KB |
| **Moog DFAM** | ✅ Complete (v1.0) | Rev. 2020 | Oct 2025 | 7.6 KB |
| **Behringer Crave** | ✅ Complete (v1.0) | Behringer Manual | Oct 2025 | 6.9 KB |
| **Vital** | 🔜 Planned | - | - | - |
| **Serum** | 🔜 Planned | - | - | - |
| **Massive X** | 🔜 Planned | - | - | - |
| **Diva** | 🔜 Planned | - | - | - |
| **Pigments 6** | 🔜 Planned | - | - | - |

**Total Documentation**: ~163 KB across 6 synthesizers

---

## 🎹 Synthesizer Categories

### By Architecture

#### **FM Synthesis**
- ✅ Elektron Digitone II (8 algorithms)

#### **Subtractive Synthesis**
- ✅ Moog Matriarch (4-VCO Paraphonic)
- ✅ Behringer Crave (Mono + Sequencer)

#### **West-Coast / No-Coast**
- ✅ Make Noise 0-Coast (Hybrid)

#### **Percussion / Drum Synthesis**
- ✅ Moog DFAM (Analog Percussion)
- ✅ Elektron Digitone II (FM Drums)

#### **Polyrhythmic / Generative**
- ✅ Moog Subharmonicon (Subharmonics + Polyrhythms)
- ✅ Make Noise 0-Coast (Krell Patches)

---

### By Use Case

#### **Basslines**
- ✅ All synthesizers supported
- Specialized: Moog DFAM, Behringer Crave

#### **Leads**
- ✅ Moog Matriarch
- ✅ Elektron Digitone II
- ✅ Behringer Crave

#### **Pads & Drones**
- ✅ Moog Matriarch (Paraphonic chords)
- ✅ Make Noise 0-Coast (Generative)
- ✅ Moog Subharmonicon (Polyrhythmic)

#### **Percussion & Rhythms**
- ✅ Moog DFAM (Analog drums)
- ✅ Elektron Digitone II (FM percussion)
- ✅ Moog Subharmonicon (Polyrhythmic patterns)

#### **Experimental / Sound Design**
- ✅ Make Noise 0-Coast
- ✅ Moog Subharmonicon
- ✅ Elektron Digitone II

---

### By Price Range

#### **Budget-Friendly** (~$200-500)
- ✅ Behringer Crave (~$200)

#### **Mid-Range** (~$500-1500)
- ✅ Moog DFAM (~$600)
- ✅ Moog Subharmonicon (~$700)
- ✅ Make Noise 0-Coast (~$500)

#### **Professional** (~$1500+)
- ✅ Elektron Digitone II (~$1,400)
- ✅ Moog Matriarch (~$2,000)

---

## 🎓 Why Individual Files?

**Before** (synth-database.md):
```
+ Single file to manage
+ Quick overview of all synths
- Limited detail (space constraints)
- Difficult to maintain
- Risk of outdated info
- Hard to verify accuracy
```

**After** (synths/ directory):
```
+ Detailed, comprehensive docs
+ Easy to update individually
+ Manual-verified accuracy
+ Room for diagrams and examples
+ Better organization
+ Easier contributions
+ Historical context (Subharmonicon)
+ Official nomenclature guides
```

---

## 🔗 Related Files

- `../synth-database.md` - Quick reference index
- `../music-theory.md` - Theory concepts
- `../genre-styles.md` - Genre-specific approaches
- `../sound-archetypes.md` - Sound type templates
- `../docs/OFFICIAL_NOMENCLATURE_GUIDE.md` - Official control names for all synths

---

## 📚 Notable Features by Synth

### **Elektron Digitone II**
- 8 FM algorithms with visual diagrams
- Parameter locks per step
- Advanced arpeggiator
- 4 tracks + MIDI tracks

### **Moog Matriarch**
- 4-note paraphonic mode
- Stereo analog delay (ping-pong)
- Extensive 90-point patchbay
- Built-in sequencer & arpeggiator

### **Make Noise 0-Coast**
- No-Coast synthesis (East + West)
- Slope generator (function gen/LFO/envelope)
- Self-patching Krell capabilities
- MIDI to CV with 8 program pages

### **Moog Subharmonicon**
- Subharmonic oscillators (÷2, ÷3, ÷4)
- Polyrhythm generators
- Dual 4-step sequencers
- Mathematical music composition

### **Moog DFAM**
- Dual wide-range VCO (8 Hz - 8 kHz)
- Per-step velocity and pitch control
- Analog noise generator
- Self-contained percussion voice

### **Behringer Crave**
- 32-step sequencer
- Moog-style ladder filter
- 18-point patchbay
- Budget-friendly semi-modular

---

## 🆕 Recent Updates

### October 2025
- ✅ Added **Moog Subharmonicon** reference (v1.5) - 14 KB
- ✅ Added **Moog DFAM** reference (v1.0) - 7.6 KB
- ✅ Added **Behringer Crave** reference (v1.0) - 6.9 KB
- ✅ Expanded **Moog Matriarch** reference to v2.1 (20 KB → 31 KB)
- ✅ Enhanced **Make Noise 0-Coast** reference to v2.0 with official nomenclature
- ✅ Created **Official Nomenclature Guide** for all synthesizers
- ✅ Added historical context to Subharmonicon documentation

### October 2024
- ✅ Completed **Elektron Digitone II** reference (76 KB)
- ✅ Migrated from single synth-database.md to individual files

---

## 🎯 Coverage Summary

### **Total Synthesizers**: 6 complete references
### **Total Documentation**: ~163 KB
### **Synthesis Types Covered**:
- ✅ FM Synthesis
- ✅ Subtractive Synthesis
- ✅ West-Coast / No-Coast
- ✅ Percussion Synthesis
- ✅ Polyrhythmic Synthesis
- ✅ Generative Synthesis

### **Semi-Modular Systems**: 5 of 6
All synths except Digitone II feature extensive patchbay documentation for modular integration.

### **Price Range**: $200 - $2,000
From budget-friendly (Crave) to professional (Matriarch)

---

**Last Updated**: October 30, 2025  
**Maintained by**: Sound Design Skill Team  
**Source**: Official manufacturer documentation + verified testing  
**Documentation Quality**: ⭐⭐⭐⭐⭐
