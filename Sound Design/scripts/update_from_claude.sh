#!/bin/bash
# update_from_claude.sh
# Script per aggiornare la skill locale con modifiche da Claude

echo "🔄 Aggiornamento Sound Design Skill da Claude..."
echo ""

# Directory della skill locale
SKILL_DIR="$HOME/Dev/Claude Skills/Sound Design"
#SKILL_DIR="$HOME/sound-design"
DOWNLOAD_DIR="$HOME/Downloads"

if [ ! -d "$SKILL_DIR" ]; then
  echo "❌ Directory $SKILL_DIR non trovata!"
  echo "💡 Crea la directory o modifica SKILL_DIR nello script"
  exit 1
fi

# Trova archivio più recente
LATEST=$(ls -t "$DOWNLOAD_DIR"/sound-design-skill-*.tar.gz 2>/dev/null | head -1)

if [ -z "$LATEST" ]; then
  echo "❌ Nessun archivio sound-design-skill-*.tar.gz trovato in $DOWNLOAD_DIR"
  echo ""
  echo "💡 Assicurati di:"
  echo "1. Aver chiesto a Claude di creare archivio"
  echo "2. Aver scaricato l'archivio"
  echo "3. L'archivio sia in $DOWNLOAD_DIR"
  exit 1
fi

echo "📦 Trovato archivio: $(basename $LATEST)"
echo "📊 Dimensione: $(du -h "$LATEST" | cut -f1)"
echo ""

# Crea backup locale
BACKUP_NAME="$SKILL_DIR-backup-$(date +%Y%m%d-%H%M%S).tar.gz"
echo "💾 Creazione backup locale..."
tar -czf "$BACKUP_NAME" -C "$SKILL_DIR" . 2>/dev/null
echo "✅ Backup salvato: $BACKUP_NAME"
echo ""

# Estrai in directory temporanea
TMP_DIR=$(mktemp -d)
echo "📂 Estrazione archivio..."
tar -xzf "$LATEST" -C "$TMP_DIR" 2>/dev/null

# Mostra differenze
echo ""
echo "🔍 Analisi differenze..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# File nuovi
NEW_FILES=$(diff -qr "$SKILL_DIR" "$TMP_DIR" 2>/dev/null | grep "Only in $TMP_DIR" | wc -l)
if [ $NEW_FILES -gt 0 ]; then
  echo "📄 File nuovi: $NEW_FILES"
  diff -qr "$SKILL_DIR" "$TMP_DIR" 2>/dev/null | grep "Only in $TMP_DIR" | head -5
fi

# File modificati
MODIFIED=$(diff -qr "$SKILL_DIR" "$TMP_DIR" 2>/dev/null | grep "differ" | wc -l)
if [ $MODIFIED -gt 0 ]; then
  echo "✏️  File modificati: $MODIFIED"
  diff -qr "$SKILL_DIR" "$TMP_DIR" 2>/dev/null | grep "differ" | head -5
fi

# File rimossi
REMOVED=$(diff -qr "$SKILL_DIR" "$TMP_DIR" 2>/dev/null | grep "Only in $SKILL_DIR" | wc -l)
if [ $REMOVED -gt 0 ]; then
  echo "🗑️  File rimossi: $REMOVED"
  diff -qr "$SKILL_DIR" "$TMP_DIR" 2>/dev/null | grep "Only in $SKILL_DIR" | head -5
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Chiedi conferma
read -p "❓ Vuoi applicare queste modifiche? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  echo "❌ Operazione annullata"
  rm -rf "$TMP_DIR"
  exit 0
fi

# Copia file
echo "📋 Copia file..."
rsync -av --delete "$TMP_DIR/" "$SKILL_DIR/"
echo "✅ File aggiornati!"
echo ""

# Git commit (se è un repo git)
if [ -d "$SKILL_DIR/.git" ]; then
  cd "$SKILL_DIR"
  
  echo "📝 Vuoi fare commit Git? (y/n)"
  read -p "" -n 1 -r
  echo ""
  
  if [[ $REPLY =~ ^[Yy]$ ]]; then
    git add .
    git status
    echo ""
    read -p "💬 Messaggio commit (default: 'Update from Claude session'): " COMMIT_MSG
    COMMIT_MSG=${COMMIT_MSG:-"Update from Claude session $(date +%Y-%m-%d)"}
    
    git commit -m "$COMMIT_MSG"
    echo "✅ Commit completato!"
    echo ""
    
    echo "🚀 Vuoi pushare su GitHub? (y/n)"
    read -p "" -n 1 -r
    echo ""
    
    if [[ $REPLY =~ ^[Yy]$ ]]; then
      git push
      echo "✅ Push completato!"
    fi
  fi
fi

# Cleanup
rm -rf "$TMP_DIR"

echo ""
echo "🎉 Aggiornamento completato!"
echo "📁 Skill locale: $SKILL_DIR"
echo "💾 Backup disponibile: $BACKUP_NAME"
