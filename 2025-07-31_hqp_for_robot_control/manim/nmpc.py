from manim import *

class NMPC(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        
        color = BLACK
        
        # equation = MathTex(
        #     r"\
        #     \begin{aligned}\
        #     & \min_x \; && f (x) \\ \
        #     & \text{s.t.} \; && x \in X \
        #     \end{aligned}\
        #     ",
        # )
        # self.add(equation)
        
        # Create the axes object and labels
        ax = Axes(
            x_range=[-4.5, 4.5],
            y_range=[0, 30, 10],
            axis_config={"include_tip": False, 'color': color}
        )
        labels = ax.get_axis_labels(
            x_label=MathTex("x", color=color),
            y_label=MathTex("f(x)", color=color)
        )
        
        # Example Function
        def func(x):
            return (0.1*(x**4)) - (x**2) + .5*x + 9 + 5*np.sin(x)
        
        # Plot the function on the axes
        graph = ax.plot(func, x_range=[-4, 4], color=BLUE)

        # Create a pair of ValueTracker objetcs, one to track the X coordinate and one to track the Y coord
        # Value Tracker objects can be animated
        xts = [ValueTracker(i) for i in range(-4,5)]
        yts = [ValueTracker(30) for i in range(9)]

        # Make a list of initial points, create the dots, put them in a VGroup object
        # NOTE: when calling a point, we must define is as a property of our axes (ax) and use the c2p() (coord_to_point) method
        points = [[xts[i].get_value(), yts[i].get_value()] for i in range(9)]
        dots = [Dot(point=ax.c2p(*p), color=color) for p in points]
        dot_group = VGroup(*dots)

        # Explicitly defining the updater fucntion in order to remove it later
        # Also need a function so an index can be input into the ValueTracker lists
        def updater_1(mobj, idx):
            mobj.add_updater(lambda x: x.move_to(ax.c2p(xts[idx].get_value(), yts[idx].get_value())))

        # Add updater, kind of a weird method here, but necessary because we also need the dots index in the value trackers
        for i, d in enumerate(dot_group):
            updater_1(d, i)

        # To play all animations at once we need them pre-looped and defined in a list
        falling_dots = [y.animate.set_value(func(x.get_value())) for x,y in zip(xts,yts)]

        # Add the (m)objects and animate changing the dot's y-value to the function line
        self.add(ax, labels, graph, dot_group)
        self.wait() # ** To add suspense **
        # Use the list of animations to play dots falling simultaneously
        self.play(LaggedStart(*falling_dots, lag_ratio=0.2))

        # Use below for loop to play dot animations one by one. I prefer the LaggedStart style though
            # for x,y in zip(xts, yts):
            #     self.play(y.animate.set_value(func(x.get_value())), run_time=0.25)

        # Clear the first updater to add a new one
        for dot in dot_group:
            dot.remove_updater(updater_1)
        
        # Define the updater for the second animation
        def updater_2(mobj, idx):
            mobj.add_updater(lambda x: x.move_to(ax.c2p(xts[idx].get_value(), func(xts[idx].get_value()))))

        # Add updater to each dot as before
        for i, d in enumerate(dot_group):
            updater_2(d, i)
        
        # Find indicies of minimum values of the function.
        # I know the relative max in the center of the function is @ 1.32, so split space there.
        xspace_left = np.linspace(-4, 1.32, 300)
        xspace_right = np.linspace(1.32, 4, 150)
        min_idx_left = func(xspace_left).argmin()
        min_idx_right = func(xspace_right).argmin()

        # Second animation step: change the x value tracker to the minimum point, updater will move dot along line.
        # Create separate animations based on if the value is on either side of the relative maximum
        rolling_dots_left = [x.animate.set_value(xspace_left[min_idx_left]) for x in xts if x.get_value() < 1.32]
        rolling_dots_right = [x.animate.set_value(xspace_right[min_idx_right]) for x in xts if x.get_value() >= 1.32]
        rolling_dots = rolling_dots_left + rolling_dots_right

        # Play the second animations
        self.play(LaggedStart(*rolling_dots, lag_ratio=0.03), run_time=2.5)
        self.wait(2)
