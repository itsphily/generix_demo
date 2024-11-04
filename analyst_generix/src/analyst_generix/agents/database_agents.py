from crewai import Agent
from analyst_generix.tools.mysql_tools import MySQLQueryTool

class DatabaseAgents:
    def __init__(self):
        self.mysql_tool = MySQLQueryTool()

    def create_query_writer(self):
        return Agent(
            role='MySQL Query Writer',
            goal='Write efficient, low-cost queries to explore database structure',
            backstory="""You are a careful database analyst who specializes in writing 
            efficient queries. You focus on exploring database structure using system 
            tables and metadata queries that are guaranteed to be lightweight and fast.""",
            tools=[],
            verbose=True
        )

    def create_query_reviewer(self):
        return Agent(
            role='Query Cost Analyst',
            goal='Review and validate queries to ensure they are cost-efficient and safe to run',
            backstory="""You are a database performance expert who specializes in query analysis.
            Your expertise lies in identifying potentially expensive queries and ensuring
            only lightweight, metadata-focused queries are approved for execution.""",
            tools=[self.mysql_tool],
            allow_delegation=False,
            verbose=True
        ) 