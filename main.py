from LLM import generateST
from parser import searchPaper
from LLM import SummarizePP


if __name__ == "__main__":
    
    prompt_tech = ''
    prompt = input('Please enter your research topic or the paper you are looking for!\n')
    if input('use CoT prompts during the paper search process?(y/n)') == 'y': prompt_tech += "CoT"
    if input('use few shot prompt during the paper search process?(y/n)') == 'y': prompt_tech += "Few_Shot"
    if input('use role playing prompt during the paper summarize process?(y/n)') == 'y': prompt_tech += "role_playing"
    d = int(input('input depth for searching(recommand: 3): '))
    print("Searching Papers...")
    terms = generateST(prompt, prompt_tech).Terms
    papers = []
    for i in terms:
        print("    - ",i)
        _ = searchPaper(i,d)
        papers = papers + [x for x in _ if x not in papers]
    print(len(papers)," Papers detected!")
    

    for paper in papers:
        print("\nPaper: ", paper["Title"])
        print("Author: ",end='')
        for arth in paper["Author"]:
            print(arth, end = ' ')
        print("\nLink: ", paper["Link"], end = '\n')

        Paper_info = SummarizePP(prompt,paper, prompt_tech)
        print("Description: ", Paper_info.description)
        print("Relevance", Paper_info.Relevance,"%")
        print()
