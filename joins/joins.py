from manim import *
from components import *

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
        userTable = createTable("Usuário", BLUE, ["- id", "- nome", "- código_país (FK)"])
        self.play(DrawBorderThenFill(userTable))
        
        self.play(userTable.animate.shift(LEFT * 3))
        
        countryTable = createTable("País", RED, ["- código", "- nome"]).move_to(RIGHT * 3)
        self.play(DrawBorderThenFill(countryTable))
        
        self.wait(3)
        
        # Demonstra relacionamento entre as tabelas
        
        
        # Transforma as tabelas em sets
        userSet = createSet("Usuário", 2, BLUE).move_to(userTable)
        countrySet = createSet("País", 2, RED).move_to(countryTable)
        
        self.play(
            Transform(userTable, userSet),
            Transform(countryTable, countrySet),
        )
        
        
        # user = Rectangle(color=BLUE, fill_opacity=0)
        # userLabel = Text("Usuário").scale(0.5).move_to(user.get_corner(UL) + RIGHT * .7 + DOWN * .3)
        
        # country = Rectangle(color=RED, fill_opacity=0)
        # countryLabel = Text("País").move_to(country)
        
        # country.move_to(RIGHT * 2.5)
        # countryLabel.move_to(RIGHT * 2.5)
        
        # self.play(DrawBorderThenFill(user))
        # self.play(Write(userLabel))
        # self.play(user.animate.shift(LEFT * 2.5), userLabel.animate.shift(LEFT * 2.5))
        
        # self.play(DrawBorderThenFill(country))
        # self.play(Write(countryLabel))
        # self.wait(2)
        
        # Desenha as tabelas se transformando em conjuntos
        # self.play(
        #     Transform(user, Circle(radius=2, color=BLUE, fill_opacity=0).move_to(user)),
        #     Transform(country, Circle(radius=2, color=RED, fill_opacity=0).move_to(country))
        # )
        # self.play(
        #     user.animate.shift(RIGHT * .8), 
        #     userLabel.animate.shift(RIGHT * 1),
        #     country.animate.shift(LEFT * .8),
        #     countryLabel.animate.shift(LEFT * 1),
        # )
        
        # intersection = Intersection(user, country, color=PURPLE, fill_opacity=0.5)
        # self.play(FadeIn(intersection))
        
        # self.wait(3) 