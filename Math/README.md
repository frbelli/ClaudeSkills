# Skill Analisi Matematica I per Ingegneria

## 📦 Contenuto del Pacchetto

Hai ricevuto:

1. **analisi-matematica.skill** - Il file della skill da installare su Claude
2. **GUIDA_UTILIZZO.md** - Guida completa all'uso della skill
3. **esempio_studio_funzione.txt** - Esempio di output per studio di funzione
4. **esempio_grafico_studio.png** - Grafico professionale generato
5. **esempio_integrale.txt** - Esempio di calcolo integrale definito
6. **esempio_grafico_integrale.png** - Visualizzazione area sotto la curva
7. **README.md** - Questo file

## 🎯 Cosa Fa Questa Skill

Trasforma Claude in un **professore universitario di Analisi Matematica I** che:

✅ Spiega concetti teorici con chiarezza (limiti, derivate, integrali, serie)
✅ Risolve esercizi passo-passo con spiegazioni dettagliate
✅ Genera grafici professionali ad alta risoluzione
✅ Evidenzia errori comuni e come evitarli
✅ Spiega PERCHÉ si usa un metodo, non solo COME

## 🚀 Installazione Rapida

### Passo 1: Carica la Skill
1. Vai su [claude.ai](https://claude.ai)
2. Clicca sull'icona strumenti (⚙️) in alto a destra
3. Seleziona "Skills"
4. Clicca "Add Skill"
5. Carica il file `analisi-matematica.skill`

### Passo 2: Testa la Skill
Scrivi uno di questi comandi per testare:
- "Spiegami cos'è un limite"
- "Studia la funzione f(x) = x³ - 3x"
- "Calcola l'integrale di x·sin(x)"

## 📚 Argomenti Coperti

### Limiti e Continuità
- Definizione formale (ε-δ)
- Limiti notevoli
- Forme indeterminate (0/0, ∞/∞, ∞-∞, 0·∞, 1^∞)
- Regola de L'Hôpital
- Teorema dei carabinieri
- Tipi di discontinuità

### Derivate
- Regole di derivazione (somma, prodotto, quoziente)
- Regola della catena
- Derivate di funzioni composte
- Teoremi fondamentali (Rolle, Lagrange)
- Applicazioni geometriche

### Studio di Funzione Completo
- Dominio e simmetrie
- Intersezioni con assi
- Studio del segno
- Limiti agli estremi
- Asintoti (verticali, orizzontali, obliqui)
- Derivata prima (crescenza, massimi/minimi)
- Derivata seconda (concavità, flessi)
- Grafico finale annotato

### Integrali
- Integrali immediati
- Integrazione per parti (con regola LIATE)
- Integrazione per sostituzione
- Frazioni parziali
- Integrali definiti e calcolo aree
- Teorema fondamentale del calcolo
- Applicazioni geometriche

### Serie e Successioni
- Limiti di successioni
- Successioni notevoli
- Serie numeriche
- Criteri di convergenza:
  - Confronto
  - Rapporto
  - Radice
  - Leibniz (serie alternate)
- Convergenza assoluta vs condizionata
- Serie di Taylor
- Sviluppi notevoli

## 🎓 Caratteristiche Uniche

### 1. Spiegazioni Approfondite
Non solo calcoli, ma vera comprensione:
- Definizioni formali + significato intuitivo
- Motivazione delle scelte metodologiche
- Collegamenti tra concetti diversi
- Esempi concreti e applicazioni

### 2. Risoluzione Step-by-Step
Ogni passaggio spiegato:
- Identificazione del problema
- Scelta del metodo e perché
- Ogni calcolo motivato
- Verifica del risultato
- Errori comuni evidenziati

### 3. Grafici Professionali
- Risoluzione 300 DPI
- Punti critici annotati
- Asintoti tracciati
- Aree colorate (integrali definiti)
- Derivate visualizzate
- Legende chiare

### 4. Database Errori Comuni
26+ errori catalogati tra cui:
- "Applicare de L'Hôpital senza forma indeterminata"
- "Derivare prodotto come somma"
- "Integrare prodotto come prodotto di integrali"
- "Dimenticare +C negli integrali indefiniti"
- E molti altri...

### 5. Esempi Guidati
11+ esercizi completamente risolti:
- Limiti con forme indeterminate
- Studi di funzione completi
- Integrali per parti e sostituzione
- Serie con criteri di convergenza

## 💡 Esempi di Utilizzo

### Esempio 1: Spiegazione Teorica
**Tu scrivi**: "Spiegami quando usare l'integrazione per parti"

**Claude risponde con**:
- Formula generale ∫ u dv = uv - ∫ v du
- Regola LIATE per scegliere u e dv
- Esempi concreti
- Quando NON usarla
- Errori comuni
- Esercizi tipo risolti

### Esempio 2: Studio di Funzione
**Tu scrivi**: "Studia f(x) = (x²-1)/(x-1)"

**Claude fornisce**:
- Dominio: ℝ \ {1}
- Semplificazione algebrica
- Discontinuità eliminabile in x=1
- Tutti i limiti
- Derivate e monotonia
- Grafico professionale
- Interpretazione geometrica

### Esempio 3: Integrale Definito
**Tu scrivi**: "Calcola l'area tra f(x)=sin(x) e l'asse x da 0 a π"

**Claude esegue**:
- Verifica che f(x) ≥ 0 nell'intervallo
- Calcola ∫[0,π] sin(x) dx
- Mostra tutti i passaggi
- Calcola F(π) - F(0) = 2
- Genera grafico con area colorata
- Interpreta il risultato

## 📊 Componenti Tecnici

### Script Python Inclusi

1. **analizza_funzione.py**
   - Analisi matematica completa
   - Calcolo automatico di derivate, limiti, asintoti
   - Generazione grafici ad alta qualità
   - Output testuale formattato

2. **calcola_integrale.py**
   - Integrazione simbolica
   - Identificazione automatica metodo ottimale
   - Spiegazione step-by-step del metodo
   - Visualizzazione grafica
   - Supporto integrali definiti e indefiniti

### File di Riferimento

1. **concetti_chiave.md** (12,000+ parole)
   - Teoria completa di Analisi I
   - Definizioni formali
   - Teoremi fondamentali
   - Formule di riferimento rapido

2. **errori_comuni.md** (8,000+ parole)
   - 26+ errori catalogati
   - Spiegazione perché sono errori
   - Versione corretta
   - Come evitarli
   - Checklist di verifica

3. **esercizi_guidati.md** (10,000+ parole)
   - 11+ esercizi risolti completamente
   - Ogni passaggio spiegato
   - Pattern riconoscibili
   - Strategie risolutive

## 🎯 Per Chi è Questa Skill

### Ideale per:
✅ Studenti di Ingegneria (primo anno)
✅ Preparazione esami di Analisi I
✅ Ripasso prima di test/compiti
✅ Comprensione approfondita dei concetti
✅ Visualizzazione di funzioni complesse
✅ Identificazione di errori comuni

### Utile anche per:
- Studenti di Fisica e Matematica
- Ripasso per concorsi
- Autodidatti che studiano analisi
- Insegnanti per preparare lezioni

## 🏆 Vantaggi Rispetto ad Altri Strumenti

| Caratteristica | Questa Skill | Calcolatrici Online | Libri di Testo |
|----------------|--------------|---------------------|----------------|
| Spiegazioni dettagliate | ✅ | ❌ | ✅ |
| Grafici di qualità | ✅ | ⚠️ | ✅ |
| Interattività | ✅ | ❌ | ❌ |
| Personalizzazione | ✅ | ❌ | ❌ |
| Errori comuni evidenziati | ✅ | ❌ | ⚠️ |
| Disponibilità 24/7 | ✅ | ✅ | ✅ |
| Spiegazione del "perché" | ✅ | ❌ | ✅ |
| Feedback immediato | ✅ | ✅ | ❌ |

## 📖 Guida Rapida Comandi

### Per Spiegazioni Teoriche
```
"Spiegami [concetto]"
"Cos'è [termine matematico]?"
"Come funziona [regola/teorema]?"
"Quando si usa [metodo]?"
```

### Per Esercizi
```
"Calcola il limite di [espressione] per x→[valore]"
"Trova la derivata di [funzione]"
"Studia la funzione [espressione]"
"Calcola l'integrale di [funzione]"
"Determina se la serie [espressione] converge"
```

### Per Approfondimenti
```
"Quali sono gli errori comuni in [argomento]?"
"Perché si usa questo metodo?"
"Mostrami esempi simili"
"Come verifico il risultato?"
```

## 🔍 Risoluzione Problemi

### La skill non si attiva?
- Verifica di averla installata correttamente
- Prova a essere più specifico nella richiesta
- Usa termini matematici chiari (limite, derivata, integrale)

### I grafici non si vedono?
- Attendi qualche secondo per la generazione
- Controlla che Claude abbia accesso agli strumenti computer
- Riprova il comando

### Risposte troppo brevi?
- Chiedi esplicitamente "con spiegazione dettagliata"
- Aggiungi "spiega tutti i passaggi"
- Richiedi "step-by-step"

## 🤝 Supporto e Feedback

Se hai suggerimenti per migliorare la skill:
1. Nota cosa vorresti fosse diverso
2. Descrivi il comportamento atteso
3. Fornisci esempi specifici

## 📄 Licenza e Uso

Questa skill è stata creata per uso educativo. 
- ✅ Usa liberamente per studiare
- ✅ Condividi con compagni di corso
- ✅ Usa per preparazione esami
- ❌ Non vendere o ridistribuire commercialmente

## 🎉 Inizia Subito!

1. Installa la skill (vedi sopra)
2. Leggi la GUIDA_UTILIZZO.md
3. Guarda gli esempi inclusi
4. Prova con: "Spiegami cos'è un limite"
5. Inizia a studiare! 📚

---

**Buono studio! Che l'analisi sia con te! 🚀**

*Skill progettata per trasformare Claude in un professore universitario sempre disponibile*

**Versione**: 1.0
**Data creazione**: Ottobre 2025
**Compatibilità**: Claude Sonnet 4.5 con computer use
