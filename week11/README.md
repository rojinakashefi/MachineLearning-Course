# Photo OCR

Photo OCR stands for Photo Optical Character Recognition.

The photo OCR problem focuses on how to get computers to read the text to the purest in images that we take.

First, given the picture it has to look through the image and detect where there is text in the picture.And after it has done that or if it successfully does that it then has to look at these text regions and actually read the text in those regions, and hopefully if it reads it correctly, it'll come up with these transcriptions of what is the text that appears in the image.

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week11/pictures/ocr-pipeline.png)

if you're designing a machine learning system one of the most important decisions will often be what exactly is the pipeline that you want to put together or , how do you  break this problem down into a sequence of different modules.

This problem of finding pedisterian is maybe slightly simpler than text detection just for the reason that the aspect ratio of most pedestrians are pretty similar.So by aspect ratio I mean the ratio between the height and the width of these rectangles.They're all the same. for different pedestrians but for text detection the height and width ratio is different for different lines of text.

## Artificial data synthesis

can we come up with a much larger training set? 

- Generating data from scratch

Modern computers often have a huge font library and if you use a word processing software, depending on what word processor you use, you might have all of these fonts and many, many more Already stored inside. 

So if you want more training examples one thing you can do is just take characters from different fonts and paste these characters against different random backgrounds.

and so by using synthetic data you have essentially an unlimited supply of training examples for artificial training synthesis and so, if you use this source synthetic data, you have essentially unlimited supply of label data to create a improvised learning algorithm for the character recognition problem.So this is an example of artificial data synthesis where youre basically creating new data from scratch.

- Taking an existing example and and introducing distortions that amplify to enlarge the training set

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week11/pictures/disortioun.png)

![](https://github.com/rojinakashefi/MachineLearning-Course/blob/main/week11/pictures/Discussion.png)

## Ceiling analysis

Estimating the errors due to each component.

What part of the pipeline should you spend the most time trying to improve?
