from manim import *

def fix_cap(mob):
    for m in mob.family_members_with_points():
        m.set_cap_style(CapStyleType.BUTT)
    return mob

def T(texto, **kwargs):
    return fix_cap(Text(texto, **kwargs))


class Aula3(Scene): #Essa aula é o último teste com updaters para uma cena só. Na próxima separarei em diferentes classes
    config.background_color = "#1E1E1E"
    Text.set_default(font = "Manrope")

    #Updater para scale
    def grow_until_target(self, mob, dt): #altura final é const
            if mob.height < 0.3:
                mob.scale(1 + 4.0 * dt) #porcentagem de crescimento
            if mob.height > 0.3:
                mob.height = 0.3
    #Caixinha (agora so texto)
    def physics_updater(self, obj, dt):
        if not 0 < dt < 0.1: #Check para ver se deltaTime foi interrompido
            return
        if obj.active == False: #Matar animação
            return
        
        obj.velocity= obj.velocity + obj.gravity * dt 

        obj.shift(obj.velocity * dt) #aplicando transformacao com deltaTime
        box_half_width= obj.width / 2
        box_half_height= obj.height / 2
        #Começo de verificação de colisão e aplicando bounce
        if obj.get_right()[0] >= config.frame_width/2:
            obj.set_x(config.frame_width/2 - box_half_width)
            obj.velocity[0]= -obj.velocity[0] * obj.damping
        if obj.get_left()[0] <= -config.frame_width/2:
            obj.set_x(-config.frame_width/2 + box_half_width)
            obj.velocity[0]= -obj.velocity[0] * obj.damping
        if obj.get_top()[1] >= config.frame_height/2:
            obj.set_y(config.frame_height/2 - box_half_height)
            obj.velocity[1]= -obj.velocity[1] * obj.damping
        if obj.get_bottom()[1] <= -config.frame_height/2:
            obj.set_y(-config.frame_height/2 + box_half_height)
            obj.velocity[1]= -obj.velocity[1] * obj.damping


    #----Funções de animação----

    def codigoLivroCarta(self):
        tituloCodigo = Text(
            "Código é texto",
            t2c={"texto": PURPLE},
            font_size=80
        ).scale(0.5)

        tituloCodigo.move_to([0,3,0])

        blocoNotas = ImageMobject("images/blocoNotas.png").scale(1.5).shift(DOWN * 0.4)

        textoNotasComp = Text(
            '#include <stdio.h>\n'
            'int main() {\n'
            '    int v[5] = {10, 20, 30, 40, 50};\n'
            '    printf("Original: ");\n'
            '    for(int i = 0; i < 5; i++) {\n'
            '        printf("%d ", v[i]);\n'
            '    }\n'
            '\n'
            '    printf("\\nInvertido: ");\n'
            '    for(int i = 4; i >= 0; i--) {\n'
            '        printf("%d ", v[i]);\n'
            '    }\n'
            '\n'
            '    return 0;\n'
            '}', font_size = 80, color = "#000000", line_spacing = 0.8
        ).scale(0.15)

        textoNotasComp.move_to(blocoNotas.get_center())
        textoNotasComp.shift(LEFT*1.25, DOWN*0.32)

        # carta, livro, codigo-fonte
        ApenasTextoComp = Text(
            "Tudo é texto",
            t2c={"texto": PURPLE}, 
            font_size=80
        ).scale(0.5)
        ApenasTextoComp.move_to([0,3,0])

        carta = ImageMobject("images/carta.png").scale(0.5)
        livro = ImageMobject("images/livro.png").scale(0.5)
        codigo = ImageMobject("images/coding.png").scale(0.5)

        igual1 = Text("=", font_size = 90).scale(1)
        igual2 = Text("=", font_size = 90).scale(1)

        grupo = Group(codigo, igual1, carta, igual2, livro)
        grupo.arrange(RIGHT, buff=1.0)
        grupo.move_to(ORIGIN)

        # linguagem de programacao vs linguagem humana
        tituloTexto = Text("Texto", font_size=80).scale(0.5)
        tituloCode = Text("Código", font_size=80).scale(0.5)

        grupo = VGroup(tituloTexto, tituloCode).arrange(RIGHT, buff=1)
        grupo.move_to([0,3,0])

        seta = Arrow(tituloTexto.get_right(), tituloCode.get_left(), buff = 0.1, color=PURPLE)

        aprender1 = Text("Se o usuário demonstra interesse em C, iniciamos sua trilha", font_size = 80).scale(0.35)
        aprender2 = Text("de aprendizado e começamos pelos fundamentos.", font_size = 80).scale(0.35)
        condicaoAprender = VGroup(aprender1, aprender2).arrange(DOWN, aligned_edge = LEFT, buff = 0.3)

        codeAprender = '''if (usuario.quer_aprender_c) {
    iniciar_trilha("C");
    usuario.nivel = 1;
    printf("Fundamentos iniciados...");
}'''
        rendered_codeAprender = Code(
            code_string = codeAprender, 
            language = "c", 
            formatter_style = "monokai", 
            background = "rectangle", 
            background_config = {"fill_color": "#4400FFFF", "stroke_color": "WHITE", "fill_opacity":0.1}).scale(1) 


        word = ImageMobject("images/docWord.png").shift(DOWN * 0.4)

        textoWord = Text(
            'if (usuario.quer_aprender_c) {\n'
            '    iniciar_trilha("C");\n'
            '    usuario.nivel = 1;\n'
            '    printf("Fundamentos iniciados...");\n'
            '}', font_size=80, color="#000000", line_spacing=0.8
        ).scale(0.15)
        
        textoWord.move_to(word.get_center())
        textoWord.shift(LEFT * 0.5)

        # codigo no bloco de notas
        self.play(Write(tituloCodigo))
        self.play(FadeIn(blocoNotas))
        self.play(AddTextLetterByLetter(textoNotasComp), run_time = 2.5)
        self.play(FadeOut(tituloCodigo),FadeOut(blocoNotas), FadeOut(textoNotasComp))
        self.wait()


        self.play(Write(ApenasTextoComp))
        self.play(
            LaggedStart(
                FadeIn(codigo),
                Write(igual1),
                FadeIn(carta),
                Write(igual2),
                FadeIn(livro),
                lag_ratio=0.5
            ), run_time = 1
        )

        self.play(FadeOut(ApenasTextoComp), FadeOut(codigo), FadeOut(igual1), FadeOut(carta), FadeOut(igual2), FadeOut(livro), run_time = 1)

        self.play(
            LaggedStart(
                Write(tituloTexto),
                GrowArrow(seta),
                Write(tituloCode),
                lag_ratio=0.3
            )
        )
        self.play(AddTextLetterByLetter(aprender1), run_time = 1.5)
        self.play(AddTextLetterByLetter(aprender2), run_time = 1.5)
        self.wait(0.5)

        self.play(FadeOut(condicaoAprender))
        self.play(Write(rendered_codeAprender))
        self.play(Unwrite(tituloTexto), Uncreate(seta), Unwrite(tituloCode))
        self.play(rendered_codeAprender.animate.scale(0.6).move_to([0,3,0]))
        self.play(FadeIn(word))
        self.play(rendered_codeAprender.animate.shift(DOWN * 2), TransformMatchingShapes(rendered_codeAprender, textoWord))
        self.wait()
        self.play(FadeOut(textoWord), FadeOut(word), run_time = 1)
        self.wait()


    def introComando(self):
        logoComando = SVGMobject("svgs/comando.svg").scale(2)
        comando = Text("COMANDO.C", font="Major Mono Display").shift(2*DOWN).scale(0.8)
        cursor = Rectangle(
            color = GREY_A,
            fill_color = GREY_A,
            fill_opacity = 1.0,
            height = 1.1,
            width = 0.5,
        ).scale(0.5).move_to(comando[0])
        self.play(Write(logoComando), run_time=2)
        self.play(logoComando.animate.shift(0.5*UP))
        self.play(TypeWithCursor(comando, cursor), run_time=1.5)
        self.play(Blink(cursor, blinks=2))
        self.wait()
        self.clear()


    def configurandoAmbiente(self):
        text = Text("Configurando seu", font_size = 45)
        text2 = Text("ambiente de programação", color = PURPLE, font_size=50)

        acronym = Tex("{{I}}{{D}}{{E}}")
        acronym.font_size = 128
        acronym.set_color(PURPLE)
        fullText = Tex("{{I}}ntegrated {{D}}evelopment {{E}}nvironment")
        fullText.scale(0.8)

        # trocar a cor das iniciais para roxo
        fullText.set_color_by_tex("I", PURPLE)
        fullText.set_color_by_tex("D", PURPLE)
        fullText.set_color_by_tex("E", PURPLE)

        codeblocks = SVGMobject("svgs\\codeblocks")
        eclipse = SVGMobject("svgs\\eclipseide")
        vim = SVGMobject("svgs\\vim")
        pycharm = SVGMobject("svgs\\pycharm")
        mvs = SVGMobject("svgs\\visualstudio").scale(0.75)
        neoVim = SVGMobject("svgs\\neovim").scale(0.5)
        vscode = SVGMobject("svgs\\vscode")
        sublimeText = SVGMobject("svgs\\sublimetext")

        ide = VGroup(pycharm, mvs, eclipse, codeblocks)
        top = VGroup(mvs, neoVim, sublimeText, pycharm)
        bottom = VGroup(eclipse, vim, codeblocks, vscode)
        naoIde= VGroup(vscode, neoVim, sublimeText, vim)

        text2Group = VGroup(VGroup(letter for letter in text2[:8]),
                            VGroup(letter for letter in text2[8:10]),
                            VGroup(letter for letter in text2[10:]))
        
        rawTitle = VGroup(text, text2).arrange(DOWN, aligned_edge = LEFT, buff = 0.2)

        #Adicionando "ferramentas desnecessárias" e ajustando parâmetros
        #Ainda to devendo de criar uma classe para esse bgl
        globalGravity = np.array([0, -9.8, 0])
        iaText = Text("Agentes de IA", font_size=78).scale(0.4)
        iaText.velocity = np.array([5.0, -1, 0]) #velocidade inicial
        iaText.gravity = globalGravity
        iaText.damping = 0.9
        iaText.active = True

        net = Text("Integração .NET", font_size=100).scale(0.2)
        net.velocity = np.array([-1.0, -2.0, 0]) #velocidade inicial
        net.gravity = globalGravity
        net.damping = 0.9
        net.active = True

        dataBase = Text("Integração com GIT", font_size=100).scale(0.2)
        dataBase.velocity = np.array([-1.0, 7.0, 0]) #velocidade inicial
        dataBase.gravity = globalGravity
        dataBase.damping = 0.9
        dataBase.active = True

        compilacao = Text("Compilador incremental", font_size=78).scale(0.1)
        compilacao.velocity = np.array([2.0, 8.0, 0]) #velocidade inicial
        compilacao.gravity = globalGravity
        compilacao.damping = 0.9
        compilacao.active = True

        debugger = Text("Debugger", font_size=78).scale(0.1)
        debugger.velocity = np.array([4.0, 3.0, 0]) #velocidade inicial
        debugger.gravity = globalGravity
        debugger.damping = 0.9
        debugger.active = True

        terminalInteg = Text("Terminal integrado", font_size=78).scale(0.1)
        terminalInteg.velocity = np.array([-7.0, 0, 0]) #velocidade inicial
        terminalInteg.gravity = globalGravity
        terminalInteg.damping = 0.9
        terminalInteg.active = True

        features = VGroup(iaText, net, dataBase, compilacao, debugger, terminalInteg)

        #Correção de svgs
        neoVim[0].set_color("#16B0ED")
        neoVim[1].set_color("#367533")
        neoVim[2].set_color("#88C649")
        pycharm[0].set_color("#07C3F2")
        pycharm[1].set_color("#21D789")
        pycharm[2].set_color("#32DA84")
        pycharm[3].set_color("#CFE865")
        pycharm[4].set_color("#F1EB5E")
        vscode[0].set_color("#32B5F1")
        vscode[1].set_color("#0E69AC")
        vscode[2].set_color("#0F6FB3")
        sublimeText[0].set_color("#D06F00")
        vim[0].set_color("#019833")
        vim[10].set_color("#049A20")

        #Separando palavras e começando animação
        self.play(Write(rawTitle))
        self.wait()
        
        #Separando letras e apps
        self.play(AnimationGroup(FadeOut(text), FadeOut(text2Group[1]), run_time=0.4),
                  text2Group[0][2].animate.move_to([5,-1.5,0]).scale(0), #B
                  text2Group[0][4].animate.move_to([-5,-1.5,0]).scale(0), #E
                  text2Group[0][7].animate.move_to([-5,-1.5,0]).scale(0), #E
                  text2Group[0][3].animate.move_to([-2,-1.5,0]).scale(0), #I
                  text2Group[0][1].animate.move_to([-5,1,0]).scale(0), #M
                  text2Group[2][6].animate.move_to([-5,1,0]).scale(0), #M
                  text2Group[0][5].animate.move_to([-2,1,0]).scale(0), #N
                  text2Group[0][6].animate.move_to([2,1,0]).scale(0), #T
                  text2Group[2][0].animate.move_to([5,1,0]).scale(0), #P
                  text2Group[2][2].animate.move_to([0,0,0]).scale(0), #O
                  text2Group[2][10].animate.move_to([0,0,0]).scale(0), #O
                  text2Group[2][1].animate.move_to([0,0,0]).scale(0), #R
                  text2Group[2][4].animate.move_to([0,0,0]).scale(0), #R
                  text2Group[2][3].animate.move_to([0,0,0]).scale(0), #G
                  text2Group[0][0].animate.move_to([0,0,0]).scale(0), #A
                  text2Group[2][5].animate.move_to([0,0,0]).scale(0), #A
                  text2Group[2][7].animate.move_to([0,0,0]).scale(0), #A
                  text2Group[2][9].animate.move_to([0,0,0]).scale(0), #Ã
                  text2Group[2][8].animate.move_to([2,-1.5,0]).scale(0) #Ç
                  )
        
        codeblocks.move_to(text2Group[0][2].get_center())
        eclipse.move_to(text2Group[0][4].get_center())
        vim.move_to(text2Group[0][3].get_center())
        mvs.move_to(text2Group[0][1].get_center())
        neoVim.move_to(text2Group[0][5].get_center())
        pycharm.move_to(text2Group[2][0].get_center())
        sublimeText.move_to(text2Group[0][6].get_center())
        vscode.move_to(text2Group[2][8].get_center())

        # colocando a parte inicial sobre código é texto, linguagem de programação e linguagem humana
        self.codigoLivroCarta()

        #adicionando a intro
        self.introComando()

        self.wait()

        #Escrevendo logos em cima
        self.play(Write(codeblocks), Write(eclipse), Write(vim), Write(mvs),
                  Write(neoVim), Write(pycharm), Write(vscode), Write(sublimeText), run_time=2)
        self.wait(3)
        
        #Fade em tudo que não saiu
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        fullText.font_size = 80
        fullText[0].scale(1.1)
        fullText[2].scale(1.1)
        fullText[4].scale(1.1)

        #Reposicionando ferramentas
        top.shift([-15, 1, 0]).scale(0.8)
        bottom.shift([15, -1, 0]).scale(0.8)
        #---Texto expandindo e ferramentas---
        self.wait()
        self.play(Write(acronym))
        self.wait()
        
        self.play(TransformMatchingTex(acronym, fullText))
        
        self.wait(2)
        self.play(fullText.animate.scale(0.6))
        self.play(
                  top.animate.shift([15,0,0]),
                  bottom.animate.shift([-15,0,0]),
                  rate_func = rate_functions.ease_out_back)
        self.wait()
        
        #Ides e chinelada no codeblocks acontecem aqui
        self.play(FadeOut(naoIde))
        self.play(ide.animate.arrange(direction=RIGHT,buff=0.5, center=True),
                  ShrinkToCenter(fullText))
        self.wait()
        
        #---Mostrar features desnecessários---
        net.move_to(mvs.get_center())
        debugger.move_to(codeblocks.get_center())
        compilacao.move_to(eclipse.get_center())
        dataBase.move_to(pycharm.get_center())
        self.play(*[Wiggle(singleide, n_wiggles=1000, run_time=1) for singleide in ide])
        self.add(features)

        for feature in features:
            feature.add_updater(self.grow_until_target)
            feature.add_updater(self.physics_updater)
        self.wait(0.6)

        for feature in features:
            feature.remove_updater(self.grow_until_target)
            feature.remove_updater(self.physics_updater)
        #não precisa desses features
        
        self.wait()

        crossGroup = VGroup(*[Cross(feature, color=RED, stroke_width=3).scale(1.1).move_to(feature) for feature in features])
        crossGroup.set_cap_style("round")
        self.play(Write(crossGroup))
        self.wait(2)

        self.play(*[FadeOut(obj) for obj in self.mobjects])
        
    def editoresTexto(self):
        titulo = Text("Editores de texto")

        vim = SVGMobject("svgs\\vim")
        sublimeText = SVGMobject("svgs\\sublimetext")
        notePad = SVGMobject("svgs\\notepad")
        vscode = SVGMobject("svgs\\vscode")
        editors = VGroup(vim, sublimeText, notePad, vscode).scale(0.9)

        caixa1 = RoundedRectangle(corner_radius=0.5, color = BLUE,
                          fill_opacity=0.1,height=2.0,width=8.0).move_to([0,0,-1])
        caixa2 = RoundedRectangle(corner_radius=0.5, color = BLUE,
                          fill_opacity=0.1,height=2.0,width=2.5)

        vscode[0].set_color("#32B5F1")
        vscode[1].set_color("#0E69AC")
        vscode[2].set_color("#0F6FB3")
        sublimeText[0].set_color("#D06F00")
        vim[0].set_color("#019833")
        vim[10].set_color("#049A20")

        for elements in notePad[:11]:
            elements.set_color(WHITE)

        titulo.move_to([0,3,0])
        editors.arrange(direction=RIGHT, buff=0.8)
        
        #Editores aparecem, destaque em vs code
        self.play(Write(titulo), run_time = 1.5)
        self.play(Write(editors), run_time=2)
        self.wait(2)
        
        self.play(editors.animate.shift([0,-0.5,0]))
        caixa1.move_to(editors.get_center())
        self.play(editors.animate.scale(0.8), Create(caixa1))
        
        self.wait(1)
        self.play(Wiggle(vim, run_time=1))
        self.play(Wiggle(sublimeText, run_time=1))
        self.play(Wiggle(notePad, run_time=1))
        self.play(Wiggle(vscode, run_time=1))
        self.wait()
        
        self.play(FadeOut(vim, sublimeText, notePad), run_time=0.6)
        self.play(vscode.animate.move_to([0,-0.5,0]),
                  Transform(caixa1, caixa2.move_to([0,-0.5,0])))
        self.wait()
        
        # tem que ser na caixa1, porque não foi feita uma copia da caixa2 no Transform
        self.play(Uncreate(caixa1), run_time = 0.5)
        self.play(vscode.animate.move_to(ORIGIN))
        self.play(vscode.animate.scale(1.2))

        #Fade em tudo que não saiu
        self.play(*[FadeOut(obj) for obj in self.mobjects])
        self.wait()

    def posInstalacao(self):
        #text = Text("Configurando um ambiente de programação:", font_size = 45)

        text = Text(
            "Configurando um ambiente de programação:",
            t2c={"ambiente": PURPLE},
            font_size = 45
        )

        text2 = Text("- Instalar editor de texto")
        text3 = Text("- Instalar o gcc")
        text4 = Text("- Usar o terminal")

        fullText = VGroup(text, text2, text3, text4).arrange(DOWN, aligned_edge = LEFT, buff = 0.5).scale(0.8)
        risco = Line(text2.get_left(), text2.get_right(), cap_style=CapStyleType.ROUND).set_color(RED)
        risco.set_stroke(RED, 24)
        risco.set_stroke(opacity = 0.7)
        risco.move_to(text2.get_center())

        terminal = ImageMobject("images/terminal.png")
        compilador = ImageMobject("images/compilador.png")
        vscode = ImageMobject("images/vscode.png")

        vscodeGroup = Group(vscode, Text("Editor de texto", font_size = 80).scale(0.3))
        vscodeGroup[1].next_to(vscode, UP, buff = 0.2)
        vscodeGroup[1].align_to(vscode, ORIGIN) # centraliza no meio horizontal

        compiladorGroup = Group(compilador, Text("Compilador", font_size = 80).scale(0.3))
        compiladorGroup[1].next_to(compilador, UP, buff = 0.2)
        compiladorGroup[1].align_to(compilador, ORIGIN) 

        terminalGroup = Group(terminal, Text("Terminal", font_size = 80).scale(0.3))
        terminalGroup[1].next_to(terminal, UP, buff = 0.2)
        terminalGroup[1].align_to(terminal, ORIGIN)

        imsGroup = Group(vscodeGroup, compiladorGroup, terminalGroup)
        imsGroup.arrange(direction=RIGHT, buff=0.8)

        # check (editor de texto já instalado)
        check = VGroup(
            Line([-0.3, -0.3, 0], [0, -0.6, 0]),   # perna curta
            Line([0, -0.6, 0], [0.6, 0, 0])      # perna longa
        ).set_color(GREEN).set_stroke(width=10)

        check.set_cap_style("round")
        check.next_to(vscode, DOWN, buff = 0.3)

        #Riscando
        self.play(Write(text))
        self.play(Write(text2), run_time = 0.7)
        self.play(Write(text3), run_time = 0.7)
        self.play(Write(text4),  run_time = 0.7)
        self.wait()
        self.play(Create(risco))
        self.wait()
        
        #Fade em tudo que não saiu
        self.play(*[FadeOut(obj) for obj in self.mobjects])

        self.play(GrowFromCenter(vscodeGroup[0]),
                GrowFromCenter(compiladorGroup[0]),
                GrowFromCenter(terminalGroup[0])
        )

        self.play(Wiggle(vscodeGroup[0]), run_time = 1)
        self.play(Wiggle(compiladorGroup[0]), run_time = 1)
        self.play(Wiggle(terminalGroup[0]), run_time = 1)

        self.play(
                FadeIn(vscodeGroup[1], shift=UP*0.2),
                FadeIn(compiladorGroup[1], shift=UP*0.2),
                FadeIn(terminalGroup[1], shift=UP*0.2)
        )
        self.wait(0.5)
        self.play(Create(check), run_time = 0.3)
        self.wait(2)
        self.play(Uncreate(check), run_time = 0.3)

        #Fade em tudo que não saiu
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time = 0.5)


    def separacao(self):
        linha1 = Line([-3,2,0], [-3,-2,0],  cap_style = CapStyleType.ROUND).set_stroke("#aa77c7", 20)
        linha2 = Line([3,2,0], [3,-2,0],  cap_style = CapStyleType.ROUND).set_stroke("#aa77c7", 20)

        linux = SVGMobject("svgs\\linux")
        mac = SVGMobject("svgs\\mac")
        windows = SVGMobject("svgs\\windows11")

        fix_cap(linux)
        fix_cap(mac)
        fix_cap(windows)

        winText1 = Text("Windows", font_size = 90).scale(0.5)
        winText2 = Text("Windows 11", font_size = 90).scale(0.5)

        linux[0].set_color("#000000")

        logos = VGroup(linux, windows, mac).arrange(buff=3)

        winText1.move_to(windows.get_center())
        winText2.move_to(windows.get_center())

        winText1.next_to(windows, DOWN, buff = 1)

        winText2.next_to(windows, DOWN, buff = 1)

        self.play(Create(linha1), Create(linha2))
        self.wait(0.5)
        self.play(Write(logos), run_time=1.45)
        self.wait()
        self.play(FadeOut(linha1), FadeOut(linha2), FadeOut(mac), FadeOut(linux))
        self.wait(0.6)
        self.play(windows.animate.scale(1.5))
        self.play(FadeIn(winText1))
        self.play(Transform(winText1, winText2))
        self.play(FadeOut(winText1))
        self.play(ShrinkToCenter(windows), run_time = 0.5)
        self.wait(1)

        #FINAL
        text = T("Para a próxima aula:", font_size = 45)
        text2 = T("Variáveis e os 5 Tipos de Dados", color = PURPLE, font_size=50)
        rawTitle = VGroup(text, text2).arrange(DOWN, aligned_edge = LEFT, buff = 0.2)

        self.play(Write(text), run_time = 1.5)
        self.play(Write(text2), run_time = 1.5)
        self.wait()
        

    def creditos(self):
        #creditos
        logo = ImageMobject("images/icon_c.png").scale(0.2)
        logoOrigin=logo.copy().move_to(UP*8).rotate(PI)
        cursor=ImageMobject("images/cursor.png").move_to(DOWN*6+LEFT*2).scale(0.05)
        titulo=Text("Créditos", font_size=80)
        titulo.color="#AA77C7"

   
        diretor = VGroup(T("Diretor", color = "#AA77C7", font_size=60), T("Rainier R. Waki", font_size=50)).arrange(DOWN, buff=0.3)
        tutor = VGroup(T("Tutor", color = "#AA77C7", font_size=60), T("Alyson V. Isaluski", font_size=50)).arrange(DOWN, buff=0.3)
        animadores = VGroup(
            T("Animadores", color = "#AA77C7", font_size=60),
            VGroup(
                T("Eduarda dos R. Mendes", font_size=50),
                T("Leandro M. M. Hyeda", font_size=50)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        editora = VGroup(T("Editora", color = "#AA77C7", font_size=60), T("Sophia B. Peraza", font_size=50)).arrange(DOWN, buff=0.3)
        roteirista = VGroup(
            T("Roteiristas", color = "#AA77C7", font_size=60),
            VGroup(
                T("Alyson V. Isaluski", font_size=50),
                T("Kia de P. Marins", font_size=50)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        utfpr = ImageMobject("images/utfpr.png").scale(0.7)
        
        creditos = VGroup(diretor, tutor, animadores, editora, roteirista).scale(0.4)

        for bloco in creditos:
            if isinstance(bloco, VGroup):
                bloco.arrange(DOWN, aligned_edge=LEFT)

        creditos.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        creditos.to_edge(LEFT, buff=0.5)

        utfpr.scale(0.4)
        utfpr.next_to(creditos, DOWN, buff = 0.3)
        utfpr.to_edge(LEFT, buff=0.5)

        self.play(
            logoOrigin.animate.become(logo),
            run_time=2
        )

        # Cursor aparece e se move
        self.play(cursor.animate.move_to(ORIGIN+RIGHT*0.25+DOWN*0.45))
        self.play(cursor.animate.scale(0.8), run_time=0.1, rate_func=linear)  # Clica
        self.play(cursor.animate.scale(1.2), run_time=0.1, rate_func=linear)  #

        # Vinheta Puxada
        self.play(
            GrowFromCenter(Rectangle(color="#0A0A0A", fill_opacity=1, width=20, height=10), run_time=0.5)
        )

        # Nomes e Cargos
        self.play(Write(creditos), FadeIn(utfpr))
        self.wait()
        self.play(FadeOut(utfpr), Unwrite(creditos))
        self.wait()

    def construct(self):
        self.configurandoAmbiente()
        self.editoresTexto()
        self.posInstalacao()
        self.separacao()
        self.creditos()
