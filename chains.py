# =========================
# chains.py
# =========================


from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


SYSTEM = (
"You are a precise study assistant.\n"
"- Always cite sources like [Title, p.X] after claims.\n"
"- If unsure, say so and suggest where to read.\n"
"- Prefer short bullets."
)


_prompt = ChatPromptTemplate.from_messages([
("system", SYSTEM),
("human", "Question: {question}\n\nContext:\n{context}"),
])




def build_chain(llm):
    return _prompt | llm | StrOutputParser()

