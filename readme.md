# GovInfra AI

**AI-Powered Infrastructure Project Submission & Compliance Assistant**

GovInfra AI is an AI-powered platform designed to assist government employees in preparing and submitting infrastructure development projects.

The system helps users understand applicable **regulations, SOPs, technical requirements, required documents, and approval procedures** by combining traditional text search, semantic search, Retrieval-Augmented Generation (RAG), document analysis, and Agentic AI.

The initial use case focuses on **government infrastructure projects**, such as road and bridge construction.

---

## 1. Problem Statement

Government infrastructure project submissions often require employees to understand and comply with a large number of:

* Regulations
* Ministerial regulations
* SOPs
* Technical guidelines
* Construction standards
* Administrative requirements
* Environmental requirements
* Supporting documents
* Approval procedures

These requirements may be distributed across many documents and different sources.

As a result, project applicants may face difficulties answering questions such as:

> "What documents do I need to submit for a road construction project?"

> "Which regulations apply to my project?"

> "What technical requirements must be fulfilled?"

> "Which documents are still missing from my submission?"

> "What is the next approval step?"

GovInfra AI aims to simplify this process by providing an intelligent assistant that can retrieve and explain relevant information from official government documents.

---

# 2. Project Objectives

The main objectives of GovInfra AI are:

1. Provide **semantic search** across government regulations and technical documents.
2. Provide **traditional text search** and autocomplete.
3. Combine both approaches through **hybrid search**.
4. Implement **Retrieval-Augmented Generation (RAG)** for question answering.
5. Provide answers with **document and page-level sources**.
6. Analyze uploaded project documents.
7. Identify missing or incomplete submission requirements.
8. Provide an explanation and legal/technical basis for each requirement.
9. Eventually introduce **Agentic RAG** to orchestrate multiple tools and data sources.

---

# 3. Example Use Case

A government employee wants to propose:

> **Construction of a 10 km district road.**

The employee enters:

```text
Project Type: Road Construction
Location: Kabupaten X
Length: 10 km
Estimated Budget: Rp 50 Billion
```

GovInfra AI analyzes the project and retrieves applicable requirements.

Example:

```text
Required Documents
────────────────────────────────────

✅ Project Proposal
✅ Technical Design / DED
✅ Cost Estimate / RAB
✅ Feasibility Study
❌ Land Acquisition Document
❌ Environmental Document
⚠️ Traffic Data – Needs Review
```

The system also provides the source of each requirement:

```text
Requirement:
Feasibility Study

Status:
Completed

Source:
Pedoman Studi Kelayakan Proyek Jalan

Reference:
Chapter III
Page 42
```

---

# 4. Core Features

## 4.1 Government Document Knowledge Base

The system will ingest official documents such as:

* Regulations
* Ministerial regulations
* SOPs
* Technical guidelines
* Construction standards
* Circular letters
* Manuals
* FAQs
* Other official publications

Initial documents will focus on road and bridge infrastructure.

---

## 4.2 Document Processing Pipeline

Government documents will be processed through the following pipeline:

```text
PDF / DOCX
    ↓
Document Extraction
    ↓
Text Cleaning
    ↓
Structure Detection
    ↓
Chunking
    ↓
Metadata Extraction
    ↓
Embedding Generation
    ↓
Vector Database
```

Important metadata will be preserved:

```text
document_id
title
document_type
publisher
year
status
chapter
section
page
source_url
```

This metadata will later support filtering, citations, and explainability.

---

# 5. Search Architecture

GovInfra AI will support three search approaches.

## 5.1 Text Search

Traditional keyword-based search will be used for:

* Exact terms
* Keyword matching
* Fuzzy search
* Autocomplete
* Filtering

Technology:

```text
Elasticsearch
```

Example:

```text
"Permen PUPR 5 2023"
```

---

## 5.2 Semantic Search

Semantic search retrieves documents based on meaning rather than exact keywords.

Example:

```text
User:
"Dokumen apa yang diperlukan untuk membangun jalan?"

```

The system can retrieve content containing:

```text
"Persyaratan pengajuan pembangunan jalan..."
```

even if the exact wording is different.

Technology:

```text
BGE-M3
   ↓
Qdrant
```

---

## 5.3 Hybrid Search

Text search and semantic search will be combined.

```text
                   User Query
                       │
              ┌────────┴────────┐
              ↓                 ↓
        Text Search       Semantic Search
        Elasticsearch         Qdrant
              │                 │
              └────────┬────────┘
                       ↓
                 Hybrid Ranking
                       ↓
                    Top-K
```

Hybrid search is expected to provide better retrieval quality than relying on only one retrieval method.

---

# 6. Embedding & Vector Database

The initial embedding model will be:

```text
BAAI/bge-m3
```

BGE-M3 converts text into numerical vectors.

Example:

```text
"Persyaratan teknis pembangunan jalan"
                ↓
             BGE-M3
                ↓
[0.12, -0.42, 0.81, ...]
```

The resulting vectors will be stored in:

