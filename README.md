# Database Analysis Crew AI Project

This project implements a CrewAI-based system for analyzing MySQL databases using AI agents. The system uses two specialized agents: a query writer and a query reviewer, to safely explore and analyze database structures.

## Requirements

### Python Version
- Python 3.10 or higher

### Required Packages
```
crewai>=0.11.0
langchain>=0.1.0
sqlalchemy>=2.0.0
pymysql>=1.1.0
python-dotenv>=1.0.0
pyyaml>=6.0.1
openai>=1.3.0
```

## Project Structure
```
analyst_generix/
├── README.md
├── setup.py
├── requirements.txt
├── .env
└── src/
    └── analyst_generix/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── __init__.py
        │   └── mysql_tools.py
        ├── agents/
        │   ├── __init__.py
        │   └── database_agents.py
        └── tasks/
            ├── __init__.py
            └── database_tasks.py
```

## Features

- **Query Writer Agent**: Creates safe, efficient queries to explore database structure
- **Query Reviewer Agent**: Reviews and validates queries before execution
- **MySQL Query Tool**: Safe database interaction tool
- **Environment-based Configuration**: Secure credential management

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone [repository-url]
   cd analyst_generix
   ```

2. Create and activate a Python virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -e .
   ```

4. Create a `.env` file in the project root:
   ```
   MYSQL_CONNECTION_STRING=mysql+mysqlconnector://username:password@host:port/database
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

Run the analysis:
```bash
python src/analyst_generix/main.py
```

The system will:
1. Connect to your MySQL database
2. Generate safe queries to explore the database structure
3. Review and validate queries before execution
4. Execute approved queries
5. Provide analysis results

## Components

### Tools
- `mysql_tools.py`: Handles database connections and query execution

### Agents
1. Query Writer Agent:
   - Writes efficient database queries
   - Focuses on metadata and system tables
   - Ensures query safety

2. Query Reviewer Agent:
   - Reviews query efficiency
   - Validates query safety
   - Executes approved queries

### Tasks
1. Write Query Task:
   - Creates database structure queries
   - Uses information_schema
   - Focuses on lightweight operations

2. Review Query Task:
   - Analyzes query efficiency
   - Executes approved queries
   - Provides analysis results

## Security

- Environment variables for sensitive credentials
- Query validation before execution
- Focus on metadata queries
- Limited database access permissions

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.