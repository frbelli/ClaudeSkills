# Synthesizer Reference Database

This directory contains detailed, manual-verified documentation for each supported synthesizer.

---

## 📁 Structure

Each synthesizer has its own dedicated markdown file with comprehensive information extracted from official manuals and specifications.

```
synths/
├── README.md (this file)
├── digitone-ii.md
├── moog-matriarch.md (coming soon)
├── vital.md (coming soon)
└── ...
```

---

## ✅ Currently Available

### [digitone-ii.md](digitone-ii.md)
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
- [ ] moog-matriarch.md
- [ ] vital.md
- [ ] serum.md

### Medium Priority
- [ ] moog-dfam.md
- [ ] moog-subharmonicon.md
- [ ] massive-x.md

### Low Priority
- [ ] diva.md
- [ ] pigments-6.md
- [ ] behringer-crave.md
- [ ] make-noise-0-coast.md

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

| Synth | Status | Manual Source | Last Updated |
|-------|--------|---------------|--------------|
| Digitone II | ✅ Complete | OS 1.00A (Oct 2024) | Oct 2024 |
| Moog Matriarch | 🔜 Planned | - | - |
| Vital | 🔜 Planned | - | - |
| Serum | 🔜 Planned | - | - |
| Massive X | 🔜 Planned | - | - |
| Diva | 🔜 Planned | - | - |
| Pigments 6 | 🔜 Planned | - | - |
| DFAM | 🔜 Planned | - | - |
| Subharmonicon | 🔜 Planned | - | - |
| Crave | 🔜 Planned | - | - |
| 0-Coast | 🔜 Planned | - | - |

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
```

---

## 🔗 Related Files

- `../synth-database.md` - Quick reference index
- `../music-theory.md` - Theory concepts
- `../genre-styles.md` - Genre-specific approaches
- `../sound-archetypes.md` - Sound type templates

---

**Last Updated**: October 2024  
**Maintained by**: Sound Design Skill Team  
**Source**: Official manufacturer documentation + verified testing
