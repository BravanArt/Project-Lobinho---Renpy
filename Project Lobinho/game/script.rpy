# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define K = Character ("Koha",  color="#8B008B")
define P = Character ("Punk1",  color="6B8E23")
define U = Character ("Punk2",  color="#BC8F8F")
define V = Character ("Viktor",  color="#8B0000")
define R = Character ("Roberto",  color="#FF8C00")

# cenas
image Bunker = im.Scale("porao.jpg", 1920,1080)
image Escada = im.Scale("escadas.jpg", 1920,1080)
image RuaM = im.Scale("rua mercado.jpg", 1920,1080)
image Mercado = im.Scale("mercado.jpg", 1920,1080)
image Rua = im.Scale("rua.jpg", 1920,1080)
image Barril = im.Scale("esconder.jpg", 1920,1080)
image Sala = im.Scale("vr-sala.jpg", 1920,1080)
image Jump = im.Scale("gatinho.jpg", 1920, 1080)

# personagens
image Viktor = im.Scale("viktor.png", 600, 811)
image Koha = im.Scale("koha.png", 358, 640)
image Punk1 = im.Scale("punk1.png", 600, 811)
image Punk2 = im.Scale("punk2.png", 600, 811)
image Cao1 = im.Scale("cao1.png", 200, 260)
image Cao2 = im.Scale("cao2.png", 200, 220)
image Cao3 = im.Scale("cao3.png", 200, 220)


# The game starts here.

label start:
    
    scene black with dissolve
    
    show text "{size=+30}FATEC Carapicuíba presents...{/size}" with zoomin
    $renpy.pause(2, hard="True")
    show text "{size=+30}LOBINHO \n The Game{/size}" with zoomout
    $renpy.pause(2, hard="True")
    $A = renpy.input("Digite seu nome:")
    scene Bunker with  dissolve
    "%(A)s acorda no bunker e vê seus dois colegas conversando. Viktor estava sentado se apoiando na parede e Koha estava agachada ao seu lado. "
    "Os dois tinham acabado de voltar de uma expedição em busca de comida, mas não obtiveram sucesso. "
    show Viktor at right with moveinleft
    V "De que adianta, não temos mais comida, temos que voltar lá pra cima!!"
    show Koha at center with moveinright
    K "Mas Viktor, você acabou de quebrar a perna, como quer pegar algo se nem andar consegue?"
    V "A questão não é querer, é precisar!"
    K "Puta merda... A gente podia mandar o(a) %(A)s..."
    V "Tá doida?! Vai mandar ele(a) direto pra morte, ele(a) é cabaço, não sabe fazer nada direito..."
    K "Mas, não tem outra escolha, eu tenho que ficar aqui pra cuidar dos seus ferimentos... "
    "%(A)s ouve parte da conversa e se sente acuado(a), porém com muita coragem ele(a) enche o peite e diz algo."
    pause 1
    jump choiceMenu
    
label choiceMenu:
    menu:
        "Vou te mostrar quem é cabaço, eu já volto.":
            "Ele(a) se equipa com uma mochila pegando o pouco de água que resta, um kit médico e um revólver na cintura, sobe as escadas e saí do bunker em busca de suprimentos."
            scene Rua with dissolve
            pause 1
            scene RuaM with dissolve
            "%(A)s encontra um mercado e precisa decidir se vai entrar nele ou seguir adiante..."
            jump choiceMercado
        "Pode ir lá em cima Koha, eu consigo cuidar do Viktor.":
            "Koha então se equipa com os poucos suprimentos que restam e põe seu revolver na cintura, e começa a subir as escadas"
            A "Boa sorte Koha, vê se volta viva hein?"
            K "Hahaha muito engraçado..."
            hide Koha with dissolve
            A "Tem algo que eu possa fazer pra aliviar um pouco a dor?"
            V "Na verdade, tem sim, me deixa em paz, pode ser?"
            A "Nossa... Tá bom.."
            "Uma grande explosão ensurdecedora toma conta do bunker e %(A)s se esconde, ele(a) tenta carregar Viktor mas é muito fraco(a) para isso... "
            hide Viktor with dissolve
            scene Escada with dissolve
            "Ele(a) vê um bando de punks descendo as escadas do bunker e se separando lá dentro em busca de suprimentos, até que acham Viktor e o matam a sangue frio com um tiro na cabeça..."
            A "{i}Puta merda... O que é que eu faço? O que é que eu faço????{/i} " 
            scene Jump with zoomin
            pause 0.5
            scene Escada with dissolve
            show Punk2 with squares
            "%(A)s é virado bruscamente por um punk que apenas o observa com olhos fundos e sem alma, então o homem aponta uma faca em sua direção e a passa em seu pescoço."
            scene black with dissolve
            pause 1
            scene Sala with dissolve
            R "Meu deus, pensei que era um jogo de sobrevivência, não terror, ah agora não vou conseguir mais dormir por alguns dias..."
            scene black with dissolve
            show text "{size=+30}The End!{/size}" with dissolve
            $renpy.pause(2, hard="True")
            return 
            
