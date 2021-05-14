from manim import *
import scipy.stats as stats


class AnimationMLDL(GraphScene, Scene):

    bottom_right_moves = [RIGHT * 5, DOWN * 3.5]
    bottom_text_scale = 0.2
    text_source_scale = 0.25

    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            y_axis_label=r"$P(letters)$",
            x_axis_label=r"$t$",
            y_max=8,
            x_max=18,
            x_min=-8,
            **kwargs
        )

    def construct(self):
        self.create_initial_text()
        self.wait(3)
        self.intro()
        self.wait(0.25)
        self.pred_network()

        self.text_prediction()
        self.handwriting_pred()
        self.handwriting_synth()
        self.conclusion()

    def conclusion(self):
        text_scale = 0.45
        text_vert_shift = .8
        small_text_scale = 0.3

        self.add_sound("./trimmed_conclusions.wav", gain=4)
        text_conc = Text(
            "Future works could apply the results of this paper could be improved by a better understanding of data distribution and possibly apply similiar techniques to text annotation"
        )
        text_conc.scale(text_scale)
        text_conc_2 = Text("The following papers were cited in this animation:")
        text_conc_2_1 = Text("1: S. Hochreiter, Y. Bengio, P. Frasconi, and J. Schmidhuber. Gradient Flow in Recurrent Nets: the Difficulty of Learning Long-term Dependencies. In S. C. Kremer and J. F. Kolen, editors, A Field Guide to Dynamical Recurrent Neural Networks. 2001.").shift(DOWN*text_vert_shift)
        text_conc_2_2 = Text("2: C. Bishop. Mixture density networks. Technical report, 1994.").next_to(text_conc_2_1, DOWN).align_to(text_conc_2_1, LEFT)
        text_conc_2_3 = Text("3: C. Bishop. Neural Networks for Pattern Recognition. Oxford Univ. Press, Inc., 1995.").next_to(text_conc_2_2, DOWN).align_to(text_conc_2_2, LEFT)
        text_conc_2_4 = Text("4: A. Graves. Sequence transduction with recurrent neural networks.\nIn ICML Representation Learning Worksop, 2012.").shift(DOWN*text_vert_shift*4).next_to(text_conc_2_3, DOWN).align_to(text_conc_2_3, LEFT)
            
        text_conc_2_grp = VGroup(
            text_conc_2_1,
            text_conc_2_2,
            text_conc_2_3,
            text_conc_2_4
        )
        text_conc_2_grp.scale(small_text_scale)
        text_conc_3 = Text("This animation required ~1000 lines of python code")
        text_conc_5 = Text(
            "It wouldn't have been possible without the Manim Community Edition library"
        )
        text_conc_6 = Text(
            "I'll be refactoring and uploading it at: github.com/gbrunofranco"
        )

        text_conc_3.scale(small_text_scale).shift(UP * text_vert_shift)
        text_conc_5.scale(small_text_scale)
        text_conc_6.scale(small_text_scale).shift(DOWN * text_vert_shift)

        self.play(Write(text_conc))
        self.wait(20)
        self.play(FadeOut(text_conc))

        self.wait()
        self.play(Write(text_conc_2))
        self.wait()
        self.play(Write(text_conc_2_grp))
        self.wait(5)
        self.play(FadeOut(text_conc_2), FadeOut(text_conc_2_grp))
        self.wait()
        self.play(Write(text_conc_3))
        self.wait()
        self.play(Write(text_conc_5))
        self.wait()
        self.play(Write(text_conc_6))
        self.wait(10)
        self.play(FadeOut(text_conc_3), FadeOut(text_conc_5), FadeOut(text_conc_6))
        self.wait()

    def handwriting_synth(self):
        self.add_sound("trimmed_hand_synt_1.wav", gain=0.8)
        second_rnn = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/second_rnn_transparent.png"
        )
        second_rnn.scale(1.1).shift(LEFT).shift(UP * 0.5).set_color(WHITE)

        arrows_scale = 0.35
        window_layer_height = 0.95
        string_layer_height = -2.75

        window_arrow = Arrow(
            np.array([-5, window_layer_height, 0]),
            np.array([-3, window_layer_height, 0]),
            buff=0,
            stroke_width=2,
        )
        VMobject.scale(window_arrow, arrows_scale).shift(LEFT * 0.5)
        window_text = (
            Text("Window Layer")
            .scale(0.35)
            .shift(UP * window_layer_height)
            .shift(LEFT * 6)
        )

        string_arrow = Arrow(
            np.array([-5, string_layer_height, 0]),
            np.array([-3, string_layer_height, 0]),
            buff=0,
            stroke_width=2,
        )
        VMobject.scale(string_arrow, arrows_scale)
        string_text = (
            Text("String Layer")
            .scale(0.35)
            .shift(UP * string_layer_height)
            .align_to(window_text, RIGHT)
        )

        transducers_text = (
            Text(
                "Custom model created because\nexploratory work on transducers\nwasn't satisfying⁵"
            )
            .scale(0.35)
            .shift(UP)
            .shift(RIGHT * 4.5)
        )
        transducers_source = (
            Text(
                "4: A. Graves. Sequence transduction with recurrent neural networks.\nIn ICML Representation Learning Worksop, 2012."
            )
            .scale(self.text_source_scale)
            .shift(DOWN * 3)
            .shift(RIGHT * 3.8)
        )

        first_results_pic = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/real_results_transparent.png"
        )
        first_results_pic.scale(0.95).shift(LEFT).shift(UP * 0.5).set_color(WHITE)
        first_results_text = (
            Text(
                "The first line is real handwriting and\n the others are generated samples"
            )
            .scale(0.35)
            .shift(UP * 0.5)
            .shift(RIGHT * 4.5)
        )

        biased_text = (
            Text("Biased sampling").scale(0.35).shift(UP * 0.5).shift(LEFT * 2)
        )
        biased_arrow = Arrow(
            np.array([-1, 0.5, 0]), np.array([-0.5, 0.5, 0]), buff=0
        ).shift(RIGHT * 0.2)
        biased_text_2 = (
            Text("Readable text\ngiven priority")
            .scale(0.35)
            .shift(UP * 0.5)
            .shift(RIGHT)
        )
        biased_arrow_2 = (
            Arrow(np.array([0, 0.5, 0]), np.array([0.5, 0.5, 0]), buff=0)
            .shift(LEFT * 0.5)
            .shift(RIGHT * 1.5)
        )

        biased_pic = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/biased_sampling_transparent.png"
        )
        biased_pic.scale(0.7).shift(RIGHT * 4).set_color(WHITE)

        primed_height = -0.5
        primed_text = (
            Text("Primed sampling")
            .scale(0.35)
            .shift(UP * primed_height)
            .align_to(biased_text, LEFT)
        )
        primed_arrow_1 = Arrow(
            np.array([-1, primed_height, 0]), np.array([-0.5, primed_height, 0]), buff=0
        ).align_to(biased_arrow, LEFT)
        primed_arrow_2 = Arrow(
            np.array([0, primed_height, 0]), np.array([0.5, primed_height, 0]), buff=0
        ).align_to(biased_arrow_2, LEFT)
        primed_text_2 = (
            Text("Input string\nis joined with\na character of\nthe wanted style")
            .scale(0.35)
            .shift(UP * primed_height)
            .align_to(biased_text_2, LEFT)
        )
        primed_pic = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/primed_sampling_transparent.png"
        )
        primed_pic.scale(0.7).align_to(biased_pic, LEFT).shift(DOWN).set_color(WHITE)
        biased_group = Group(
            biased_text,
            biased_text_2,
            biased_arrow,
            biased_arrow_2,
        )

        primed_group = Group(
            primed_text,
            primed_arrow_1,
            primed_text_2,
            primed_arrow_2,
        )

        combined_arrow = Arrow(
            np.array([-0.5, 0, 0]), np.array([0, 0, 0]), buff=0
        ).shift(RIGHT * 2)
        combined_img = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/combined_sampling_transparent.png"
        )
        combined_img.scale(0.9).shift(RIGHT * 4.5).set_color(WHITE)

        self.wait(8)
        self.play(FadeIn(second_rnn))
        self.wait()
        self.play(FadeIn(window_arrow), FadeIn(window_text))
        self.play(FadeIn(string_arrow), FadeIn(string_text))
        self.wait(8)
        self.play(Write(transducers_text))
        self.play(Write(transducers_source))
        self.wait(20)
        self.play(
            FadeOut(second_rnn),
            FadeOut(window_arrow),
            FadeOut(window_text),
            FadeOut(string_arrow),
            FadeOut(string_text),
            FadeOut(transducers_source),
            FadeOut(transducers_text),
        )
        # self.wait(1)
        self.play(FadeIn(first_results_pic), Write(first_results_text))
        self.wait(16)
        self.play(FadeOut(first_results_pic), FadeOut(first_results_text))
        self.add_sound("trimmed_hand_synt_2.wav", gain=2)
        self.play(Write(biased_text))
        self.wait(2)
        self.play(FadeIn(biased_arrow), Write(biased_text_2))
        self.wait(5)
        self.play(
            biased_text.animate.shift(LEFT),
            biased_text_2.animate.shift(LEFT),
            biased_arrow.animate.shift(LEFT),
            FadeIn(biased_arrow_2),
            FadeIn(biased_pic),
        )
        self.wait(21)
        self.play(
            biased_group.animate.shift(UP * 2),
            biased_pic.animate.shift(UP * 2).scale(0.8),
        )
        self.wait(15)
        self.play(FadeIn(primed_text))
        self.wait(3)
        self.play(Write(primed_text_2), FadeIn(primed_arrow_1))
        self.wait(5)
        self.play(
            primed_group.animate.shift(LEFT), FadeIn(primed_pic), FadeIn(primed_arrow_2)
        )
        self.wait(4)
        self.play(
            primed_group.animate.shift(LEFT * 3),
            primed_pic.animate.shift(LEFT * 3),
            biased_group.animate.shift(LEFT * 3),
            biased_pic.animate.shift(LEFT * 3),
            FadeIn(combined_arrow),
            FadeIn(combined_img),
        )
        self.wait(8)
        self.play(
            FadeOut(biased_group),
            FadeOut(biased_pic),
            FadeOut(primed_group),
            FadeOut(primed_pic),
            FadeOut(combined_arrow),
            FadeOut(combined_img),
        )

    def handwriting_pred(self):
        text_scale = 0.45
        self.add_sound("trimmed_handwritten_pred2.wav", gain=4.5)

        online_data = (
            Text("Online handwriting")
            .scale(text_scale)
            .shift(LEFT * 1.9)
            .shift(UP * 0.5)
        )
        online_arrow = Arrow(np.array([0, 0.5, 0]), np.array([0.5, 0.5, 0]), buff=0)
        online_exp_text = (
            Text("Real valued (x,y) coords")
            .scale(text_scale)
            .shift(RIGHT * 2.6)
            .shift(UP * 0.5)
        )
        online_arrow_2 = Arrow(
            np.array([0.25, 0.5, 0]), np.array([0.75, 0.5, 0]), buff=0
        ).shift(RIGHT)
        online_exp_text_2 = (
            Text("3 dimensions (2 real, 1 bool)")
            .scale(text_scale)
            .align_to(online_exp_text, LEFT)
            .shift(UP * 0.5)
            .shift(RIGHT * 1.2)
        )

        offline_data = (
            Text("Offline handwriting")
            .scale(text_scale)
            .align_to(online_data, RIGHT)
            .shift(DOWN * 0.5)
        )
        offline_arrow = Arrow(np.array([0, -0.5, 0]), np.array([0.5, -0.5, 0]), buff=0)
        offline_exp_text = (
            Text("Processing of images")
            .scale(text_scale)
            .align_to(online_exp_text, LEFT)
            .shift(DOWN * 0.5)
        )
        offline_arrow_2 = Arrow(
            np.array([0.25, -0.5, 0]), np.array([0.75, -0.5, 0]), buff=0
        ).shift(RIGHT)
        offline_exp_text_2 = (
            Text("Complex pre-processing")
            .scale(text_scale)
            .align_to(online_exp_text, LEFT)
            .shift(DOWN * 0.5)
            .shift(RIGHT * 1.2)
        )
        offline_arrow_3 = Arrow(
            np.array([2.8, -0.80, 0]), np.array([2.8, -1.3, 0]), buff=0
        ).shift(RIGHT)
        offline_exp_text_3 = (
            Text("Propagation of errors and\nreduction of variation in the data")
            .scale(text_scale)
            .align_to(online_exp_text, LEFT)
            .shift(DOWN * 1.8)
            .shift(RIGHT * 1.2)
        )

        fuziness_title = Text("Fuzziness of handwriting").scale(0.8).shift(UP * 3)

        text_arrows_types = VGroup(
            online_data,
            online_arrow,
            online_exp_text,
            offline_data,
            offline_arrow,
            offline_exp_text,
        )

        fuzziness_pic = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/fuziness_hand1.png"
        )
        fuzziness_pic.scale(4.5).set_color(WHITE)
        fuzziness_text1 = (
            Text("Should the RNN predict 'h' or 'e' here?")
            .scale(text_scale)
            .shift(DOWN * 1.2)
            .shift(RIGHT * 0.7)
        )
        fuzziness_text2 = (
            Text("This is the opposite of a one-hot encoded vector!")
            .scale(text_scale)
            .shift(DOWN * 1.8)
            .shift(RIGHT * 0.7)
        )

        def gaussian(x, amp=5, mu=3, sig=1):
            return amp * np.exp((-1 / 2 * ((x - mu) / sig) ** 2))

        gaussian_text = (
            Text("Each Gaussian curve is a \npossible prediction")
            .scale(text_scale)
            .shift(RIGHT * 1)
        )

        interpolation_text = (
            Text(
                "Prediction for the word 'under'\n\nThe colored sections are where the model guesses the next point to be\nThese are the \"mean\" of the first dot of each possible prediction"
            )
            .scale(text_scale)
            .shift(DOWN * 1.8)
        )
        interpolation_image = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/interpolation_image.png"
        )
        interpolation_image.scale(0.7).shift(UP * 0.6)

        pred_handwriting_text = (
            Text("Example of predicted text")
            .scale(text_scale)
            .shift(RIGHT * 3.5)
            .shift(DOWN * 0.3)
        )
        predicted_handwriting = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/predicted_handwriting.png"
        )
        predicted_handwriting.scale(0.45).shift(UP * 0.6).shift(RIGHT * 3.2)
        mixt_density_title = Text("Mixture Distributions").scale(0.8).shift(UP * 3)
        source_mix_nn0 = Text(
            "The idea of mixture density neural networks was first introduced in:"
        )
        source_mix_nn1 = Text(
            "2: C. Bishop. Mixture density networks. Technical report, 1994."
        )
        source_mix_nn2 = Text(
            "3: C. Bishop. Neural Networks for Pattern Recognition. Oxford Univ. Press, Inc., 1995."
        )
        source_mix_nn0.scale(self.text_source_scale).shift(DOWN * 2.7).shift(RIGHT * 2)
        source_mix_nn1.scale(self.text_source_scale).shift(DOWN * 3).align_to(
            source_mix_nn0, LEFT
        )
        source_mix_nn1.shift(RIGHT * 0.2)
        source_mix_nn2.scale(self.text_source_scale).shift(DOWN * 3.2).align_to(
            source_mix_nn1, LEFT
        )

        self.wait(3)
        self.play(Write(online_data))
        self.wait()
        self.play(FadeIn(online_arrow))
        self.play(Write(online_exp_text))
        self.wait()
        self.play(Write(offline_data))
        self.wait()
        self.play(FadeIn(offline_arrow))
        self.play(Write(offline_exp_text))
        self.wait()
        self.play(text_arrows_types.animate.shift(LEFT * 3.4))
        self.wait()
        self.play(FadeIn(offline_arrow_2), FadeIn(online_arrow_2))
        self.play(Write(offline_exp_text_2), Write(online_exp_text_2))
        self.wait()
        self.play(FadeIn(offline_arrow_3))
        self.play(Write(offline_exp_text_3))
        self.wait(45)
        self.play(
            FadeOut(offline_exp_text_2),
            FadeOut(online_exp_text_2),
            FadeOut(text_arrows_types),
            FadeOut(offline_arrow_2),
            FadeOut(offline_arrow_3),
            FadeOut(offline_exp_text_3),
            FadeOut(online_arrow_2),
        )
        self.play(Write(fuziness_title))
        self.play(FadeIn(fuzziness_pic), Write(fuzziness_text1))
        self.wait(2)
        self.play(Write(fuzziness_text2))
        self.wait(8)
        self.play(
            FadeOut(fuzziness_pic),
            FadeOut(fuzziness_text1),
            FadeOut(fuzziness_text2),
            FadeOut(fuziness_title),
        )
        # self.wait(2)
        self.play(Write(mixt_density_title))
        self.setup_axes()  # changed source of setup_axes to not play or add axes
        self.axes.scale(0.7).shift(DOWN * 0.5).shift(LEFT * 0.7)

        gaussian1 = (
            self.get_graph(gaussian, x_min=-5, x_max=15)
            .set_stroke(width=5)
            .set_color(WHITE)
        )
        gaussian2 = (
            self.get_graph(
                lambda x: gaussian(x, amp=3, mu=7, sig=0.8), x_min=-5, x_max=15
            )
            .set_stroke(width=5)
            .set_color(BLUE)
        )
        gaussian3 = (
            self.get_graph(
                lambda x: gaussian(x, amp=2, mu=-1, sig=1.4), x_min=-5, x_max=15
            )
            .set_stroke(width=5)
            .set_color(RED)
        )
        gaussian4 = (
            self.get_graph(
                lambda x: gaussian(x, amp=1.5, mu=12, sig=0.6), x_min=-5, x_max=15
            )
            .set_stroke(width=5)
            .set_color(GREEN)
        )

        self.add_sound("trimmed_mixture_density3.wav", gain=2.5)

        self.play(Create(self.axes))
        self.play(Create(gaussian1, run_time=3))
        self.play(Create(gaussian2, run_time=3))
        self.play(Create(gaussian3, run_time=3))
        self.play(Create(gaussian4, run_time=3))

        self.wait(1)
        self.play(Write(gaussian_text))
        self.play(Write(source_mix_nn0))
        self.play(Write(source_mix_nn1))
        self.play(Write(source_mix_nn2))
        self.wait(13)
        self.play(
            FadeOut(gaussian1),
            FadeOut(gaussian2),
            FadeOut(gaussian3),
            FadeOut(gaussian4),
            FadeOut(self.axes),
            FadeOut(gaussian_text),
            FadeOut(source_mix_nn0),
            FadeOut(source_mix_nn1),
            FadeOut(source_mix_nn2),
        )
        self.wait(2)
        self.play(Write(interpolation_text), FadeIn(interpolation_image))
        self.wait(12)
        self.play(
            interpolation_image.animate.shift(LEFT * 3.5), FadeIn(predicted_handwriting)
        )
        self.play(Write(pred_handwriting_text))
        self.wait(30)
        self.play(
            FadeOut(interpolation_image),
            FadeOut(interpolation_text),
            FadeOut(predicted_handwriting),
            FadeOut(pred_handwriting_text),
            FadeOut(mixt_density_title),
        )
        # self.wait(2)

    def text_prediction(self):
        text_scale = 0.45

        self.add_sound("trimmed_text_pred.wav", gain=3.5)
        self.wait(2)
        word_based_text = (
            Text("Word-based approach")
            .scale(text_scale)
            .shift(LEFT * 2.3)
            .shift(UP * 0.5)
        )
        word_based_arrow = Arrow(
            np.array([-0.15, 0.5, 0]), np.array([0.35, 0.5, 0]), buff=0
        )
        word_based_characteristics_text = (
            Text("Usually better").scale(text_scale).shift(RIGHT * 2.3).shift(UP * 0.5)
        )

        character_based_text = (
            Text("Character-based approach")
            .scale(text_scale)
            .align_to(word_based_text, RIGHT)
            .shift(DOWN * 0.5)
        )
        character_based_arrow = Arrow(
            np.array([-0.15, -0.5, 0]), np.array([0.35, -0.5, 0]), buff=0
        )
        character_based_characteristics_text = (
            Text("More interesting as\nit can create new words")
            .scale(text_scale)
            .align_to(word_based_characteristics_text, LEFT)
            .shift(DOWN * 0.5)
        )

        penn_treebank_title = Text("The Penn Treebank Dataset").scale(0.8).shift(UP * 3)
        penn_treebank_words = (
            Text("10k words").scale(text_scale).shift(LEFT * 2.3).shift(UP * 0.5)
        )
        penn_treebank_characters = (
            Text("1M characters")
            .scale(text_scale)
            .align_to(penn_treebank_words, RIGHT)
            .shift(DOWN * 0.5)
        )
        penn_treebank_arrow = Arrow(
            np.array([-0.15, 0, 0]), np.array([0.35, 0, 0]), buff=0
        )
        penn_treebank_overfit = (
            Text("Easily overfit").scale(text_scale).shift(RIGHT * 2.3)
        )
        penn_treebank_noise = (
            Text("Weighted and \nadaptively weighted noise")
            .scale(text_scale)
            .align_to(word_based_characteristics_text, LEFT)
        )
        penn_treebank_characteristics = (
            Text("Commonly used for NLP benchmarking")
            .scale(text_scale * 0.8)
            .shift(UP * 2.3)
        )
        penn_treebank_results = (
            Text(
                "Perplexity of 89.4 obtained with: ensamble of RNNs, cache model and 5-gram approach"
            )
            .scale(text_scale * 0.8)
            .shift(DOWN * 2.3)
        )

        wikipedia_title = Text("The Wikipedia Dataset").scale(0.8).shift(UP * 3)
        wikipedia_reg = (
            Text("Filled with regularities").scale(text_scale).shift(LEFT * 2.3)
        )
        wikipedia_state = (
            Text(
                "Needs to remember which state\nit's in to be able to close it properly"
            )
            .scale(text_scale)
            .align_to(word_based_characteristics_text, LEFT)
        )
        wikipedia_arrow = Arrow(np.array([-0.15, 0, 0]), np.array([0.35, 0, 0]), buff=0)
        wikipedia_characteristics = (
            Text("Commonly used for compression benchmarking")
            .scale(text_scale * 0.8)
            .shift(UP * 2.3)
        )
        wikipedia_results = (
            Text(
                "Incouraging results\nNiche articles had clear influence, this implies that it's not just the frequency of a word that influences its memorization"
            )
            .scale(text_scale * 0.8)
            .shift(DOWN * 2.3)
        )

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
        self.play(
            FadeOut(word_based_text),
            FadeOut(character_based_text),
            FadeOut(word_based_arrow),
            FadeOut(word_based_characteristics_text),
            FadeOut(character_based_arrow),
            FadeOut(character_based_characteristics_text),
        )
        self.wait(2)
        self.play(Write(penn_treebank_title))
        self.wait(1.5)
        self.play(Write(penn_treebank_words), Write(penn_treebank_characters))
        self.wait()
        self.play(Write(penn_treebank_characteristics))
        self.wait(8)
        self.play(FadeIn(penn_treebank_arrow), Write(penn_treebank_overfit))
        self.wait(3)
        self.play(
            penn_treebank_overfit.animate.shift(LEFT * 4),
            FadeOut(penn_treebank_characters),
            FadeOut(penn_treebank_words),
        )
        self.play(Write(penn_treebank_noise))
        self.wait(10)
        self.play(Write(penn_treebank_results))
        self.wait(5)
        self.play(
            FadeOut(penn_treebank_overfit),
            FadeOut(penn_treebank_noise),
            FadeOut(penn_treebank_arrow),
            FadeOut(penn_treebank_title),
            FadeOut(penn_treebank_characteristics),
            FadeOut(penn_treebank_results),
        )
        self.play(Write(wikipedia_title))
        self.wait(5)
        self.play(Write(wikipedia_characteristics))
        self.wait(12)
        self.play(Write(wikipedia_reg))
        self.wait(10)
        self.play(Create(wikipedia_arrow), Write(wikipedia_state))
        self.wait(8)
        self.play(Write(wikipedia_results))
        self.wait(6)
        self.play(
            FadeOut(wikipedia_arrow),
            FadeOut(wikipedia_state),
            FadeOut(wikipedia_title),
            FadeOut(wikipedia_reg),
            FadeOut(wikipedia_characteristics),
            FadeOut(wikipedia_results),
        )

    def pred_network(self):
        hidden_layer_height = 0
        input_layer_height = -2.68
        output_layer_height = 2.68
        text_horizontal_position = -5.5
        exp_text_horizontal_position = +1.5
        arrows_scale = 0.35

        latex_text_scale = 0.6
        surr_rect_buff = 0.05
        surr_rect_stroke_width = 1.5
        left_horizontal_latex_pos = -3.7
        first_rnn = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/first_rnn_orig_transparent_cropped.png"
        )
        first_rnn.scale(0.8).set_color(WHITE)
        self.play(FadeIn(first_rnn))
        self.add_sound("trimmed_pred_network.wav")
        self.wait(6)

        input_arrow = Arrow(
            np.array([-5, input_layer_height, 0]),
            np.array([-3, input_layer_height, 0]),
            buff=0,
            stroke_width=2,
        )
        VMobject.scale(input_arrow, arrows_scale)
        input_text = (
            Text("Input Layer")
            .scale(0.35)
            .shift(UP * input_layer_height)
            .shift(RIGHT * text_horizontal_position)
        )
        input_exp_text = (
            Text("[0, ..., 1, 0, ...]")
            .scale(0.35)
            .shift(UP * input_layer_height)
            .shift(RIGHT * exp_text_horizontal_position)
        )

        hidden_arrow = Arrow(
            np.array([-5, hidden_layer_height, 0]),
            np.array([-3, hidden_layer_height, 0]),
            buff=0,
            stroke_width=2,
        )
        VMobject.scale(hidden_arrow, arrows_scale)
        hidden_text = (
            Text("Hidden Layers")
            .scale(0.35)
            .shift(UP * hidden_layer_height)
            .align_to(input_text, RIGHT)
        )
        hidden_exp_text = (
            Text("LSTM cells")
            .scale(0.35)
            .shift(UP * hidden_layer_height)
            .align_to(input_exp_text, LEFT)
        )
        hidden_exp_text_2 = (
            Text("Stable memory &\n error recovery")
            .scale(0.35)
            .shift(UP * hidden_layer_height)
            .shift(5 * RIGHT)
        )
        hidden_arrow_2 = Arrow(
            np.array([2, hidden_layer_height, 0]),
            np.array([4, hidden_layer_height, 0]),
            buff=0,
            stroke_width=2,
        )
        VMobject.scale(hidden_arrow_2, arrows_scale)

        output_arrow = Arrow(
            np.array([-5, output_layer_height, 0]),
            np.array([-3, output_layer_height, 0]),
            buff=0,
            stroke_width=2,
        )
        VMobject.scale(output_arrow, arrows_scale)
        output_text = (
            Text("Output Layer")
            .scale(0.35)
            .shift(UP * output_layer_height)
            .align_to(input_text, RIGHT)
        )
        output_exp_text = (
            Text("Distribution of future inputs")
            .scale(0.35)
            .shift(UP * output_layer_height)
            .align_to(input_exp_text, LEFT)
        )

        arrows = VGroup(input_arrow, hidden_arrow, output_arrow)

        text = VGroup(input_text, hidden_text, output_text)

        exp_text = VGroup(input_exp_text, output_exp_text)

        shift_horiz_tex = 0.5
        big_hidden_exp_text = Text("LSTM cells").scale(0.8).shift(UP * 3)
        lstm_cell_img = ImageMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/lstm_cell_transparent.png"
        )
        lstm_cell_img.scale(0.7).set_color(WHITE)

        input_gate_tex = (
            MathTex(
                r"i_t =",
                r"\sigma",
                r"(",
                r"W_{xi}",
                r"x_t",
                r"+",
                r"W_{hi}",
                r"h_{t-1}",
                r"+",
                r"W_{ci}",
                r"c_{t-1}",
                r"+",
                r"b_i",
                r")",
            )
            .scale(latex_text_scale)
            .shift(RIGHT * left_horizontal_latex_pos)
        )
        function_gate_tex = (
            MathTex(
                r"f_t =",
                r"\sigma",
                r"(",
                r"W_{xf}",
                r"x_t",
                r"+",
                r"W_{hf}",
                r"h_{t-1}",
                r"+",
                r"W_{cf}",
                r"c_{t-1}",
                r"+",
                r"b_f",
                r")",
            )
            .scale(latex_text_scale)
            .align_to(input_gate_tex, LEFT)
            .shift(DOWN * shift_horiz_tex)
        )
        output_gate_tex = (
            MathTex(
                r"o_t =",
                r"\sigma",
                r"(",
                r"W_{xo}",
                r"x_t",
                r"+",
                r"W_{ho}",
                r"h_{t-1}",
                r"+",
                r"W_{co}",
                r"c_{t}",
                r"+",
                r"b_o",
                r")",
            )
            .scale(latex_text_scale)
            .align_to(input_gate_tex, LEFT)
            .shift(DOWN * shift_horiz_tex * 2)
        )
        cell_gate_tex = (
            MathTex(
                r"c_t = f_{t}c_{t-1} + ",
                r"i_t",
                r"tanh",
                r"(",
                r"W_{xc}",
                r"x_t",
                r"+",
                r"W_{hc}",
                r"h_{t-1}",
                r"+",
                r"b_c",
                r")",
            )
            .scale(latex_text_scale)
            .align_to(input_gate_tex, LEFT)
            .shift(DOWN * shift_horiz_tex * 3)
        )
        hidden_gate_tex = (
            MathTex(r"h_t = o_{t}", r"tanh", r"(c_t)")
            .scale(latex_text_scale)
            .align_to(input_gate_tex, LEFT)
            .shift(DOWN * shift_horiz_tex * 4)
        )

        framebox_sigma_i = SurroundingRectangle(
            input_gate_tex[1], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_weight_i_1 = SurroundingRectangle(
            input_gate_tex[3], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_weight_i_2 = SurroundingRectangle(
            input_gate_tex[6], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_weight_i_3 = SurroundingRectangle(
            input_gate_tex[9], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_input_i_1 = SurroundingRectangle(
            input_gate_tex[4], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_input_i_2 = SurroundingRectangle(
            input_gate_tex[7], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_input_i_3 = SurroundingRectangle(
            input_gate_tex[10], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_bias_i = SurroundingRectangle(
            input_gate_tex[-2], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )

        framebox_sigma_f = SurroundingRectangle(
            function_gate_tex[1],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )
        framebox_weight_f_1 = SurroundingRectangle(
            function_gate_tex[3],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )
        framebox_weight_f_2 = SurroundingRectangle(
            function_gate_tex[6],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )
        framebox_weight_f_3 = SurroundingRectangle(
            function_gate_tex[9],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )
        framebox_input_f_1 = SurroundingRectangle(
            function_gate_tex[4],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )
        framebox_input_f_2 = SurroundingRectangle(
            function_gate_tex[7],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )
        framebox_input_f_3 = SurroundingRectangle(
            function_gate_tex[10],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )
        framebox_bias_f = SurroundingRectangle(
            function_gate_tex[-2],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )

        framebox_sigma_o = SurroundingRectangle(
            output_gate_tex[1], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_weight_o_1 = SurroundingRectangle(
            output_gate_tex[3], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_weight_o_2 = SurroundingRectangle(
            output_gate_tex[6], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_weight_o_3 = SurroundingRectangle(
            output_gate_tex[9], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_input_o_1 = SurroundingRectangle(
            output_gate_tex[4], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_input_o_2 = SurroundingRectangle(
            output_gate_tex[7], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_input_o_3 = SurroundingRectangle(
            output_gate_tex[10],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )
        framebox_bias_o = SurroundingRectangle(
            output_gate_tex[-2],
            buff=surr_rect_buff,
            stroke_width=surr_rect_stroke_width,
        )

        framebox_sigma_c = SurroundingRectangle(
            cell_gate_tex[2], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_weight_c_1 = SurroundingRectangle(
            cell_gate_tex[4], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_weight_c_2 = SurroundingRectangle(
            cell_gate_tex[7], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_input_c_1 = SurroundingRectangle(
            cell_gate_tex[5], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_input_c_2 = SurroundingRectangle(
            cell_gate_tex[8], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )
        framebox_bias_c = SurroundingRectangle(
            cell_gate_tex[-2], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )

        framebox_sigma_h = SurroundingRectangle(
            hidden_gate_tex[1], buff=surr_rect_buff, stroke_width=surr_rect_stroke_width
        )

        math_text = VGroup(
            input_gate_tex,
            function_gate_tex,
            output_gate_tex,
            cell_gate_tex,
            hidden_gate_tex,
        )

        framebox_first_f = VGroup(
            framebox_sigma_i,
            framebox_sigma_f,
            framebox_sigma_o,
            framebox_sigma_c,
            framebox_sigma_h,
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

        code_scale = 0.41
        code_ex_text = (
            Text("Example for output gate during forward pass:")
            .scale(0.4)
            .shift(2 * UP)
            .shift(3.7 * RIGHT)
        )
        code_out_gate = Code(
            code="// output gate\n"
            + "// extra input from peephole (from current state)\n"
            + "#ifdef PEEPS\n"
            + "dot(stateBegin + cellStart, stateBegin + cellEnd, peepWtIt, inActIt,inActIt + 1);\n"
            + "peepWtIt += cellsPerBlock;\n"
            + "#endif\n"
            + "real_t outGateAct = G::fn(*inActIt);\n"
            + "outGateActBegin[b] = outGateAct;\n"
            + "++inActIt;\n\n"
            + "// output activations\n"
            + "transform(preOutGateActBegin + cellStart, preOutGateActBegin + cellEnd,\n"
            + "actBegin + cellStart,\n"
            + "bind2nd(multiplies<real_t>(), outGateAct));\n"
            + "cellStart = cellEnd;\n"
            + "cellEnd += cellsPerBlock;\n"
            + "fgActBegin = fgActEnd;\n"
            + "fgActEnd += this->num_seq_dims();\n",
            language="cpp",
            line_no_from=177,
            style="monokai",
        )

        code_out_gate.scale(code_scale).align_to(code_ex_text, LEFT)
        code_source = Text(
            "Code directly from source at:\nhttps://github.com/szcom/rnnlib/blob/master/src/LstmLayer.hpp"
        )
        code_source.scale(0.25).align_to(code_ex_text, LEFT).shift(DOWN * 3)

        self.play(FadeIn(input_arrow), FadeIn(input_text))
        self.play(FadeIn(hidden_arrow), FadeIn(hidden_text))
        self.play(FadeIn(output_arrow), FadeIn(output_text))
        self.wait(20)
        self.play(FadeOut(first_rnn))
        self.play(arrows.animate.shift(RIGHT * 3.5), text.animate.shift(RIGHT * 3))
        self.wait(1)
        self.play(FadeIn(input_exp_text))
        self.wait(3)
        self.play(FadeIn(output_exp_text))
        self.wait(1)
        self.play(FadeIn(hidden_exp_text))
        self.wait(1)
        self.play(FadeIn(hidden_exp_text_2), FadeIn(hidden_arrow_2))

        self.wait(8)
        self.play(
            FadeOut(arrows),
            FadeOut(text),
            FadeOut(exp_text),
            FadeOut(hidden_exp_text_2),
            FadeOut(hidden_arrow_2),
        )
        self.play(Transform(hidden_exp_text, big_hidden_exp_text))
        self.wait(1)
        self.add_sound("trimmed_lstm_cells.wav", gain=4.5)
        self.play(FadeIn(lstm_cell_img))
        self.wait(3)
        self.play(lstm_cell_img.animate.scale(0.6).shift(*[UP * 2, LEFT * 5]))
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
        self.play(
            FadeOut(framebox_bias),
            FadeOut(code_source),
            FadeOut(lstm_cell_img),
            FadeOut(math_text),
            FadeOut(code_ex_text),
            FadeOut(hidden_exp_text),
            FadeOut(code_out_gate),
        )

    def intro(self):
        svg_scale = 0.2
        text_scale = 0.45

        first_handwriting = SVGMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/first_hand_ex.svg"
        )
        first_handwriting.scale(svg_scale).set_color(WHITE)
        first_handwriting.shift(RIGHT * 2)
        first_font_text = Text("He dismissed the idea")
        first_font_text.scale(text_scale).shift(LEFT * 2)
        first_arrow = Arrow(np.array([-0.15, 0, 0]), np.array([0.35, 0, 0]), buff=0)
        self.play(FadeIn(first_handwriting))
        self.wait(2)
        self.play(FadeIn(first_font_text), FadeIn(first_arrow))
        self.wait(3)
        first_rnn = VGroup(first_handwriting, first_font_text, first_arrow)
        self.play(first_rnn.animate.shift(UP))
        self.wait(1.5)

        second_handwriting = SVGMobject(
            "/home/delta/Documents/Università/Machine Learning and Deep Learning/animation/second_hand_ex.svg"
        )
        second_handwriting.scale(svg_scale).align_to(first_font_text, LEFT).set_color(
            WHITE
        )
        second_font_text = Text("... ?")
        second_font_text.scale(text_scale).shift(RIGHT * 2)
        second_arrow = Arrow(np.array([-0.15, 0, 0]), np.array([0.35, 0, 0]), buff=0)
        second_rnn = VGroup(second_handwriting, second_font_text, second_arrow)

        self.wait(1)

        third_font_text = (
            Text("He dismissed the").scale(text_scale).shift(LEFT * 2.3).shift(DOWN)
        )
        fourth_font_text = Text("... ?").scale(text_scale).shift(RIGHT * 2).shift(DOWN)
        third_arrow = Arrow(np.array([-0.15, -1, 0]), np.array([0.35, -1, 0]), buff=0)
        third_rnn = VGroup(third_font_text, fourth_font_text, third_arrow)
        self.play(FadeIn(third_rnn))
        self.wait(2)
        self.play(FadeIn(second_rnn))
        self.wait(6)

        self.play(FadeOut(first_rnn), FadeOut(second_rnn), FadeOut(third_rnn))

        text_lstm = Text(
            "LSTM approach achieves better results than standard RNNs because it retains more information as well as having better possibility of recovering from errors¹"
        )
        text_lstm.scale(text_scale)
        source_lstm = Text(
            "1: S. Hochreiter, Y. Bengio, P. Frasconi, and J. Schmidhuber. Gradient Flow in Recurrent Nets: the Difficulty of Learning Long-term Dependencies. In S. C. Kremer and J. F. Kolen, editors, A Field Guide to Dynamical Recurrent Neural Networks. 2001."
        )
        source_lstm.scale(self.text_source_scale).shift(DOWN * 2.5)
        self.play(Write(text_lstm, run_time=3), FadeIn(source_lstm))
        self.wait(14)
        self.play(FadeOut(text_lstm), FadeOut(source_lstm))

    def create_initial_text(self):
        self.add_sound("trimmed_intro_final3.wav")
        text_polito = Text("Politecnico di Torino - Apr 2021")
        text_polito.scale(self.bottom_text_scale)
        text_polito.shift(*self.bottom_right_moves)
        self.add(text_polito)
        polito_icon = ImageMobject("polito_logo_transparent.png")
        polito_icon.scale(0.15).next_to(text_polito, RIGHT).set_color(WHITE)
        self.add(polito_icon)
        personal_name_text = Text("Gabriele Bruno Franco")
        final_personal_name_text = Text("Gabriele Bruno Franco - s282245")
        final_personal_name_text.scale(self.bottom_text_scale).align_to(
            text_polito, UP
        ).shift(LEFT * 5)
        self.wait(1)

        self.play(Write(personal_name_text))
        self.wait(0.5)
        self.play(Transform(personal_name_text, final_personal_name_text))
        self.wait()

        paper_name_text = Text("Generating Sequences With \nRecurrent Neural Networks")
        author_name_text = Text("Alex Graves")
        author_name_text.move_to(DOWN * 1.4).scale(0.7)

        self.play(Write(paper_name_text), Write(author_name_text))
        self.wait(3)

        final_paper_name_text = Text(
            "  Generating Sequences With Recurrent Neural Networks  "
        )
        final_author_name_text = Text("  Alex Graves  ")
        final_paper_name_text.scale(self.bottom_text_scale).align_to(
            text_polito, UP
        ).shift(LEFT * 1.5)
        final_author_name_text.scale(self.bottom_text_scale).align_to(
            text_polito, UP
        ).shift(RIGHT * 1.5)

        self.play(
            Transform(paper_name_text, final_paper_name_text),
            Transform(author_name_text, final_author_name_text),
        )
