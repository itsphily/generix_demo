from crewai import Task

class DatabaseTasks:
    @staticmethod
    def create_write_query_task(agent):
        return Task(
            name="Write Database Query",
            description="""Write a simple, lightweight query to explore the database structure.
            Use information_schema views to get basic metadata about the database.
            Focus on getting table names and basic statistics that won't require
            full table scans or heavy computations.
            
            The query should focus on:
            1. Table names and row counts from information_schema
            2. Basic schema information
            3. Avoid any full table scans or complex joins""",
            agent=agent,
            expected_output="A single SQL query that explores database structure using information_schema or similar system views",
            tools=[],
            async_execution=False,
        )

    @staticmethod
    def create_review_query_task(agent):
        return Task(
            name="Review and Execute Query",
            description="""Review the provided query and analyze its potential cost and impact.
            Verify that it only uses system views and metadata tables.
            
            If the query is approved:
            1. Use the MySQL Query Tool to execute it
            2. Return the results along with your analysis
            
            If not approved:
            1. Explain why it's too expensive
            2. Suggest modifications to make it more efficient""",
            agent=agent,
            expected_output="Analysis of the query's efficiency and either approval with results or rejection with explanation",
            tools=[agent.tools[0]],
            async_execution=False,
        ) 