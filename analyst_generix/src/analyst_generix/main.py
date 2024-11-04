import os
from dotenv import load_dotenv, find_dotenv
from analyst_generix.crew import AnalystCrew

def main():
    try:
        # Find and load .env file
        env_path = find_dotenv()
        print(f"Loading .env from: {env_path}")
        load_dotenv(env_path, override=True)
        
        # Debug environment variables
        openai_key = os.getenv("OPENAI_API_KEY")
        database_name = os.getenv("MYSQL_DATABASE_NAME")
        
        print("\n=== Environment Variables ===")
        if openai_key:
            print(f"OpenAI API Key found (length: {len(openai_key)})")
            print(f"Key starts with: {openai_key[:10]}...")
        else:
            print("WARNING: OpenAI API Key not found!")
            
        if database_name:
            print(f"Database name: {database_name}")
        else:
            print("WARNING: Database name not found!")
            
        if not openai_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
            
        # Set up inputs
        inputs = {"database_name": database_name}
        
        # Run the crew
        result = AnalystCrew().crew().kickoff(inputs=inputs)
        
        print("\n=== Analysis Results ===")
        print(result)
        
    except Exception as e:
        print(f"\n=== Error Details ===")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        raise

if __name__ == "__main__":
    main()
