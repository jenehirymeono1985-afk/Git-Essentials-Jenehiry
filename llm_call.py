def generate_prompt():
    """
    Revised prompt asking for standard Markdown code block,
    which is more reliable than custom tags.
    """
    return f"""write the python code to calculate
a loan payment with the following inputs: interest,
term, present value. return code only wrapped in a Markdown code block (triple backticks). Do not add any extra text or explanation outside the code block.
"""