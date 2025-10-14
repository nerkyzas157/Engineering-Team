# Autonomous Engineering Team – Web App Builder

This project demonstrates an **autonomous full engineering team of AI agents** capable of turning user input into a **fully functional web application**. The system is built using the **CrewAI Crews Framework**, allowing for exceptional collaboration between AI roles with minimal boilerplate code.

---

## Overview

The project automates the complete web application development lifecycle using AI agents that act as specialized team members. Each agent has a distinct engineering role and collaborates to design, architect, build, and validate applications dynamically based on user prompts.

---

## AI Engineering Team

| Role | Model |
|------|--------|
| **Project Manager** | gpt-4o |
| **System Architect** | gpt-4o |
| **Backend Engineer** | claude-3-5-haiku |
| **Frontend Engineer** | claude-3-5-haiku |
| **QA Engineer** | claude-3-5-haiku |

Each agent autonomously contributes to their respective domain, guided by a structured coordination protocol defined within the CrewAI framework.  
I went with haiku models for their hight TPM limit and much lower running cost.  

---

## Tech Stack

- **Framework:** [CrewAI Crews](https://github.com/joaomdmoura/crewAI)
- **Language:** Python 3.11+
- **Package Manager:** [uv](https://github.com/astral-sh/uv)
- **AI Models:** GPT-4o and Claude family models
- **Execution Flow:** CrewAI task orchestration

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://huggingface.co/spaces/nerkyzas/engineering-team
cd engineering-team
```

### 2. Install Dependencies

```bash
pip install uv
```
Docker is necessary for the code to work. Install it if you don't have it yet.

### 3. Install CrewAI Framework

```bash
crewai install
```

### 4. Run the Project

```bash
crewai run
```

---

## How It Works

1. The user provides **a high-level description** of the desired web application.
2. The **Project Manager** interprets the request and delegates tasks.
3. The **System Architect** designs the technical architecture.
4. The **Backend and Frontend Developers** build the components.
5. The **QA Engineer** performs validation and testing before delivery.

---

## Why CrewAI + uv?

- **CrewAI** provides a seamless way to manage autonomous AI roles with clear boundaries and cooperative workflows.
- **uv** offers **blazing-fast dependency management** and **tight integration** with CrewAI, making environment setup and execution highly efficient.

---

## Example Use Case

**Input:**  
> "Enter the name of the project: "
> "Enter the requirements for the project: "

**Output:**  
An automatically designed, architected, and coded web app, ready to run and deploy.  
You can find example output in **output/** directory.  

---

## License
This project is licensed under the (MIT License)[LICENSE] — feel free to use and adapt it for your own research automation workflows.
