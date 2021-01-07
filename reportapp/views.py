import csv
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from django.http import HttpResponse

from rant_post.models import RantPost


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def export_rants(request):
    """ return all rants posted by a user in a csv file """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="posts.csv"'

    feelings_dict = {
        'S': 'Sad',
        'VS': 'Very Sad',
        'N': 'Neutral',
        'P': 'Pissed',
        'EP': 'Extremely Pissed',
        'FF': 'Fucking Furious'
    }
    
    posts = RantPost.objects.filter(author=request.user)

    writer = csv.writer(response)
    writer.writerow(['Title', 'Body', 'Feeling Level', 'Created Date', 'Created Time'])
    for post in posts:
        writer.writerow([ post.title, post.text, feelings_dict[post.feeling_level], post.created_on.date(), post.created_on.time() ])

    return response

