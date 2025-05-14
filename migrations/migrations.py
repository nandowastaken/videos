from manim import *

class Introduction(Scene):
    def construct(self):
        title = Text("Migrations").scale(0.6)
        self.play(Write(title))
        self.play(FadeOut(title))

class Table(Scene):
    def construct(self):
       userTable = Rectangle(color=BLUE, fill_opacity=0)
       
       userTableLabel = Text("Usuário").scale(0.4)
       userTableLabel.next_to(userTable.get_corner(UL), DOWN + RIGHT, buff=0.1)
       
       fields = ["- id", "- nome", "- senha"]
       field_texts = VGroup(*[Text(f).scale(0.35) for f in fields])
       field_texts.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
       field_texts.next_to(userTableLabel, DOWN, aligned_edge=LEFT)
       
       aniversario_text = Text("- aniversario", color=YELLOW).scale(0.35)
       aniversario_text.next_to(field_texts, DOWN, aligned_edge=LEFT, buff=0.3)
       
       self.play(DrawBorderThenFill(userTable))
       self.play(Write(userTableLabel))
       self.play(LaggedStartMap(Write, field_texts, lag_ratio=0.2))
       
       self.wait(2)
       self.play(Write(aniversario_text))
       self.wait(3)
       self.play(FadeOut(userTable), FadeOut(userTableLabel), FadeOut(field_texts), FadeOut(aniversario_text))

class AlterTable(Scene):
    def construct(self):
       code = Text("ALTER TABLE USUARIO ADD COLUMN 'aniversarion' STRING;", t2c={"USUARIO": YELLOW, "'aniversario'": YELLOW}).scale(0.2)
       self.play(Write(code))
       self.wait(2)
       
       self.play(FadeOut(code))
       explanation = Text("Migration é um conjunto de mudanças aplicadas a uma base de dados").scale(0.2)
       self.play(Write(explanation))
       self.wait(2)
       
       self.play(FadeOut(explanation))
       
class UpDownMigration(Scene):
    def construct(self):
        upMigrationCode = Text(
            "ALTER TABLE USUARIO ADD COLUMN aniversario STRING;", 
            t2c={"USUARIO": YELLOW, "'aniversario'": YELLOW}
        ).scale(0.2)

        upMigration = Text("Up Migration", color=GREEN).scale(0.5)
        x = Text("x").scale(0.5)
        down = Text("Down Migration", color=RED).scale(0.5)

        texts = VGroup(upMigration, x, down).arrange(DOWN, buff=0.4).scale(1)
        texts.move_to(ORIGIN)
        self.play(Write(texts))
        self.wait(5)
        self.play(FadeOut(texts))
        texts.scale(0.5)
        
        upMigration.align_to(upMigrationCode, LEFT)       
        self.play(Write(upMigrationCode))
        self.play(Write(upMigration))
        self.wait(1)
        
        self.play(
            upMigration.animate.shift(UP * 0.5),
            upMigrationCode.animate.shift(UP * 0.5)
        )

        downMigrationCode = Text(
            "ALTER TABLE USUARIO DROP COLUMN aniversario;", 
            t2c={"USUARIO": YELLOW, "aniversario;": YELLOW}
        ).scale(0.2)

        downMigrationCode.align_to(upMigrationCode, LEFT)
        downMigrationCode.shift(DOWN * .3)
        down.align_to(downMigrationCode, LEFT)
        down.shift(UP * .25)
        

        self.play(Write(down))
        self.play(Write(downMigrationCode))
        
        self.wait(5.5)
        self.play(FadeOut(down), FadeOut(downMigrationCode), FadeOut(upMigration), FadeOut(upMigrationCode))