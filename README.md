# ArchSys — AI Systems Architect Curriculum

A 3-year, 156-week project roadmap that takes you from engineering foundations to AI systems architecture. Every phase ends in a concrete deliverable, every quarter ends in a capstone, and the final quarter produces a public signature portfolio.

> **ArchSys** is the short name for this curriculum.

---

## Table of Contents

- [At a Glance](#at-a-glance)
- [Who This Is For](#who-this-is-for)
- [The 12 Levels](#the-12-levels)
- [Weekly Operating System](#weekly-operating-system)
- [Year 1: Foundations to AI/ML Engineer (Weeks 1–52)](#year-1-foundations-to-aiml-engineer-weeks-152)
- [Year 2: AI Engineer to AI Systems Engineer (Weeks 53–104)](#year-2-ai-engineer-to-ai-systems-engineer-weeks-53104)
- [Year 3: AI Systems Engineer to AI Systems Architect (Weeks 105–156)](#year-3-ai-systems-engineer-to-ai-systems-architect-weeks-105156)
- [Capstone Standard](#capstone-standard)
- [Final Portfolio Requirements](#final-portfolio-requirements)
- [Languages, Hardware, and Cost](#languages-hardware-and-cost)
- [Repository Layout](#repository-layout)
- [Disclaimer](#disclaimer)
- [Contributing](#contributing)

---

## At a Glance

| | |
|---|---|
| **Duration** | 156 weeks (3 years) |
| **Structure** | 3 years, 12 quarters, 4 quarters per year |
| **Target load** | 20–25 hours per week |
| **Deliverables** | 60 (one per topic block, listed below) |
| **Capstones** | 10 quarterly capstones (Weeks 13, 39, 52, 65, 78, 91, 104, 117, 130, 143) |
| **Final output** | At least 3 polished, public systems plus a signature portfolio |

---

## Who This Is For

This is **not** a from-zero beginner course. Week 1 starts with advanced Python (OOP, decorators, async/await, type hints), so you should already be comfortable writing basic Python and using a terminal before you begin.

It suits you if you want to become an ML or AI systems engineer and eventually an architect, and you are willing to commit roughly 20–25 hours a week for three years.

---

## The 12 Levels

Each quarter is one level. Levels are presentation labels for tracking progress; they do not change the curriculum.

| Level | Title | Quarter | Weeks |
|---|---|---|---|
| 01 | Engineering Foundations | Q1 | 1–13 |
| 02 | Mathematical Intelligence | Q2 | 14–26 |
| 03 | Deep Learning Engineer | Q3 | 27–39 |
| 04 | Generative AI Engineer | Q4 | 40–52 |
| 05 | Distributed AI Engineer | Q5 | 53–65 |
| 06 | AI Inference Engineer | Q6 | 66–78 |
| 07 | Agent Systems Engineer | Q7 | 79–91 |
| 08 | LLMOps Engineer | Q8 | 92–104 |
| 09 | Cloud AI Systems Engineer | Q9 | 105–117 |
| 10 | Responsible AI Systems Engineer | Q10 | 118–130 |
| 11 | AI Architecture Leader | Q11 | 131–143 |
| 12 | Master AI Systems Architect | Q12 | 144–156 |

---

## Weekly Operating System

A suggested 20-hour week:

| Day | Hours | Focus |
|---|---|---|
| Monday | 2 | Theory |
| Tuesday | 3 | Hands-on implementation |
| Wednesday | 2 | Theory + design reading |
| Thursday | 3 | Hands-on implementation |
| Friday | 2 | Review + testing + documentation + Anki |
| Saturday | 5 | Capstone / portfolio |
| Sunday | 3 | Open source / networking / retrospective |
| **Total** | **20** | |

The stated target load is 20–25 hours per week; add extra time on Saturday or Sunday as needed.

---

## Year 1: Foundations to AI/ML Engineer (Weeks 1–52)

**Goal:** Master programming, mathematics, classical ML, deep learning, and first production LLM applications.

### Q1 — Programming & Systems Foundations (Weeks 1–13)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 1–2 | Python advanced: OOP, decorators, async/await, type hints | Fluent Python; Real Python | Build a CLI tool with argparse + asyncio |
| 3–4 | Data structures & algorithms: arrays, trees, graphs, DP, recursion | LeetCode; Grokking Algorithms | Solve 50 medium-level problems |
| 5–6 | Linux & DevOps: Bash, Docker, Git, CI/CD | Docker docs; GitHub Actions | Containerize a Flask app and deploy it |
| 7–8 | Networking & OS: TCP/IP, HTTP/2, gRPC, processes, threads | Computer Networking: A Top-Down Approach | FastAPI service with rate limiting |
| 9–10 | Databases: PostgreSQL, Redis, vector databases | PostgreSQL and Redis docs | Caching layer for an API |
| 11–12 | Go or Rust: concurrency and performance systems | The Go Programming Language | Distributed key-value store |
| 13 | **Capstone:** Kubernetes deployment | Kubernetes docs; K3s | Three-service application with autoscaling |

### Q2 — Mathematics & Classical ML (Weeks 14–26)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 14–16 | Linear algebra: matrices, eigenvalues, SVD, PCA | MIT 18.06; 3Blue1Brown | Implement PCA in NumPy |
| 17–18 | Probability & statistics: Bayes, distributions, testing | Harvard Stat 110 | A/B-testing simulator |
| 19–20 | Calculus: gradients, chain rule, optimization | Khan Academy; Deep Learning | Visualize gradient descent |
| 21–23 | Classical ML: regression, classification, clustering, ensembles | Andrew Ng ML; scikit-learn | Recommendation system with XGBoost |
| 24–26 | ML pipelines: validation, tuning, features | scikit-learn; Optuna | End-to-end ML pipeline on a public dataset |

### Q3 — Deep Learning & PyTorch (Weeks 27–39)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 27–29 | Neural networks: backpropagation, activations | Deep Learning; PyTorch tutorials | Neural net from scratch in NumPy |
| 30–32 | CNNs and computer vision | Stanford CS231N; PyTorch Vision | CIFAR-10 classifier |
| 33–35 | RNNs, LSTMs, GRUs, attention | Stanford CS224N lectures 1–5 | IMDB sentiment classifier |
| 36–38 | Transformers: self-attention, encoder-decoder, BERT | Illustrated Transformer; Hugging Face Course | Fine-tune BERT on a benchmark |
| 39 | **Capstone:** Transformer from scratch | Karpathy nanoGPT | Train a small GPT on Shakespeare |

### Q4 — Generative AI & LLM Applications (Weeks 40–52)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 40–42 | LLM architectures: decoder-only, MoE, tokenization | CMU LLM Systems materials | Implement BPE tokenization |
| 43–45 | Prompt engineering: structured output, ReAct | DAIR.AI guide; LangChain docs | QA bot with structured outputs |
| 46–48 | RAG: hybrid retrieval, chunking, reranking | LangChain; LlamaIndex; Hugging Face | RAG system with vector search and reranking |
| 49–50 | Fine-tuning: LoRA, QLoRA, preference optimization | Hugging Face PEFT; LLM Course | Fine-tune an open model on a curated dataset |
| 51–52 | **Capstone:** Deployed RAG system (AWS Bedrock or GCP Vertex AI) | AWS Bedrock or GCP Vertex AI | Deploy, monitor latency, throughput, and cost |

---

## Year 2: AI Engineer to AI Systems Engineer (Weeks 53–104)

**Goal:** Master distributed training, inference optimization, agentic systems, and LLMOps.

### Q5 — Distributed ML (Weeks 53–65)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 53–55 | GPU programming: CUDA, kernels, memory | CMU LLM Systems | Custom CUDA LayerNorm kernel |
| 56–58 | Data parallelism: DDP, all-reduce | PyTorch DDP docs | Multi-GPU ResNet training |
| 59–61 | Model and pipeline parallelism | Megatron-LM; GPipe papers | Pipeline parallel GPT-2 |
| 62–64 | 3D parallelism: data, tensor, pipeline | DeepSpeed; FSDP docs | ZeRO-3/FSDP training experiment |
| 65 | **Capstone:** Distributed training pipeline | CMU-style assignments | Reproducible distributed training with checkpoints |

### Q6 — Inference Optimization & Serving (Weeks 66–78)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 66–68 | Serving: vLLM, TGI, TensorRT-LLM | Official documentation | Deploy an open LLM with vLLM |
| 69–71 | Quantization: INT8, FP8, AWQ, GPTQ | Hugging Face guides | 4-bit model benchmark |
| 72–74 | Memory optimization: KV cache, PagedAttention | vLLM and FlashAttention papers | KV-cache profiling experiment |
| 75–77 | Speculative decoding | Medusa and decoding papers | Prototype speculative decoding |
| 78 | **Capstone:** Scalable inference service | Cloud load testing tools | Load-tested service with SLOs and cost dashboard |

### Q7 — Agentic Systems (Weeks 79–91)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 79–81 | Agent designs: ReAct, planning, reflection | LangGraph docs; agent papers | Research agent |
| 82–84 | Tool use: APIs, code execution, browser workflows | AutoGen/LangChain docs | Tool-using synthesis agent |
| 85–87 | Memory: context, retrieval, episodic memory | MemGPT paper; vector DB docs | Persistent-memory agent |
| 88–90 | Multi-agent orchestration | AutoGen; CrewAI docs | Multi-agent customer-support prototype |
| 91 | **Capstone:** Autonomous agent workflow | Agent evaluation framework | Agent that plans, tests, and ships a small task |

### Q8 — LLMOps, Monitoring & Cost (Weeks 92–104)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 92–94 | LLMOps: CI/CD, evaluations, canary releases | LangSmith; GitHub Actions | Automated evaluation pipeline |
| 95–97 | Monitoring: latency, tokens, drift, quality | Arize Phoenix; observability docs | Operational dashboard |
| 98–100 | Cost: routing, caching, budgets | Provider pricing and routing guides | Model router with cache |
| 101–103 | Security: prompt injection, leakage, isolation | LLM security guidance | Defense-in-depth test suite |
| 104 | **Capstone:** Production LLMOps platform | — | Multi-tenant RAG with evals, monitoring, and security |

---

## Year 3: AI Systems Engineer to AI Systems Architect (Weeks 105–156)

**Goal:** Design resilient enterprise AI systems, practice governance, lead decisions, and complete a public signature portfolio.

### Q9 — Cloud & Multi-Region Architecture (Weeks 105–117)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 105–107 | Primary cloud deep dive: AWS or GCP | Cloud architecture documentation | Autoscaled RAG deployment |
| 108–110 | Kubernetes and managed AI services | GKE/EKS and model-platform docs | Multi-region serving prototype |
| 111–113 | Hybrid and portability design | Terraform; Kubernetes; OpenTelemetry | Portable deployment architecture |
| 114–116 | Reliability: SLOs, backups, DR, failover | Well-Architected Framework | 99.99% availability design and DR drill |
| 117 | **Capstone:** Global AI platform design | Architecture review templates | Three-region design, load test, cost model |

### Q10 — Governance, Compliance & Safety (Weeks 118–130)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 118–120 | Model risk, fairness, evaluation | AI Fairness 360; SHAP | Risk and quality dashboard |
| 121–123 | Privacy, compliance, auditability | GDPR/HIPAA/SOC 2 guidance | Data-flow map and audit-log service |
| 124–126 | Explainability and incident response | Captum; postmortem templates | Explainability and incident playbook |
| 127–129 | Safety and red teaming | Red-team guides; safety research | Red-team your deployed agent |
| 130 | **Capstone:** Governance platform | Policy-as-code concepts | Controls, evidence, reviews, and alerts |

### Q11 — Architecture Leadership (Weeks 131–143)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 131–133 | Requirements and stakeholder management | Architecture decision records | Convert a business case into system requirements |
| 134–136 | Roadmaps, capacity, technical debt, FinOps | OKR and FinOps materials | 12-month platform roadmap |
| 137–139 | Technical writing: RFCs and design reviews | Writing for Computer Science | Publish a full architecture RFC |
| 140–142 | Communication and influence | Toastmasters; presentation practice | Record a 15-minute architecture talk |
| 143 | **Capstone:** Architecture review simulation | Peer review rubric | Defend a design to engineering, product, and security |

### Q12 — Signature Portfolio (Weeks 144–156)

| Weeks | Topic | Resources | Deliverable |
|---|---|---|---|
| 144–148 | Scope and architect one flagship system | System design references | Architecture, threat model, SLOs, cost model |
| 149–152 | Implement and operate it | Chosen production stack | Public repository, tests, deployment, dashboard |
| 153–156 | Validate, document, present, and apply | Portfolio and interview practice | Case study, demo, RFC, incident report, interview portfolio |

---

## Capstone Standard

Every capstone should include:

- Source code
- Architecture diagram
- Automated tests
- Observability
- Cost estimate
- Written design document

---

## Final Portfolio Requirements

By the end of the curriculum, publish at least three polished systems:

1. **Evaluated RAG Application**
2. **Scalable LLM Serving / Distributed Training Project**
3. **Enterprise-Style AI Platform Capstone**

For every project:

- Write an RFC
- Diagram the architecture
- Define SLOs
- Expose metrics
- Write tests
- Threat-model the system
- Document cost/performance trade-offs

---

## Languages, Hardware, and Cost

**Languages and tools used:** Python (primary), Go or Rust (Weeks 11–12), CUDA C/C++ (Weeks 53–55), plus Bash and SQL throughout.

**Learning resources:** Most are free (documentation, open courses, papers, tutorials). A few are paid books, such as *Fluent Python*, *Computer Networking: A Top-Down Approach*, and *The Go Programming Language*; check your library or alternatives.

**Hardware and cloud:** Free resources alone are not enough for every project.

- **Weeks 53–78 (GPU-heavy work):** CUDA kernels, multi-GPU DDP, pipeline parallelism, and FSDP/ZeRO-3 need real GPU access, and multi-GPU experiments need more than one GPU. Budget for rented GPUs.
- **Weeks 51–52 and 105–117:** Deployments on AWS Bedrock, GCP Vertex AI, and multi-region cloud infrastructure incur cloud costs.

Performance numbers mentioned anywhere in this curriculum (for example, 99.99% availability) are **targets to validate in your own environment**, not guaranteed outcomes.

---

## Repository Layout

Projects are organized by programming language, one directory per language:

- `Python/` — all projects written in Python
- Other languages get their own directory named after the language (for example `Go/` or `Rust/` for the Weeks 11–12 key-value store, and `CUDA/` for the Weeks 53–55 kernel)
- `README.md` — this document

---

## Disclaimer

This is a personal learning plan. It is not an accredited program, a credential, or a guarantee of employment or compensation. Resources and tools change over time; check each one before relying on it.

---

## Contributing

Suggestions are welcome, especially from experienced engineers. If you spot an outdated resource, a missing prerequisite, a sequencing problem, or an error, please open an Issue or a Pull Request with the week number and what you would change.