label choiceMercado:
    menu:
        "Entrar no mercado":
            A "Que saco, nunca me deixam fazer nada e quando acontece algo assim ainda me xingam, falam que não presto pra nada... Talvez seja verdade, mas agora tenho que me focar em achar suprimentos."
            scene Mercado with dissolve
            show Cao1 at left with moveinright
            show Cao2 at right with moveinleft
            show Cao3 at center with squares
            "%(A)s encontra com um cachorro selvagem dentro do mercado, e quando pensa ser só um, aparece mais outro, e do nada um terceiro cachorro o ataca de surpresa."
            scene black with dissolve
            pause 1
            scene Sala with dissolve
            R "Nossa, esses jogos estão cada vez mais realista, fiquei até com dor de cabeça, melhor descansar..."
            scene black with dissolve
            show text "{size=+30}The End!{/size}" with dissolve
            $renpy.pause(2, hard="True")
            return
        "Segue em frente":
            A "Melhor continuar seguindo, esse mercadinho já deve estar todo saqueado."
            scene Rua with dissolve
            "%(A)s encontra com um grupo de punks armados andando em sua direção e rapidamente se esconde."
            scene Barril with dissolve
            A "{i}Puta merda, acho que eles me viram, e agora?!?!?{/i} "
            show Punk1 at left with moveinleft
            P "Passarinho? Acha que a gente é cego é? Hahahah, aparece logo e passa tudo, imbecil!"
            "%(A)s precisa fazer uma escolha..."
            jump choicePunk
label choicePunk:
    menu:
        "Entrega tudo":
            A "{i}Que merda...{/i} "
            A "Beleza, tá aqui, é tudo que eu tenho, ok?"
            P "Hm, mas ainda é muito pouco, quer saber? Hoje sai de casa com sangue de morte, hahaha... "
            "~Tiro~"
            scene black with dissolve
            pause 1
            scene Sala with dissolve
            R "Nossa, fiquei realmente assustado com esses punks, ainda bem que eles não existem na vida real, acho que vou tirar um cochilo... "
            scene black with dissolve
            show text "{size=+30}The End!{/size}" with dissolve
            $renpy.pause(2, hard="True")
            return
        "Decide lutar":
            A "{i}Ok, tenho que fazer um ataque surpresa, bora, 3 2 1 e...{/i}"
            A "AAAAARGGH!!!!! ~ Atirando"
            "%(A)s gasta todos os tiros e não acerta um!"
            P "HAHAHHAHAHAHAH sério? Isso é tudo? Ai cara, eu ri tanto agora que até perdi a vontade de te matar, mas quer saber? que se foda..."
            "~Leva tiro e morre~"
            scene black with dissolve
            pause 1
            scene Sala with dissolve
            R "Nossa, é difícil acertar um tiro nesses jogos, ainda bem que não tenho que atirar em ninguém na vida real, até cansei um pouco, acho que vou tirar um cochilo... "
            scene black with dissolve
            show text "{size=+30}The End!{/size}" with dissolve
            $renpy.pause(2, hard="True")
            return
            
            
            
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.

   

    # This ends the game.

    return
