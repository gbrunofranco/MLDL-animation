## Start

Hi, I'm Gabriele Bruno Franco and this video is an explanation of my assigned paper: Generating Sequences With Recurrent Neural Networks by Alex Graves.

## Introduction

This paper's goal was to create a recurrent neural network that is able to generate highly realistic, cursive handwriting in a variety of styles starting from an input text string.
In order to achieve this objective Graves started by creating a different neural network with the goal of predicting text, extended it to predicting handwriting and finally adapted this second neural network to the final generative recurrent neural network. These RNNs were created with a Long Short Term Memory approach. This was a deliberate choice that was taken by considering previous work that showed how standard RNNs are unable to store information long enough as well as having very little chance of recovering from past mistakes.

## Prediction Network

This figure shows the text prediction RNN architecture. The circles represent network layers, the solid lines represent weigthed connections and the dashed lines represent predictions.

An input vector sequence x is passed through weighted connections to a stack of N reccurently connected hidden layers, these compute the hidden vector sequences h and then the output vector sequence y. The input vectors are one-hot encoded and each output vector is used to compute a predictive distribution over the possible next inputs.
The hidden layers pass information both vertically and horizontally through the network, these layers make it easier for the network to recover from errors and to have stable memory.

### Long Short Term Memory

The hidden layers were purpose-built with custom gates that make it possible to store and find long range dependencies in the data.

The memory cell used both the sigmoid and hyperbolic tangent functions in different gates and while the functions can be quiet heavy on the notation they all have a similar concept: each weight is multiplied by their respecitve variable known at step t: the input, the previous hipotesis and the previous state and the bias terms are added at the end.

## Text Prediction

Usually text prediction is performed on words and even though characters-based prediction is  slightly worse than the more common words-based approach, predicting characters is more interesting as it can create entirely new words based on common patterns such as 'wh' and 'th'.

Two different datasets were used to test this network: Penn Treebank and Wikipedia.
Composed by more than one million characters the Penn Treebank dataset is commonly used for language modeling benchmarking but with a vocabulary limited to 10,000 words the RNN easily overfits on the training data. In order to limit the overfitting, Graves experimented with two different regularisation techniques: weight noise with a std. deviation of 0.075 and the adaptive weight noise.
The best result, a perplexity of 89.4, was achieved with an ensamble of RNNs, a cache model and a 5-gram based approach.

On the other hand the Wikipedia dataset was created for a challenge proposed in 2006 by Marcus Hutter, Jim Bowery and Matt Mahoney with the goal of compressing the first 100 million bytes of English Wikipedia data as it was at a certain point in time in 2006. This dataset was used because Wikipedia contains a lot regularities such as double squared parenthesis, triple quotes and triple equal signs. In order to close, as an example, double parenthesis the network clearly needs to remember that it's in the "open parenthesis status".
The compression rate wasn't up to par with the state of the art compression algorithms but the results were incouraging and the effect of some niche articles such as one on ballistic missiles was clear as it ifluenced the vocaboulary of the network.

## Handwriting Prediction

Data during the handwriting prediction phase was treated as "online", which in this context means as real-valued x and y coordinates instead of "offline" handwriting which referes to the images being avaiable altogether. This was a deliberate choice due to the low dimensionality of online handwriting, in fact just three dimensions are needed: two real-valued features for each data point and a boolean variable stating if the pen was lifted from the paper or not.

Complex pre-processing and features extraction techniques were avoided in order to steer clear of errors that are bound to happen when processing handwritten text, such as separating a single letter or not separating two different ones. These errors could be propagated through the whole network increasing the prediction and then synthetis error. Furthermore processing handwritten letters usually entails reducing the variation in the data by normalising skew, character size and other features that Graves wanted the network to model.

One of the challenges of predicting handwritten as opossed to digital text is the fuzzy nature of the former, specifically points that are at the end of a letter and at the beginning of another could be part of both, this is the complete opposite of a one-hot encoded vector where each variable has a clearly assigned single value.

### Mixture Density Outputs

In order to handle this characteristic of handwritten text Graves utilized the idea of mixture density networks, the intuition is to parameterise a mixture distribution at each timestep, specifically a mixture of gaussian distributions where each spike, or top part of a gaussian curve, corresponds to a possible upcoming prediction depending on which part of the graph the network sees itself in.

A further challenge of online handwritten text is the fact that the pen could be lifted from the paper, effectively creating a section of space in which the network needs to interpolate between a known point, the last predicted one and an unknown point, the initial dot of the following letter. This problem is also handled by mixture distributions because each gaussian will have a starting point for the letter it represents so, by putting each distribution together, the network can create a section of space in which the first point of the predicted letter is likely to be, regardless of which letter it ends up being.

The model was tested on a custom dataset and the results were quiet incouraging. The network, by predicting text like the one shown in the picture can clearly model strokes and long-range structures. As previously stated the model creates entirely new words due to the characters-based focus since its inception.

## Handwriting Synthesis

Handwriting synthesis refers to the generation of text for a given input string. The previous Recurrent Neural Network is unable to do so as it doesn't account for any digital input text so Graves needed to change the structure of the network to the one shown in the picture.
This model was used instead of a transducer because exploratory work on transducers didn't show encouraging results. 

The input string is passed to the hidden layers through the the window layer, which gives to each previous character an attention level which is a measure of how important a certain section of text input actually is for the prediction as opposed to traditional networks that usually will take into consideration the complete avaiable data.

The results were very good already, as the network was clearly able to synthesise human-like text in a lot of different styles. The author wanted to expand it to both write in a certain hand-picked style and write in a more readable way. 

In order to achieve the former the author changed the sampling technique, instead of sampling randomly from the dataset, more readable text was given priority over unreadable text. The intuition between what is more readable is that what it's more easily predictable by the network also corresponds to what it's more readable by a human. By sampling in this manner the results changed quiet clearly, by increasing the bias even more towards easily readable strings, the synthetised text becomes very akin to a font, with barely no variation in each letter.

On the contrary, the intuition behind being able to select a certain style of writing the author could have simply sampled just the wanted style but this would have reduced the avaiable data by a large margin. The proposed solution is "primed" sampling, the intuition behind it is that we join each string with a character of the wanted style.

Primed and biased sampling can be combined, the result is a more human-readable version of the selected style.

## Conclusions

This paper clearly showed that LSTM-based RNNs are clearly fit for synthetisation of text. A possible way of approaching future work could be to better understand the internal representation of the data in order to better distribute the data and apply a similar technique to extract annotation from text. 