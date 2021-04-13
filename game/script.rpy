#  Dichiara i personaggi usati in questo gioco. L'argomento 'color' colora il nome del personaggio.
define f = Character("Ragazza", color="#f44000")
define m = Character("Ragazzo", color="#1363CC")
define c = Character("Console")

image fem = im.Scale("fem.png", 392, 901)
image mas = "masfr.png"
image bg stanza = im.Scale("bg stanza.jpg",1920,1080)
image bg nero = im.Scale("bg nero.jpg",1920,1080)
image bg cantina = im.Scale("bg cantina",1920,1080)

# image mas = im.Scale("masfr.png", 400, 833)
# Il gioco comincia qui. 

label start:

    scene bg nero 
    with fade

    # Questo mostra linee di dialogo.
    "\"Citta' brutta e' sperduta, 204X..\""

    scene bg stanza 
    with fade

    show fem at center 
    

    show mas:
        xalign 0.9
        yalign 1.0
    
    
    f "Ugh.. Non capisco cosa non vada con la mia console"
    m "Ma che noiosa che seii! Ma staccati ogni tanto da questi computer e vieni fuori a giocare"
    f "Se non vuoi aiutarmi stai zitto almeno."
    m "Come faccio ad aiutarti se non fai altro che lamentarti?!!"
    f "Shh, su dai aiutami con questo cavo che non riesco ad accendere la console..."
    m "Uff ok arrivo..."
    pause 1.5
    m "Si è accesa??"
    f "No... ma che problema avrà mai?..."
    m "Ho trovato! Aspetta che provo a cambiare presa.."
    pause 1.0
    f "AH!! Guarda si è accesaaaa"
    m "Eheh ecco mancava il mio tocco magico"
    f "Bene! Come premio hai ricevuto una partita flash contro di me eheheh"
    m "Uff... ma che nerd che sei"
    f "Su dai... scegli un giocatore!"
    m "Voglio quello lì a destra"
    c "*si spegne*"
    f "Ugh figuriamoci, mi sembrava strano fosse così facile..."
    m "Tranquillaaaa ci penso io ad aggiustare di nuovo tutto "
    m "Faccio un salto in cantina a prendere gli attrezzi e vediamo di aprire questo rottame"
    f "Ehii non è un rottame!"
    m "Beh considerando che l’hai dal 2015, direi che sarebbe il momento di cambiarla..."
    f "Basta fare commenti sulla mia console! su scendi a prendere gli attrezzi."
    pause 1.0
    "*In cantina..*"
    scene bg cantina
    with fade
     pause 1.0
    m "Uhm vediamo un po'.. dove saranno?"
    m "AH eccoli!"
    "*FIUU*"
    m "EHHH cos'è stato??"
    m "...."
    m "Ah, è solo caduto uno scatolo...fiù"
    m "Signorina, ha per caso bisogno di un tuttofare?"
    f "Non fare l'idiota e sbrigati su!"
    m "Subito" 
    m "Prima di tutto apriamola"
    m "Ma...ci sono dei fili staccati"
    m "E qua è tutto ammaccato"
    m "Ma cosa hai combinato a questa console??"
    f "Cosa?? io non l’ho mai toccata...non ho idea di come si sia ridotta così"
    m "Strano…"
    m "Non fa niente , mettiamoci all’opera"
    m "Ho prima di tutto vari fili staccati…ma una sola entrata"
    m "quale dovrei mettere prima…"

    menu:
        "rosso":
            m "proviamo il rosso…"
            "(zzt... scossa)"
            m "AAAHG"
            f "tutto bene??"
            m "ho preso la scossa accidenti"
            f "ottimo..."
        "verde":
            jump badEnd
        "blu":
            m "beh penso che sia veramente arrivato il momento di buttare via questo affare"
            f "uff...vado a metterla nel casonetto"

            f "ugh è difficile aprire la porta con questo coso in mano"
            f "uh? cosa è questo pacco?"
            f "che strano non ho ordinato niente di recente…"
            m "apriamolo!"
            f "mh si, io vado a buttare questo vecchia cara console, tu comincia a portarlo dentro."



    return

label badEnd:
    "OPS SIETE MORTI!"

# label scegliNome:
#     python:
#         name = name.input("Come ti chiami?", 20)
#         name = name.split()