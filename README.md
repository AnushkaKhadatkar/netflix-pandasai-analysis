# 🎬 Netflix Data Analysis with PandasAI

> Exploring 8,000+ Netflix titles using natural language data analysis

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PandasAI](https://img.shields.io/badge/PandasAI-1.5+-green.svg)](https://github.com/gventuri/pandas-ai)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Medium](https://img.shields.io/badge/Medium-Blog%20Post-black.svg)](YOUR_MEDIUM_LINK_HERE)

## 🎯 Overview

This project demonstrates the power of **PandasAI**—a Python library that enables natural language data analysis. Instead of writing complex pandas code, you can simply ask questions in plain English and get instant visualizations and insights.

Using Netflix's content library dataset (8,807 titles), I explored content strategy, production patterns, and geographic distribution through conversational AI.

**Research Questions:**
1. How has Netflix's content strategy evolved over time?
2. What patterns exist in content duration and format?
3. Where does Netflix's content come from geographically?

## 🔍 Key Findings

### 1. Movies Dominate the Platform (69%)
- **6,131 movies** vs **2,676 TV shows**
- Strategy: Rapid content expansion through film licensing

### 2. Explosive Growth After 2015
- Flat content additions pre-2015
- **Sharp increase** starting 2015-2016
- Peak additions around 2017-2019
- Aligns with Netflix's original content pivot

### 3. Standard Movie Lengths Preferred
- Most movies: **90-120 minutes**
- Normal distribution centered at ~100 minutes
- Optimized for single-sitting viewing

### 4. Limited Series Strategy for TV
- Majority of TV shows have **only 1 season**
- Preference for self-contained narratives
- Lower production risk, higher experimentation

### 5. US-Centric with Growing Global Presence
- **United States**: Dominant producer (3,000+ titles)
- **India**: Significant second contributor
- Growing international production (UK, South Korea, Canada)

## 🚀 Installation

### Prerequisites

- Python 3.9 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/netflix-pandasai-analysis.git
cd netflix-pandasai-analysis

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## 📁 Project Structure

```
netflix-pandasai-analysis/
│
├── data/
│   ├── netflix_titles.csv          # Dataset (download separately)
│
├── src/
│   ├── netflix_pandasai.py                  
│
├── visualizations/
│   ├── viz1_movies_vs_tv.png
│   ├── viz2_content_timeline.png
│   ├── viz3_movie_durations.png
│   ├── viz4_tv_seasons.png
│   └── viz5_top_countries.png
│
├── requirements.txt
├── LICENSE
└── README.md
```

## 📊 Data

**Source:** [Netflix Shows Dataset on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

**Dataset Details:**
- **Size:** 8,807 titles
- **Features:** 12 columns
  - `show_id`: Unique identifier
  - `type`: Movie or TV Show
  - `title`: Name of the content
  - `director`: Director(s)
  - `cast`: Main cast
  - `country`: Production country
  - `date_added`: Date added to Netflix
  - `release_year`: Original release year
  - `rating`: Content rating (PG, TV-MA, etc.)
  - `duration`: Movie runtime or TV show seasons
  - `listed_in`: Genres
  - `description`: Synopsis

## 📈 Results

### Performance Comparison

| Metric | Traditional Pandas | PandasAI | Improvement |
|--------|-------------------|----------|-------------|
| **Time per query** | 15-30 min | 1-2 min | **90% faster** |
| **Code lines** | 10-30 lines | 1 line | **95% reduction** |
| **Syntax errors** | Common | Rare | **Minimal debugging** |
| **Accessibility** | Requires coding | Natural language | **Anyone can analyze** |

### Visualizations

<details>
<summary>Click to view all visualizations</summary>

#### 1. Content Type Distribution
![Movies vs TV Shows](visualizations/viz1_movies_vs_tv.png)

#### 2. Temporal Trends
![Content Timeline](visualizations/viz2_content_timeline.png)

#### 3. Movie Duration Distribution
![Movie Durations](visualizations/viz3_movie_durations.png)

#### 4. TV Show Seasons
![TV Seasons](visualizations/viz4_tv_seasons.png)

#### 5. Geographic Distribution
![Top Countries](visualizations/viz5_top_countries.png)

</details>

## 📝 Blog Post

I wrote a comprehensive Medium blog post about this analysis:

**[Analyzing Netflix with PandasAI: Data Science in Plain English](YOUR_MEDIUM_LINK_HERE)**


## 👤 Contact

**Your Name**
- GitHub: https://github.com/AnushkaKhadatkar
- LinkedIn: https://www.linkedin.com/in/anushka-khadatkar/
- Medium: [@YOUR_MEDIUM](https://medium.com/@YOUR_MEDIUM)
- Email: anushkak1202@gmail.com

---

<div align="center">


Made with ❤️ and PandasAI

</div>


![GitHub stars](https://img.shields.io/github/stars/YOUR_USERNAME/netflix-pandasai-analysis?style=social)
![GitHub forks](https://img.shields.io/github/forks/YOUR_USERNAME/netflix-pandasai-analysis?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/YOUR_USERNAME/netflix-pandasai-analysis?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/netflix-pandasai-analysis)
![GitHub issues](https://img.shields.io/github/issues/YOUR_USERNAME/netflix-pandasai-analysis)
