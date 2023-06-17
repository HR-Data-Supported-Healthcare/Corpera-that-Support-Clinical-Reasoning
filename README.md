# Dynamic ETL

Dynamic ETL is a Python class that enables you to perform dynamic Extraction, Transformation, and Loading (ETL) of data from DOCX files. It provides a flexible and customizable approach to process DOCX files according to your specific requirements.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
## Introduction

DynamicETL is a class that allows you to extract data from DOCX files, transform the extracted data based on specified flags, and load the transformed data into a destination file in JSON format. It provides a convenient way to perform ETL operations on DOCX files.

## Installation

To use DynamicETL, follow these steps:

1. Install the required dependencies:
   ```shell
   pip install spacy nltk
   ```

2. Download the required NLTK data by running the following Python code:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('averaged_perceptron_tagger')
   ```

3. Import the necessary modules in your Python script:
   ```python
   from docx import Document
   from data_classes.flag import FlagContainer, TextFlags, ParagraphFlags
   from modifiers.paragraph_modifier import ParagraphModifier
   from modifiers.text_modifier import TextModifier
   from .base_etl_class import BaseETL
   from json import loads
   ```

## Usage

To use DynamicETL, follow these steps:

1. Create a `FlagContainer` object to specify the transformation operations. Set the desired flags for text and paragraph transformations.

2. Instantiate the `DynamicETL` class with the input data directory, destination directory, and the `FlagContainer` object.

3. The `DynamicETL` class will automatically execute the ETL process based on the specified flags.

4. The transformed data will be saved in the destination directory as a JSON file.

Example usage:

```python
flags = FlagContainer()
# Set the desired flags for text and paragraph transformations

data_dir = 'input_data'
dest_dir = 'output_data'

etl = DynamicETL(data_dir, dest_dir, flags)
```

## API Reference

### DynamicETL(data_dir, dest_dir, flags)
The main class for performing dynamic Extraction, Transformation, and Loading (ETL) of data from DOCX files.

#### Parameters:
- `data_dir` (str): The directory containing the input DOCX files.
- `dest_dir` (str): The directory to save the transformed data.
- `flags` (FlagContainer): The flags specifying the transformation operations.

### _execute_etl(data_dir, dest_dir, flags)
Executes the ETL process.

#### Parameters:
- `data_dir` (str): The directory containing the input DOCX files.
- `dest_dir` (str): The directory to save the transformed data.
- `flags` (FlagContainer): The flags specifying the transformation operations.

### _transform(data, flags)
Transforms the extracted data according to the specified flags.

#### Parameters:
- `data` (list[Document]): The extracted data as a list of `Document` objects.
- `flags` (FlagContainer): The flags specifying the transformation operations.

#### Returns:
- dict: The transformed data as a dictionary.

### _load(dest_str, data)
Loads the transformed data to the specified destination.

#### Parameters:
- `dest_str` (str): The destination file path.
- `data`: The transformed data.

### __remove_paragraphs_from_doc(doc_paragraphs, paragraph_flags)
Removes paragraphs from a document based on the specified paragraph flags.

#### Parameters:
-

 `doc_paragraphs`: The paragraphs in the document.
- `paragraph_flags` (ParagraphFlags): The flags specifying the paragraph removal operations.

#### Returns:
- tuple: A tuple containing the remaining paragraphs and the removed paragraphs.

### __transform_paragraphs_from_doc(doc_paragraphs, text_flags)
Transforms the paragraphs from a document based on the specified text flags.

#### Parameters:
- `doc_paragraphs`: The paragraphs in the document.
- `text_flags` (TextFlags): The flags specifying the text transformation operations.

#### Returns:
- list[dict]: The transformed paragraphs as a list of dictionaries.
