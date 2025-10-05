# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI-powered factory for researching, analyzing, and creating studies about the current geopolitical and economic environment, ultimately deriving portfolio generation and optimization decisions. The system uses the Gemini CLI to execute prompts stored as domain models and generate comprehensive financial analysis reports.

## Architecture

The project follows a **Domain-Driven Design (DDD)** architecture with clear separation of concerns:

### Core Layers

- **`src/domain/models/`**: Contains prompt templates (markdown files) that define portfolio analysis blueprints. These are the primary assets of the application—detailed prompts that instruct the AI to generate portfolio analysis reports for different strategies (e.g., `portfolio_static_etf_blueprint.md`, `portfolio_dynamic_etf_blueprint.md`, `etf_research.md`). Each prompt includes persona instructions, task specifications, process definitions, and structured output requirements.

- **`src/cli/`**: Command-line interface components that bridge user interaction with the Gemini CLI:
  - `main.py`: Orchestrates prompt selection and execution flow
  - `gemini_cli.py`: Wrapper class for executing Gemini CLI commands via subprocess
  - Entry point allows either interactive prompt selection or direct execution via `--prompt` argument

- **`src/application/`**: Application logic layer including commands, queries, services, use cases, factories, listeners, and subscribers (event-driven components)

- **`src/infrastructure/`**: Technical infrastructure including adapters, repositories, middleware, guards, caching, events, and exceptions

- **`src/api/`**: API layer with controllers, serializers, and resources

- **`src/shared/`**: Reusable components including DTOs, adapters, helpers, and custom exceptions

- **`config/`**: Configuration files including environment-specific settings in `config/env/`

## Running the Application

### Execute with interactive prompt selection
```bash
python main.py
```

This will display a numbered list of available prompts from `src/domain/models/` and allow you to select one.

### Execute with a custom prompt
```bash
python main.py --prompt "Your custom prompt text here"
```

### Execute from within src directory
```bash
python src/main.py
```

## Key Development Patterns

### Domain Models as Prompts

The domain models in this project are **not traditional data models** but rather **AI prompt templates** written in markdown. Each prompt file:
- Defines a persona for the AI (e.g., "Senior Quantitative Analyst")
- Specifies the task and deliverables (e.g., generate IEEE-style portfolio analysis)
- Includes multi-stage processing instructions (e.g., draft with placeholders, verify, finalize formatting)
- Contains user-specific variables like investment universe (ETF ISINs), risk profile, and analysis criteria

### Event-Driven Architecture

The application distinguishes between:
- **Listeners** (`src/application/listeners/`): React to specific events with focused, single-purpose actions
- **Subscribers** (`src/application/subscribers/`): Handle multiple related events and coordinate broader workflows

Domain events (`src/domain/events/`) represent business occurrences and are kept separate from infrastructure events (`src/infrastructure/events/`).

### CQRS Pattern

- **Commands** (`src/application/commands/`): Encapsulate write operations and task execution
- **Queries** (`src/application/queries/`): Handle read-only data retrieval operations

## External Dependencies

- **Gemini CLI**: The application relies on the `gemini` command-line tool being installed and available in the PATH. The CLI is invoked via Python's `subprocess` module.
- **Python 3.11+**: The codebase uses Python 3.x

## Directory Structure Philosophy

The folder structure strictly follows OOP and DDD best practices:
- Clear separation between domain logic (business rules), application logic (orchestration), and infrastructure (technical concerns)
- Domain layer remains independent and testable
- Each layer has a specific purpose documented in layer-specific markdown files (e.g., `DOMAIN.md`, `APPLICATION.md`)
