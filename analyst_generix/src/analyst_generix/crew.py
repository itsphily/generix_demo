from crewai import Crew, Process
from analyst_generix.agents.database_agents import DatabaseAgents
from analyst_generix.tasks.database_tasks import DatabaseTasks
import os

class AnalystCrew:
    def __init__(self):
        # Debug environment variables in crew
        print("\n=== Crew Initialization ===")
        openai_key = os.getenv("OPENAI_API_KEY")
        mysql_conn = os.getenv("MYSQL_CONNECTION_STRING")
        
        print(f"OpenAI API Key in crew: {'Present' if openai_key else 'Missing'}")
        print(f"MySQL Connection in crew: {'Present' if mysql_conn else 'Missing'}")
        
        if not os.getenv("MYSQL_CONNECTION_STRING"):
            raise ValueError("MYSQL_CONNECTION_STRING environment variable is required")
        
        # Initialize agents
        self.db_agents = DatabaseAgents()
        
    def run_analysis(self):
        try:
            print("\n=== Creating Agents ===")
            # Create agents
            query_writer = self.db_agents.create_query_writer()
            query_reviewer = self.db_agents.create_query_reviewer()
            
            print("\n=== Creating Tasks ===")
            # Create tasks
            tasks = DatabaseTasks()
            write_task = tasks.create_write_query_task(query_writer)
            review_task = tasks.create_review_query_task(query_reviewer)
            
            print("\n=== Setting up Crew ===")
            # Create and run crew
            crew = Crew(
                agents=[query_writer, query_reviewer],
                tasks=[write_task, review_task],
                process=Process.sequential,
                verbose=True
            )
            
            print("\n=== Starting Crew Execution ===")
            # Run the crew and return results
            return crew.kickoff()
            
        except Exception as e:
            print(f"\n=== Crew Error Details ===")
            print(f"Error type: {type(e).__name__}")
            print(f"Error message: {str(e)}")
            raise