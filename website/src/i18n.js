import {
  dictionary,
  locale,
  _, t,
} from 'svelte-i18n';
function setupI18n({
  withLocale: _locale
} = {
    withLocale: 'en'
  }) {
  dictionary.set({
    en: {
      "intro": {
        "testo": "A studio flat inspired by the <span class='font-black'>Vespa world</span>, located in a historic pedestrian lane in the medieval village of <a href='https://goo.gl/maps/ckj5VXFV7nW2ay9PA' class='underline text-sky-600 font-black'>Marciana</a>. Furnished with taste and attention to detail, it's a <span class='font-black'>cozy space</span> for <span class='font-black'>young couples</span> looking for a charming and elegant getaway.",

      },
      "details": {
        "title": "Details",
        "body": "The apartment has a designer sofa bed that encloses inside a comfortable <span class='font-black'>double bed</span>, the kitchenette is equipped with <span class='font-black'>induction cookers</span>, and the bathroom includes an <span class='font-black'>oversize shower</span>. The linen (sheets, towels) is not included, but it will be possible to rent it on request.",
        "letto": "Double bed",
        "bathroom": "Bathroom",
        "wifi": "Free wi-fi",
        "dim": "Dimensions",
        "flat": "Flat studio",
        "cuc": "Equipped kichen",
        "park": "Free parking",
        "sconto": "Ferry discount",
        "farmacia":"Nearby pharmacy"
      },
      "services": {
        "title": "Services",
        "body": "Traveling around the island with a <span class='font-black'>Vespa 50</span>  is an excellent solution to explore the beaches and coves near Marciana without problems of traffic and parking. It is an economical option that allows you to move comfortably and enjoy your vacation without stress.<br><span class='font-black'>Adequate scooter driving experience and AM or B license are required.</span>",
        "click": "Click here for more details."
      },
      "gallery": {
        "title": "Gallery",
      },
      "nav": {
        "det": "Details",
        "ser": "Services",
        "gal": "Gallery",
        "loc": "Location",
        "pre": "Price",
      },
      "dove": {
        "title": "Where we are",
        "body1": "Marciana is a characteristic village that offers a unique mix of history, culture, and natural beauty. You can explore the narrow streets of the town and discover small shops that sell local products and traditional restaurants that serve typical dishes.",
        "title2": "How to reach Marciana from Portoferraio",
        "body2": "You can reach Marciana from Portoferraio by <span class='font-black'>bus, taxi or car</span>. The travel time is approximately 40 minutes.",
        "foot": "Marciana is a peaceful medieval village located on the slopes of <span class='font-black'>Mount Capanne </span>, in the western part of the island of Elba. It is one of the oldest settlements on the island, with foundations dating back to 35 BC. You can visit the ancient fortress, which offers a breathtaking view of the surrounding area. If you are interested in hiking, you will find many trekking and mountain biking trails. <br> <br> Immersed in the greenery of oaks, pines, and chestnuts, and enjoying the freshest air, the area of Marciana exudes a special atmosphere with a mountain climate even though the sea is only <span class='font-black'>five kilometers</span> away. Like the rest of the island, the area of Marciana is rich in breathtaking beaches, such as the sandy expanses of Paolina, Procchio, and Spartaia, the sand and cliffs of Sant'Andrea, the cliffs of Punta Nera and Chiessi, and the rocks and pebbles of Pomonte and Patresi. In the village, there are available cafes, restaurants, wine bars, pizzerias, typical shops, ATMs, and tobacco shops."
      },
      "vicino": {
        "title": "What's near",
        "beach1": "Procchio beach",
        "beach2": "Paolina beach",
        "beach3": "Sant'Andrea beach",
        "beach4": "Marciana Marina beach",
        "beach1desc": "The beach of Procchio is one of the longest and best-equipped sandy beaches on the island of Elba. It is located in Procchio, about 10 km from Marciana. The beach is about one kilometer long and has fine golden sand. It can be reached by car in about 20 minutes from Marciana.",
        "beach2desc": "The Paolina beach is characterized by a small island covered in Mediterranean vegetation. The sand is mixed with pebbles. The water is clear and the seabed is splendid. It can be reached by car in about 15 minutes from Marciana. ",
        "beach3desc": "The beach of Sant'Andrea is one of the most famous beaches on Elba. The beach is characterized by turquoise and crystal-clear water, and smooth granite rocks that descend to the sea. It can be reached by car in about 10 minutes from Marciana.",
        "beach4desc": "The beach of Marciana Marina is well suited for families with children and is equipped with rental chairs, umbrellas, canoes, and pedal boats. It can be reached by car in about 8 minutes from Marciana.",
        "bottone": "Go"
      },
      "chisono": {
        "title":"About me",
        "body":"I am a former executive of a company with a great passion for storytelling, motorcycle riding, traveling, and table tennis. Currently, I live between Pisa and the Island of Elba, where I have created a characteristic and comfortable accommodation in the center of Marciana. I want to offer my guests the opportunity to experience a holiday in freedom, enjoying everything the island has to offer."
      }
      ,
      "prezzo": {
        "title": "Prices",
        "body": " The cost of the apartment varies depending on the month of booking, but in any case it starts from <span class='font-black'>60 euros</span> per night. <br> <br> <span class='font-black'>Payment methods:</span> The booking payment requires a deposit of 30% of the total, which must be paid at the time of booking. The remaining can be paid at check-in.",
        "mese1": "July",
        "mese2": "August",
        "mese3": "June & September",
        "mese4": "May",
        "notte": "/night",
        "info1": "Minimum stay 5 nights",
        "info2": "Minimum stay 3 nights",
        "info5": "Minimum stay 7 nights",
        "info4": " +30€ final cleaning",
        "info3": "Rent linen (sheets, towels) on request"
      }
    },
    it: {
      "intro": {
        "testo": "Un appartamento ispirato al <span class='font-black'>mondo Vespa</span>, situato in una storica strada pedonale nel villaggio medievale di <a href='https://goo.gl/maps/ckj5VXFV7nW2ay9PA' class='underline text-sky-600 font-black'>Marciana</a>. Arredato con gusto e attenzione ai dettagli, è uno <span class='font-black'>spazio accogliente</span> per <span class='font-black'>giovani coppie</span> in cerca di una location economica e affascinante.",
        "subtopic": "Internationalization and Localization"
      },
      "details": {
        "title": "Dettagli",
        "body": "L’appartamento ha un divano letto che racchiude all’interno un comodo <span class='font-black'>letto matrimoniale</span>, l’angolo cottura è dotato di <span class='font-black'>fornelli a induzione</span> e il bagno include <span class='font-black'>un'ampia doccia</span>. La biancheria (lenzuola, asciugamani) non è inclusa, ma sarà possibile noleggiarla su richiesta.",
        "letto": "Letto matrimoniale",
        "bathroom": "Bagno",
        "wifi": "Wi-fi gratis",
        "dim": "Dimensioni",
        "flat": "Su un piano",
        "cuc": "Cucina accessoriata",
        "park": "Parcheggio gratis",
        "sconto": "Sconto traghetto",
        "farmacia":"Farmacia vicina"
      },
      "services": {
        "title": "Servizi",
        "body": "Viaggiare sull'isola con una <span class='font-black'>Vespa 50</span> è un’ottima soluzione per esplorare le spiagge e le calette vicine a Marciana senza problemi di code e parcheggi. È un’opzione economica che ti permette di spostarti comodamente e goderti la tua vacanza senza stress. <br> <span class='font-black'>È necessaria una adeguata esperienza di guida di scooter e la patente AM o B.</span>",
        "click": "Clicca qui per maggiori informazioni."
      },
      "gallery": {
        "title": "Galleria",
      },
      "nav": {
        "det": "Dettagli",
        "ser": "Servizi",
        "gal": "Galleria",
        "loc": "Posizione",
        "pre": "Prezzi",
      },
      "dove": {
        "title": "Dove siamo",
        "body1": "Marciana è un caratteristico villaggio che offre un mix unico di storia, cultura e bellezza naturale. Potrai esplorare le stradine del paese e scoprire piccoli negozi che vendono prodotti locali e ristoranti tradizionali che servono piatti tipici.",
        "title2": "Come raggiungere Marciana da Portoferraio",
        "body2": "Puoi raggiungere Marciana da Portoferraio in <span class='font-black'>autobus, taxi o auto</span>. Il tempo di percorrenza è di circa 40 minuti.",
        "foot": "Marciana è un tranquillo villaggio medievale situato sulle pendici del <span class='font-black'>Monte Capanne</span>, nella parte occidentale dell’isola d’Elba. È uno dei più antichi insediamenti dell’isola con fondazioni risalenti al 35 a.C. Potrai visitare l'antica Fortezza, che offre una vista mozzafiato della zona circostante. Se sei interessato all’escursionismo, troverai molti sentieri per trekking e mountain bike.<br> <br> Immersa nel verde di querce, pini e castagni e godendo dell’aria più fresca, l’area di Marciana emana un’atmosfera speciale con un clima di montagna anche se il mare dista solo <span class='font-black'> cinque chilometri</span>. Come il resto dell’isola, l’area di Marciana è ricca di spiagge mozzafiato, come le distese sabbiose di Paolina, Procchio e Spartaia, la sabbia e le scogliere di Sant’Andrea; le scogliere di Punta Nera e Chiessi e le rocce e i ciottoli di Pomonte e Patresi. Nel villaggio sono disponibili bar caffè, ristoranti, enoteche, pizzerie, negozi tipici, bancomat e tabacchi."
      },
      "vicino": {
        "title": "Cosa c'è vicino",
        "beach1": "Spiaggia di Procchio",
        "beach2": "Spiaggia della Paolina",
        "beach3": "Spiaggia di Sant'Andrea",
        "beach4": "Spiaggia di Marciana Marina",
        "beach1desc": "La spiaggia di Procchio è una delle spiagge sabbiose più lunghe e meglio attrezzate dell’Isola d’Elba. Si trova a Procchio, a circa 10 km da Marciana. La spiaggia è lunga circa un chilometro e ha sabbia dorata e fine. In auto si raggiunge in circa 20 minuti da Marciana.",
        "beach2desc": "La spiaggia della Paolina è caratterizzata da una piccola isola coperta di macchia mediterranea. La sabbia è mista a ciottoli. L’acqua è trasparente e il fondale marino è splendido. In auto si raggiunge in circa 15 minuti da Marciana.",
        "beach3desc": "La spiaggia di Sant’Andrea è una delle spiagge più famose dell'Elba. La spiaggia è caratterizzata da acqua turchese e cristallina e da lisci massi di granito che scendono fino al mare. In auto si raggiunge in circa 10 minuti da Marciana.",
        "beach4desc": "La spiaggia di Marciana Marina si presta bene ad essere frequentata da famiglie con bambini ed è attrezzata con noleggio sdraio, ombrelloni, noleggio canoe e pedalò. In auto si raggiunge in circa 8 minuti da Marciana.",
        "bottone": "Vai"
      },
      "chisono": {
        "title":"Chi sono",
        "body":"Sono un ex dirigente d'azienda con una grande passione per la narrativa, il motociclismo, i viaggi e il tennis tavolo. Attualmente vivo tra Pisa e l'Isola d'Elba, dove ho creato un alloggio caratteristico e confortevole nel centro di Marciana. Desidero offrire ai miei ospiti la possibilità di vivere un'esperienza di vacanza in libertà, godendosi tutto ciò che l'isola ha da offrire."
      },
      "prezzo": {
        "title": "Prezzi",
        "body": "Il costo dell’appartamento varia a seconda del mese di prenotazione, ma in ogni caso parte da <span class='font-black'>60 euro</span> a notte. <br> <br><span class='font-black'>Modalità di pagamento:</span> Il pagamento della prenotazione richiede una caparra del 30% del totale, che andrà effettuata al momento della prenotazione. Il restante potrà essere saldato al momento del check-in.",
        "mese1": "Luglio",
        "mese2": "Agosto",
        "mese3": "Giugno e Settembre",
        "mese4": "Maggio",
        "notte": "/notte",
        "info1": "Permanenza minima 5 notti",
        "info2": "Permanenza minima 3 notti",
        "info5": "Permanenza minima 7 notti",
        "info3": "Biancheria prenotabile su richiesta",
        "info4": "+30€ pulizia finale"
      }
    },
  });
  locale.set(_locale);
}
export {
  _,
  setupI18n,
  t
};