from manim import *

def createTable(tableName, tableColor, columns):
    table = Rectangle(color=tableColor, fill_opacity=0)
    label = Text(tableName).scale(0.5).next_to(table.get_corner(UL), direction=DOWN + RIGHT, buff=0.15)
    
    column_labels = VGroup()
    for i, col in enumerate(columns):
        col_text = Text(col).scale(0.4)
        col_text.move_to(DOWN * i * .25)
        col_text.align_to(label, LEFT)
        column_labels.add(col_text)
    
    column_labels.move_to(UP * .1)
    column_labels.align_to(label, LEFT)
    return VGroup(table, label, column_labels)

def createSet(setName, setRadius, setColor): 
    set = Circle(radius=setRadius, color=setColor, fill_opacity=0)
    setName = Text(setName).move_to(set)
    return VGroup(set, setName), set