from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.memory import ConversationBufferMemory

from tools.file_reader import file_reader_tool
from models.hf_model import load_hf_llm

from dotenv import load_dotenv
load_dotenv()

def get_agent():
    llm = load_hf_llm()

    tools = [
        file_reader_tool,              # already a @tool
        TavilySearchResults()          # predefined tool
    ]

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        memory=memory,
        agent_type=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    return agent
