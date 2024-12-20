

ASSYMETRIC_SHORT_LONG_TASK_GENERATOR = """Brainstorm a list of potentially useful text retrieval tasks.
Here are a few examples for your reference:
- Retrieve relevant documents for a short keyword web search query that asks for weather information.
- Search for documents that answers a FAQ-style query on children’s nutrition.
Please adhere to the following guidelines:
- Specify what the query is, and what the desired documents are.
- Each retrieval task should cover a wide range of queries, and should not be too specific.
Your output must always be a python list of strings only, with about 20 elements, and each element corresponds to a distinct
retrieval task in one sentence. Do not explain yourself or output anything else. Be creative!
"""

ASSYMETRIC_SHORT_LONG_GENERATOR= """You have been assigned a retrieval task: {task}
Your mission is to write one text retrieval example for this task in JSON format. The JSON object must contain the following
keys:
- "user_query": a string, a random user search query specified by the retrieval task.
- "positive_document": a string, a relevant document for the user query.
- "hard_negative_document": a string, a hard negative document that only appears relevant to the query.
Please adhere to the following guidelines:
- The "user_query" should be {query_type}, {query_length}, {clarity}, and diverse in topic.
- All documents must be created independent of the query. Avoid copying the query verbatim. It’s acceptable if some parts of
the "positive_document" are not topically related to the query.
- All documents should be at least {num_words} words long.
- The "hard_negative_document" contains some useful information, but it should be less useful or comprehensive compared
to the "positive_document".
- Both the query and documents should be in {language}.
- Do not provide any explanation in any document on why it is relevant or not relevant to the query.
- Both the query and documents require {difficulty} level education to understand.
Your output must always be a JSON object only, do not explain yourself or output anything else. Be creative!
"""

ASSYMETRIC_SHORT_LONG_PLACEHOLDERS = {
    'query_type': ["extremely long-tail", "long-tail", "common"],
    'query_length': ["less than 5 words", "5 to 15 words", "at least 10 words"],
    'difficulty': ["high school", "college", "PhD"],
    'clarity': ["clear", "understandable with some effort", "ambiguous"],
    'num_words': [50, 100, 200, 300, 400, 500],
}

ASSYMETRIC_LONG_SHORT_TASK_GENERATOR = """Brainstorm a list of potentially useful text classification tasks.
Please adhere to the following guidelines:
- Tasks should cover a diverse range of domains and task types.
Your output must always be a python list of strings only, with about 20 elements, and each element corresponds to a distinct
text classification task in one sentence. Do not explain yourself or output anything else. Be creative!
"""

ASSYMETRIC_LONG_SHORT_GENERATOR = """You have been assigned a text classification task: {task}
Your mission is to write one text classification example for this task in JSON format. The JSON object must contain the
following keys:
- "input_text": a string, the input text specified by the classification task.
- "label": a string, the correct label of the input text.
- "misleading_label": a string, an incorrect label that is related to the task.
Please adhere to the following guidelines:
- The "input_text" should be {num_words} words and diverse in expression.
- The "misleading_label" must be a valid label for the given task, but not as appropriate as the "label" for the "input_text".
- The values for all fields should be in {language}.
- Avoid including the values of the "label" and "misleading_label" fields in the "input_text", that would make the task too
easy.
- The "input_text" is {clarity} and requires {difficulty} level education to comprehend.
Your output must always be a JSON object only, do not explain yourself or output anything else. Be creative!"""


ASSYMETRIC_LONG_SHORT_PLACEHOLDERS = {
    'num_words': ["less than 10", "at least 10", "at least 50", "at least 100", "at least 200"],
    'difficulty': ["high school", "college", "PhD"],
    'clarity': ["clear", "understandable with some effort", "ambiguous"],
}

ASSYMETRIC_SHORT_SHORT_TASK_GENERATOR = """Brainstorm a list of text matching tasks where both the queries and the groundtruth documents are very short (one or two
sentences, even a short phrase).
Here are a few examples:
- Given a scientific paper title, retrieve the title of papers that cite the given paper.
- Match a word with its definition.
- Provided a notable person’s name, identify their occupation or achievement.
Your output must always be a python list of strings only, with about 20 elements, and each element corresponds to a distinct
task in one sentence. Do not explain yourself or output anything else. Be creative!
"""

ASSYMETRIC_SHORT_SHORT_GENERATOR = """You have been assigned a text matching task: {task}
Your mission is to write one example for this task in JSON format. The JSON object must contain the following keys:
- "input": a string, a random input specified by the task.
- "positive_document": a string, a relevant document for the "input" according to the task.
Please adhere to the following guidelines:
- The values of all fields should be in {language}.
- Both the "input" and "positive_document" should be very short (a sentence or a phrase), avoid substantial word overlaps,
otherwise the task would be too easy.
- The "input" and "positive_document" should be independent of each other.
Your output must always be a JSON object only, do not explain yourself or output anything else. Be creative!"""

ASSYMETRIC_LONG_LONG_TASK_GENERATOR = """Brainstorm a list of text matching tasks where the queries are long documents.
Here are a few examples:
- Given a document that supports a debatable argument, find another document that contains opposite arguments.
- Provided a lengthy business proposal, retrieve competitive business strategies in the same industry.
Your output must always be a python list of strings only, with about 20 elements, and each element corresponds to a distinct
task in one sentence. Do not explain yourself or output anything else. Be creative!"""