```text
Qdrant
```

Each vector will be associated with metadata:

```json
{
  "document_id": "PERMEN-PUPR-5-2023",
  "title": "Persyaratan Teknis Jalan",
  "chapter": "BAB III",
  "section": "Persyaratan Teknis",
  "page": 24
}
```

---

# 7. Retrieval-Augmented Generation (RAG)

After implementing search, GovInfra AI will use retrieved documents as context for an LLM.

```text
User Question
      ↓
Query Processing
      ↓
Hybrid Search
      ↓
Top-K Relevant Chunks
      ↓
Context Construction
      ↓
LLM
      ↓
Answer
```

The LLM should answer based on retrieved official documents rather than relying only on its internal knowledge.

Example:

```text
User:
Apa saja persyaratan pengajuan pembangunan jalan?

AI:
Berdasarkan dokumen yang tersedia, terdapat beberapa
persyaratan utama:

1. Proposal proyek
2. Studi kelayakan
3. Rencana teknis
4. RAB
5. Dokumen lingkungan

Sources:
- Permen PUPR No. 5 Tahun 2023, Page 24
- SOP Prosedur Pembangunan Jalan, Page 12
```

---

# 8. Document Compliance

One of the main features of GovInfra AI is document compliance checking.

The system compares:

```text
Required Documents
        VS
Uploaded Documents
```

Example:

```text
Required Requirement
        ↓
"Feasibility Study"
        ↓
Search Uploaded Documents
        ↓
Semantic Matching
        ↓
Result
```

Possible statuses:

```text
COMPLETED
MISSING
NEEDS_REVIEW
```

Example:

```text
Requirement                     Status
------------------------------------------------
Project Proposal                 ✅ COMPLETED
Technical Design                 ✅ COMPLETED
Feasibility Study                ✅ COMPLETED
Land Acquisition Document        ❌ MISSING
Environmental Document           ⚠️ NEEDS_REVIEW
```

---

# 9. Explainability & Sources

GovInfra AI should not simply generate an answer.

Every important requirement should have a traceable source.

Example:

```text
Requirement:
Feasibility Study

Basis:
Pedoman Studi Kelayakan Proyek Jalan

Chapter:
III

Page:
42

Source:
Official Government Document
```

This is particularly important because the system deals with regulations and government procedures.

The system should distinguish between:

```text
Source-backed information
        VS
AI-generated interpretation
```

---

# 10. Agentic RAG

After the basic RAG system is stable, GovInfra AI will be extended into an Agentic RAG architecture.

The AI Agent will be able to decide which tools are required to answer a question.

Example:

```text
                    AI Agent
                       │
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
 Regulation       Project Data    Document
   Search            Query         Analysis
        │              │              │
    Qdrant          SQL Server       Qdrant
        │              │              │
        └──────────────┼──────────────┘
                       ↓
                      LLM
                       ↓
                  Final Answer
```

Potential tools:

```text
search_regulations()
search_sop()
search_technical_guidelines()
get_project()
get_requirements()
check_uploaded_documents()
```

This will allow the system to move from simple RAG to **tool-based Agentic RAG**.

---

# 11. Technology Stack

## Backend

```text
Python
FastAPI
```

The existing backend experience with .NET can also be integrated later through service-to-service communication.

---

## AI / RAG

```text
LangChain
BGE-M3
LLM
```

LangChain will primarily be introduced after the underlying RAG pipeline is understood and working independently.

---

## Search

```text
Elasticsearch
```

Used for:

```text
- Full-text search
- BM25
- Fuzzy search
- Autocomplete
- Filtering
```

---

## Vector Database

```text
Qdrant
```

Used for:

```text
- Vector storage
- Similarity search
- Semantic retrieval
- Metadata filtering
```

---

## Database

```text
SQL Server
```

Used for structured business data such as:

```text
Projects
Project Types
Requirements
Project Requirements
Users
Departments
Submissions
Approval Stages
Documents
```

---

## Document Processing

Initial implementation:

```text
PyMuPDF
```

Potential future support:

```text
DOCX
HTML
OCR
Scanned PDF
```

---

## Infrastructure

```text
Docker
Docker Compose
```

Initial local architecture:

```text
Docker Compose
│
├── Qdrant
├── Elasticsearch
└── SQL Server
```

Python services can run locally or inside containers.

---

# 12. High-Level Architecture

```text
                         ┌──────────────┐
                         │     User     │
                         └──────┬───────┘
                                │
                                ▼
                     ┌────────────────────┐
                     │    Web Application │
                     └─────────┬──────────┘
                               │
                               ▼
                     ┌────────────────────┐
                     │      FastAPI       │
                     │     AI Service     │
                     └─────────┬──────────┘
                               │
                ┌──────────────┼──────────────┐
                │              │              │
                ▼              ▼              ▼
          SQL Server     Elasticsearch     Qdrant
          Structured       Text Search     Vector Search
             Data             BM25          Semantic
                │              │              │
                └──────────────┼──────────────┘
                               │
                               ▼
                        Hybrid Retrieval
                               │
                               ▼
                            LangChain
                               │
                               ▼
                              LLM
                               │
                               ▼
                    ┌────────────────────┐
                    │ AI Generated       │
                    │ Response           │
                    │ + Sources          │
                    │ + Requirements     │
                    └────────────────────┘
```

