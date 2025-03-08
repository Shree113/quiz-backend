from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Disable CSRF for now
def login_user(request):
    if request.method == 'POST':
        try:
            print("Raw Request Body:", request.body)

            data = json.loads(request.body)  # Parse JSON
            username = data.get('username', '').strip()
            password = data.get('password', '').strip()

            if not username or not password:
                return JsonResponse({'error': 'Username and password required'}, status=400)

            print("Checking user:", username)

            user = authenticate(username=username, password=password)

            if user:
                return JsonResponse({'message': 'Login successful'})
            else:
                return JsonResponse({'error': 'Invalid username or password'}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'error': 'Only POST requests allowed'}, status=405)