ASSYMETRIC_LONG_LONG_GENERATOR = """You have been assigned a text matching task: {task}
Your mission is to write one example for this task in JSON format. The JSON object must contain the following keys:
- "input": a string, a random input specified by the task.
- "positive_document": a string, a relevant document for the "input" according to the task.
Please adhere to the following guidelines:
- The values of all fields should be in {language}.
- Both the "input" and "positive_document" should be long documents (at least 300 words), avoid substantial word overlaps,
otherwise the task would be too easy.
- The "input" and "positive_document" should be independent of each other.
Your output must always be a JSON object only, do not explain yourself or output anything else. Be creative!
"""

MONOLINGUAL_STS_TASK_GENERATOR = """Write a {unit} triple with varying semantic similarity scores in JSON format. The semantic similarity score ranges from 1 to
5, with 1 denotes least similar and 5 denotes most similar.
Please adhere to the following guidelines:
- The keys in JSON are "S1", "S2", and "S3", the values are all strings in {language}, do not add any other keys.
- There should be some word overlaps between all three {unit}s.
- The similarity score between S1 and S2 should be {high_score}.
- The similarity score between S1 and S3 should be {low_score}.
- The {unit}s require {difficulty} level education to understand and should be diverse in terms of topic and length.
Your output must always be a JSON object only with three keys "S1", "S2" and "S3", do not explain yourself or output
anything else. Be creative!"""

MONOLINGUAL_STS_PLACEHOLDERS = {
    'high_score': [4, 4.5, 5],
    'low_score': [2.5, 3, 3.5],
    'unit': ["sentence", "phrase", "passage"],
    'difficulty': ["elementary school", "high school", "college"],
    'language': ["DANISH"],
}

BITEXT_RETRIEVAL_TASK_GENERATOR = """Write a {unit} triple with one {unit} in {src_lang} and two {unit}s in {tgt_lang} with varying translation qualities in JSON
format.
The triple is denotes as ("S1", "S2", "S3"). The translation quality score ranges from 1 to 5, with higher scores are better.
Please adhere to the following guidelines:
- The values of "S1" is a string in {src_lang}, the value of "S2" and "S3" are strings in {tgt_lang}.
- There should be some word overlaps between "S2" and "S3".
- The translation quality score of "S2" with respect to "S1" should be {high_score}.
- The translation quality score of "S3" with respect to "S1" should be {low_score}.
- "S3" should be grammatical and fluent, but contain some keyword or number translation errors, or miss some information,
or contain some redundant information.
- "S1" requires {difficulty} level education to understand and should be diverse in terms of topic and length.
Your output must always be a JSON object only with three keys "S1", "S2" and "S3", do not explain yourself or output
anything else. Be creative!"""

BITEXT_RETRIEVAL_PLACEHOLDERS = {
    'high_score': [4, 4.5, 5],
    'low_score': [1.5, 2, 2.5],
    'unit': ["sentence", "phrase", "passage"],
    'difficulty': ["elementary school", "high school", "college"],
    'src_lang': ["DANISH", "ENGLISH"],
    'tgt_lang': ["ENGLISH", "DANISH"],
}



ALL_PROMPTS = {
    "ASSYMETRIC_SHORT_LONG_TASK_GENERATOR": ASSYMETRIC_SHORT_LONG_TASK_GENERATOR,
    "ASSYMETRIC_SHORT_LONG_GENERATOR": ASSYMETRIC_SHORT_LONG_GENERATOR,
    "ASSYMETRIC_SHORT_LONG_PLACEHOLDERS": ASSYMETRIC_SHORT_LONG_PLACEHOLDERS,
    "ASSYMETRIC_LONG_SHORT_TASK_GENERATOR": ASSYMETRIC_LONG_SHORT_TASK_GENERATOR,
    "ASSYMETRIC_LONG_SHORT_GENERATOR": ASSYMETRIC_LONG_SHORT_GENERATOR,
    "ASSYMETRIC_LONG_SHORT_PLACEHOLDERS": ASSYMETRIC_LONG_SHORT_PLACEHOLDERS,
    "ASSYMETRIC_SHORT_SHORT_TASK_GENERATOR": ASSYMETRIC_SHORT_SHORT_TASK_GENERATOR,
    "ASSYMETRIC_SHORT_SHORT_GENERATOR": ASSYMETRIC_SHORT_SHORT_GENERATOR,
    "ASSYMETRIC_LONG_LONG_TASK_GENERATOR": ASSYMETRIC_LONG_LONG_TASK_GENERATOR,
    "ASSYMETRIC_LONG_LONG_GENERATOR": ASSYMETRIC_LONG_LONG_GENERATOR,
    #"MONOLINGUAL_STS_TASK_GENERATOR": MONOLINGUAL_STS_TASK_GENERATOR,
    #"MONOLINGUAL_STS_PLACEHOLDERS": MONOLINGUAL_STS_PLACEHOLDERS,
    #"BITEXT_RETRIEVAL_TASK_GENERATOR": BITEXT_RETRIEVAL_TASK_GENERATOR,
    #"BITEXT_RETRIEVAL_PLACEHOLDERS": BITEXT_RETRIEVAL_PLACEHOLDERS,
}