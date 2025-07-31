# manim -p -s -qk manim/block_diagram.py BlockDiagram

from manim import *

class BlockDiagram(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        color = "#0f4a7c"

        # Blocks
        mpc_block = RoundedRectangle(corner_radius=0.2, height=1, width=2.5, color=color).move_to(UP * 2)
        mpc_text = Text("MPC", font_size=36, color=color).move_to(mpc_block.get_center())

        model_block = RoundedRectangle(corner_radius=0.2, height=1, width=2.5, color=color).move_to(DOWN * 2)
        model_text = Text("Model", font_size=36, color=color).move_to(model_block.get_center())

        # Coordinates
        p1 = mpc_block.get_right()
        p2 = p1 + RIGHT * 1.5
        p3 = model_block.get_right() + RIGHT * 1.5
        p4 = model_block.get_right()

        q1 = model_block.get_left()
        q2 = q1 + LEFT * 1.5
        q3 = mpc_block.get_left() + LEFT * 1.5
        q4 = mpc_block.get_left()

        # Arrow from MPC → Model (right side, down, in)
        path1 = VMobject(color=color)
        path1.set_points_as_corners([p1, p2, p3])
        arrow1 = Line(p3, p4, color=color).add_tip(tip_length=0.2)

        # Arrow from Model → MPC (left side, up, in)
        path2 = VMobject(color=color)
        path2.set_points_as_corners([q1, q2, q3])
        arrow2 = Line(q3, q4, color=color).add_tip(tip_length=0.2)

        # Animate
        self.add(mpc_block, mpc_text)
        self.add(model_block, model_text)
        self.add(path1, arrow1)
        self.add(path2, arrow2)
        self.wait(0.1)
