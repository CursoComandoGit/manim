from manim import *
from customTerminal import CustomTerminal

class Part1(Scene): #Essa aula é o último teste com updaters para uma cena só. Na próxima separarei em diferentes classes
    config.background_color = "#1E1E1E"
    Text.set_default(font = "Manrope")
    #Updater para scale
    #com interpolação
    def modifyTerminal(self, mob , alpha):
        target_width = interpolate(mob.sizeX, mob.newWidth, alpha)
        target_height = interpolate(mob.sizeY, mob.newHeight, alpha)
        mob.resize_terminal(new_width = target_width, new_height = target_height)

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

    def configurandoAmbiente(self):
        text = Text("Configurando seu", font_size = 45)
        text2 = Text("ambiente de programação", color = PURPLE, font_size=50)
        acronym = Tex("{{I}}{{D}}{{E}}")
        acronym.font_size = 128
        fullText = Tex("{{I}}ntegrated {{D}}evelopment {{E}}nviroment")
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
        iaText.velocity = np.array([2.0, -4.0, 0]) #velocidade inicial
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
        features = VGroup(iaText, net, dataBase, compilacao, debugger)
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
        crossGroup = VGroup(*[Cross(feature, color=RED, stroke_width=4) for feature in features])
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
        cLanguage = SVGMobject("svgs\\C").shift([0,0.2,0])
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
        #Editores aparecem, linguagem C e destaque em vs code
        self.play(Write(titulo), Write(editors), run_time=2)
        self.wait(2)
        
        self.play(editors.animate.shift([0,-2.5,0]))
        caixa1.move_to(editors.get_center())
        self.play(editors.animate.scale(0.8), Create(caixa1))
        self.play(GrowFromCenter(cLanguage))
        self.wait(2)
        self.play(Wiggle(vim, run_time=1))
        self.play(Wiggle(sublimeText, run_time=1))
        self.play(Wiggle(notePad, run_time=1))
        self.play(Wiggle(vscode, run_time=1))
        self.wait()
        
        self.play(FadeOut(vim, sublimeText, notePad), run_time=0.6)
        self.play(vscode.animate.move_to([0,-2.5,0]),
                  Transform(caixa1, caixa2.move_to([0,-2.5,0])))
        self.wait(2)
        #Fade em tudo que não saiu
        self.play(*[FadeOut(obj) for obj in self.mobjects])

    #trocar pelo da Eduarda
    def posInstalacao(self):
        text = Text("Configurando um ambiente de programação:", font_size = 45)
        text2 = Text("-Instalar editor de texto")
        text3 = Text("-Instalar o gcc")
        text4 = Text("-Usar o terminal")
        fullText = VGroup(text, text2, text3, text4).arrange(DOWN, aligned_edge = LEFT, buff = 0.5).scale(0.8)
        risco = Line(text2.get_left(), text2.get_right()).set_color(RED)
        risco.set_stroke(RED, 10)
        #Riscando
        self.play(Write(fullText))
        self.wait()
        self.play(Create(risco))
        self.wait()
        
        #Fade em tudo que não saiu
        self.play(*[FadeOut(obj) for obj in self.mobjects])

    def linuxEWindows(self):
        sample = "1. Estabilidade; 2. Confiabilidade; 3. Flexibilidade; 4. Servidores rodam linux; 5. Customização; 6. Segurança; 7. Privacidade; 8. Open Source; 9. Compatibilidade; 10. Portabilidade; 11. Performance; 12. Escalabilidade; 13. Ambiente de Desenvolvimento Nativo; 14. “Scriptable”; 15. Gerenciador de Pacotes"
        sample = sample.split(';')
        linux = SVGMobject("svgs\\linux").move_to([-1,0,0]).scale(1.2)
        windows = SVGMobject("svgs\\windows").scale(0.8).shift([9.8,0,0])
        linuxBeneficios = VGroup(*[Text(texto, fill_opacity=0, font_size=75).scale(1/3) for texto in sample])
        linuxBeneficiosVisivel = VGroup(*[Text(texto, font_size=75).scale(1/3) for texto in sample])
        linuxBeneficios.arrange(DOWN, buff=0.2, aligned_edge = LEFT, center = False).move_to([-2.5,0,0])
        linuxBeneficiosVisivel.arrange(ORIGIN, buff=0.2, aligned_edge = LEFT, center=False).move_to([-12,0,0])
        #arrumando logo
        linux[0].set_color("#000000")
        #Cada elemento aparece individualmente
        self.add(linuxBeneficiosVisivel)
        i = 0
        while i < len(linuxBeneficios):
            self.play(linuxBeneficiosVisivel[i].animate.move_to(linuxBeneficios[i].get_center()), run_time=0.1)
            i+=1
        #Comparação
        self.play(GrowFromCenter(linux),
                  run_time = 0.65)
        self.wait(0.8)
        #Fade em tudo que não saiu
        self.play(*[FadeOut(obj) for obj in self.mobjects])

    #----SUJEITO A SER DESCARTADO----#
    def explicandoLinux(self):
        usuario = SVGMobject("svgs\\person").move_to([0,2.8,0]).scale(0.9)
        cLanguage = SVGMobject("svgs\\C").move_to([-5,-2.5,0]).scale(0.9)
        linux = SVGMobject("svgs\\linux").move_to([5,-2.5,0]).scale(0.9)
        wsl = SVGMobject("svgs\\wsl").scale(0.9)
        linux2 = SVGMobject("svgs\\linux")
        loveTriangle = VGroup(usuario, cLanguage, linux).set_z_index(1)

        linux[0].set_color("#000000")
        linux2[0].set_color("#000000")
        wsl[0].set_color(DARK_BLUE)
        wsl[8].set_color(ORANGE)
        wsl[9].set_color(ORANGE)
        wsl[10].set_color(YELLOW)
        #---conectar componentes---
        self.play(FadeIn(loveTriangle))
        self.wait()
        self.play(usuario.animate.move_to([0,1.8,0]),
                  cLanguage.animate.move_to([-2.6,-1.4,0]),
                  linux.animate.move_to([2.6,-1.4,0]))
        self.play(Create(Line(cLanguage.get_center(), usuario.get_center(), stroke_width = 3)),
                  Create(Line(usuario.get_center(), linux.get_center(), stroke_width = 3)),
                  Create(Line(linux.get_center(), cLanguage.get_center(), stroke_width = 3)))
        self.wait(2)
        
        #Transform no wsl
        wsl.move_to(linux.get_center())
        self.play(ClockwiseTransform(linux, wsl))
        self.wait(1.6)
        #Transform no linux novamente
        linux2.move_to(linux.get_center())
        self.play(CounterclockwiseTransform(linux, linux2))
        self.wait()
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.5)
        self.clear()

    #Trocar pela da eduarda
    def separacao(self):
        linha1 = Line([-3,2,0], [-3,-2,0]).set_stroke("#aa77c7", 20).set_cap_style(CapStyleType.ROUND)
        linha2 = Line([3,2,0], [3,-2,0]).set_stroke("#aa77c7", 20).set_cap_style(CapStyleType.ROUND)
        linux = SVGMobject("svgs\\linux").set_cap_style(CapStyleType.AUTO)
        mac = SVGMobject("svgs\\iconMacOS").set_cap_style(CapStyleType.AUTO)
        windows = SVGMobject("svgs\\windows").set_cap_style(CapStyleType.AUTO)
        initialLetters = VGroup(*[Text(l, color=PURPLE, font_size=50) for l in ["W","S","L"]])
        fullWords = VGroup(*[Text(w, font_size=45) for w in ["indows","ubsystem","inux"]])
        initialLetters.arrange(direction=DOWN, buff=1)
        for w in range(3):
            fullWords[w].move_to(initialLetters[w].get_corner([1,-1,0]), aligned_edge=[-1,-1,0])

        linux[0].set_color("#000000")
        logos = VGroup(linux, windows, mac).arrange(buff=3)

        self.play(Create(linha1), Create(linha2))
        self.wait(0.5)
        self.play(Write(logos), run_time=1.45)
        self.wait()
        self.play(FadeOut(linha1), FadeOut(linha2), FadeOut(mac), FadeOut(linux))
        self.wait(0.6)
        self.play(windows.animate.scale(1.5))
        self.wait(1.5)
        self.play(Transform(windows, initialLetters))
        self.wait(0.5)
        fullWords.shift([-0.8,0,0])
        fullWords[1].shift([0,-0.15,0])
        self.play(windows.animate.shift(LEFT), run_time=0.65)
        linhaReset = Line([-10,2,0], [-10,-2,0]).set_stroke("#aa77c7", 20).set_cap_style(CapStyleType.AUTO)
        self.play(Succession(*[AddTextLetterByLetter(word) for word in fullWords]), Create(linhaReset),run_time=1.25)
        self.play(FadeOut(*self.mobjects))
        self.clear()

