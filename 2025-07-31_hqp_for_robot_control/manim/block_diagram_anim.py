# manim manim/block_diagram.py BlockDiagramAnim

from manim import *

class BlockDiagramAnim(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        color = "#0f4a7c"

        # Blocks
        mpc_block = RoundedRectangle(corner_radius=0.2, height=1, width=2.5, color=color).move_to(UP * 2)
        mpc_text = Text("MPC", font_size=36, color=color).move_to(mpc_block.get_center())
        mpc_group = VGroup(mpc_block, mpc_text)

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
        self.wait(1)
        
        # Rename MPC → Planner
        planner_text = Text("Planner", font_size=36, color=color).move_to(mpc_text.get_center())
        self.play(Transform(mpc_text, planner_text))

        # Shift Planner left, and arrows accordingly
        shift_left = LEFT * 2
        shift_right = RIGHT * 2

        # Update q1, q2, and q4 after mpc_group shifts
        new_q2 = q2 + shift_left
        new_q3 = q3 + shift_left
        new_q4 = q4 + shift_left
        
        new_p1 = p1 + shift_right
        new_p2 = p2 + shift_right
        new_p3 = p3 + shift_right
        
        tracker_block = RoundedRectangle(corner_radius=0.2, height=1, width=2.5, color=color).move_to(new_p1 + LEFT * 1.25)
        tracker_text = Text("Tracker", font_size=36, color=color).move_to(tracker_block.get_center())
        
        q5 = mpc_block.get_right() + shift_left
        q6 = tracker_block.get_left()
        arrow3 = Line(q5, q6, color=color).add_tip(tip_length=0.2)

        # Animate arrow path and tip to follow the moved block
        self.play(
            mpc_group.animate.shift(shift_left),
            Create(tracker_block), Write(tracker_text),
            path1.animate.become(VMobject(color=color).set_points_as_corners([new_p1, new_p2, new_p3])),
            arrow1.animate.become(Line(new_p3, p4, color=color).add_tip(tip_length=0.2)),
            path2.animate.become(VMobject(color=color).set_points_as_corners([q1, new_q2, new_q3])),
            arrow2.animate.become(Line(new_q3, new_q4, color=color).add_tip(tip_length=0.2)),
            Create(arrow3),
        )
