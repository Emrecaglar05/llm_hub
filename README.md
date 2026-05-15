# 🚀 My LLM & AI Learning Journey

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-00D9FF?style=for-the-badge&logo=python&logoColor=white)
![LLMs](https://img.shields.io/badge/LLMs-Transformers-00D9FF?style=for-the-badge&logo=huggingface&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-00D9FF?style=for-the-badge)

*Personal repository documenting my journey in mastering Large Language Models, NLP, and AI technologies*

</div>

---

## 📚 Learning Path Overview

This repository contains my hands-on projects and implementations as I progress through advanced LLM and AI concepts. Each module represents a milestone in my data science and artificial intelligence journey.

### 🎯 Learning Objectives
- Master LLM fundamentals and architectures
- Develop expertise in prompt engineering techniques
- Optimize model pipelines for production
- Build RAG (Retrieval-Augmented Generation) systems
- Create advanced LangChain applications

---

## 📂 Repository Structure

```
my-llm-journey/
├── README.md                 # This file
├── .gitignore               # Git ignore rules
│
├── module_1_llm_basics/     # Foundation: LLM Fundamentals
│   ├── turkish_simple.py    # Turkish language model experiments
│   ├── microsoft_phi.py     # Microsoft Phi model implementation
│   ├── qwen_model.py        # Qwen model exploration
│   └── llm_env/            # Virtual environment
│
├── module_2_prompt_engineering/  # Advanced Prompting Techniques
│   ├── README.md
│   ├── requirements.txt
│   ├── 01_zero_shot.py          # Zero-shot learning
│   ├── 02_few_shot.py           # Few-shot learning
│   ├── 03_chain_of_thought.py   # CoT prompting
│   ├── 04_role_based.py         # Role-based prompts
│   ├── 05_chat_api.py           # Chat completion API
│   ├── 06_function_calling.py   # Function calling
│   ├── 07_functional_chatbot.py # Chatbot with functions
│   ├── 08_simple_chatbot.py     # Basic chatbot
│   ├── 09_web_chatbot.py        # Web-based chatbot
│   └── prompt_env/              # Virtual environment
│
├── module_3_pipeline_optimization/  # Performance & Optimization
│   ├── README.md
│   ├── SETUP.md
│   ├── requirements.txt
│   ├── setup.sh                     # Setup script (macOS/Linux)
│   ├── setup.bat                    # Setup script (Windows)
│   ├── 01_autotokenizer_automodel.py
│   ├── 02_model_comparison.py       # GPT vs BERT vs T5
│   ├── 03_cpu_gpu_optimization.py   # Hardware optimization
│   ├── 04_performance_metrics.py    # Benchmarking
│   └── pipeline_env/                # Virtual environment
│
├── module_4_vector_search_rag/      # RAG Systems
│   ├── README.md
│   ├── requirements.txt
│   ├── simple_rag_demo.py
│   ├── chroma_vector_search.py
│   ├── pinecone_integration.py
│   ├── project_notes.md
│   └── diagrams/
│
└── module_5_advanced_langchain/     # Advanced LangChain
    ├── README.md
    ├── requirements.txt
    ├── setup_venv.py
    ├── test_installation.py
    ├── 1_chains_basic.py
    ├── 2_memory_examples.py
    ├── 3_tools_and_agents.py
    ├── 4_real_world_scenarios.py
    ├── 5_streaming_examples.py
    └── project_notes.md
```

---

## 🛠️ Quick Start

### Prerequisites
```bash
Python 3.8+
pip or conda
8GB+ RAM (16GB recommended)
GPU optional (speeds up training/inference)
```

### Installation

**Option 1: Clone Repository**
```bash
git clone https://github.com/Emrecaglar05/my-llm-journey.git
cd my-llm-journey
```

**Option 2: Start with Specific Module**
```bash
cd module_3_pipeline_optimization

# macOS/Linux
chmod +x setup.sh
./setup.sh

# Windows
setup.bat
```

### API Keys Setup
Create a `.env` file in the project root:
```bash
# OpenAI (for Module 2+)
OPENAI_API_KEY=your_openai_key_here

# Hugging Face (for Module 3+)
HUGGINGFACE_TOKEN=your_hf_token_here

# Pinecone (for Module 4)
PINECONE_API_KEY=your_pinecone_key_here
PINECONE_ENV=your_pinecone_environment
```

---

## 📖 Module Details

### 🎯 Module 1: LLM Fundamentals
**Status:** ✅ Completed  
**Focus:** Understanding transformer architectures, tokenization, and basic model usage

**Key Learnings:**
- Transformer architecture fundamentals
- Tokenization methods (BPE, WordPiece)
- Model loading and inference
- Turkish NLP models

### 🎯 Module 2: Prompt Engineering
**Status:** ✅ Completed  
**Focus:** Mastering different prompting techniques and chat APIs

**Key Learnings:**
- Zero-shot and few-shot learning
- Chain-of-thought prompting
- Function calling with OpenAI API
- Building conversational AI systems

### 🎯 Module 3: Pipeline Optimization
**Status:** 🔄 In Progress  
**Focus:** Optimizing model performance and deployment

**Key Learnings:**
- CPU vs GPU optimization techniques
- Model quantization and pruning
- Batch processing strategies
- Performance benchmarking

**System Requirements:**
- **Minimum:** 8 GB RAM, Python 3.8+
- **Recommended:** 16 GB RAM, GPU (CUDA/MPS)
- **Storage:** 10 GB free space for model cache

**Supported Platforms:**
- macOS (Native MPS support for Apple Silicon)
- Linux (CUDA GPU support)
- Windows (CUDA GPU and CPU support)

### 🎯 Module 4: Vector Search & RAG
**Status:** 📅 Planned  
**Focus:** Building retrieval-augmented generation systems

**Planned Topics:**
- Vector embeddings and similarity search
- ChromaDB and Pinecone integration
- Document chunking strategies
- RAG system architecture

### 🎯 Module 5: Advanced LangChain
**Status:** 📅 Planned  
**Focus:** Complex chains, agents, and production systems

**Planned Topics:**
- Advanced chain architectures
- Memory management
- Custom tools and agents
- Streaming responses
- Production deployment

---

## 💡 Personal Notes & Insights

### 🌟 Key Takeaways
- **LLM Selection:** Choose models based on use case, not just size
- **Prompt Engineering:** Precision in prompts = better outputs
- **Optimization:** GPU isn't always necessary; optimize for your hardware
- **RAG Benefits:** Reduces hallucinations, enables real-time knowledge
---

## 🔧 Technical Stack

### Core Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Transformers](https://img.shields.io/badge/🤗%20Transformers-FFD21E?style=flat-square)

### Frameworks & Libraries
- **LLM Frameworks:** LangChain, LlamaIndex
- **Vector DBs:** ChromaDB, Pinecone, FAISS
- **APIs:** OpenAI, Hugging Face, Cohere
- **Tools:** Jupyter, Google Colab, VS Code

---

## 📊 Progress Tracker

| Module | Status | Completion | Projects | Notes |
|--------|--------|-----------|----------|-------|
| Module 1 | ✅ | 100% | 3 | Turkish NLP focus |
| Module 2 | ✅ | 100% | 9 | OpenAI API mastery |
| Module 3 | 🔄 | 60% | 4 | GPU optimization ongoing |
| Module 4 | 📅 | 0% | 0 | Starting soon |
| Module 5 | 📅 | 0% | 0 | Planned for next phase |

---

## 🎯 Goals & Milestones

### Short-term (Next 2 months)
- [ ] Complete Module 3 optimization projects
- [ ] Build first production-ready RAG system
- [ ] Deploy chatbot with vector search
- [ ] Contribute to open-source LLM project

### Long-term (6 months)
- [ ] Master LangChain advanced patterns
- [ ] Build portfolio of 5 LLM applications
- [ ] Write technical blog posts on learnings
- [ ] Participate in AI/ML hackathons

---

## 📝 Project Documentation

Each module contains:
- **README.md:** Module overview and objectives
- **requirements.txt:** Python dependencies
- **project_notes.md:** Personal insights and challenges
- **Code files:** Annotated implementations

---

## 🤝 Connect & Collaborate

I'm always open to discussions about LLMs, AI, and data science!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/emre-%C3%A7a%C4%9Flar-9bb493294/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/Emrecaglar05)
[![Kaggle](https://img.shields.io/badge/Kaggle-Follow-20BEFF?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/emrecaglar05)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:emrecaglar05@gmail.com)

---

## 📜 License

This project is licensed under the MIT License - feel free to use and adapt for your own learning journey.

---

<div align="center">

**🚀 "Learning by doing - one model at a time"**

*Last Updated: May 2026*

![Visitor Count](https://komarev.com/ghpvc/?username=Emrecaglar05&color=00D9FF&style=flat-square)

</div>