class Main(Scene):
    #---Trocada por edição. Apenas uma parte utilizada---
    def porqueUsasWindows(self):
        throne = SVGMobject("svgs\\throne").scale(1.1)
        linux = SVGMobject("svgs\\linux").set_z_index(2)
        crown = SVGMobject("svgs\\crown").set_z_index(3).scale(0.25).move_to(linux.get_top(), aligned_edge=DOWN)
        machine = SVGMobject("svgs\\maquina").scale(0.8)
        money = SVGMobject("svgs\\money").scale(0.8).move_to([5,-6,0])
        openLock = SVGMobject("svgs\\openLock").scale(0.8).move_to([5,6,0]).set_color(WHITE)
        closedLock = SVGMobject("svgs\\closedLock.svg").scale(0.8).set_color(WHITE)

        tcompilador = Text("Compilador", font_size=45).move_to(machine.get_bottom(), aligned_edge=UP).shift([0,-0.25,0])
        compilador = VGroup(machine, tcompilador).move_to([-5,6,0])
        msgErro = Text("Undeclared identifier 'varivel'", font_size=30,color=RED)
        sugestao = Text("Did you mean 'variavel'?", font_size=30,color=RED)

        linux[0].set_color("#000000")

        self.add(money)
        self.add(compilador)
        self.play(FadeIn(linux))
        self.wait()
        self.play(compilador.animate.move_to([-5,2.25,0]))
        msgErro.move_to(machine.get_right(), aligned_edge=LEFT).shift([0.25,0,0])
        sugestao.move_to(msgErro.get_center())

        self.play(Wiggle(machine, run_time=1), GrowFromPoint(msgErro, machine.get_center()))
        self.wait()
        self.play(Transform(msgErro, sugestao))
        self.wait()

        self.play(money.animate.move_to([5,-2.25,0]))
        cross = Cross(money, color=RED)
        self.play(Create(cross), FadeOut(msgErro))
        self.wait()

        stringKernel = ''' static int get_random_numbers(u8 *buf, unsigned int len)
{
    struct crypto_rngrng = NULL;
    chardrbg = "drbg_nopr_sha256"; /* Hash DRBG with SHA-256, no PR */
    int ret;
    if (!buf || !len) {
        pr_debug("No output buffer provided\n");
        return -EINVAL;
    }
    rng = crypto_alloc_rng(drbg, 0, 0);
    if (IS_ERR(rng)) {
        pr_debug("could not allocate RNG handle for %s\n", drbg);
        return -PTR_ERR(rng);
    }
    ret = crypto_rng_get_bytes(rng, buf, len);
    if (ret < 0)
        pr_debug("generation of random numbers failed\n");
    else if (ret == 0)
        pr_debug("RNG returned no data");
    else
        pr_debug("RNG returned %d bytes of data\n", ret);
out:
    crypto_free_rng(rng);
    return ret;
} '''
        kernelCode = Code(code_string=stringKernel, language="c", formatter_style="monokai", background="rectangle", background_config={"fill_color": "#4400FFFF", "stroke_color": "WHITE", "fill_opacity":0.1}).scale(0.25)
        kernelCode.move_to([-5,-2.25,0]).set_cap_style(CapStyleType.AUTO)
        self.play(Write(kernelCode))
        self.wait()

        self.play(openLock.animate.move_to([5,2.25,0]))
        closedLock.move_to(openLock.get_center())
        self.wait(0.6)
        self.play(openLock.animate.remove(), closedLock.animate.add(), Flash(closedLock, flash_radius=0.8))
        self.wait(2)
        self.play(FadeIn(throne, crown))
        self.wait(2)
        self.play(FadeOut(*self.mobjects))

    def trocarDeOS(self):
        linux = SVGMobject("svgs\\linux").set_z_index(2).move_to([-8,0,0])
        windows = SVGMobject("svgs\\windows").set_z_index(2).scale(0.8)
        laptop = SVGMobject("svgs\\laptop").scale(1.5)

        acronym = Tex("{{W}}{{S}}{{L}}").move_to([0,-2,0]).set_color(PURPLE)
        fullText = Tex("{{W}}indows {{S}}ubsystem {{L}}inux").move_to([0,-2,0])

        rectangle = Rectangle(color=RED_E, height=3).set_fill(RED, opacity=1)
        rectangle2 = Rectangle(color=WHITE, height=1.5,width=4).set_fill(WHITE, opacity=1).move_to(rectangle.get_bottom(), aligned_edge=DOWN).shift([0,0.5,0])
        texto = Text("Hello!\nMy name is", font_size=35, weight=BOLD).move_to(rectangle.get_top(), aligned_edge=UP)
        name = Text("Linux", font_size=45,font="Segoe Script", color=BLACK).move_to(rectangle2.get_center())
        hello = VGroup(rectangle, rectangle2, texto, name).set_z_index(5)
        linux[0].set_color("#000000")

        self.add(linux)
        self.play(Write(windows), Write(laptop))
        self.play(linux.animate.move_to(laptop.get_left(), aligned_edge=RIGHT))
        self.play(linux.animate.shift([1.5,0,0]), windows.animate.shift([0.5,0,0]), rate_func=rate_functions.ease_in_circ, run_time=1.5)
        self.play(linux.animate.move_to([-9,0,0]).rotate(-90), windows.animate.shift([-1,0,0]), rate_func=rate_functions.ease_out_back,  run_time=0.8)
        self.play(windows.animate.center(), run_time=0.6)
        self.wait(0.5)
        self.play(Write(acronym))
        self.wait(0.5)
        self.play(TransformMatchingTex(acronym, fullText))
        self.wait()

        hello.move_to(windows.get_corner([1,-1,0])).scale(0.35)
        self.play(FadeIn(hello))

        self.wait(2)
        self.play(FadeOut(*self.mobjects))
    
    def interfaceTerminal(self):
        download = SVGMobject("svgs\\download").set_color(WHITE).set_stroke(WHITE, 5)
        terminal = CustomTerminal()
        cursor=ImageMobject("images/cursor.png").move_to(DOWN*6+LEFT*2).scale(0.05)

        self.play(Write(download))
        self.wait()
        # Cursor aparece e se move
        self.play(cursor.animate.move_to(ORIGIN+RIGHT*0.25+DOWN*0.45))
        self.play(cursor.animate.scale(0.8),run_time=0.1,rate_func=linear)  # Clica
        self.play(cursor.animate.scale(1.2),run_time=0.1,rate_func=linear)  #
        
        self.play(FadeOut(cursor), ShrinkToCenter(download))
        self.play(GrowFromCenter(terminal))
        terminal.initialize_line(self, "find . -name \"*.txt\"")
        terminal.cursorNewLine()
        terminal.initializeMultiLineString(self, 0.1, r'''./notes.txt
./todo_list.txt
./project_ideas.txt
./comando/aula2/roteiro.txt
./teste.txt
./testDates.txt
./ssssspi.txt
./comando/aula1/roteiro.txt
./prova.txt
./ed.txt''')
        terminal.initialize_path("manim@manim:~$")

        self.wait(2)
        self.play(FadeOut(*self.mobjects))

    def proximaAula(self):
        #FINAL
        text = Text("Para a próxima aula:", font_size = 45)
        text2 = Text("Variáveis e os 5 Tipos de Dados", color = PURPLE, font_size=50)
        rawTitle = VGroup(text, text2).arrange(DOWN, aligned_edge = LEFT, buff = 0.2)

        self.play(Write(rawTitle))
        self.wait()
        self.play(*[FadeOut(obj) for obj in self.mobjects], run_time=0.5)
        
    #Trocar pela atual
    def creditos(self):
        #creditos
        logo = ImageMobject("images/icon_c.png").scale(0.2)
        logoOrigin=logo.copy().move_to(UP*8).rotate(PI)
        cursor=ImageMobject("images/cursor.png").move_to(DOWN*6+LEFT*2).scale(0.05)
        titulo=Text("Créditos", font_size=80)
        titulo.color="#AA77C7"

        diretor = Group(Text("Diretor", font_size=60), Text("Rainier R. Waki", font_size=45)).arrange(DOWN, buff=0.3)
        tutor = Group(Text("Tutor (voz)", font_size=60), Text("Alyson V. Isaluski", font_size=45)).arrange(DOWN, buff=0.3)
        redator = Group(Text("Redator", font_size=60),Text("Wallace P. F. Junior", font_size=45)).arrange(DOWN, buff=0.3)
        manimator = Group(Text("Manimators", font_size=60),Text("Leandro M. M. Hyeda", font_size=45)).arrange(DOWN, buff=0.3)

        utfpr= ImageMobject("images/utfpr.png").scale(0.7)
        creditos = Group(titulo, diretor, tutor, redator, manimator,utfpr).arrange(DOWN, buff=1).scale(0.5)

        self.play(
            logoOrigin.animate.become(logo),
            run_time=2
        )

        # Cursor aparece e se move
        self.play(cursor.animate.move_to(ORIGIN+RIGHT*0.25+DOWN*0.45))
        self.play(cursor.animate.scale(0.8),run_time=0.1,rate_func=linear)  # Clica
        self.play(cursor.animate.scale(1.2),run_time=0.1,rate_func=linear)  #

        # Vinheta Puxada
        self.play(
            GrowFromCenter(Rectangle(color="#0A0A0A",fill_opacity=1,width=20, height=10),run_time=0.5)
        )

        # Nomes e Cargos
        self.play(AnimationGroup(FadeIn(creditos.move_to(ORIGIN))))
        self.wait()

    def construct(self):
        Part1.linuxEWindows(self)
        self.porqueUsasWindows()
        self.trocarDeOS()
        self.interfaceTerminal()
        self.proximaAula()
