from manim import *

class Thumbnail(Scene):
    def construct(self):
       title = Text("SQL JOINS").scale(0.6)
       title.move_to([0, .85, 0])
        
       tableA = Circle(radius=1.0, color=WHITE, fill_opacity=0)
       tableA.move_to([0.5, -.25, 0])
       
       tableB = Circle(radius=1.0, color=WHITE, fill_opacity=0)
       tableB.move_to([-0.5, -.25, 0])
       
       un = Intersection(tableA, tableB, color=BLUE, fill_opacity=1)
       
       
       
       labelA = Text("A", color=WHITE).scale(0.5).next_to(tableA, LEFT)
       labelB = Text("B", color=WHITE).scale(0.5).next_to(tableB, RIGHT)
       labelAB = Text("A ∩ B", color=WHITE).scale(0.4).move_to(un)
       
       venn_group = VGroup(tableA, tableB, un, labelA, labelB, labelAB).scale(0.8)
       
       self.add(title, venn_group)

