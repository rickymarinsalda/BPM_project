# BPM_project

Idea:

Analisi automatica delle recensioni di un utente: 

Dato un dataset di review (di amazon o altro) prenderle, darle in pasto a un API di un AI tipo chatgpt e ottenere un riassunto di tutte le recensioni per ciascun prodotto. 
Riassunti utili sia al consumatore che si può fare un'idea di come è il prodotto senza doversi leggere tutte le recensioni, sia al produttore che leggendo un riassunto può farsi un'idea su cosa ne pensa il consumatore del prodotto e capire come migliorarlo. 

Inoltre siccome al prof piace vedere la spiegabilità delle AI generetive, per fare una valutazione sull'efficacia del riassunto si possono usare metodi come: 
- analisi parole usate nel riassunto comparate alle parole usate nelle recensioni effettive
- nel dataset che ho trovato spesso c'è scritto se le recensioni sono positive o meno. Possiamo usare queste come ground truth e compararle con il risultato del riassunto per capire se effettivamente il giudizio che ha dato chatgpt è vicino quantomeno alla verità.
- eventuali altri metodi di giudizio TASK (possibili):
- trovare un dataset buono
- dataset cleaning
- fare il programma python che gestisce le api e fa le richieste a chatgpt
- ottenere il giudizio complessivo e mostrarlo in qualche modo (eventualmente si può fare un interfaccia anche usando un sito che mostra un modo per inserire le recensioni e poi dare in output in modo user-friendly il riassunto)

Altre cose implementabili:
- Scelta dell'API:  il progetto può essere arricchito esplorando diverse API di AI generative per confrontare le loro prestazioni e valutare la loro spiegabilità. Ad esempio,  API come OpenAI's DALL-E per generare immagini creative o altre varianti di GPT come GPT-Neo o GPT-3.5, o modelli sviluppati da altre aziende come Google o Microsoft o altri a caso che si trovano su internet.

-Metodi di valutazione della spiegabilità specifici per l'output generato dall'AI: ad esempio, si può utilizzare LIME (Local Interpretable Model-agnostic Explanations) o SHAP (SHapley Additive exPlanations) per ottenere spiegazioni locali riguardanti le scelte fatte dall'AI generativo nel processo di generazione dei riassunti. Questi metodi servono ad identificare quali parti del testo hanno maggiormente influenzato il risultato finale.

- altri approcci per valutare l'efficacia dei riassunti generati: ad esempio, misure di somiglianza del testo come BLEU o ROUGE per valutare la qualità del riassunto rispetto alle recensioni originali.

- esplorazione di approcci multilingue: se il dataset che troviamo contiene recensioni in diverse lingue, potresmmo considerare l'utilizzo di modelli di AI generativi multilingue o l'adattamento dei modelli esistenti per supportare più lingue

- confrontare i risultati ottenuti utilizzando l'AI generativa con tecniche di elaborazione del linguaggio naturale più tradizionali, come l'utilizzo di modelli di regressione o classificazione per il riassunto delle recensioni
