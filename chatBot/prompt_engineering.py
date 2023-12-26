from langchain import PromptTemplate


def prompt_engineering(question: str):
    prompt = PromptTemplate.from_template("""
    You are a helpful assistant, Perform the following task: 
    
    1- Answer this question: {question}
    """)
    return prompt.format(question=question)


"""
if _name_ == "_main_":
    print(prompt_engineering(question="give me a summary"))
"""