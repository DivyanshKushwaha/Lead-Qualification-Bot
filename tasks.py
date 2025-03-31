from crewai import Task
from agents import collector_agent, qualification_agent, routing_agent
from models import CollectedLead, QualifiedLead,RoutedAndArchivedLeads
import os 
os.makedirs('output',exist_ok=True)

collect_leads_task = Task(
    description="Collect and validate inbound sales leads for completeness and consistency.",
    agent=collector_agent,
    expected_output="JSON file of collected leads according to the CollectedLead model.",
    output_pydantic=CollectedLead,
    output_file="output/collected_leads.json"
)

qualify_leads_task = Task(
    description="Evaluate leads and assign scores and decisions for qualification or disqualification.",
    agent=qualification_agent,
    expected_output="JSON file of qualified leads according to the QualifiedLead model, with scores and decisions.",
    output_pydantic=QualifiedLead,
    context=[collect_leads_task],
    output_file="output/qualified_leads.json"
)

route_leads_task = Task(
    description="Route qualified leads to sales and archive disqualified ones with summaries.",
    agent=routing_agent,
    expected_output="JSON file containing routed and archived leads according to the RoutedAndArchivedLeads model.",
    output_pydantic=RoutedAndArchivedLeads,
    context=[qualify_leads_task],
    output_file="output/routed_and_archived_leads.json"
)
