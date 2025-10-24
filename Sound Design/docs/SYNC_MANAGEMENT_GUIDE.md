# 🔄 GESTIONE SKILL: LOCALE → GITHUB → CLAUDE

Guida completa per sincronizzare la skill sound-design tra i tre ambienti.

---

## 📍 I TRE AMBIENTI

### 1. **LOCALE** (Il tuo computer)
```
~/sound-design/  (o dove hai i file)
```
- ✅ Dove sviluppi e modifichi
- ✅ Hai il controllo completo
- ✅ Puoi testare localmente

### 2. **GITHUB** (Repository remoto)
```
https://github.com/tuo-username/sound-design
```
- ✅ Backup cloud
- ✅ Versioning (Git)
- ✅ Condivisione pubblica/privata
- ✅ Collaborazione

### 3. **CLAUDE** (Skill attiva)
```
/mnt/skills/user/sound-design/
```
- ✅ Dove Claude legge i file
- ✅ Aggiornata quando lavori con Claude
- ✅ Resettata tra sessioni

---

## 🎯 WORKFLOW CONSIGLIATO

### Flusso Ideale

```
LOCALE (develop) → GITHUB (push) → CLAUDE (sync)
     ↓                  ↓               ↓
   Edit             Backup          Use with AI
```

---

## 🚀 SETUP INIZIALE (FAI UNA VOLTA SOLA)

### PASSO 1: Inizializza Git in Locale

```bash
# Nel tuo computer, nella directory della skill
cd ~/sound-design  # o dove hai i file

# Inizializza Git
git init

# Crea .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Backup files
*.backup
*.old
*.bak

# MIDI temporanei (opzionale, se generi tanti test)
# examples/*.mid

# Log files
*.log
EOF

# Aggiungi tutto
git add .

# Primo commit
git commit -m "Initial commit: Sound Design Skill v2.0"
```

### PASSO 2: Crea Repository su GitHub

