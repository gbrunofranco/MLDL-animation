from manim import *


class AnimationMLDL(Scene):
    # config.background_color = WHITE
    # bottom_left_moves = [LEFT*5, DOWN*3]
    bottom_right_moves = [RIGHT*5, DOWN*3.5]
    # bottom_center_right_moves = [RIGHT*1.5, DOWN*4]
    # bottom_center_left_moves = [LEFT*1.5, DOWN*3]
    bottom_text_scale = 0.2
    text_source_scale = .25

    def construct(self):

        self.create_initial_text()
        self.wait(3)
        self.intro()
        self.wait(.25)
        self.pred_network()
        self.wait(1.5)
        self.text_prediction()
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

    def text_prediction(self):
        text_scale = .45

        self.add_sound("trimmed_text_pred.wav")
        self.wait(2 )
        word_based_text = Text("word-based approach").scale(text_scale).shift(LEFT*2.3).shift(UP*.5)
        word_based_arrow = Arrow(np.array([-.15, .5, 0]), np.array([.35, .5, 0]), buff=0)
        word_based_characteristics_text = Text("slightly better").scale(text_scale).shift(RIGHT*2.3).shift(UP*.5)

        character_based_text = Text("character-based approach").scale(text_scale).align_to(word_based_text, RIGHT).shift(DOWN*.5)
        character_based_arrow = Arrow(np.array([-.15, -.5, 0]), np.array([.35, -.5, 0]), buff=0)
        character_based_characteristics_text = Text("more interesting").scale(text_scale).align_to(word_based_characteristics_text, LEFT) .shift(DOWN*.5)

        penn_treebank_title = Text("The Penn Treebank Dataset").scale(.8).shift(UP*3)
        penn_treebank_words = Text("10k words").scale(text_scale).shift(LEFT*2.3).shift(UP*.5)
        penn_treebank_characters = Text("1M characters").scale(text_scale).align_to(penn_treebank_words, RIGHT).shift(DOWN*.5)
        penn_treebank_arrow = Arrow(np.array([-.15, 0, 0]), np.array([.35, 0, 0]), buff=0)
        penn_treebank_overfit = Text("easily overfit").scale(text_scale).shift(RIGHT*2.3) 
        penn_treebank_noise = Text("weighted and \nadaptively weighted noise").scale(text_scale).align_to(word_based_characteristics_text, LEFT)

        wikipedia_title = Text("The Wikipedia Dataset").scale(.8).shift(UP*3)
        wikipedia_reg = Text("filled with regularities").scale(text_scale).shift(LEFT*2.3)
        wikipedia_state = Text("needs to remember\nwhich state it's in").scale(text_scale).align_to(word_based_characteristics_text, LEFT)
        wikipedia_arrow = Arrow(np.array([-.15, 0, 0]), np.array([.35, 0, 0]), buff=0)


        self.play(Write(word_based_text))
        self.wait()
        self.play(Write(character_based_text))
        self.wait()
        self.play(FadeIn(word_based_arrow))
        self.play(FadeIn(word_based_characteristics_text))
        self.wait()
        self.play(FadeIn(character_based_arrow))
        self.play(FadeIn(character_based_characteristics_text))
        self.wait(9)
        self.play(FadeOut(word_based_text), FadeOut(character_based_text), FadeOut(word_based_arrow), FadeOut(word_based_characteristics_text), FadeOut(character_based_arrow),  FadeOut(character_based_characteristics_text))
        self.wait(2)
        self.play(Write(penn_treebank_title))
        self.wait(1.5)
        self.play(Write(penn_treebank_words), Write(penn_treebank_characters))
        self.wait(8)
        self.play(FadeIn(penn_treebank_arrow), Write(penn_treebank_overfit))
        self.wait(3)
        self.play(penn_treebank_overfit.animate.shift(LEFT*4), FadeOut(penn_treebank_characters), FadeOut(penn_treebank_words))
        self.play(Write(penn_treebank_noise))
        self.wait(21)
        self.play(FadeOut(penn_treebank_overfit), FadeOut(penn_treebank_noise), FadeOut(penn_treebank_arrow), FadeOut(penn_treebank_title))
        self.play(Write(wikipedia_title))
        self.wait(17)
        self.play(Write(wikipedia_reg))
        self.wait(10)
        self.play(Create(wikipedia_arrow), Write(wikipedia_state))
        self.wait(16)
        self.play(FadeOut(wikipedia_arrow), FadeOut(wikipedia_state), FadeOut(wikipedia_title), FadeOut(wikipedia_reg))



    def pred_network(self):
        hidden_layer_height = 0
        input_layer_height = -2.68
        output_layer_height = 2.68
        text_horizontal_position = -5.5
        exp_text_horizontal_position = +1.5
        arrows_scale = .35
        
        latex_text_scale = .6
        surr_rect_buff = 0.05
        surr_rect_stroke_width = 1.5
        left_horizontal_latex_pos = -3.7
        first_rnn= ImageMobject("/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/first_rnn_orig_transparent_cropped.png")
        first_rnn.scale(.8).set_color(WHITE)
        self.play(FadeIn(first_rnn))
        self.add_sound("trimmed_pred_network.wav")
        self.wait(6)


        input_arrow = Arrow(np.array([-5, input_layer_height, 0]), np.array([-3, input_layer_height, 0]), buff=0, stroke_width=2)
        VMobject.scale(input_arrow, arrows_scale)
        input_text = Text("Input Layer").scale(.35).shift(UP*input_layer_height).shift(RIGHT*text_horizontal_position)
        input_exp_text = Text("[0, ..., 1, 0, ...]").scale(.35).shift(UP*input_layer_height).shift(RIGHT*exp_text_horizontal_position)

        hidden_arrow = Arrow(np.array([-5, hidden_layer_height, 0]), np.array([-3, hidden_layer_height, 0]), buff=0, stroke_width=2)
        VMobject.scale(hidden_arrow, arrows_scale)
        hidden_text = Text("Hidden Layers").scale(.35).shift(UP*hidden_layer_height).align_to(input_text, RIGHT)
        hidden_exp_text = Text("LSTM cells").scale(.35).shift(UP*hidden_layer_height).align_to(input_exp_text, LEFT)


        output_arrow = Arrow(np.array([-5, output_layer_height, 0]), np.array([-3, output_layer_height, 0]), buff=0, stroke_width=2)
        VMobject.scale(output_arrow, arrows_scale)
        output_text = Text("Output Layer").scale(.35).shift(UP*output_layer_height).align_to(input_text, RIGHT)
        output_exp_text = Text("Distribution of future inputs").scale(.35).shift(UP*output_layer_height).align_to(input_exp_text, LEFT)
        
        arrows = VGroup(
                input_arrow,
                hidden_arrow,
                output_arrow
        )
        text = VGroup(
            input_text,
            hidden_text,
            output_text
        )
        exp_text = VGroup(
            input_exp_text,
            output_exp_text
        )
        shift_horiz_tex = .5
        big_hidden_exp_text = Text("LSTM cells").scale(.8).shift(UP*3)
        lstm_cell_img= ImageMobject("/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/lstm_cell_transparent.png")
        lstm_cell_img.scale(.7).set_color(WHITE)

        input_gate_tex = MathTex(r"i_t =",r"\sigma",r"(", r"W_{xi}", r"x_t", r"+",r"W_{hi}",r"h_{t-1}", r"+", r"W_{ci}", r"c_{t-1}", r"+", r"b_i", r")").scale(latex_text_scale).shift(RIGHT*left_horizontal_latex_pos)
        function_gate_tex = MathTex(r"f_t =",r"\sigma",r"(", r"W_{xf}", r"x_t", r"+",r"W_{hf}",r"h_{t-1}", r"+", r"W_{cf}", r"c_{t-1}", r"+", r"b_f", r")").scale(latex_text_scale).align_to(input_gate_tex, LEFT).shift(DOWN*shift_horiz_tex)
        output_gate_tex = MathTex(r"o_t =",r"\sigma",r"(", r"W_{xo}", r"x_t", r"+",r"W_{ho}",r"h_{t-1}", r"+", r"W_{co}", r"c_{t-1}", r"+", r"b_o", r")").scale(latex_text_scale).align_to(input_gate_tex, LEFT).shift(DOWN*shift_horiz_tex*2)
        cell_gate_tex = MathTex(r"c_t =",r"i_t", r"tanh",r"(", r"W_{xi}", r"x_t", r"+",r"W_{hi}",r"h_{t-1}", r"+", r"b_i", r")").scale(latex_text_scale).align_to(input_gate_tex, LEFT).shift(DOWN*shift_horiz_tex*3)
        hidden_gate_tex = MathTex(r"h_t = ", r"tanh", r"(c_t)").scale(latex_text_scale).align_to(input_gate_tex, LEFT).shift(DOWN*shift_horiz_tex*4)

        framebox_sigma_i = SurroundingRectangle(input_gate_tex[1], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_i_1 = SurroundingRectangle(input_gate_tex[3], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_i_2 = SurroundingRectangle(input_gate_tex[6], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_i_3 = SurroundingRectangle(input_gate_tex[9], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_i_1 = SurroundingRectangle(input_gate_tex[4], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_i_2 = SurroundingRectangle(input_gate_tex[7], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_i_3 = SurroundingRectangle(input_gate_tex[10], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_bias_i = SurroundingRectangle(input_gate_tex[-2], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        

        framebox_sigma_f = SurroundingRectangle(function_gate_tex[1], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_f_1 = SurroundingRectangle(function_gate_tex[3], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_f_2 = SurroundingRectangle(function_gate_tex[6], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_f_3 = SurroundingRectangle(function_gate_tex[9], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_f_1 = SurroundingRectangle(function_gate_tex[4], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_f_2 = SurroundingRectangle(function_gate_tex[7], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_f_3 = SurroundingRectangle(function_gate_tex[10], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_bias_f = SurroundingRectangle(function_gate_tex[-2], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)

        framebox_sigma_o = SurroundingRectangle(output_gate_tex[1], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_o_1 = SurroundingRectangle(output_gate_tex[3], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_o_2 = SurroundingRectangle(output_gate_tex[6], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_o_3 = SurroundingRectangle(output_gate_tex[9], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_o_1 = SurroundingRectangle(output_gate_tex[4], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_o_2 = SurroundingRectangle(output_gate_tex[7], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_o_3 = SurroundingRectangle(output_gate_tex[10], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_bias_o = SurroundingRectangle(output_gate_tex[-2], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
                
        framebox_sigma_c = SurroundingRectangle(cell_gate_tex[2], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_c_1 = SurroundingRectangle(cell_gate_tex[4], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_weight_c_2 = SurroundingRectangle(cell_gate_tex[7], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_c_1 = SurroundingRectangle(cell_gate_tex[5], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_input_c_2 = SurroundingRectangle(cell_gate_tex[8], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        framebox_bias_c = SurroundingRectangle(cell_gate_tex[-2], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)


        framebox_sigma_h = SurroundingRectangle(hidden_gate_tex[1], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width)
        
        
        math_text = VGroup(
            input_gate_tex,
            function_gate_tex,
            output_gate_tex,
            cell_gate_tex,
            hidden_gate_tex
        )

        framebox_first_f = VGroup(
            framebox_sigma_i,
            framebox_sigma_f,
            framebox_sigma_o,
            framebox_sigma_c,
            framebox_sigma_h
        )

        framebox_bias = VGroup(
            framebox_bias_i,
            framebox_bias_f,
            framebox_bias_o,
            framebox_bias_c,
        )

        framebox_input = VGroup(
            framebox_input_i_1,
            framebox_input_i_2,
            framebox_input_i_3,
            framebox_input_f_1,
            framebox_input_f_2,
            framebox_input_f_3,
            framebox_input_o_1,
            framebox_input_o_2,
            framebox_input_o_3,
            framebox_input_c_1,
            framebox_input_c_2,
        )

        framebox_weight = VGroup(
            framebox_weight_i_1,
            framebox_weight_i_2,
            framebox_weight_i_3,
            framebox_weight_f_1,
            framebox_weight_f_2,
            framebox_weight_f_3,
            framebox_weight_o_1,
            framebox_weight_o_2,
            framebox_weight_o_3,
            framebox_weight_c_1,
            framebox_weight_c_2,
        )

        code_scale = .41
        code_ex_text = Text("Example for output gate during forward pass:").scale(.4).shift(2*UP).shift(3.7*RIGHT)
        code_out_gate = Code(code="// output gate\n"+
                            "// extra input from peephole (from current state)\n"+
                            "#ifdef PEEPS\n"+
                            "dot(stateBegin + cellStart, stateBegin + cellEnd, peepWtIt, inActIt,inActIt + 1);\n"+
                            "peepWtIt += cellsPerBlock;\n"+
                            "#endif\n"+
                            "real_t outGateAct = G::fn(*inActIt);\n"+
                            "outGateActBegin[b] = outGateAct;\n"+
                            "++inActIt;\n\n"+
                            "// output activations\n"+
                            "transform(preOutGateActBegin + cellStart, preOutGateActBegin + cellEnd,\n"+
                            "actBegin + cellStart,\n"+
                            "bind2nd(multiplies<real_t>(), outGateAct));\n"+
                            "cellStart = cellEnd;\n"+
                            "cellEnd += cellsPerBlock;\n"+
                            "fgActBegin = fgActEnd;\n"+
                            "fgActEnd += this->num_seq_dims();\n", 
                                language="cpp", line_no_from=177, style="monokai")

        code_out_gate.scale(code_scale).align_to(code_ex_text, LEFT)
        code_source = Text("Code directly from source at:\nhttps://github.com/szcom/rnnlib/blob/master/src/LstmLayer.hpp")
        code_source.scale(.25).align_to(code_ex_text, LEFT).shift(DOWN*3)


        self.play(FadeIn(input_arrow),  FadeIn(input_text))
        self.play(FadeIn(hidden_arrow), FadeIn(hidden_text))
        self.play(FadeIn(output_arrow), FadeIn(output_text))
        self.wait(20)
        self.play(FadeOut(first_rnn))
        self.play(arrows.animate.shift(RIGHT*3.5), text.animate.shift(RIGHT*3))
        self.wait(1)
        self.play(FadeIn(input_exp_text))
        self.wait(3)
        self.play(FadeIn(output_exp_text))
        self.wait(1)
        self.play(FadeIn(hidden_exp_text))
        self.wait(10)
        self.play(FadeOut(arrows), FadeOut(text), FadeOut(exp_text))
        self.play(Transform(hidden_exp_text, big_hidden_exp_text))
        self.wait(1)
        self.add_sound("trimmed_lstm_cells.wav", gain=2.5)
        self.play(FadeIn(lstm_cell_img))
        self.wait(3)
        self.play(lstm_cell_img.animate.scale(.6).shift(*[UP*2, LEFT*5]))
        self.wait(1)
        self.play(Write(math_text), FadeIn(code_ex_text))
        self.play(FadeIn(code_source), FadeIn(code_out_gate))
        self.wait(3)
        self.play(Create(framebox_first_f, rate_func=linear))
        self.wait(2)
        self.play(FadeOut(framebox_first_f))
        self.wait(5)
        self.play(Create(framebox_weight, rate_func=linear))
        self.wait(2)
        self.play(ReplacementTransform(framebox_weight, framebox_input))
        self.wait(5)
        self.play(ReplacementTransform(framebox_input, framebox_bias))
        self.wait(3)
        self.play(FadeOut(framebox_bias), FadeOut(code_source), FadeOut(lstm_cell_img), FadeOut(math_text), FadeOut(code_ex_text), FadeOut(hidden_exp_text), FadeOut(code_out_gate))


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
        self.wait(1.5)

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

        self.wait(1)

        third_font_text = Text("He dismissed the").scale(text_scale).shift(LEFT*2.3).shift(DOWN)
        fourth_font_text = Text("... ?").scale(text_scale).shift(RIGHT*2).shift(DOWN)
        third_arrow = Arrow(np.array([-.15, -1, 0]), np.array([.35, -1, 0]), buff=0)
        third_rnn = VGroup(
                third_font_text,
                fourth_font_text,
                third_arrow
            )
        self.play(FadeIn(third_rnn))
        self.wait(2)        
        self.play(FadeIn(second_rnn))
        self.wait(6)

        self.play(FadeOut(first_rnn), FadeOut(second_rnn), FadeOut(third_rnn))
        
        text_lstm = Text("LSTM approach achieves better results than standard RNNs because it retains more information as well as having better possibility of recovering from errors¹")
        text_lstm.scale(text_scale)
        source_lstm = Text("1: S. Hochreiter, Y. Bengio, P. Frasconi, and J. Schmidhuber. Gradient Flow in Recurrent Nets: the Difficulty of Learning Long-term Dependencies. In S. C. Kremer and J. F. Kolen, editors, A Field Guide to Dynamical Recurrent Neural Networks. 2001.")
        source_lstm.scale(self.text_source_scale).shift(DOWN*2.5)
        self.play(Write(text_lstm, run_time=3), FadeIn(source_lstm))
        self.wait(14)
        self.play(FadeOut(text_lstm), FadeOut(source_lstm))

    def create_initial_text(self):
        self.add_sound("trimmed_intro_final3.wav")
        text_polito = Text("Politecnico di Torino - Apr 2021")
        text_polito.scale(self.bottom_text_scale)
        text_polito.shift(*self.bottom_right_moves)
        self.add(text_polito)


        personal_name_text = Text("Gabriele Bruno Franco")
        final_personal_name_text = Text("  Gabriele Bruno Franco  ")
        final_personal_name_text.scale(self.bottom_text_scale).align_to(text_polito, UP).shift(LEFT*5)
        self.wait(1)

        self.play(Write(personal_name_text))
        self.wait(.5)
        self.play(Transform(personal_name_text, final_personal_name_text))
        self.wait()


        paper_name_text = Text("Generating Sequences With \nRecurrent Neural Networks")
        author_name_text = Text("Alex Graves")
        author_name_text.move_to(DOWN*1.4).scale(.7)


        self.play(Write(paper_name_text), Write(author_name_text))
        self.wait(3)

        final_paper_name_text = Text("  Generating Sequences With Recurrent Neural Networks  ")
        final_author_name_text = Text("  Alex Graves  ")
        final_paper_name_text.scale(self.bottom_text_scale).align_to(text_polito, UP).shift(LEFT*1.5)
        final_author_name_text.scale(self.bottom_text_scale).align_to(text_polito, UP).shift(RIGHT*1.5)


        self.play(Transform(paper_name_text, final_paper_name_text), Transform(author_name_text, final_author_name_text))
        