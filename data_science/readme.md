# Data science
A primary intention of [gen_corpora.py](../gen_corpora.py) is to facilitate data science projects using corpora generated from case studies by being able to apply different combinations of paragraph and text modifications.
This `data_science` directory contains such a project, conducted by team member Sebastiaan Booman.
The objective was to evaluate different text modifications on [text classifier Natural Language Processing models](https://monkeylearn.com/blog/text-classification-machine-learning/#:~:text=Text%20classification%20is%20a%20machine,and%20more%20accurately%20than%20humans.) using both models trained from scratch as transfer learning models. Within this directory the the NLP-models' final training statistics can be found as well as the Python code written to transform the corpora and train the respective models.
## Corpora transformation
In order to prepare a text classification dataset for machine learning `transform_doccano_ds.py` has been provided. During the project the [Doccano](https://github.com/doccano/doccano) annotating tool was used to categorize the [dataset](#dataset) on paragraph level. To use `transform_doccano_ds.py` from the CMD two arguments must be provided: input directory and output directory as follows: 
   ```shell
   py transform_doccano_ds.py input_dir output_dir
   ```
## Training from scratch
Training models from scratch was conducted using a custom [Keras sequential model](https://keras.io/guides/sequential_model/). `train_from_scratch.py` provides the Python code of said model and the logic to train models using data with the same format as the output of `transform_doccano_ds.py`.
## Transfer learning
To use transfer learning the Dutch [RoBerta](https://arxiv.org/abs/1907.11692v1) model based on BERT was used. `train_transfer_learning.py` provides the code to train models using data with the same format as the output of `transform_doccano_ds.py`.

**BOTH `transform_doccano_ds.py` and `train_transfer_learning.py` shuffle the datasets and apply K-Fold validation during training**
***

## Data Science Project
### Dataset
The original "baseline" dataset contains an aggregation of 50 case studies written by physiotherapy students and can be found on the project's research drive. The case studies were split on paragraph level. A deeper explanation on the dataset can be found in the research rapport by Sebastiaan Booman.

### Models evaluated
The following 7 text modification combinations have been applied to generate 7 different versions of the corpora.
1. baseline (no text modifications)
2. combo (combination of stop words removal, punctuation removal, lowercase and lemmatization)
3. lemmatization (using spaCy's dutch SM lemmatizer)
4. lowercase
5. punctuation
6. stemming (using Snowball stemmer)
7. stop words (using NLTK default dutch stop words list)
In total 14 models have been trained (each text modification both from scratch and using transfer learning)

### Results
CSV files containing the training statistics of the 14 models can be found in `/statistics` 

### TODO (possible improvements)
- [ ] Create a dataclass for the corpora format which corresponds to output of `transform_doccano_ds.py` and input of `train_from_scratch.py` and `train_transfer_learning.py` 
- [ ] Separate the shuffling and K-Fold validation to different files completely (seperation of concerns)
- [ ] Implement being able to pass arguments through CMD using `train_from_scratch.py` and `train_transfer_learning.py`