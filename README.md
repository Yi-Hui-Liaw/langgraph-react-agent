## Introduction
A Supplier Researcher Agent is built using Watsonx.ai Agent Lab. This agent will allow you to research the suppliers for procuring Xtralife based on past supplier performance, procurement rules and customer reviews. In addition, the agent can perform web searches using the integrated Google tool within Watsonx.ai Agent Lab. For example, it can answer queries such as "What is the weather today?".

## Prerequisites
* **Python 3.11**
* **[Poetry](https://python-poetry.org/)** package manager (install via [pipx](https://github.com/pypa/pipx))
* IBM Cloud access and permissions

## Installation

To begin working with this template using the Command Line Interface (CLI), please ensure that the IBM watsonx AI CLI tool is installed on your system. You can install or upgrade it using the following command:

1. **Install CLI**:

   ```sh
   pip install -U ibm-watsonx-ai-cli
   ```

2. **Change Directory**:
   ```sh
   cd langgraph-react-agent
   ```

3. **Install Poetry**:

   ```sh
   pipx install --python 3.11 poetry
   ```

4. **Install the template**:

    Running the below commands will install the repository in a separate virtual environment
   
   ```sh
   poetry install
   ```

5. **(Optional) Activate the virtual environment**:

   ```sh
   source $(poetry -q env use 3.11 && poetry env info --path)/bin/activate
   ```

6. **Export PYTHONPATH**:

   Adding working directory to PYTHONPATH is necessary for the next steps.

   ```sh
   export PYTHONPATH=$(pwd):${PYTHONPATH}
   ```

## Configuration

1. Copy `config.toml.example` → `config.toml`.
2. Fill in IBM Cloud credentials:
   watsonx_apikey
   watsonx_url
   space_id
   deployment_id

## Running the application locally
### CLI

```sh
watsonx-ai service invoke --deployment_id "<DEPLOYMENT_ID>" "<PROMPT>"
```

*If `deployment_id` is set in `config.toml`, omit the flag.*

```sh
watsonx-ai service invoke "<PROMPT>"
```

## Running the graphical app locally

You can also run the graphical application locally using the deployed model. All you need to do is deploy the model and follow the steps below. Detailed information for each app is available in its README file.


   ```bash
   cd <app_name>
   cp template.env .env
   ```
   
   ```bash
   watsonx-ai app run
   ```
