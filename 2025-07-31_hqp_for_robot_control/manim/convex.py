from manim import *


class Convex(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=0*DEGREES, theta=0*DEGREES)
        axes = ThreeDAxes()

        parabola = Surface(
            lambda u, v: np.array([
                -(u**2 + v**2),
                u,
                v,
            ]),
            v_range=[-2, 2],
            u_range=[-2, 2],
            resolution=(32, 32),
            fill_opacity=0.5,
        )
        
        self.add(axes)
        self.add(parabola)
        self.begin_ambient_camera_rotation(rate=-0.5, about='phi')
        self.wait(2)
        self.stop_ambient_camera_rotation()
