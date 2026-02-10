import os
import ast
import numpy as np
import pandas as pd
import pandasai as pai
from pandasai import Agent
import matplotlib.pyplot as plt
from pandasai_openai import OpenAI

OUTPUT_DIR = "exports/charts_generated_using_python"
os.makedirs(OUTPUT_DIR, exist_ok = True)

movies = pd.read_csv('netflix_titles.csv', low_memory=False)

print(f"1. Dataset loaded: {movies.shape[0]} rows, {movies.shape[1]} columns")

movies["release_year"] = pd.to_numeric(movies["release_year"], errors="coerce")

print("\n2. Checking API key...")
api_key = os.environ.get('PANDASAI_API_KEY')
print(f"OPENAI_API_KEY value: {api_key}")

if not api_key:
    print("API key not found!")
print(api_key[:20])
   
llm = OpenAI(
    api_token=os.environ["PANDASAI_API_KEY"],
    model="gpt-3.5-turbo"  
)


pai.config.set({
    "llm": llm,
    "use_pandasai_api": False
})

agent = Agent(movies)

# STEP 4(b): RESEARCH QUESTION 1 


print("\n" + "="*80)
print("RESEARCH QUESTION 1: How has Netflixs content mix changed over time?")
print("="*80)

questions_rq1 = [
    "How many movies and TV shows are in the dataset?",
    "How has the number of movies vs TV shows changed over the years?",
    "Which release years have the most content on Netflix?"
]

for i, question in enumerate(questions_rq1, 1):
    print(f"\n{'─'*80}")
    print(f"Question 1.{i}: {question}")
    print(f"{'─'*80}")
    try:
        response = agent.chat(question)
        print(f"Answer: {response}")
    except Exception as e:
        print(f"Error: {e}")

# # STEP 4(b): RESEARCH QUESTION 2 - RATINGS & AUDIENCE

print("\n" + "="*80)
print("RESEARCH QUESTION 2: How do content ratings and duration characteristics differ between movies and TV shows on Netflix?")
print("="*80)

questions_rq2 = [
    "What are the most common rating categories for movies and TV shows on Netflix?",
    "What is the distribution of movie durations on Netflix?",
    "What is the distribution of the number of seasons for TV shows on Netflix?"
]

for i, question in enumerate(questions_rq2, 1):
    print(f"\n{'─'*80}")
    print(f"Question 2.{i}: {question}")
    print(f"{'─'*80}")
    try:
        response = agent.chat(question)
        print(f"Answer: {response}")
    except Exception as e:
        print(f"Error: {e}")


# # STEP 5: FOLLOW-UP QUESTIONS (DEEPER EXPLORATION)

print("\n" + "="*80)
print("RESEARCH QUESTION 3: Deeper Analysis on the dataset")
print("="*80)

followup_questions = [
    "Which countries produce the most Netflix content?",
    "What are the most common genres on Netflix?",
    "Has international content increased in recent years?"
]

for i, question in enumerate(followup_questions, 1):
    print(f"\n{'─'*80}")
    print(f"Question 3.{i}: {question}")
    print(f"{'─'*80}")
    try:
        response = agent.chat(question)
        print(f"Answer: {response}")
    except Exception as e:
        print(f"Error: {e}")

print("\n" + "="*80)
print("Conversation Complete!")
print("="*80)


# ============================================================================
# STEP 6: VISUALIZATIONS (PandasAI - Netflix Dataset)
# ============================================================================

print("\n" + "="*80)
print("STEP 6: VISUALIZATIONS USING PANDASAI")
print("="*80)

viz_questions = [

    # RQ1: Content Mix
    "Create a bar chart showing the number of Movies versus TV Shows on Netflix. "
    "Save the chart to 'exports/charts_generated_using_python/movies_vs_tvshows.png' "
    "and briefly summarize the insight.",

    # RQ1: Content over time
    "Create a line chart showing how many titles were released each year on Netflix. "
    "Save the chart to 'exports/charts_generated_using_python/content_over_time.png' "
    "and describe the overall trend.",

    # RQ2: Movie duration distribution
    "Create a histogram of movie durations (in minutes) on Netflix. "
    "Save the chart to 'exports/charts_generated_using_python/movie_duration_distribution.png' "
    "and describe the distribution.",

    # RQ2: TV show seasons
    "Create a bar chart showing the distribution of the number of seasons for TV shows on Netflix. "
    "Save the chart to 'exports/charts_generated_using_python/tv_show_seasons_distribution.png' "
    "and explain the pattern.",

    # RQ3: Country analysis
    "Show the top 10 countries producing Netflix content using a bar chart."
    "Save the chart to 'exports/charts_generated_using_python/top_countries.png' "
    "and explain which countries dominate."
]

for i, question in enumerate(viz_questions, 1):
    print(f"\n{'─'*80}")
    print(f"Visualization {i}")
    print(f"{'─'*80}")
    try:
        response = agent.chat(question)
        print(f"Answer: {response}")
    except Exception as e:
        print(f"Error: {e}")

# FALLBACK VISUALIZATION: Top Countries (Pandas)
countries = movies["country"].dropna().str.split(", ")
countries_exploded = countries.explode()

top_countries = countries_exploded.value_counts().head(10)

plt.figure(figsize=(10, 5))
top_countries.plot(kind="bar")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.title("Top 10 Content Producing Countries on Netflix")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/top_countries.png")
plt.close()

print("Fallback visualization saved: top_countries.png")

print("\n" + "="*80)
print("VISUALIZATION STEP COMPLETE!")
print("="*80)
