## Start

Hi, I'm Gabriele Bruno Franco and this video is an explanation of my assigned paper: Generating Sequences With Recurrent Neural Networks by Alex Graves.

## Introduction

This paper's goal was to create a recurrent neural network that is able to generate highly realistic, cursive handwriting in a variety of styles starting from an input text string.
In order to achieve this objective Graves started by creating a different neural network with the goal of predicting text, extended it to predict handwriting and finally adapted this second neural network to the final generative recurrent neural network. These RNNs were created with a Long Short Term Memory approach. This was a deliberate choice that was taken by considering previous work that showed how standard RNNs are unable to store information long enough as well as having very little chance of recovering from past mistakes.

## Text Prediction

This figure shows the text prediction RNN architecture. The circles represent network layers, the solid lines represent weigthed connections and the dashed lines represent predictions.

An input vector sequence x is passed through weighted connections to a stack of N reccurently connected hidden layers, these compute the hidden vector sequences h and then the output vector sequence y. Each output vector is used to compute a predictive distributiuon over the possible next inputs.
The layer pass information both vertically and horizontally through the network, these make it easier for the network to recover from errors and to have stable memory.

### Long Short Term Memory

The hidden layers were purpose-built with custom gates that make it possible to store and find long range dependencies in the data.

The memory cell used both the sigmoid and hyperbolic tangent functions in different gates and while the functions can be quiet heavy on the notation they all have a similar concept: each weight is multiplied by their respecitve variable known at step t: the input, the previous hipotesis and the previous state and the bias terms are added at the end.
## Handwriting Prediction

## Handwriting Synthesis

## Conclusions