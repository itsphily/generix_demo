from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from analyst_generix.tools.mysql_tools import MySQLQueryTool
from langchain.llms import OpenAI
import yaml
import os
from crewai import LLM

@CrewBase
class AnalystCrew:
    """Database Analysis crew"""
    # Get the current directory path
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Set config paths relative to current file
    agents_config = os.path.join(base_path, 'config', 'agents.yaml')
    tasks_config = os.path.join(base_path, 'config', 'tasks.yaml')

    def __init__(self):
        super().__init__()
        self.mysql_tool = MySQLQueryTool()

    @agent
    def query_writer(self) -> Agent:
        # Using GPT-4 for the query writer as it's better at code generation
        llm = LLM(model="gpt-4o")
        return Agent(
            config=self.agents_config['query_writer'],
            tools=[],
            llm=llm,
            verbose=True,
            memory=True
        )

    @agent
    def query_reviewer(self) -> Agent:
        # Using Claude for the reviewer as it's good at analysis
        llm = LLM(model="gpt-4o")
        return Agent(
            config=self.agents_config['query_reviewer'],
            tools=[self.mysql_tool],
            llm=llm,
            verbose=True,
            memory=True
        )

    @agent
    def database_documentation_specialist(self) -> Agent:
        llm = LLM(model="gpt-4o")
        return Agent(
            config=self.agents_config['database_documentation_specialist'],
            tools=[],
            llm=llm,
            verbose=True,
            memory=True
        )

    @task
    def write_queries(self) -> Task:
        return Task(
            config=self.tasks_config['write_queries'],
            agent=self.query_writer()
        )

    @task
    def review_and_execute_queries(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_execute_queries'],
            agent=self.query_reviewer(),
            context=[self.write_queries()]
        )
    
    @task
    def document_database(self) -> Task:
        return Task(
            config=self.tasks_config['document_database'],
            agent=self.database_documentation_specialist(),
            context=[self.review_and_execute_queries(), self.write_queries()],
            output_file= "Database Analysis.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Database Analysis crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )