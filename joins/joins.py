from manim import *

class Thumbnail(Scene):
    def construct(self):
       title = Text("SQL JOINS").scale(2.5)
       title.move_to([0, 2.5, 0])
        
       tableA = Circle(radius=3, color=WHITE, fill_opacity=0)
       tableA.move_to([2, -1, 0])
       
       tableB = Circle(radius=3, color=WHITE, fill_opacity=0)
       tableB.move_to([-2, -1, 0])
       
       un = Intersection(tableA, tableB, color=BLUE, fill_opacity=1)
       
       labelA = Text("A", color=WHITE).scale(1.5).move_to(tableA)
       labelB = Text("B", color=WHITE).scale(1.5).move_to(tableB)
       labelAB = Text("A ∩ B", color=WHITE).scale(1).move_to(un)
       
       venn_group = VGroup(tableA, tableB, un, labelA, labelB, labelAB).scale(0.8)
       
       self.add(title, venn_group)

class Introduction(Scene):
    def construct(self):
        text = Text("O que seria um JOIN em SQL?")
        self.play(Write(text))
        self.play(text.animate.shift(UP*3))
        
        # Desenha as tabelas User e Country
        user = Rectangle(color=BLUE, fill_opacity=0)
        userLabel = Text("Usuário").move_to(user)
        
        country = Rectangle(color=RED, fill_opacity=0)
        countryLabel = Text("País").move_to(country)
        
        country.move_to(RIGHT * 2.5)
        countryLabel.move_to(RIGHT * 2.5)
        
        self.play(DrawBorderThenFill(user))
        self.play(Write(userLabel))
        self.play(user.animate.shift(LEFT * 2.5), userLabel.animate.shift(LEFT * 2.5))
        
        self.play(DrawBorderThenFill(country))
        self.play(Write(countryLabel))
        self.wait(2)
        
        # Desenha as tabelas se transformando em conjuntos
        self.play(
            Transform(user, Circle(radius=2, color=BLUE, fill_opacity=0).move_to(user)),
            Transform(country, Circle(radius=2, color=RED, fill_opacity=0).move_to(country))
        )
        self.play(
            user.animate.shift(RIGHT * .8), 
            userLabel.animate.shift(RIGHT * 1),
            country.animate.shift(LEFT * .8),
            countryLabel.animate.shift(LEFT * 1),
        )
        
        intersection = Intersection(user, country, color=PURPLE, fill_opacity=0.5)
        self.play(FadeIn(intersection))
        
        self.wait(3) 