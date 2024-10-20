from django.http import HttpResponse


def homepage(request):
    return HttpResponse(
        """
        <h1>Welcome to polls application!</h1>
        <ul>
            <li><a href="/polls/">Go to Polls</a></li>
            <li><a href="/admin/">Go to Admin</a></li>
        </ul>
    """
    )
