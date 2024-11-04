import os
from dotenv import load_dotenv, find_dotenv
from analyst_generix.crew import AnalystCrew

def main():
    try:
        # Find and load .env file
        env_path = find_dotenv()
        print(f"Found .env file at: {env_path}")
        
        # Load environment variables
        load_dotenv(env_path, override=True)
        
        # Debug environment variables
        openai_key = os.getenv("OPENAI_API_KEY")
        mysql_conn = os.getenv("MYSQL_CONNECTION_STRING")
        
        print("\n=== Environment Variables ===")
        print(f"OpenAI API Key present: {'Yes' if openai_key else 'No'}")
        if openai_key:
            print(f"OpenAI API Key length: {len(openai_key)}")
            print(f"OpenAI API Key starts with: {openai_key[:10]}...")
            print(f"OpenAI API Key ends with: ...{openai_key[-10:]}")
        print(f"MySQL Connection present: {'Yes' if mysql_conn else 'No'}")
        
        if not openai_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        if openai_key.startswith("your_") or "your_" in openai_key:
            raise ValueError("OPENAI_API_KEY appears to be a placeholder value")
            
        # Initialize and run the crew
        crew = AnalystCrew()
        result = crew.run_analysis()
        
        print("\n=== Analysis Results ===")
        print(result)
        
    except Exception as e:
        print(f"\n=== Error Details ===")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        raise

if __name__ == "__main__":
    main()
