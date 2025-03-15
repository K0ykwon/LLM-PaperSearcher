class prompts:
    # CoT prompting (91 tokens)
    CoT = """ 
    Example(CoT):
    Question: We are working on a project related to artificial intelligence for medical imaging (CT) analysis.

    CoT:
    The focus is on medical imaging in the context of CT scans, which means we should incorporate CT imaging in the search term.
    The technology being used is artificial intelligence (AI), particularly focusing on deep learning or similar AI techniques.
    We want the search terms to be broad but still specific enough to guide us to research related to image analysis and segmentation.
    
    Response:
    "AI for CT image analysis" – This directly targets the use of AI techniques for analyzing CT images.
    "Deep learning in medical imaging" – A broader search term that includes various AI applications in medical imaging, including CT.
    "CT scan image segmentation using AI" – Focuses specifically on the task of segmenting CT images using AI techniques, a common application in medical image analysis.

    Answer:
    "AI for CT image analysis"
    "Deep learning in medical imaging"
    "CT scan image segmentation using AI"


    """

    # Few shot prompting (92 tokens)
    Few_shot = """
    Example(Few shot):
    Example 1: We are working on a project related to natural language processing (NLP) for sentiment analysis of social media posts.
    Response for Example 1:
    "NLP sentiment analysis social media"
    "Deep learning for sentiment analysis"
    "Social media text classification NLP"

    Example 2: We are developing an AI-based recommendation system for personalized shopping experiences.
    Response for Example 2:
    "AI recommendation system personalized shopping"
    "Collaborative filtering AI"
    "Deep learning for product recommendation"
    
    Example 3: We are working on a project related to medical imaging (CT) analysis using AI.
    Response for Example 3:
    "AI for CT image analysis"
    "Deep learning in medical imaging"
    "CT scan image segmentation using AI"


    """

    # role playing prompting (31 tokens)
    Role_Playing = """
    **English translation:**
    You are a co-researcher collaborating with the questioner. 
    Your colleague asked you for a relevant paper regarding the current topic, and you have recommended the following paper. 
    You need to explain the content of the paper to the questioner and inform them how relevant it is to their situation.


    """