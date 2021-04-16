from manim import *


class AnimationMLDL(Scene):
    # config.background_color = WHITE
    bottom_left_moves = [LEFT*5, DOWN*3]
    bottom_right_moves = [RIGHT*5, DOWN*3]
    bottom_center_right_moves = [RIGHT*1.5, DOWN*3]
    bottom_center_left_moves = [LEFT*1.5, DOWN*3]
    bottom_text_scale = 0.2
    text_source_scale = .25

    def construct(self):

        self.create_initial_text()
        self.wait(3)
        self.intro()
        self.wait()

        # text_polito = Text("Politecnico di Torino Apr 2021", size=self.bottom_text_scale)
        # # for move in self.bottom_right_moves:
        # #     text_polito.shift(move)
        # text_polito.to_edge(DOWN).to_edge(RIGHT)
        # self.add(text_polito)
        # personal_name_text = Text("Gabriele Bruno Franco", size=1)
        # final_personal_name_text = Text("Politecnico di Torino Apr 2021", size=self.bottom_text_scale)
        # final_personal_name_text.to_edge(DOWN).to_edge(RIGHT).shift(2*LEFT)
        # self.play(Write(personal_name_text))
        # self.wait()
        
        # self.play(Transform(personal_name_text, final_personal_name_text))

        # self.wait()

        # paper_name_text = Text("Generating Sequences With \nRecurrent Neural Networks")
        # author_name_text = Text("Alex Graves")
        # author_name_text.move_to(DOWN*1.4).scale(.7)
        # self.play(Write(paper_name_text), Write(author_name_text))

        # # paper_text_group = VGroup(
        # #     paper_name_text,
        # #     author_name_text
        # # )
        # # self.wait()
        # # self.play(paper_text_group.animate.scale(self.bottom_text_scale).to_edge(DOWN))

        # self.wait()
        # final_paper_name_text = Text("Generating Sequences With Recurrent Neural Networks").scale(self.bottom_text_scale).align_to(text_polito, DOWN).shift(1.3*LEFT)
        # final_author_name_text = Text("Alex Graves").scale(self.bottom_text_scale).align_to(text_polito, DOWN).shift(1.3*RIGHT)
        # self.play(Transform(paper_name_text, final_paper_name_text), Transform(author_name_text, final_author_name_text))

        # self.wait()


    def intro(self):
        svg_scale = .2
        text_scale = .45

        first_handwriting = SVGMobject('/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/first_hand_ex.svg')
        first_handwriting.scale(svg_scale).set_color(WHITE)
        first_handwriting.shift(RIGHT*2)
        first_font_text = Text("He dismissed the idea")
        first_font_text.scale(text_scale).shift(LEFT*2)
        first_arrow = Arrow(np.array([-.15, 0, 0]), np.array([.35, 0, 0]), buff=0)
        self.play(FadeIn(first_handwriting))
        self.wait(2)
        self.play(FadeIn(first_font_text), FadeIn(first_arrow))
        self.wait(3)
        first_rnn = VGroup(
                first_handwriting,
                first_font_text,
                first_arrow
            )
        self.play(first_rnn.animate.shift(UP))
        self.wait(5)

        second_handwriting = SVGMobject('/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/second_hand_ex.svg')
        second_handwriting.scale(svg_scale).align_to(first_font_text, LEFT).set_color(WHITE)
        second_font_text = Text("... ?")
        second_font_text.scale(text_scale).shift(RIGHT*2)
        second_arrow = Arrow(np.array([-.15, 0, 0]), np.array([.35, 0, 0]), buff=0)
        second_rnn = VGroup(
                second_handwriting,
                second_font_text,
                second_arrow
            )

        self.wait(3)

        third_font_text = Text("He dismissed the").scale(text_scale).shift(LEFT*2.3).shift(DOWN)
        fourth_font_text = Text("... ?").scale(text_scale).shift(RIGHT*2).shift(DOWN)
        third_arrow = Arrow(np.array([-.15, -1, 0]), np.array([.35, -1, 0]), buff=0)
        third_rnn = VGroup(
                third_font_text,
                fourth_font_text,
                third_arrow
            )
        self.play(FadeIn(third_rnn))
        self.wait(4)        
        self.play(FadeIn(second_rnn))
        self.wait()

        self.play(FadeOut(first_rnn), FadeOut(second_rnn), FadeOut(third_rnn))
        
        text_lstm = Text("LSTM approach achieves better results than standard RNNs because it retains more information as well as having better possibility of recovering from errors¹")
        text_lstm.scale(text_scale)
        source_lstm = Text("1: S. Hochreiter, Y. Bengio, P. Frasconi, and J. Schmidhuber. Gradient Flow in Recurrent Nets: the Difficulty of Learning Long-term Dependencies. In S. C. Kremer and J. F. Kolen, editors, A Field Guide to Dynamical Recurrent Neural Networks. 2001.")
        source_lstm.scale(self.text_source_scale).shift(DOWN*2.5)
        self.play(Write(text_lstm, run_time=2), FadeIn(source_lstm))
        self.wait()


    def create_initial_text(self):
        text_polito = Text("Politecnico di Torino - Apr 2021")
        text_polito.scale(self.bottom_text_scale)
        text_polito.shift(*self.bottom_right_moves)
        self.add(text_polito)


        personal_name_text = Text("Gabriele Bruno Franco")
        final_personal_name_text = Text("  Gabriele Bruno Franco  ")
        final_personal_name_text.scale(self.bottom_text_scale).align_to(text_polito, UP).shift(LEFT*5)
        self.play(Write(personal_name_text))
        self.wait()
        self.play(Transform(personal_name_text, final_personal_name_text))
        self.wait()


        paper_name_text = Text("Generating Sequences With \nRecurrent Neural Networks")
        author_name_text = Text("Alex Graves")
        author_name_text.move_to(DOWN*1.4).scale(.7)


        self.play(Write(paper_name_text), Write(author_name_text))
        self.wait()

        final_paper_name_text = Text("  Generating Sequences With Recurrent Neural Networks  ")
        final_author_name_text = Text("  Alex Graves  ")
        final_paper_name_text.scale(self.bottom_text_scale).align_to(text_polito, UP).shift(LEFT*1.5)
        final_author_name_text.scale(self.bottom_text_scale).align_to(text_polito, UP).shift(RIGHT*1.5)


        self.play(Transform(paper_name_text, final_paper_name_text), Transform(author_name_text, final_author_name_text))
        