import requests
from bs4 import BeautifulSoup

def get_movies_by_genre(genres):
    genre_url = '+'.join(genres)
    url = f"https://www.imdb.com/search/title/?genres={genre_url}&start=1&explore=genres&ref_=adv_nxt"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    movie_items = soup.find_all('div', class_='lister-item-content')
    movies = []
    for item in movie_items:
        title = item.find('a').text
        image_element = item.find('img')
        image = image_element['src'] if image_element else None
        
        cast_element = item.find('p', class_='').text.strip().split(':')
        if len(cast_element) == 2:
            cast = cast_element[1].split(',')
        else:
            cast = None
        
        synopsis = item.find_all('p', class_='text-muted')[1].text.strip()
        rating_element = item.find('div', class_='ratings-bar')
        rating = rating_element.strong.text.strip() if rating_element and rating_element.strong else None
        
        movies.append({'title': title, 'image': image, 'cast': cast, 'synopsis': synopsis, 'rating': rating})
        
    return movies[:20]

# Prompt the user to enter genres separated by spaces
# user_input = input("Enter genres separated by spaces: ")
# genres = user_input.split()

# # Get recommended movies
# recommended_movies = get_movies_by_genre(genres)

# # Display the information for each movie
# for movie in recommended_movies:
#     print("Title:", movie['title'])
#     print("Image:", movie['image'])
#     if movie['cast']:
#         print("Cast:", ', '.join(movie['cast']))
#     else:
#         print("Cast: N/A")
#     print("Synopsis:", movie['synopsis'])
#     print("Rating:", movie['rating'])
#     print()
