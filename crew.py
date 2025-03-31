from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from agents import collector_agent, qualification_agent, routing_agent
from tasks import collect_leads_task, qualify_leads_task, route_leads_task

@CrewBase
class LeadManagementCrew():
    """Lead Management Crew"""

    @agent
    def collector(self) -> Agent:
        """Returns the Collector Agent"""
        return collector_agent 

    @agent
    def qualifier(self) -> Agent:
        """Returns the Qualification Agent"""
        return qualification_agent  
    @agent
    def router(self) -> Agent:
        """Returns the Routing Agent"""
        return routing_agent  

    @task
    def collect_leads_task(self) -> Task:
        """Returns the Collect Leads Task"""
        return collect_leads_task  
    @task
    def qualify_leads_task(self) -> Task:
        """Returns the Qualify Leads Task"""
        return qualify_leads_task  
    @task
    def route_leads_task(self) -> Task:
        """Returns the Route Leads Task"""
        return route_leads_task  

    @crew
    def crew(self) -> Crew:
        """Creates the Lead Management Crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks,  
            process=Process.sequential, 
            verbose=True,  
        )
