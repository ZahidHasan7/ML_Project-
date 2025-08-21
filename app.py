from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the pickle files
popular_df = pickle.load(open('popular.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
books = pickle.load(open('books.pkl', 'rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))

app = Flask(__name__)

# --- Routes ---

@app.route('/')
def index():
    """
    Renders the home page with the top 50 most popular books.
    Passes book details to the template.
    """
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           # CORRECTED: Use the numpy array's round method
                           rating=list(popular_df['avg_rating'].values.round(2))
                           )

@app.route('/recommend')
def recommend_ui():
    """
    Renders the recommendation page.
    Passes the list of all book titles for the dropdown.
    """
    return render_template('recommend.html',
                           book_list=list(pt.index))

@app.route('/recommend_books', methods=['post'])
def recommend():
    """
    Handles the book recommendation logic based on user input.
    """
    user_input = request.form.get('user_input')
    data = []

    try:
        # Find the index for the user's selected book
        index = np.where(pt.index == user_input)[0][0]
        # Get top 4 similar items (and skip the first one, which is the book itself)
        similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

        # Collect data for the recommended books
        for i in similar_items:
            item = []
            # Get the book details from the main 'books' dataframe
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            
            # Use drop_duplicates once to be more efficient
            unique_book = temp_df.drop_duplicates('Book-Title')
            
            item.extend(list(unique_book['Book-Title'].values))
            item.extend(list(unique_book['Book-Author'].values))
            item.extend(list(unique_book['Image-URL-M'].values))
            
            data.append(item)
    except IndexError:
        # This block will execute if the book is not found, preventing a crash.
        # For this app, the dropdown prevents this, but it's good practice.
        print(f"Book '{user_input}' not found in the pivot table.")
        # You could pass an error message to the template here if you want.
        pass

    return render_template('recommend.html',
                           data=data,
                           book_list=list(pt.index)) # Pass the list again to repopulate the dropdown

if __name__ == '__main__':
    # MODIFIED: Changed the port to 5001 to avoid conflicts
    app.run(debug=True, port=5001)