from django.shortcuts import render
from joblib import load
model = load('./model')
# Create your views here.

def home(request):
    if request.method == 'GET':
        try:
            online_book = int(request.GET.get('Online Booking'))
            Book_Table = int(request.GET.get('Book-table'))
            votes = request.GET.get('votes')
            location = int(request.GET.get('location'))
            rest_type = int(request.GET.get('rest_type'))
            like = request.GET.get('liked')
            cuisines = int(request.GET.get('cuisines'))
            cost = request.GET.get('cost')  # Assuming this is a string field
            area = int(request.GET.get('area'))  # Assuming this is an integer field

            # Make predictions using the model
            y_pred = model.predict([[online_book, Book_Table, votes, location, rest_type, like, cuisines, cost, area]])

            # Return the result along with the form data
            return render(request, 'index.html', {'result': y_pred, 'form_submitted': True})

        except (ValueError, TypeError) as e:
            # Handle conversion errors or missing values
            return render(request, 'index.html', {'error': str(e)})

    # If the request method is not GET, render the form page
    return render(request, 'index.html')