#!/bin/bash
# sync_to_claude.sh
# Script per preparare la skill da caricare su Claude

echo "📦 Preparazione Sound Design Skill per Claude..."
echo ""

# Directory della skill (modifica se diversa)
SKILL_DIR="$HOME/Dev/Claude Skills/Sound Design"
#SKILL_DIR="$HOME/sound-design"

if [ ! -d "$SKILL_DIR" ]; then
  echo "❌ Directory $SKILL_DIR non trovata!"
  echo "💡 Modifica la variabile SKILL_DIR nello script"
  exit 1
fi

cd "$SKILL_DIR"

# Nome archivio con data
ARCHIVE_NAME="sound-design-skill-$(date +%Y%m%d-%H%M%S).tar.gz"
ARCHIVE_DIR="$HOME/Downloads"
echo "📁 Directory: $SKILL_DIR"
echo "📦 Archivio: $ARCHIVE_NAME"
echo "📁 Directory di destinazione archivio: $ARCHIVE_DIR"

# Crea archivio escludendo file non necessari
tar -czf "$ARCHIVE_NAME" \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='.DS_Store' \
  --exclude='*.backup' \
  --exclude='*.old' \
  --exclude='node_modules' \
  .

# Verifica dimensione
SIZE=$(du -h "$ARCHIVE_NAME" | cut -f1)
mv "$ARCHIVE_NAME" "$ARCHIVE_DIR"
echo "✅ Archivio creato con successo!"
echo "📊 Dimensione: $SIZE"
echo "📁 Path: $ARCHIVE_DIR $ARCHIVE_NAME"
echo ""
echo "📋 PROSSIMI PASSI:"
echo "1. Carica $ARCHIVE_NAME su Claude"
echo "2. Chiedi a Claude: 'Estrai questo archivio in /mnt/skills/user/sound-design/'"
echo "3. Claude eseguirà: tar -xzf $ARCHIVE_NAME -C /mnt/skills/user/sound-design/"
echo ""
echo "🎛️ La tua skill sarà aggiornata su Claude!"
