# cuddly-sniffle

## Document Review Platform

This is a Flask application for reviewing and tagging documents based on a YAML input file.

### Setup

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd cuddly-sniffle
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python app.py
    ```

### Usage

- Navigate to `http://127.0.0.1:5000/` to start reviewing documents.

### Data Files

The application uses YAML files to manage input and output data. Below are instructions on how to create and use these files.

#### Input Data File

The input data file, named `data.yaml`, should be structured as follows:

```yaml
---
questions:
  - what is the capital of France
  - what are the names of all the oceans on earth
  - how many people live on Mars
tags:
  - relevant
  - highly-relevant
  - not-relevant
documents:
  - id: <document id>
    content: <document content>
```

Replace `<document id>` with a unique identifier for each document, and `<document content>` with the actual content of the document you wish to review.

#### Output Data File

As you review documents and assign tags, the application will save the results in an output file named `results.yaml`. This file will be created automatically and will contain entries in the following format:

```yaml
- document_id: <document id>
  question: <question text>
  tag: <selected tag>
```

Each entry corresponds to a review decision made in the application.

#### Creating the YAML Files

To create these YAML files, you can use any text editor to write the content following the structure shown above. Save the file with the `.yaml` extension and place it in the root directory of the application.

Once you have created the `data.yaml` file, you can start the application, and it will load the documents for review. After completing the reviews, you can find the results in the `results.yaml` file.

### Technology Stack

- Flask
- Flask TailwindCSS
- PyYAML
