import numpy as np
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder


def register(request):
    if request.method == 'POST':
        # Handle registration form submission
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})

        # Create a new user with the provided details
        #

            # Handle authentication failure
        return render(request, 'travel_preferences.html', {'error': 'Failed to register'})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        # Handle login form submission
        # Example:
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Authenticate the user and redirect to appropriate page
        return redirect('travel_preferences')
    else:
        return render(request, 'login.html')

def password_recovery(request):
    if request.method == 'POST':
        # Handle password recovery form submission
        # Example:
        email = request.POST.get('email')
        # Send password recovery email
        # Redirect to a success page or render a template
    else:
        return render(request, 'password_recovery.html')


def import_data_from_csv():
    attractions_df = pd.read_csv('media/dest.csv')
    restaurants_df = pd.read_csv('media/bobby_cleaned.csv')
    print(attractions_df.head())
    print(restaurants_df.head())
    print("Data imported successfully")
    return attractions_df, restaurants_df




from django.shortcuts import render
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

def import_data_from_csv():
    attractions_df = pd.read_csv('media/dest.csv')
    restaurants_df = pd.read_csv('media/bobby_cleaned.csv')
    return attractions_df, restaurants_df

def train_ml_model(restaurants_df):
    # Use RandomForestRegressor to train a model
    le = LabelEncoder()
    restaurants_df['Location'] = le.fit_transform(restaurants_df['Location'])
    return RandomForestRegressor().fit(restaurants_df[['Location']], restaurants_df['Review'])

def predict_best_restaurants(restaurant_model, restaurants_df, num_restaurants=5):
    # Perform predictions using the trained model
    restaurants_df['predicted_review'] = restaurant_model.predict(restaurants_df[['Location']])
    # Sort restaurants by predicted review
    best_restaurants = restaurants_df.sort_values(by='predicted_review', ascending=False).head(num_restaurants)
    return best_restaurants

def travel_preferences(request):
    if request.method == 'POST':
        destination = request.POST.get('destination')
        budget = request.POST.get('budget')
        num_travelers = request.POST.get('num_travelers')
        num_female_travelers = request.POST.get('num_female_travelers')

        # Load data
        attractions_df, restaurants_df = import_data_from_csv()

        # Train ML model using restaurant data
        restaurant_model = train_ml_model(restaurants_df)

        # Predict best restaurants
        best_restaurants = predict_best_restaurants(restaurant_model, restaurants_df)
        restaurants_with_ratings = []
        # Precompute star ratings
        for restaurant in best_restaurants:
            star_rating= np.random.randint(1, 6)

            restaurant_with_rating = {
                'name': "Biverlly hills hotel", #restaurant['name'], # "Biverlly hills hotel
                'location': "Biverlly hills", #restaurant['location'], # "Biverlly hills
                'star_rating': star_rating
            }

            # Append the restaurant with its rating to the list
            restaurants_with_ratings.append(restaurant_with_rating)


        # Mock data for hotels, laws, crime records, and climatic conditions
        recommended_hotel = {'name': 'Sample Hotel', 'location': 'Sample Location'}
        laws = 'Sample laws and regulations'
        crime_records = 'Sample crime records'
        top_crimes = 'Sample top crimes'
        climatic_season_condition = 'Sample climatic season and condition'

        # Render template with data
        data = {
            'destination': destination,
            'budget': budget,
            'num_travelers': num_travelers,
            'num_female_travelers': num_female_travelers,
            'best_restaurants': best_restaurants,
            'recommended_hotel': recommended_hotel,
            'laws': laws,
            'crime_records': crime_records,
            'top_crimes': top_crimes,
            'climatic_season_condition': climatic_season_condition,
            'restaurants_with_ratings': restaurants_with_ratings

        }

        return render(request, 'travelplan.html', data)
    else:
        return render(request, 'travel_preferences.html')


