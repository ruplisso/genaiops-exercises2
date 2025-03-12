## GenAIOps workshop - Evaluate and Trace Generative AI application

### Overview

This tutorial provides a step-by-step guide on how to evaluate prompts and models using AI-assisted evaluators (*LLM-as-a-judge*).

### Objective

The main objective of this tutorial is to help users understand the process of evaluating model endpoints using AI as Judge quality evaluators. By the end of this tutorial, you should be able to:

 - Learn about evaluations
 - Evaluate prompt against model endpoint of your choice.
 - Evaluate and compare different models on same dataset and evaluation methods.
 - Instrument your applications to trace GenAI end-to-end workflow

### Samples

1. NLP_Evaluators: Evaluate dataset on traditional ML evaluation methods (F1-score, Rouge, Bleu, etc).
2. Risk_Safety_Evaluators: Evaluate dataset on AI-assisted evaluation methods to assess model ouputs on from a risk and safety perspective.
3. GenAI_Quality_Evaluators (single model): Evaluate model ouputs on a dataset through quality AI-assisted evaluation methods (Coherence, Fluency, Groundedness, Relevance).
4. GenAI_Quality_Evaluators (multi models): Evaluate and compare different models ouputs on a dataset through quality AI-assisted evaluation methods (*Composite* QAEvaluator that contains multiple methods).
5. Tracing: Implement tracing capabilities to capture traces on different steps of a GenAI application.

### Programming Languages
 - Python

### Pre-requisites
 - Rename  ```.sample.env``` file to ```.env``` by filling missing environment varibales (mostly Azure OpenAI connections and Azure AI Foundry Project information).
 - Make sure you have an Azure AI Foundry Hub created and an Azure AI Foundry Project associated.
 - Make sure you have an Azure OpenAI Service resource associated with your Azure AI Foundry Project.
 - If you're willing to make use of the safety evaluations ```02_Risk_Safety_Evalutors```, make sure to have an Azure AI Foundry project resource located in **East US 2**, **Sweden Central**, **France Central** or **Switzerland West** region (only regions where those evaluation methods are in preview at the moment).

### Troubleshoot guidance
 - Ensure that you assign the proper permissions to the storage account linked to your Azure AI Studio hub. This can be done with the following command. More information can be found here.
    - Subscription ID of the Azure AI Studio hub's linked storage account (available in Azure AI hub resource view in Azure Portal).
    - Resource group of the Azure AI Studio hub's linked storage account.
    - User object ID for role assignment (retrieve with "az ad user show" command).
    ```az role assignment create --role "Storage Blob Data Contributor" --scope /subscriptions/<mySubscriptionID>/resourceGroups/<myResourceGroupName> --assignee-principal-type User --assignee-object-id "<user-id>"```