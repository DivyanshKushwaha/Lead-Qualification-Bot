from crewai import Agent, LLM
import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7,
    api_key=GEMINI_API_KEY
)

collector_agent = Agent(
    role="Lead Collection Specialist",
    goal="Retrieve inbound sales leads from {input_text} and ensure the data is complete and consistent.",
    backstory="You are an expert in gathering leads, capable of handling missing or ambiguous data.",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    instructions=[
        "Extract the following key fields: company_name, contact_person, title, email, phone, website, budget, timeline, usecase.",
        "Return structured data as per the CollectedLead model."
    ],

)
qualification_agent = Agent(
    role="Lead Qualification Expert",
    goal="Evaluate leads using predefined criteria, assigning scores and decisions based on quality.",
    backstory="You are an expert in evaluating and filtering leads for sales accuracy.",
    verbose=True,
    allow_delegation=True,
    llm=llm,
    instructions=[
        "Evaluate leads based on company_name, budget, industry, timeline, and usecase extracted from collector_agent",
        "Only use extracted lead data to evaluate and for giving score, don't add anything from your own",
        "Leads are better if the budget exceeds $10,000, the industry is tech/innovation/IT, and the timeline is over 2 months.",
        "Assign a score between 0-100 and return structured data according to the QualifiedLead model."
    ]
)

routing_agent = Agent(
    role="Lead Routing Manager",
    goal="Route high-quality leads to sales and archive low-quality ones.",
    backstory="You ensure only the most promising leads are passed to sales while archiving others efficiently.",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    instructions=[
        "Route leads with scores above 50 to routed_leads and archive the rest.",
        "Return structured data according to the RoutedAndArchivedLeads model."
    ]
)