1. Vai su https://github.com
2. Click "New Repository"
3. Nome: `sound-design-skill`
4. Descrizione: `Complete music production skill for Claude AI`
5. Scegli: **Public** o **Private**
6. **NON** inizializzare con README (ce l'hai già)
7. Click "Create repository"

### PASSO 3: Collega Locale a GitHub

```bash
# Aggiungi remote
git remote add origin https://github.com/TUO-USERNAME/sound-design-skill.git

# Push iniziale
git branch -M main
git push -u origin main
```

✅ **Ora hai: Locale ↔ GitHub sincronizzati!**

---

## 📝 WORKFLOW QUOTIDIANO

### Scenario 1: Modifichi in Locale → Sync Everything

```bash
# 1. LOCALE: Fai modifiche
cd ~/sound-design
# ... modifica files ...

# 2. LOCALE → GITHUB: Push
git add .
git commit -m "Aggiunti nuovi synth al database"
git push

# 3. LOCALE/GITHUB → CLAUDE: Sync con Claude
# Quando lavori con Claude, carica i file aggiornati
```

### Scenario 2: Lavori con Claude → Salva in Locale

```bash
# 1. CLAUDE crea/modifica file
# (durante la sessione con Claude)

# 2. CLAUDE → LOCALE: Download
# Scarica i file aggiornati da /mnt/user-data/outputs/

# 3. LOCALE: Integra modifiche
cd ~/sound-design
# copia i nuovi file
# rivedi le modifiche

# 4. LOCALE → GITHUB: Push
git add .
git commit -m "Aggiornamenti da sessione Claude"
git push
```

---

## 🔄 SINCRONIZZAZIONE CLAUDE

### Metodo A: Upload Manuale (Semplice)

Ogni volta che inizi una sessione con Claude:

1. **Comprimi la skill**:
```bash
cd ~/sound-design
tar -czf sound-design-latest.tar.gz .
```

2. **Upload su Claude**:
   - Carica `sound-design-latest.tar.gz`
   - Chiedi a Claude di estrarlo in `/mnt/skills/user/sound-design/`

3. **Claude estrae**:
```bash
cd /mnt/skills/user/
tar -xzf sound-design-latest.tar.gz -C sound-design/
```

### Metodo B: File per File (Granulare)

Carica solo i file modificati:

```bash
# Nel tuo computer, identifica file modificati
git status

# Carica su Claude solo quelli modificati
# Claude poi li copia:
cp uploaded-file.md /mnt/skills/user/sound-design/references/
```

### Metodo C: Script di Sync (Avanzato)

Crea uno script che Claude può eseguire:

```bash
# sync_skill.sh
#!/bin/bash

echo "🔄 Sincronizzazione skill da uploads..."

SKILL_DIR="/mnt/skills/user/sound-design"
UPLOAD_DIR="/mnt/user-data/uploads"

# Copia references
cp $UPLOAD_DIR/references/*.md $SKILL_DIR/references/ 2>/dev/null

# Copia scripts
cp $UPLOAD_DIR/scripts/*.py $SKILL_DIR/scripts/ 2>/dev/null
chmod +x $SKILL_DIR/scripts/*.py

# Copia docs
cp $UPLOAD_DIR/docs/*.md $SKILL_DIR/docs/ 2>/dev/null

# Copia root files
cp $UPLOAD_DIR/README.md $SKILL_DIR/ 2>/dev/null
cp $UPLOAD_DIR/SKILL.md $SKILL_DIR/ 2>/dev/null

echo "✅ Sincronizzazione completata!"
```

Poi carica lo script e chiedi a Claude di eseguirlo.

---

## 📁 STRUTTURA RACCOMANDATA

### Repository GitHub

```
sound-design-skill/
├── .github/
│   └── workflows/          # CI/CD (opzionale)
├── .gitignore
├── README.md               # Documentazione principale
├── LICENSE                 # MIT, Apache, etc.
├── CHANGELOG.md            # Log delle modifiche
│
├── docs/                   # Tutta la documentazione
├── references/             # Database teorici
├── scripts/                # Tool Python
├── examples/               # File esempio
├── tests/                  # Test unitari (opzionale)
│
└── SKILL.md               # File per Claude AI
```

### File Essenziali per GitHub

1. **README.md** - Overview, installation, usage
2. **LICENSE** - Scegli una licenza open source
3. **CHANGELOG.md** - Versioning delle modifiche
4. **.gitignore** - Esclusioni Git

---

## 📋 CHANGELOG.md (Template)

```markdown
# Changelog

All notable changes to the Sound Design Skill will be documented here.

## [2.0.0] - 2024-10-24

### Added
- Harmonic analysis tool (analyze_harmony.py)
- Mood to composition generator (mood_to_composition.py)
- Complete music theory database
- Chord progressions database (50+)
- Scales and modes database (14+)
- 8 comprehensive guides in docs/

### Changed
- Expanded synth database to 11 synthesizers
- Restructured skill with docs/ and examples/ directories
- Updated README with professional documentation

### Fixed
- Script permissions for Python tools

## [1.0.0] - 2024-10-23

### Added
- Initial release
- Basic sound design for Matriarch and Digitone
- Rhythm pattern generator
- Signal flow diagram generator
- 4 reference documents
```

---

## 🏷️ VERSIONING

Usa **Semantic Versioning**: `MAJOR.MINOR.PATCH`

### Quando Incrementare:

- **MAJOR** (2.0.0): Breaking changes, ristrutturazioni importanti
- **MINOR** (2.1.0): Nuove features, backward compatible
- **PATCH** (2.0.1): Bug fixes, piccoli miglioramenti

### Git Tags

```bash
# Crea tag per versione
git tag -a v2.0.0 -m "Version 2.0.0: Complete music production suite"
git push origin v2.0.0

# Lista tag
git tag -l
```

---

## 🔐 FILE SENSIBILI

### Cosa NON mettere su GitHub (se pubblico):

- ❌ API keys personali
- ❌ Token di accesso
- ❌ File personali privati
- ❌ Preset commerciali protetti da copyright

### Cosa È OK mettere:

- ✅ Codice Python
- ✅ Documentazione
- ✅ Database teorici
- ✅ Esempi MIDI (se generati da te)
- ✅ Preset open source (Vital, etc.)

---

## 🚀 COMANDI RAPIDI

### Workflow Standard

```bash
# 1. Modifica in locale
cd ~/sound-design
# ... edit files ...

# 2. Vedi cosa è cambiato
git status
git diff

# 3. Commit
git add .
git commit -m "Descrizione modifiche"

# 4. Push su GitHub
git push

# 5. Quando lavori con Claude, carica i file aggiornati
```

### Sync da GitHub a Locale

```bash
# Pull modifiche da GitHub (se lavori da più computer)
cd ~/sound-design
git pull
```

### Sync da Claude a Locale

```bash
# 1. Chiedi a Claude di salvare modifiche in /mnt/user-data/outputs/
# 2. Scarica i file
# 3. Copia nel tuo repo locale
cd ~/sound-design
# copia file scaricati
# 4. Commit
git add .
git commit -m "Aggiornamenti da sessione Claude"
git push
```

---

## 🎯 BEST PRACTICES

### 1. Commit Frequenti e Descrittivi

❌ **Non fare**:
```bash
git commit -m "fix"
git commit -m "update"
git commit -m "changes"
```

✅ **Fai invece**:
```bash
git commit -m "Add jazz chord progressions to database"
git commit -m "Fix key detection confidence calculation"
git commit -m "Update Digitone FM algorithm documentation"
```

### 2. Branches per Features Grandi

```bash
# Crea branch per nuova feature
git checkout -b feature/audio-analysis

# Lavora sul branch
# ... modifiche ...
git add .
git commit -m "Implement audio analysis tool"

# Merge in main quando pronto
git checkout main
git merge feature/audio-analysis
git push
```

### 3. README Aggiornato

Aggiorna sempre il README quando:
- Aggiungi nuovi tool
- Cambi la struttura
- Aggiungi dipendenze

### 4. Testing Prima di Push

```bash
# Test script prima di push
cd scripts/
python mood_to_composition.py test
python analyze_harmony.py ../examples/test.mid

# Se tutto OK, push
git push
```

---

## 📦 SCRIPT DI AUTOMAZIONE

### sync_to_claude.sh

```bash
#!/bin/bash
# Script per preparare file da caricare su Claude

echo "📦 Preparazione skill per Claude..."

cd ~/sound-design

# Crea archivio
tar -czf sound-design-$(date +%Y%m%d).tar.gz \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.DS_Store' \
  .

echo "✅ Archivio creato: sound-design-$(date +%Y%m%d).tar.gz"
echo "📤 Carica questo file su Claude e chiedi di estrarlo"
```

### update_from_claude.sh

```bash
#!/bin/bash
# Script per integrare modifiche da Claude

echo "🔄 Aggiornamento da Claude..."

DOWNLOAD_DIR="$HOME/Downloads"
SKILL_DIR="$HOME/sound-design"

# Trova l'archivio più recente scaricato
LATEST=$(ls -t $DOWNLOAD_DIR/sound-design-*.tar.gz 2>/dev/null | head -1)

if [ -z "$LATEST" ]; then
  echo "❌ Nessun archivio trovato in Downloads"
  exit 1
fi

echo "📦 Trovato: $LATEST"

# Backup locale
tar -czf "$SKILL_DIR-backup-$(date +%Y%m%d-%H%M%S).tar.gz" -C "$SKILL_DIR" .

# Estrai modifiche in directory temporanea
TMP_DIR=$(mktemp -d)
tar -xzf "$LATEST" -C "$TMP_DIR"

# Mostra differenze
echo "🔍 Differenze trovate:"
diff -r "$SKILL_DIR" "$TMP_DIR" | grep "^diff" || echo "Nessuna differenza"

# Chiedi conferma
read -p "Vuoi copiare questi file? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
  rsync -av --delete "$TMP_DIR/" "$SKILL_DIR/"
  echo "✅ File aggiornati!"
  
  # Commit automatico
  cd "$SKILL_DIR"
  git add .
  git commit -m "Update from Claude session $(date +%Y%m%d)"
  
  echo "💾 Vuoi pushare su GitHub? (y/n)"
  read -p "" -n 1 -r
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    git push
    echo "✅ Push completato!"
  fi
fi

# Cleanup
rm -rf "$TMP_DIR"
```

Salva questi script, rendili eseguibili:
```bash
chmod +x sync_to_claude.sh update_from_claude.sh
```

---

## 🎓 WORKFLOW COMPLETO: ESEMPIO

### Scenario: Aggiungi Nuovo Synth

```bash
# 1. LOCALE: Crea branch
cd ~/sound-design
git checkout -b feature/add-prophet-synth

# 2. LOCALE: Modifica files
nano references/synth-database.md
# ... aggiungi Prophet 5 ...

# 3. LOCALE: Test
# verifica che tutto sia corretto

# 4. LOCALE: Commit
git add references/synth-database.md
git commit -m "Add Prophet 5 to synth database with complete specs"

# 5. LOCALE: Merge in main
git checkout main
git merge feature/add-prophet-synth

# 6. LOCALE → GITHUB: Push
git push

# 7. LOCALE → CLAUDE: Sync
./sync_to_claude.sh
# Carica su Claude e chiedi di estrarre

# 8. CLAUDE: Testa
"Claude, usando il synth Prophet 5, programma un pad warm"
# Claude dovrebbe ora conoscere Prophet 5!

# 9. AGGIORNA CHANGELOG
nano CHANGELOG.md
# Aggiungi sotto [2.1.0]:
# - Added Prophet 5 synthesizer to database

# 10. Tag version
git tag -a v2.1.0 -m "Added Prophet 5 support"
git push origin v2.1.0
```

---

## 📊 MONITORING & MANUTENZIONE

### Controlla Dimensione Repository

```bash
# Vedi dimensione
du -sh ~/sound-design/.git

# Se troppo grande (>100MB), considera:
# - Rimuovere file grossi dalla history
# - Usare Git LFS per MIDI/binari
```

### Backup Periodici

```bash
# Backup automatico settimanale (cron job)
0 0 * * 0 cd ~/sound-design && tar -czf ~/backups/sound-design-$(date +\%Y\%m\%d).tar.gz .
```

### Pulizia File Vecchi

```bash
# Rimuovi branch vecchi
git branch --merged | grep -v "main" | xargs git branch -d

# Rimuovi file non tracciati
git clean -fd
```

---

## 🆘 TROUBLESHOOTING

### Problema: "Merge Conflict"

```bash
# Quando GitHub e locale sono diversi
git pull  # Errore: conflict

# Risolvi manualmente i conflitti
nano file-in-conflitto.md
# Cerca <<<<<<, ======, >>>>>>
# Scegli quale versione tenere

# Completa merge
git add file-in-conflitto.md
git commit -m "Resolve merge conflict"
git push
```

### Problema: "Claude ha vecchia versione"

```bash
# Forza sync completa
# 1. Crea nuovo archivio
cd ~/sound-design
tar -czf skill-fresh.tar.gz .

# 2. Carica su Claude
# 3. Claude pulisce e riesegue:
rm -rf /mnt/skills/user/sound-design/*
tar -xzf skill-fresh.tar.gz -C /mnt/skills/user/sound-design/
```

### Problema: "Ho perso modifiche locali"

```bash
# Se hai committato, puoi recuperare
git reflog  # Vedi history completa
git checkout <commit-hash>

# Se non hai committato... 😢 sono perse
# Moral: Commit spesso!
```

---

## ✅ CHECKLIST QUOTIDIANA

### Prima di Lavorare
- [ ] `git pull` (se lavori da più computer)
- [ ] Verifica sei sul branch giusto: `git branch`

### Dopo Modifiche
- [ ] `git status` - Vedi cosa è cambiato
- [ ] `git diff` - Rivedi modifiche
- [ ] Test script modificati
- [ ] `git add .`
- [ ] `git commit -m "descrizione"`
- [ ] `git push`

### Prima di Sessione Claude
- [ ] Commit tutto in locale
- [ ] Push su GitHub (backup)
- [ ] Prepara archivio: `./sync_to_claude.sh`
- [ ] Carica su Claude

### Dopo Sessione Claude
- [ ] Scarica file modificati da Claude
- [ ] Integra in locale
- [ ] Commit: "Update from Claude session"
- [ ] Push su GitHub

---

## 🎯 STRATEGIA RACCOMANDATA

### Per Sviluppo Frequente

**LOCALE** = Source of truth principale
- Sviluppi qui
- Commit frequenti
- Push su GitHub quotidianamente

**GITHUB** = Backup e condivisione
- Sempre aggiornato con locale
- Usalo per rollback se serve
- Condividi con altri

**CLAUDE** = Environment di test/uso
- Sync all'inizio sessione
- Usa per generare/testare
- Salva output interessanti
- Re-sync periodicamente

---

## 📚 RISORSE UTILI

### Git
- https://git-scm.com/doc
- https://www.atlassian.com/git/tutorials

### GitHub
- https://docs.github.com
- https://guides.github.com

### Best Practices
- https://github.com/elsewhencode/project-guidelines
- https://www.conventionalcommits.org

---

## 🎊 SETUP COMPLETO!

Ora hai un sistema professionale per gestire la skill tra:
- 💻 **Locale** (sviluppo)
- 🐙 **GitHub** (versioning + backup)
- 🤖 **Claude** (utilizzo AI)

**Next steps**:
1. Inizializza Git in locale
2. Crea repo su GitHub  
3. Fai primo push
4. Crea script di sync
5. Inizia a lavorare!

---

**Happy coding!** 🎛️✨
