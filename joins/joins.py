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
        user_field = userTable[0][0]  
        country_field = countryTable[0][0]
        line = Line(
            start=user_field.get_right(),
            end=country_field.get_left(),
            color=YELLOW,
            stroke_width=3
        )
        n_text = Text("N").scale(0.5).next_to(line.get_start(), UP + RIGHT, buff=0.15)
        one_text = Text("1").scale(0.5).next_to(line.get_end(), UP + LEFT, buff=0.15)

        self.play(Create(line))
        self.play(FadeIn(n_text), FadeIn(one_text))
        
        self.wait(5)
        
        # Mostra como selecionar todos os usuários
        select_user = Text("SELECT * FROM Usuario;").scale(.8)
        select_user.move_to(ORIGIN)
        select_user.move_to(DOWN * 2.25)
        
        self.play(Write(select_user))
        self.wait(3)
        
        doubt = Text("???").scale(.8)
        doubt.move_to(ORIGIN)
        doubt.move_to(DOWN * 2.5)
        
        self.play(Transform(select_user, doubt))
        self.wait(2)
        
        join = Text(
            "SELECT * FROM Usuario INNER JOIN Pais ON Usuario.codigo_pais = Pais.codigo;",
            t2c={"INNER": YELLOW, "JOIN": YELLOW, "ON": YELLOW}
        ).scale(0.5)
        join.move_to(ORIGIN)
        join.move_to(DOWN * 2.5)
        
        self.play(Transform(select_user, join))
        self.wait(5)
        
        # Transforma as tabelas em sets
        self.play(FadeOut(n_text), FadeOut(one_text), FadeOut(line))
        
        userSet, userCircle = createSet("Usuário", 2, BLUE)
        userSet.move_to(userTable)
        
        countrySet, countryCircle = createSet("País", 2, RED)
        countrySet.move_to(countryTable)
        
        self.play(
            Transform(userTable, userSet),
            Transform(countryTable, countrySet),
        )
        
        self.wait(5)
        
        self.play(
            userTable.animate.shift(RIGHT * 1.25),
            countryTable.animate.shift(LEFT * 1.25),
            userSet.animate.shift(RIGHT * 1.25),
            countrySet.animate.shift(LEFT * 1.25)
        )
        
        intersection = Intersection(userCircle, countryCircle, color=PURPLE, fill_opacity=.5)
        self.play(FadeIn(intersection))
        
        self.wait(5)
        
        left_join = Text("SELECT * FROM Usuario LEFT JOIN Pais ON Usuario.codigo_pais = Pais.codigo;",
                         t2c={"LEFT": YELLOW, "JOIN": YELLOW, "ON": YELLOW}).scale(.5)
        left_join.move_to(ORIGIN)
        left_join.move_to(DOWN * 2.5)
        
        self.remove(intersection)
        self.play(Transform(select_user, left_join), 
                  userCircle.animate.set_fill(color=PURPLE, opacity=.5)
                  )
        self.wait(3)
        
        right_join = Text("SELECT * FROM Usuario RIGHT JOIN Pais On Usuario.codigo_pais = Pais.codigo;",
                          t2c={"RIGHT": YELLOW, "JOIN": YELLOW, "ON": YELLOW}).scale(.5)
        right_join.move_to(ORIGIN)
        right_join.move_to(DOWN * 2.5)
        
        self.play(Transform(select_user, right_join),
                  userCircle.animate.set_fill(opacity=0),
                  countryCircle.animate.set_fill(color=PURPLE, opacity=.5)
                  )
        self.wait(3)
        
        full_outer_join = Text("SELECT * FROM USUARIO FULL OUTER JOIN Pais On Usuario.codigo_pais = Pais.codigo;",
                               t2c={"FULL": YELLOW, "OUTER": YELLOW, "JOIN": YELLOW, "ON": YELLOW}).scale(.5)
        full_outer_join.move_to(ORIGIN)
        full_outer_join.move_to(DOWN * 2.5)
        
        self.play(Transform(select_user, full_outer_join),
                  userCircle.animate.set_fill(opacity=.5)
                  )
        self.wait(5)