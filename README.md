## GenAIOps workshop - Evaluate and Trace Generative AI application

### Overview

This workshop provides step-by-step exercises on how to evaluate prompts and models using AI-assisted evaluators (*LLM-as-a-judge*). Additionally, it goes through the observability implementation with the tracing capability of the Azure AI Foundry.
Ultimately, it deals with agent and agent evaluation.

### Objective

The main objective of this tutorial is to help users understand the process of evaluating model endpoints using AI as Judge quality evaluators both for simple LLM calls but also for agent. By the end of this tutorial, you should be able to:

 - Learn about evaluations
 - Evaluate prompt against model endpoint of your choice.
 - Evaluate and compare different models on same dataset and evaluation methods.
 - Instrument your applications to trace GenAI end-to-end workflow.
 - Create an agent and evaluate its performance.

### Samples

You'll find 7 exercises. Each of them have a completed notebook in the solutions folder. 

1. NLP_Evaluators: Evaluate dataset on traditional ML evaluation methods (F1-score, Rouge, Bleu, etc).
2. Risk_Safety_Evaluators: Evaluate dataset on AI-assisted evaluation methods to assess model ouputs on from a risk and safety perspective.
3. GenAI_Quality_Evaluators (single model): Evaluate model ouputs on a dataset through quality AI-assisted evaluation methods (Coherence, Fluency, Groundedness, Relevance) and create your custom evaluators.
4. GenAI_Quality_Evaluators (multi models): Evaluate and compare different models ouputs on a dataset through quality AI-assisted evaluation methods.
5. Tracing: Implement tracing capabilities to capture traces on different steps of a GenAI application.
6. Agent: Create an agent that is leveraging a function in its toolset and evaluate its performance on Intent resolution, Tool Call Accuracy and Task Adherence.
9. MCP Server: Integrate an Azure AI Projects agent with an external Model Context Protocol (MCP) server, run an agent that uses MCP tools, and handle approval and inspection of tool calls.

### Pre-requisites
 - Rename  ```.sample.env``` file to ```.env``` by filling missing environment variables (mostly Azure OpenAI connections and Azure AI Foundry Project information).
 - Make sure you have created an Azure AI Foundry Project (do not take a Hub based Project).
   https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry&pivots=fdp-project
 - Make sure you have an Azure OpenAI Service resource with the different deployments required in the .env file. 
 - If you're willing to make use of the safety evaluations ```02_Risk_Safety_Evaluators```, make sure to have an Azure AI Foundry project resource located in **East US 2**, **Sweden Central**, **France Central** or **Switzerland West** region (only regions where those evaluation methods are in preview at the moment).

### IDE & Dev Environments
 - Python - Solutions tested with 3.12.11
 - Prefer the use of Visual Studio Code with Jupyter or Polyglot Extension
 https://code.visualstudio.com/
 - Reminder : leverage a virtual environment such as Conda for example or Venv
    - Conda : conda create -n <your-env> python=3.12
 - The requirements for the environment are listed in  ```requirements.txt``` file.
    - pip install -r requirements.txt
 - You will also need the Azure CLI to connect to the Azure subscription. 
 https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&pivots=winget
 or the Azure CLI Developer https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd?tabs=winget-windows%2Cbrew-mac%2Cscript-linux&pivots=os-windows
    - Few commands :
        - Login : az login (CLI) or azd auth login (developer CLI)
        - Get the active tenant : az account show
        - Change the active subscription : az account set --subscription "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" or az account set --subscription "My subscription Name"

        

