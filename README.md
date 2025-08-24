## Book Recommender System 📚

A web-based book recommendation system that suggests books to users based on overall popularity and personalized collaborative filtering. This project is built with Python, Pandas, and Scikit-learn, with a user-friendly interface created using Flask.

## 🚀 Live Demo
You can view the live deployed application here:
 (https://book-recommender-system-v20n.onrender.com/)

## Features
This recommender system operates in two modes:

🌟 Popularity-Based Recommendations: Provides a list of the top 50 most popular and highly-rated books. This is perfect for new users who are looking for a generally good read.

🤝 Collaborative Filtering Recommendations: When a user selects a book they like, the system suggests similar books. This personalized recommendation is based on the preferences of other users who also enjoyed the selected book (Item-Based Collaborative Filtering).

## Screenshots
Here's a glimpse of the application in action.

Homepage & Top 50 Books:

A user can browse the most popular books or select one to get recommendations.
   ![Alt text](https://github.com/ZahidHasan7/Book_Recommender_System/blob/main/book%201.PNG)
   
 

Recommendation Results:

After selecting a book, the system displays a list of similar books with their covers and authors.
   ![Alt text](https://github.com/ZahidHasan7/Book_Recommender_System/blob/main/book%202.PNG)
  

## Technologies Used
Backend: Python, Flask

Data Manipulation: Pandas, NumPy

Machine Learning: Scikit-learn (for K-Nearest Neighbors and Cosine Similarity)

Deployment: Gunicorn, Render

Dataset: Book-Crossing Dataset on Kaggle

## How It Works
The recommendation logic is based on two different models:

1. Popularity-Based Model
This model identifies books that are both highly rated and have a significant number of ratings.

Books with less than 250 total ratings are filtered out to ensure statistical significance.

The remaining books are ranked based on their average rating.

The top 50 books from this list are presented to the user.

2. Collaborative Filtering Model
This model finds books that are "similar" based on user rating patterns.

A user-item matrix is created from the ratings data, with users as rows and book titles as columns.

The matrix is extremely sparse, so it's filtered to include only users who have rated more than 200 books.

Cosine Similarity is used to calculate a similarity score between every pair of books.

When a user selects a book, the system retrieves the top 5 most similar books from the pre-computed similarity matrix to provide a personalized recommendation.

## How to Run This Project Locally
To set up and run this project on your local machine, follow these steps:

Clone the repository:

Bash
[
git clone (https://github.com/ZahidHasan7/Book_Recommender_System.git) ] 

cd Book_Recommender_System

Create a virtual environment:

Bash

python -m venv venv
source venv/bin/activate  

## On Windows, use `venv\Scripts\activate`
Install the required dependencies:

##Bash

pip install -r requirements.txt'

Run the Flask application:

##Bash

python app.py


Open your web browser and navigate to http://127.0.0.1:5000 to see the application.

## Acknowledgements
This project is based on the Book-Crossing Dataset.

Inspiration and guidance from various data science and web development tutorials.
