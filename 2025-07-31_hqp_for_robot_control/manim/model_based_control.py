from copy import deepcopy

from manim import *


class ModelBasedControl(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        color = "#0f4a7c"
        
        eom = MathTex(
            r"\begin{gathered} \text{Model:}\\ M (q) \ddot{q} + h(q, \dot{q}) = \tau + J^T(q) f \end{gathered}",
            font_size=96,
            color=color,
        )
        eom_small = deepcopy(eom)
        eom_small.font_size = 18
        eom_small.to_corner(UL)
        
        self.add(eom)
        
        self.wait(1)
        
        state_input = MathTex(
            r"\begin{aligned} " +
            r"& \text{State:} \; && s = \begin{bmatrix} q^T, \dot{q}^T, \ddot{q}^T \end{bmatrix}^T\\" +
            r"& \text{Input:} \; && u = \begin{bmatrix} \tau^T, f^T \end{bmatrix}^T" +
            r" \end{aligned}",
            font_size=96,
            color=color,
        )
        
        state_input_small = deepcopy(state_input)
        state_input_small.font_size = 18
        state_input_small.next_to(eom_small, RIGHT, aligned_edge=UP, buff=3.0)
        
        self.play(
            ReplacementTransform(eom, state_input),
            Create(eom_small),
        )
        self.wait(1)
        
        opt_var = MathTex(
            r"\begin{gathered} \text{Optimization Variable:} \\ x \end{gathered}",
            font_size=96,
            color=color,
        )
        
        opt_var_small = deepcopy(opt_var)
        opt_var_small.font_size = 18
        opt_var_small.next_to(state_input_small, RIGHT, aligned_edge=UP, buff=3.0)

        self.play(
            ReplacementTransform(state_input, opt_var),
            Create(state_input_small),
        )
        self.wait(1)
        
        ss = MathTex(
            r"\begin{gathered} " +
            r"\text{Single Shooting:} \\" +
            r"x = \begin{bmatrix} u_0^T, u_1^T, \dots, u_{n_c-1}^T \end{bmatrix}^T" +
            r"\end{gathered}",
            font_size=36,
            color=color,
        ).next_to(opt_var, DOWN + 0.75*LEFT, aligned_edge=LEFT, buff=1.0)
        arrow_to_ss = Arrow(
            start=opt_var.get_bottom(),
            end=ss.get_top(),
            buff=0.1,
            stroke_color=color,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.05,
        )
         
        
        ms = MathTex(
            r"\begin{gathered} " +
            r"\text{Multiple Shooting:} \\" +
            r"x = \begin{bmatrix} u_0^T, \dots, u_{n_c-1}^T, s_1^T, \dots, s_{n_c}^T \end{bmatrix}^T" +
            r"\end{gathered}",
            font_size=36,
            color=color,
        ).next_to(opt_var, DOWN + 0.75*RIGHT, aligned_edge=RIGHT, buff=1.0)
        arrow_to_ms = Arrow(
            start=opt_var.get_bottom(),
            end=ms.get_top(),
            buff=0.1,
            stroke_color=color,
            stroke_width=2,
            max_tip_length_to_length_ratio=0.05,
        )
        
        self.play(
            Create(ss),
            Create(arrow_to_ss),
        )
        self.play(
            Create(ms),
            Create(arrow_to_ms),
        )
        
        opt_problem = MathTex(
            r"\begin{aligned} " +
            r"&\text{Optimization Problem:}\\ & \min_x \quad f(x) \\ & \text{s.t.} \quad x \in X" +
            r" \end{aligned}",
            font_size=96,
            color=color,
        )
        
        self.play(
            ReplacementTransform(opt_var, opt_problem),
            Create(opt_var_small),
            FadeOut(ss),
            FadeOut(ms),
            FadeOut(arrow_to_ms),
            FadeOut(arrow_to_ss),
        )
        self.wait(1)
