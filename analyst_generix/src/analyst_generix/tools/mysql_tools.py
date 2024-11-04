from typing import Any, Optional
from crewai_tools import BaseTool
from sqlalchemy import create_engine
import os
from pydantic import Field

class MySQLQueryTool(BaseTool):
    name: str = "MySQL Query Tool"
    description: str = """
    Use this tool to execute MySQL queries and retrieve data from the database.
    """
    database_name: Optional[str] = Field(default=None)

    def _run(self, query: str) -> Any:
        """Execute a MySQL query and return results"""
        try:
            connection = os.getenv("MYSQL_CONNECTION_STRING")
            if not connection:
                raise ValueError("MySQL connection string not found in environment variables")
            
            print(f"\nExecuting query:\n{query}\n")  # Debug print
            
            engine = create_engine(connection)
            with engine.connect() as conn:
                result = conn.execute(query)
                return result.fetchall()
                
        except Exception as e:
            return f"Error executing query: {str(e)}"
