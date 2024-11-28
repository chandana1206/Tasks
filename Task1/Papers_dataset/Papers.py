# from scholarly import scholarly
import pandas as pd

# def fetch_research_papers(query, num_papers, output_file):
    
#     papers = []
#     search_query = scholarly.search_pubs(query)
    
#     for i in range(num_papers):
#         try:
#             paper = next(search_query)
#             papers.append({
#                 "Title": paper['bib']['title'],
#                 "Authors": paper['bib']['author'],
#                 "Year": paper['bib']['pub_year'],
#                 "Journal": paper['bib'].get('journal', 'N/A'),
#                 "Citations": paper.get('num_citations', 0),
#                 "URL": paper.get('eprint_url', 'N/A')
#             })
#         except StopIteration:
#             print("No more papers found!")
#             break
    
#     df = pd.DataFrame(papers)
#     df.to_csv(output_file, index=False)
#     print(f"Data saved to {output_file}")

# fetch_research_papers("Artificial Intelligence", 100, "AI.csv")
# # fetch_research_papers("Machine Learning", 100, "ML.csv")
# # fetch_research_papers("Data Science", 100, "DS.csv")
# # fetch_research_papers("Neural Networks", 100, "NN.csv")
