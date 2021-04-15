#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.
define f = Character("Ragazza", color="#f44000")
define m = Character("Ragazzo", color="#1363CC")
define c = Character("Console", color="#FFFFFF")

#Fem
image fem = im.Scale("fem.png", 392, 901)
image fem infastidita = "fem infastidita.png"
#Mas
image mas = "masfr.png"
image mas spaventato = "mas spaventato.png"
image mas sorridente = "mas sorridente.png"
image mas seccato = "mas seccato.png"
image mas confuso = "mas confuso.png"

#Bg
image bg stanza = im.Scale("bg stanza.jpg",1920,1080)
image bg nero = im.Scale("bg nero.jpg",1920,1080)
image bg cantina = im.Scale("bg cantina.jpg",1920,1080)

# image mas = im.Scale("masfr.png", 400, 833)
# Il gioco comincia qui. 

label start:

    scene bg nero 
    with fade

    # Questo mostra linee di dialogo.
    "\"Citta' brutta e sperduta, 204X..\""

    scene bg stanza 
    with fade

    show fem at center 
    

    show mas:
        xalign 0.9
        yalign 1.0
    
    
    f "Ugh.. Non capisco cosa non vada con la mia console."
    m "Ma che noiosa che seii! Ma staccati ogni tanto da questi computer e vieni fuori a giocare."
    f "Se non vuoi aiutarmi stai zitto almeno."
    m "Come faccio ad aiutarti se non fai altro che lamentarti?!!"
    f "Shh, su dai aiutami con questo cavo che non riesco ad accendere la console..."
    m "Uff ok arrivo..."
    pause 1.5
    m "Si è accesa??"
    f "No... ma che problema avrà mai?..."
    m "Ho trovato! Aspetta che provo a cambiare presa.."
    pause 1.0
    f "AH!! Guarda si è accesaaaa."
    m "Eheh ecco mancava il mio tocco magico."
    f "Bene! Come premio hai ricevuto una partita flash contro di me."
    m "Uff... ma che nerd che sei."
    f "Su dai... scegli un giocatore!"
    m "Voglio quello lì a destra."
    c "*si spegne*"
    f "Ugh figuriamoci, mi sembrava strano fosse così facile..."
    m "Tranquillaaaa ci penso io ad aggiustare di nuovo tutto."
    m "Faccio un salto in cantina a prendere gli attrezzi e vediamo di aprire questo rottame."
    f "Ehii non è un rottame!"
    m "Beh considerando che l’hai dal 2015, direi che sarebbe il momento di cambiarla..."
    f "Basta fare commenti sulla mia console! su scendi a prendere gli attrezzi."
    pause 1.0
    scene bg cantina
    with fade
    show mas at center
    "*In cantina*"
    pause 0.5
    m "Uhm vediamo un po'...dove saranno?"
    pause 1.0
    m "AH eccoli!"
    "*FIUU*"
    hide mas
    show mas spaventato

    m "EHHH cos'è stato??"
    m "...."
    m "Ah, è solo caduto uno scatolo..."
    pause 1.0
    scene bg stanza
    with fade
    show mas sorridente:
        xalign 0.9
        yalign 1.0
    show fem at center 
    m "Signorina, ha per caso bisogno di un tuttofare?"
    hide fem
    show fem infastidita
    f "Non fare l'idiota e sbrigati su!"
    m "Subito." 
    m "Prima di tutto apriamola."
    pause 1.0
    hide mas sorridente
    show mas confuso
    m "Ma...ci sono dei fili staccati."
    m "E qua è tutto ammaccato."
    m "Ma cosa hai combinato a questa console??"
    f "Cosa?? io non l’ho mai toccata...non ho idea di come si sia ridotta così."
    m "Strano…"
    m "Non fa niente, mettiamoci all’opera."
    m "Prima di tutto ci sono vari fili staccati…ma una sola entrata."
    m "Quale dovrei collegare prima??"

    menu:
        "Rosso":
            m "Proviamo il rosso…"
            "(zzt...)"
            m "AAAHG"
            f "Tutto bene??"
            m "Ho preso la scossa accidenti."
            f "Ottimo..."
        "Verde":
            "(zzztt…)"
            m "Oh no cavolo."
            f "Ehi allontanati!"
            "BOOOOM"
            jump badEnd
        "Blu":
            m "Oh, ecco fatto!!"
            m "Prova ad accenderla."
            pause 1.0
            f "Wow"
            m "Il signor tuttofare colpisce ancora eheh funziona!"
            "(zzzppp…)"
            pause 0.5
            f"Sì il signor tuttofare ha proprio colpito…"
            m"Oh cavolo."

    m "Beh penso che sia veramente arrivato il momento di buttare via questo affare."
    f "Uff...vado a metterla nel casonetto."
    pause 1.0
    f "Ugh è difficile aprire la porta con questo coso in mano."
    f "Uh? cosa è questo pacco?"
    f "Che strano non ho ordinato niente di recente…"
    m "Apriamolo!"
    f "Mh si, io vado a buttare questo vecchia cara console, tu comincia a portarlo dentro."

    return

label badEnd:
    scene bg nero 
    with fade
    pause 0.5
    "BAD END"

# label scegliNome:
#     python:
#         name = name.input("Come ti chiami?", 20)
#         name = name.split()