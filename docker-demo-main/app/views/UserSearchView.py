from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class UserSearchView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        page = request.data.get('page', 1)
        
        if not username and not email:
            return Response({"error": "Please provide either a username or an email."}, status=status.HTTP_400_BAD_REQUEST)
        
        if username and email:
            return Response({"error": "Please provide either a username or an email, not both."}, status=status.HTTP_400_BAD_REQUEST)
        
        query = username or email
        field = 'username' if username else 'email'

        # Determine if the requesting user is a staff member
        is_staff_user = request.user.is_staff
        
        # Define the base query for exact matches and potential matches
        exact_match_query = {f"{field}__iexact": query}
        potential_match_query = {f"{field}__icontains": query}
        
        # If the requesting user is not a staff member, exclude staff users from the search results
        if not is_staff_user:
            exact_match_query["is_staff"] = False
            potential_match_query["is_staff"] = False
        
        # Try to find an exact match
        exact_match = User.objects.filter(**exact_match_query).first()
        
        if exact_match:
            return Response({
                "exact_match": {
                    "id": exact_match.id,
                    "username": exact_match.username,
                    "email": exact_match.email
                }
            })
        
        # If no exact match, find potential matches
        potential_matches = User.objects.filter(**potential_match_query).order_by('username')
        
        # Paginate the results
        paginator = Paginator(potential_matches, 10)  # 10 results per page
        
        try:
            current_page = paginator.page(page)
        except Exception:
            return Response({"error": "Invalid page number."}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            "potential_matches": {
                "results": list(current_page.object_list.values_list('username', flat=True)),
                "current_page": current_page.number,
                "num_pages": paginator.num_pages,
                "has_next": current_page.has_next(),
                "has_previous": current_page.has_previous(),
                "next_page_number": current_page.next_page_number() if current_page.has_next() else None,
                "previous_page_number": current_page.previous_page_number() if current_page.has_previous() else None,
                "per_page": 10,
                "total_results": paginator.count,
                "page_range": list(paginator.page_range)
            }
        })