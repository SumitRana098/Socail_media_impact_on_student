# Data Science Project

This project analyzes student social media addiction data using Python and Streamlit. It includes scripts for loading, processing, visualizing, and generating insights from the data.

## Project Structure

```
data-science-project
├── src
│   └── social_media_combat.py      # Main script for data processing, analysis, and Streamlit dashboard
├── data
│   └── Students Social Media Addiction (1) copy.csv  # Dataset for analysis
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd data-science-project
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Streamlit dashboard:**
   Execute the following command to start the interactive dashboard:
   ```
   streamlit run src/social_media_combat.py
   ```

## Purpose

The purpose of this project is to provide a framework for data analysis using Python. It serves as a template for data science projects, allowing users to easily load and manipulate datasets, perform analyses, and visualize results.

## Insights from Social Media Addiction Data

1. **Average Daily Usage**  
   - Undergraduate students and high schoolers tend to have higher average daily social media usage compared to graduates.
   - Females generally spend more time on social media than males.

2. **Platform Popularity**  
   - Instagram and TikTok are the most popular platforms among younger age groups.
   - LinkedIn and Twitter are more popular among graduate students.

3. **Academic Impact**  
   - Students who report that social media affects their academic performance tend to have higher average daily usage.

4. **Sleep & Mental Health**  
   - There is a negative correlation between addiction score and sleep hours, suggesting higher addiction may reduce sleep.
   - Countries with higher average daily usage also tend to have lower average mental health scores.

5. **Addiction Score Patterns**  
   - TikTok and Instagram users have higher average addiction scores.
   - Addiction scores are higher among students in complicated relationships.

6. **Relationship Status**  
   - Students in relationships or with complicated relationship status show higher social media usage and addiction scores.

7. **Conflicts Over Social Media**  
   - A significant number of students report having conflicts over social media, especially those with higher usage and addiction scores.

8. **Country Comparison**  
   - Usage and addiction scores vary by country, with some countries showing notably higher averages.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.