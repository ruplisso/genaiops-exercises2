# GenAIOps Exercises Repository - Comprehensive Explanation

## 📋 Table of Contents
1. [Overview](#overview)
2. [Repository Purpose](#repository-purpose)
3. [Key Concepts](#key-concepts)
4. [Repository Structure](#repository-structure)
5. [Exercise Modules](#exercise-modules)
6. [Technology Stack](#technology-stack)
7. [Setup and Prerequisites](#setup-and-prerequisites)
8. [Getting Started](#getting-started)
9. [Learning Path](#learning-path)

---

## Overview

This repository contains a **comprehensive workshop on GenAIOps** (Generative AI Operations) focused on **evaluating and tracing Generative AI applications**. It's designed as a hands-on learning resource with step-by-step exercises covering everything from traditional NLP metrics to advanced AI-assisted evaluation methods and agent systems.

### What is GenAIOps?
GenAIOps refers to the operational practices, tools, and methodologies for:
- **Evaluating** AI model outputs for quality, safety, and reliability
- **Tracing** and monitoring AI application workflows
- **Testing** and validating AI agents and their performance
- **Ensuring** responsible AI practices through safety evaluations

---

## Repository Purpose

The main objectives of this repository are to help you:

1. **Understand AI Evaluation Methodologies**
   - Learn different types of evaluators (traditional NLP, AI-assisted, safety)
   - Compare evaluation approaches for various use cases

2. **Implement Quality Assessments**
   - Evaluate prompts against model endpoints
   - Compare different models using standardized datasets
   - Create custom evaluators for specific needs

3. **Master Observability**
   - Instrument applications with tracing capabilities
   - Monitor end-to-end GenAI workflows
   - Use Azure AI Foundry's tracing features

4. **Build and Evaluate Agents**
   - Create AI agents with tool capabilities
   - Evaluate agent performance on specific metrics
   - Integrate with Model Context Protocol (MCP) servers

---

## Key Concepts

### 🎯 LLM-as-a-Judge
A paradigm where large language models are used to evaluate the outputs of other AI models. This approach enables:
- Automated quality assessment at scale
- Nuanced understanding of context and semantics
- Evaluation of subjective qualities like coherence and relevance

### 📊 Evaluation Types

**1. Traditional NLP Evaluators**
- BLEU, GLEU, METEOR, ROUGE scores
- Precision and recall-based metrics
- Primarily for translation and summarization tasks

**2. AI-Assisted Quality Evaluators**
- **Relevance**: How well responses address the query
- **Coherence**: Logical flow and readability
- **Fluency**: Natural language quality
- **Groundedness**: Factual accuracy based on context

**3. Risk & Safety Evaluators**
- Content safety assessment
- Bias detection
- Harmful content identification

**4. Agent-Specific Evaluators**
- Intent resolution accuracy
- Tool call correctness
- Task adherence

### 🔍 Tracing
Capturing detailed execution traces of GenAI applications to:
- Debug complex workflows
- Monitor performance
- Understand decision-making processes
- Track token usage and costs

---

## Repository Structure

```
genaiops-exercises2/
├── .devcontainer/              # Development container configuration
├── .sample.env                 # Template for environment variables
├── requirements.txt            # Python dependencies
├── README.md                   # Main documentation
│
├── 01_NLP_Evaluators/         # Traditional NLP metrics
│   ├── NLP_Evaluators.ipynb
│   └── data.jsonl
│
├── 02_Risk_Safety_Evaluators/  # Safety & risk assessments
│   └── Risks_Safety_metrics.ipynb
│
├── 03_GenAI_Quality_Evaluators (single model)/  # Quality metrics for one model
│   ├── AI_Assisted_Quality_Evaluators.ipynb
│   ├── evaluation_dataset.jsonl
│   ├── helpfulness.prompty      # Custom evaluator template
│   ├── helpfulness.py
│   └── model_endpoint.py
│
├── 04_GenAI_Quality_Evaluators (multi models)/  # Comparing multiple models
│   ├── AI_Assisted_Quality_Evaluators_Multi_Models.ipynb
│   ├── evaluation_dataset.jsonl
│   └── model_endpoints.py
│
├── 05_Tracing/                # Observability & tracing
│   ├── AI_Model_Tracing.ipynb
│   └── README.md
│
├── 06_Agent_Evaluation/       # Agent creation & evaluation
│   └── Agent_evaluation.ipynb
│
├── 09_MCP_Server/             # Model Context Protocol integration
│   └── MPC_Server_foundry_integration.ipynb  # Note: filename has typo (MPC vs MCP)
│
└── solutions/                  # Completed notebooks for reference
    ├── 01_NLP_Evaluators/
    ├── 02_Risk_Safety_Evaluators/
    ├── 03_GenAI_Quality_Evaluators (single model)/
    ├── 04_GenAI_Quality_Evaluators (multi models)/
    ├── 05_Tracing/
    ├── 06_Agents_Evaluator/
    ├── 07_Simulator/
    ├── 08_AI_Red_Teaming/
    └── 09_MCP_Server/
```

---

## Exercise Modules

### 🔢 Exercise 1: NLP Evaluators
**File**: `01_NLP_Evaluators/NLP_Evaluators.ipynb`

**What you'll learn**:
- Traditional NLP evaluation metrics (BLEU, GLEU, METEOR, ROUGE)
- When to use precision vs. recall-based metrics
- Limitations of traditional metrics for GenAI applications

**Key Metrics**:
- **BLEU**: Machine translation, precision-focused
- **GLEU**: Grammar correction, balanced precision/recall
- **METEOR**: Semantic similarity with synonym support
- **ROUGE**: Text summarization, recall-focused

**Use Case**: Understanding foundational evaluation concepts before moving to AI-assisted methods.

---

### 🛡️ Exercise 2: Risk & Safety Evaluators
**File**: `02_Risk_Safety_Evaluators/Risks_Safety_metrics.ipynb`

**What you'll learn**:
- Evaluating AI outputs for safety concerns
- Detecting potentially harmful content
- Implementing responsible AI practices

**Requirements**: 
- Azure AI Foundry project in **East US 2**, **Sweden Central**, **France Central**, or **Switzerland West** (preview regions)

**Use Case**: Ensuring AI applications meet safety and compliance standards.

---

### ✨ Exercise 3: GenAI Quality Evaluators (Single Model)
**File**: `03_GenAI_Quality_Evaluators (single model)/AI_Assisted_Quality_Evaluators.ipynb`

**What you'll learn**:
- AI-assisted evaluation with "LLM-as-a-judge"
- Built-in quality evaluators (Relevance, Coherence, Fluency, Groundedness)
- Creating custom evaluators with `.prompty` templates

**Key Features**:
- **RelevanceEvaluator**: Measures how well responses address queries (1-5 scale)
- **CoherenceEvaluator**: Assesses readability and natural flow
- **FluencyEvaluator**: Evaluates language quality
- **GroundednessEvaluator**: Checks factual accuracy against context
- **Custom Evaluators**: Build domain-specific evaluation criteria

**Use Case**: Comprehensive quality assessment of a single model's outputs.

---

### 🔄 Exercise 4: GenAI Quality Evaluators (Multi Models)
**File**: `04_GenAI_Quality_Evaluators (multi models)/AI_Assisted_Quality_Evaluators_Multi_Models.ipynb`

**What you'll learn**:
- Comparing multiple models side-by-side
- Standardized evaluation across different endpoints
- Model selection based on quality metrics

**Use Case**: A/B testing different models (e.g., GPT-4o vs GPT-4o-mini) to choose the best for your use case.

---

### 🔎 Exercise 5: Tracing
**File**: `05_Tracing/AI_Model_Tracing.ipynb`

**What you'll learn**:
- Instrumenting GenAI applications with OpenTelemetry
- Capturing traces in Azure AI Foundry
- Monitoring multi-step AI workflows
- Analyzing performance and debugging

**Key Concepts**:
- Trace spans for different operations
- Integration with Azure Monitor Application Insights
- End-to-end visibility into AI application behavior

**Use Case**: Production monitoring and debugging of complex AI systems.

---

### 🤖 Exercise 6: Agent Evaluation
**File**: `06_Agent_Evaluation/Agent_evaluation.ipynb`

**What you'll learn**:
- Building AI agents with function calling capabilities
- Agent-specific evaluation metrics
- Tool integration and validation

**Evaluation Metrics**:
- **Intent Resolution**: Did the agent understand the user's goal?
- **Tool Call Accuracy**: Were the correct tools called with proper parameters?
- **Task Adherence**: Did the agent complete the requested task?

**Use Case**: Validating autonomous AI agents that use tools and APIs.

---

### 🔌 Exercise 9: MCP Server Integration
**File**: `09_MCP_Server/MPC_Server_foundry_integration.ipynb`
*Note: The notebook filename contains a typo (MPC instead of MCP)*

**What you'll learn**:
- Integrating Azure AI Projects agents with Model Context Protocol (MCP)
- Using external MCP servers for tool capabilities
- Handling tool call approval and inspection

**Key Concepts**:
- MCP (Model Context Protocol) for standardized tool integration
- External tool server connectivity
- Security and approval workflows for tool usage

**Use Case**: Extending agents with external capabilities through standardized protocols.

---

## Technology Stack

### Core Technologies
- **Python 3.12.11**: Primary programming language
- **Azure AI Foundry**: Cloud platform for AI evaluation and tracing
- **Azure OpenAI Service**: Access to GPT models
- **Jupyter Notebooks**: Interactive development environment

### Key Python Libraries
```
openai==1.99.0                          # OpenAI API client
azure-ai-evaluation==1.10.0             # Azure AI evaluation framework
azure-ai-projects==1.1.0b3              # Azure AI project management
azure-ai-inference[opentelemetry]==1.0.0b9  # Model inference with tracing
azure-monitor-opentelemetry==1.6.13     # Monitoring and observability
azure-identity==1.21.0                  # Azure authentication
promptflow==1.18.0                      # Prompt engineering workflows
pandas==2.2.3                           # Data manipulation
python-dotenv==1.0.0                    # Environment variable management
```

### Azure Services Required
1. **Azure AI Foundry Project** (FDP-based, not Hub-based)
2. **Azure OpenAI Service** with model deployments:
   - GPT-4o or GPT-4.1
   - GPT-4o-mini or GPT-4.1-mini
3. **Azure Monitor Application Insights** (for tracing)
4. **Azure CLI** or **Azure Developer CLI**

### External Services
- **Weather API** (optional, for agent examples): Free API key from weatherapi.com

---

## Setup and Prerequisites

### 1. Azure Resources Setup

**a) Create Azure AI Foundry Project**
- Must be a **FDP-based project** (not Hub-based)
- Follow: [Create Projects Guide](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/create-projects?tabs=ai-foundry&pivots=fdp-project)

**b) Deploy Azure OpenAI Models**
- Create an Azure OpenAI resource
- Deploy the following models:
  - `gpt-4o` or `gpt-4.1`
  - `gpt-4o-mini` or `gpt-4.1-mini`

**c) Regional Considerations**
- For Exercise 2 (Safety Evaluators), your Azure AI Foundry project must be in:
  - East US 2
  - Sweden Central
  - France Central
  - Switzerland West

### 2. Development Environment

**Install Python 3.12.11**
```bash
# Using Conda (recommended)
conda create -n genaiops python=3.12
conda activate genaiops

# OR using venv
python3.12 -m venv genaiops-env
source genaiops-env/bin/activate  # On Windows: genaiops-env\Scripts\activate
```

**Install Dependencies**
```bash
pip install -r requirements.txt
```

**Install Azure CLI**
- Windows: [Install Guide](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows)
- macOS/Linux: [Install Guide](https://learn.microsoft.com/en-us/azure/developer/azure-developer-cli/install-azd)

### 3. Configuration

**Create `.env` file from template**
```bash
cp .sample.env .env
```

**Fill in the environment variables**:
```bash
# Azure AI Project
AI_PROJECT_ENDPOINT=https://<your-ai-services>.services.ai.azure.com/api/projects/<project-name>

# Azure OpenAI Connection
AZURE_OPENAI_ENDPOINT=https://<aoai-resource>.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_API_KEY=<your-api-key>
AZURE_OPENAI_API_VERSION=2024-10-21
AZURE_OPENAI_GPT4O_DEPLOYMENT=gpt-4o
AZURE_OPENAI_GPT4O_MINI_DEPLOYMENT=gpt-4o-mini

# Multi-model endpoints
AOAI_GPT4O_ENDPOINT=https://<resource>.openai.azure.com/openai/deployments/<deployment>/chat/completions?api-version=2024-10-21
AOAI_GPT4O_MINI_ENDPOINT=https://<resource>.openai.azure.com/openai/deployments/<deployment>/chat/completions?api-version=2024-10-21

# Azure AI Inference
AZURE_AI_CHAT_ENDPOINT=https://<AIservices>.services.ai.azure.com/openai/deployments/<deployment>
AZURE_AI_CHAT_KEY=<your-key>

# Tracing
APP_INSIGHTS_CONNECTION_STRING=InstrumentationKey=<key>;IngestionEndpoint=https://<region>.in.applicationinsights.azure.com/...

# Optional
WEATHER_API_KEY=<get-from-weatherapi.com>
```

### 4. Azure Authentication
```bash
# Login to Azure
az login

# Verify subscription
az account show

# Change subscription if needed
az account set --subscription "<subscription-id-or-name>"
```

### 5. IDE Setup
**Recommended**: Visual Studio Code with extensions:
- Jupyter (for notebooks)
- Python
- Polyglot Notebooks (alternative)

---

## Getting Started

### Quick Start Steps

1. **Clone and Setup**
   ```bash
   git clone https://github.com/ruplisso/genaiops-exercises2.git
   cd genaiops-exercises2
   ```

2. **Create Virtual Environment**
   ```bash
   conda create -n genaiops python=3.12
   conda activate genaiops
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   cp .sample.env .env
   # Edit .env with your Azure credentials
   ```

5. **Authenticate with Azure**
   ```bash
   az login
   ```

6. **Open First Exercise**
   ```bash
   # Open VS Code
   code .
   # Navigate to 01_NLP_Evaluators/NLP_Evaluators.ipynb
   ```

### Verification Checklist
- [ ] Python 3.12 installed
- [ ] Virtual environment activated
- [ ] All dependencies installed (`pip list`)
- [ ] `.env` file configured with Azure credentials
- [ ] Azure CLI authenticated (`az account show`)
- [ ] Azure AI Foundry project created
- [ ] Azure OpenAI models deployed
- [ ] Jupyter/VS Code can run notebooks

---

## Learning Path

### Recommended Order

**Beginner Path** (Start here if new to AI evaluation):
1. **Exercise 1**: NLP Evaluators → Understand basic metrics
2. **Exercise 3**: GenAI Quality (Single) → Learn AI-assisted evaluation
3. **Exercise 5**: Tracing → Add observability
4. **Exercise 6**: Agent Evaluation → Build autonomous agents

**Comparison Path** (If comparing models):
1. **Exercise 3**: GenAI Quality (Single) → Baseline with one model
2. **Exercise 4**: GenAI Quality (Multi) → Compare multiple models
3. **Exercise 5**: Tracing → Monitor production performance

**Safety-Focused Path**:
1. **Exercise 2**: Risk & Safety → Learn safety evaluation
2. **Exercise 3**: GenAI Quality (Single) → Combine with quality metrics
3. **Solutions/08_AI_Red_Teaming** → Advanced adversarial testing

**Advanced Path**:
1. **Exercise 6**: Agent Evaluation → Build agents
2. **Exercise 9**: MCP Server → External tool integration
3. **Solutions/07_Simulator** → Synthetic data generation
4. **Solutions/08_AI_Red_Teaming** → Security testing

### Time Estimates
- Each exercise: 1-2 hours
- Complete workshop: 8-12 hours
- With deep dive into solutions: 15-20 hours

---

## Additional Resources

### Solutions Folder
The `solutions/` directory contains completed notebooks for all exercises, including additional advanced topics:
- **07_Simulator**: Synthetic conversation generation
- **08_AI_Red_Teaming**: Adversarial testing and security evaluation

These are great for:
- Checking your work
- Understanding complex implementations
- Exploring advanced topics beyond the main exercises

### Microsoft Documentation
- [Azure AI Foundry Evaluation Concepts](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/)
- [Textual Similarity Evaluators](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/textual-similarity-evaluators)
- [RAG Evaluators](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/rag-evaluators)
- [Custom Evaluators](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/custom-evaluators)

### Key Takeaways

After completing this workshop, you will:
- ✅ Understand multiple evaluation paradigms for GenAI
- ✅ Implement quality, safety, and performance evaluations
- ✅ Compare and select models based on data-driven metrics
- ✅ Instrument applications with comprehensive tracing
- ✅ Build and evaluate autonomous AI agents
- ✅ Integrate external tools via MCP protocol
- ✅ Apply responsible AI practices in production systems

---

## Repository Maintenance

- **Primary Language**: Python
- **Notebook Format**: Jupyter (.ipynb)
- **Configuration**: Environment variables via `.env`
- **Dependencies**: Managed via `requirements.txt`
- **Solutions**: Complete implementations in `solutions/` folder

---

## Summary

This repository is a **comprehensive, hands-on learning resource** for anyone working with Generative AI applications in production. It covers the complete lifecycle from evaluation methodologies (traditional and AI-assisted) to observability (tracing) and advanced agent systems (with tool use and MCP integration).

The workshop is structured to be:
- **Progressive**: Start simple, build to complex
- **Practical**: Every exercise is hands-on with real Azure services
- **Complete**: Includes solutions for self-verification
- **Production-Ready**: Focuses on real-world operational concerns

Whether you're a data scientist evaluating models, an ML engineer building production systems, or a developer integrating AI capabilities, this workshop provides the essential knowledge and practical skills for successful GenAIOps implementation.
