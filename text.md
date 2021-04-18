## Start

Hi, I'm Gabriele Bruno Franco and this video is an explanation of my assigned paper: Generating Sequences With Recurrent Neural Networks by Alex Graves.

## Introduction

This paper's goal was to create a recurrent neural network that is able to generate highly realistic, cursive handwriting in a variety of styles starting from an input text string.
In order to achieve this objective Graves started by creating a different neural network with the goal of predicting text, extended it to predict handwriting and finally adapted this second neural network to the final generative recurrent neural network. These RNNs were created with a Long Short Term Memory approach. This was a deliberate choice that was taken by considering previous work that showed how standard RNNs are unable to store information long enough as well as having very little chance of recovering from past mistakes.

## Prediction Network

This figure shows the text prediction RNN architecture. The circles represent network layers, the solid lines represent weigthed connections and the dashed lines represent predictions.

An input vector sequence x is passed through weighted connections to a stack of N reccurently connected hidden layers, these compute the hidden vector sequences h and then the output vector sequence y. The input vectors are one-hot encoded, each output vector is used to compute a predictive distribution over the possible next inputs.
The layer pass information both vertically and horizontally through the network, these make it easier for the network to recover from errors and to have stable memory.

### Long Short Term Memory

The hidden layers were purpose-built with custom gates that make it possible to store and find long range dependencies in the data.

The memory cell used both the sigmoid and hyperbolic tangent functions in different gates and while the functions can be quiet heavy on the notation they all have a similar concept: each weight is multiplied by their respecitve variable known at step t: the input, the previous hipotesis and the previous state and the bias terms are added at the end.

## Text Prediction

Usually text prediction is performed on words and even though characters-based prediction is  slightly worse than the more common words-based approach, predicting characters is more interesting as it can create entirely new words based on common patterns such as 'wh' and 'th'.

Two different datasets were used to test this network: Penn Treebank and Wikipedia.
Composed by more than one million characters the Penn Treebank dataset is commonly used for language modeling benchmarking but with a vocabulary limited to 10,000 words the RNN easily overfits on the training data. In order to limit the overfitting Graves experimented with two different regularisation techniques: weight noise with a std. deviation of 0.075 and the adaptive weight noise.
The best result, a perplexity of 89.4, was achieved with an ensamble of RNNs, a cache model and a 5-gram based approach.

On the other hand the Wikipedia dataset was created for a challenge proposed in 2006 by Marcus Hutter, Jim Bowery and Matt Mahoney with the goal of compressing the first 100 million bytes of English Wikipedia data as it was at a certain point in time in 2006. This dataset was used because Wikipedia contains a lot regularities such as double squared parenthesis, triple quotes and triple equal signs. In order to close, as an example, double parenthesis the network clearly needs to remember that it's in the "open parenthesis status".
The compression rate wasn't up to par with the state of the art compression algorithms but the results were incouraging and the effect of some niche articles such as one on ballistic missiles was clear as it ifluenced the vocaboulary of the network.

## Handwriting Prediction

## Handwriting Synthesis

## Conclusions