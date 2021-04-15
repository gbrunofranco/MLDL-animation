from manim import *


class AnimationMLDL(Scene):
    # config.background_color = WHITE
    bottom_left_moves = [LEFT*5, DOWN*3]
    bottom_right_moves = [RIGHT*5, DOWN*3]
    bottom_center_right_moves = [RIGHT*1.5, DOWN*3]
    bottom_center_left_moves = [LEFT*1.5, DOWN*3]
    bottom_text_scale = 0.2
    def construct(self):

        self.create_text()
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

        
    def create_text(self):
        text_polito = Text("Politecnico di Torino - Apr 2021")
        text_polito.scale(self.bottom_text_scale)
        text_polito.shift(*self.bottom_right_moves)
        self.add(text_polito)


        personal_name_text = Text("Gabriele Bruno Franco")
        final_personal_name_text = Text("|  Gabriele Bruno Franco  |")
        final_personal_name_text.scale(self.bottom_text_scale).align_to(text_polito, DOWN).shift(LEFT*5)
        self.play(Write(personal_name_text))
        self.wait()
        self.play(Transform(personal_name_text, final_personal_name_text))
        self.wait()


        paper_name_text = Text("Generating Sequences With \nRecurrent Neural Networks")
        author_name_text = Text("Alex Graves")
        author_name_text.move_to(DOWN*1.4).scale(.7)


        self.play(Write(paper_name_text), Write(author_name_text))
        self.wait()

        final_paper_name_text = Text("|  Generating Sequences With Recurrent Neural Networks  |")
        final_author_name_text = Text("|  Alex Graves  |")
        final_paper_name_text.scale(self.bottom_text_scale).align_to(text_polito, DOWN).shift(LEFT*1.5)
        final_author_name_text.scale(self.bottom_text_scale).align_to(text_polito, DOWN).shift(RIGHT*1.5)


        self.play(Transform(paper_name_text, final_paper_name_text), Transform(author_name_text, final_author_name_text))
        