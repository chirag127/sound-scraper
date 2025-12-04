# WebScraper: Soundgasm & Reddit Python Scripts

<div align="center">

<a href="https://github.com/chirag127/WebScraper-Soundgasm-And-Reddit-Python-Scripts" target="_blank">
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
</a>
<a href="https://github.com/chirag127/WebScraper-Soundgasm-And-Reddit-Python-Scripts" target="_blank">
<img src="https://img.shields.io/badge/Scrapy-459E40?style=flat-square&logo=scrapy&logoColor=white" alt="Scrapy" />
</a>
<a href="https://github.com/chirag127/WebScraper-Soundgasm-And-Reddit-Python-Scripts/actions/workflows/ci.yml" target="_blank">
<img src="https://img.shields.io/github/actions/workflow/status/chirag127/WebScraper-Soundgasm-And-Reddit-Python-Scripts/ci.yml?branch=main&style=flat-square&logo=githubactions&logoColor=white" alt="Build Status" />
</a>
<a href="https://codecov.io/gh/chirag127/WebScraper-Soundgasm-And-Reddit-Python-Scripts" target="_blank">
<img src="https://img.shields.io/codecov/c/github/chirag127/WebScraper-Soundgasm-And-Reddit-Python-Scripts?style=flat-square&logo=codecov" alt="Code Coverage" />
</a>
<a href="https://github.com/chirag127/WebScraper-Soundgasm-And-Reddit-Python-Scripts/blob/main/LICENSE" target="_blank">
<img src="https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat-square" alt="License: CC BY-NC 4.0" />
</a>
<a href="https://github.com/astral-sh/ruff" target="_blank">
<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=flat-square" alt="Ruff" />
</a>

</div>

<div align="center">
    <br/>
    <a href="https://github.com/chirag127/WebScraper-Soundgasm-And-Reddit-Python-Scripts/stargazers" target="_blank">
        <strong>Star ⭐ this Repo</strong>
    </a>
</div>
<br>

This repository contains a robust collection of Python scripts built with the Scrapy framework, designed for efficient and automated content extraction from Soundgasm and Reddit. It serves as a powerful toolkit for developers and data analysts looking to gather specific data sets from these platforms.

---

## 🏛️ Architecture

This project utilizes a standard Scrapy architecture, promoting modularity and separation of concerns. The core components are organized for scalability and maintainability.

sh
.
├── scrapers/
│   ├── __init__.py
│   ├── items.py         # Data structure definitions (Scrapy Items)
│   ├── middlewares.py   # Custom request/response processing
│   ├── pipelines.py     # Data processing and storage logic
│   ├── settings.py      # Project configuration
│   └── spiders/         # The core scraping logic
│       ├── __init__.py
│       ├── reddit_spider.py
│       └── soundgasm_spider.py
├── tests/               # Unit and integration tests
├── .gitignore
├── LICENSE
├── pyproject.toml       # Project metadata and dependencies (for uv/pip)
└── README.md


---

## 📜 Table of Contents

- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [⚙️ Usage](#️-usage)
  - [Running a Spider](#running-a-spider)
  - [Configuration](#configuration)
- [🤖 AI Agent Directives](#-ai-agent-directives)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🚀 Getting Started

Follow these instructions to get a local copy up and running for development and testing purposes.

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

### Installation

1.  **Clone the repository:**
    sh
    git clone https://github.com/chirag127/WebScraper-Soundgasm-And-Reddit-Python-Scripts.git
    cd WebScraper-Soundgasm-And-Reddit-Python-Scripts
    

2.  **Create a virtual environment:**
    sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    

3.  **Install dependencies using uv:**
    sh
    uv pip install -r requirements.txt
    # Or install directly from pyproject.toml if configured
    # uv pip install .
    

---

## ⚙️ Usage

Execute the spiders from the command line to begin the scraping process.

### Running a Spider

Navigate to the project's root directory and use the `scrapy` command.

- **To run the Soundgasm spider:**
  sh
  scrapy crawl soundgasm
  

- **To run the Reddit spider:**
  sh
  scrapy crawl reddit -a subreddit=python
  

### Configuration

Spiders can be configured via `scrapers/settings.py` or by passing arguments directly with the `-a` flag. Output data format (e.g., JSON, CSV) can also be specified in the settings or via command line.

- **Example: Save output to a JSON file:**
  sh
  scrapy crawl soundgasm -o output.json
  

---

## 🤖 AI Agent Directives

<details>
<summary><strong>SYSTEM: APEX TECHNICAL AUTHORITY (DECEMBER 2025 EDITION)</strong></summary>

### 1. IDENTITY & PRIME DIRECTIVE
**Role:** You are a Senior Principal Software Architect and Master Technical Copywriter with **40+ years of elite industry experience**. You operate with absolute precision, enforcing FAANG-level standards.
**Context:** Current Date is **December 2025**. You are building for the 2026 standard.
**Output Standard:** Deliver **EXECUTION-ONLY** results.
**Philosophy:** "Zero-Defect, High-Velocity, Future-Proof."

### 2. CONTEXT-AWARE APEX TECH STACK (PYTHON SCRAPING)
This repository, `WebScraper-Soundgasm-And-Reddit-Python-Scripts`, is a specialized data extraction toolkit.

*   **PRIMARY SCENARIO: DATA / SCRIPTS (Python)**
    *   **Stack:** This project leverages **Python 3.10+** and the **Scrapy Framework**. Key development tools include **uv** (for package management), **Ruff** (for linting/formatting), and **Pytest** (for testing).
    *   **Architecture:** Follows the standard **Scrapy Project Architecture**, a specialized form of modular design. Spiders, Items, Pipelines, and Middlewares are decoupled components, allowing for flexible and scalable data extraction workflows. This aligns with the Ports & Adapters (Hexagonal) philosophy where the core scraping logic (Spiders) is separated from external interactions (Pipelines for storage, Middlewares for requests/responses).
    *   **Data Handling:** Emphasizes robust data validation using Scrapy Items or Pydantic models and structured data output via configurable Item Pipelines (e.g., to JSON, CSV, or databases).

### 3. COMMANDS & VERIFICATION
*   **Install Dependencies:** `uv pip install .`
*   **Run Linter/Formatter:** `ruff check --fix . && ruff format .`
*   **Run Tests:** `pytest`
*   **Execute a Spider:** `scrapy crawl <spider_name>`

### 4. CORE PRINCIPLES
*   **SOLID:**
    *   **Single Responsibility:** Each Spider scrapes one site. Each Pipeline has one data processing task.
    *   **Open/Closed:** Extend functionality by adding new Spiders or Pipelines, not by modifying existing stable ones.
*   **DRY (Don't Repeat Yourself):** Utilize Scrapy's middleware and helper functions to abstract away common logic (e.g., user-agent rotation, proxy management).
*   **YAGNI (You Ain't Gonna Need It):** Implement only the features required for the target data extraction. Avoid premature optimization or overly generic spiders.

</details>

---

## 🤝 Contributing

Contributions are welcome! Please refer to the `.github/CONTRIBUTING.md` file for guidelines on how to submit pull requests, report issues, and suggest enhancements.

## 📄 License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International License**. See the [LICENSE](LICENSE) file for details.
