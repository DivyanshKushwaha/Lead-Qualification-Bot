from crewai import Agent, LLM
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# LLM Configuration
llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.3,  # Lower temperature for deterministic and precise outputs
    api_key=GEMINI_API_KEY
)

# Collector Agent
collector_agent = Agent(
    role="Lead Collection Specialist",
    goal="Retrieve inbound sales leads from {input_text} and ensure the data is complete and consistent.",
    backstory="You are an expert in extracting leads, capable of handling incomplete or ambiguous data accurately.",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    instructions=[
        "Extract and return the following fields in a structured manner: company_name, contact_person, title, email, phone, website, budget, timeline, usecase.",
        "Do not include additional information or reasoning beyond these fields.",
        "Ensure extracted data is consistent and complete as per the CollectedLead model."
    ]
)

# Qualification Agent
qualification_agent = Agent(
    role="Lead Qualification Expert",
    goal="Evaluate leads based on key criteria and assign a qualification score.",
    backstory="You are an expert evaluator focused on lead quality using strict predefined rules.",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    instructions=[
        "Use only the extracted fields (budget, industry, timeline, and usecase) provided by the collector_agent to evaluate the lead.",
        "Scoring Criteria (out of 100):",
        "- Budget: 40 points if > $10,000; 20 points if $5,000-$10,000; 0 points if < $5,000.",
        "- Timeline: 30 points if > 2 months; 10 points if 1-2 months; 0 points if < 1 month.",
        "- Industry: 20 points if tech/innovation/IT; 0 points otherwise.",
        "- Usecase Complexity: 10 points if innovative or impactful; 0 for basic/simple usecases.",
        "Generate a single-sentence summary (max 20 words) just stating the score and decision.",
        "decision only can be Qualified or Disqualified",
        "Example Summary: 'Lead scored 75 points; decision: Qualified based on strong budget and timeline.'",
        "Return structured data according to the QualifiedLead model."
    ]
)

# Routing Agent
routing_agent = Agent(
    role="Lead Routing Manager",
    goal="Route high-quality leads to sales and archive low-quality ones.",
    backstory="You ensure efficient lead routing by strictly adhering to score thresholds.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    instructions=[
        "Route leads with scores > 50 to routed_leads; archive leads with scores <= 50.",
        "Do not modify or add any information to the leads.",
        "Return structured data according to the RoutedAndArchivedLeads model."
    ]
)
