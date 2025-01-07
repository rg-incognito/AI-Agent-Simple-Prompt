from crewai import Agent, Task, Crew, Process
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "llama3.1",
    base_url = "http://localhost:11434")

rohit = Agent(role = 'Physics teacher',
              goal = 'Tech student with updated concepts of quantum physics',
              backstory = 'Have a phd in Quantum physics and had been working as teacher for 20 years at Oxford university',
              verbose = True,
              allow_delegation = True,
              llm = llm
              )
task = Task(description = 'Teach me atomic structure of Helium',
            agent = rohit,
            expected_output = 'The electronic configuration is as follow .....')
crew = Crew(
    agents = [rohit],
    tasks = [task],
    verbose = 2,
    process = Process.sequential
)
result = crew.kickoff();
print('#######################################')
print(result)
