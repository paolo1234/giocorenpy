#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.
define f = Character("Femmina", color="#f44000")
define m = Character("Maschio", color="#1363CC")

image fem = im.Scale("fem.png", 392, 901)
image mas = "masfr.png"
# image mas = im.Scale("masfr.png", 400, 833)
# Il gioco comincia qui. 

label start:

    scene bg room

    show fem at center

    show mas:
        xalign 0.9
        yalign 1.0
    with fade

    # Questo mostra linee di dialogo.
    "\"Citta brutta e sperduta, 2021..\""
    "..."
    f "Ugh.. Non capisco cosa non vada con la mia console"
    m "Ma che noiosa che seii! Ma staccati ogni tanto da questi computer e vieni fuori a giocare"
    f "Se non vuoi aiutarmi stai zitto almeno."
    m "Come faccio ad aiutarti se non fai altro che lamentarti?!!"
    f "Shh, su dai aiutami con questo cavo che non riesco ad accendere la console..."
    m "Uff ok arrivo..."
    m "Si è acceso??"
    f "No... ma che problema avrà mai?..."
    m "Ho trovato! Aspetta che provo a cambiare presa.."
    f "AH!! Guarda si è accesaaaa"
    m "Eheh ecco mancava il mio tocco magico"
    f "Bene! Come premio hai ricevuto una partita flash contro di me eheheh"
    m "Uff... ma che nerd che sei"
    f "Su dai... scegli un giocatore!"
    m "Voglio quello lì a destra"
    "Console: *si spegne*"
    f "Ugh figuriamoci, mi sembrava strano fosse così facile..."
    m "Tranquillaaaa ci penso io ad aggiustare di nuovo tutto eheh"
    m "Faccio un salto in cantina a prendere gli attrezzi e vediamo di aprire questo rottame"
    f "Ehii non è un rottame!"
    m

    return