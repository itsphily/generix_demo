from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from analyst_generix.tools.mysql_tools import MySQLQueryTool
import yaml
import os

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
        return Agent(
            config=self.agents_config['query_writer'],
            tools=[],
            verbose=True,
            memory=False
        )

    @agent
    def query_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['query_reviewer'],
            tools=[self.mysql_tool],
            verbose=True,
            memory=False
        )

    @task
    def write_query_task(self) -> Task:
        return Task(
            config=self.tasks_config['write_query'],
            agent=self.query_writer()
        )

    @task
    def review_query_task(self) -> Task:
        return Task(
            config=self.tasks_config['review_query'],
            agent=self.query_reviewer(),
            context=[self.write_query_task()]
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