# Titolo del Progetto

## Descrizione
Breve introduzione al progetto: spiega cosa fa, a chi è destinato e qual è il suo obiettivo principale.  
Puoi aggiungere informazioni tecniche di base o il contesto in cui il progetto è stato sviluppato.

---

## Struttura del Progetto
Esempio di organizzazione delle cartelle:

```
📦 nome-progetto
 ┣ 📂 src/              # codice sorgente
 ┣ 📂 profiles/         # profili dei partecipanti
 ┣ 📂 docs/             # documentazione e materiali
 ┣ 📄 README.md         # questo file
 ┗ 📄 LICENSE           # licenza del progetto
```

---

## Contributi
1. Crea un branch di sviluppo:
   ```bash
   git checkout -b feature/<nome-feature>
   ```
2. Effettua le modifiche e il commit:
   ```bash
   git commit -m "Aggiunge nuova funzionalità"
   ```
3. Esegui il push e apri una Pull Request su GitHub.

---

## Sviluppo e Test

Il progetto contiene una funzione di mock per generare un JSON di report status. 
Fare riferimento a  [status_report.py](status_report.py) e la funzione `get_status()`.

### Esecuzione dei Test
Per eseguire i test del progetto, utilizzare il seguente comando:

    bash python -m unittest test_status_report.py

I test verificano:
- La corretta generazione dei servizi individuali
- La struttura completa del JSON di stato
- La validità dei dati e dei tipi
- La presenza di tutti i campi richiesti

### Come Aggiungere Nuovi Test
1. Creare nuovi metodi di test nella classe `TestStatusReport`
2. I nomi dei metodi devono iniziare con `test_`
3. Utilizzare gli assertions di unittest per le verifiche


---

## Autori
- [Mario Rossi](profiles/mario.profile.md)  
- [Lucia Bianchi](profiles/lucia.profile.md)  
- [Giovanni Verdi](profiles/giovanni.profile.md)

---

## Licenza
Questo progetto è distribuito sotto licenza MIT.  
Consulta il file [LICENSE](LICENSE) per maggiori dettagli.
