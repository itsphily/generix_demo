from typing import Any, Optional
from crewai_tools import BaseTool
from sqlalchemy import create_engine
import os

class MySQLQueryTool(BaseTool):
    name: str = "MySQL Query Tool"
    description: str = """
    Use this tool to execute MySQL queries and retrieve data from the database.
    The tool returns the query results as a list of rows.
    """

    def __init__(self):
        super().__init__()

    def _run(self, query: str) -> Any:
        """Execute a MySQL query and return results"""
        try:
            connection = os.getenv("MYSQL_CONNECTION_STRING")
            if not connection:
                raise ValueError("MySQL connection string not found in environment variables")
            
            engine = create_engine(connection)
            with engine.connect() as conn:
                result = conn.execute(query)
                return result.fetchall()
                
        except Exception as e:
            return f"Error executing query: {str(e)}"

    def _arun(self, query: str) -> Any:
        """Async implementation of the tool"""
        return self._run(query)