---

# 13. Initial Data Sources

The initial knowledge base will focus on official Indonesian government infrastructure documents.

Potential sources include:

* Directorate General of Highways (Direktorat Jenderal Bina Marga)
* Ministry of Public Works
* JDIH Ministry of Public Works
* Official government regulations
* Official technical guidelines
* Official SOP documents

Only publicly available documents will be used for the initial prototype.

---

# 14. Development Roadmap

## Phase 1 — Document Processing

```text
[ ] Collect official documents
[ ] Extract PDF text
[ ] Preserve page information
[ ] Clean extracted text
[ ] Implement chunking
[ ] Add document metadata
```

---

## Phase 2 — Semantic Search

```text
[ ] Setup Qdrant
[ ] Setup BGE-M3
[ ] Generate embeddings
[ ] Store vectors
[ ] Implement similarity search
[ ] Implement metadata filtering
```

---

## Phase 3 — Text Search

```text
[ ] Setup Elasticsearch
[ ] Index documents
[ ] Implement BM25
[ ] Implement fuzzy search
[ ] Implement autocomplete
[ ] Implement filtering
```

---

## Phase 4 — Hybrid Search

```text
[ ] Combine BM25 + vector search
[ ] Implement result fusion
[ ] Implement ranking
[ ] Evaluate retrieval quality
[ ] Experiment with Top-K
```

---

## Phase 5 — RAG

```text
[ ] Integrate LLM
[ ] Build retrieval pipeline
[ ] Build prompts
[ ] Generate grounded answers
[ ] Add citations
[ ] Handle insufficient context
```

---

## Phase 6 — Document Compliance

```text
[ ] Define project requirements
[ ] Create requirement database
[ ] Upload project documents
[ ] Match documents against requirements
[ ] Detect missing documents
[ ] Generate compliance report
```

---

## Phase 7 — LangChain

```text
[ ] Integrate LangChain
[ ] Implement retrievers
[ ] Implement prompt templates
[ ] Implement structured output
[ ] Implement chains
[ ] Implement tools
```

---

## Phase 8 — Agentic RAG

```text
[ ] Build AI Agent
[ ] Implement tool calling
[ ] Implement tool orchestration
[ ] Implement query routing
[ ] Connect SQL tools
[ ] Connect search tools
[ ] Implement multi-step reasoning workflow
```

---

# 15. Evaluation

The project will not only evaluate whether the LLM produces a good-looking answer.

Retrieval quality will also be evaluated.

Important metrics include:

```text
Retrieval:
- Precision@K
- Recall@K
- MRR
- Hit Rate

RAG:
- Faithfulness
- Answer Relevance
- Context Relevance
- Citation Accuracy
```

The goal is to understand whether the system retrieves the **correct government regulation or requirement**, not merely whether the generated answer sounds convincing.

---

# 16. Project Principles

GovInfra AI follows several principles:

### 1. Grounded Answers

The AI should prioritize information retrieved from official documents.

### 2. Traceability

Important answers should be traceable to their source documents.

### 3. Separation of Data and AI

Structured business data belongs in the relational database, while semantic document retrieval belongs in the vector database.

### 4. Hybrid Retrieval

Keyword search and semantic search should complement each other.

### 5. Human-in-the-Loop

The system is an assistant, not the final authority for government decisions.

Final approval and interpretation remain with authorized government officials.

---

# 17. Current Project Status

**Status: 🚧 Early Development**

Current focus:

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
BGE-M3
 ↓
Qdrant
 ↓
Semantic Search
```

Next milestone:

> Build the first working semantic search pipeline using real public government infrastructure documents.

---

# 18. Long-Term Vision

GovInfra AI aims to evolve from a simple document search system into an intelligent government project assistant.

```text
Document Search
      ↓
Semantic Search
      ↓
Hybrid Search
      ↓
RAG
      ↓
Document Compliance
      ↓
AI Assistant
      ↓
Agentic RAG
      ↓
Intelligent Project Submission Assistant
```

The long-term goal is to help government employees understand requirements, prepare project submissions, identify missing documents, and navigate applicable procedures while maintaining clear references to official sources.

---

## Project Learning Goals

This project is also designed as an end-to-end learning project covering:

```text
Information Retrieval
        ↓
Embeddings
        ↓
Vector Databases
        ↓
Semantic Search
        ↓
Full-Text Search
        ↓
Hybrid Search
        ↓
RAG
        ↓
Reranking
        ↓
LangChain
        ↓
Tool Calling
        ↓
Agentic RAG
        ↓
Production AI Architecture
```

The project therefore serves both as a **functional prototype** and as a practical exploration of modern AI application architecture.
