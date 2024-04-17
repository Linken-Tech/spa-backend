def request_user(request):
    user_auth = request.user
    try:
        if user_auth.is_anonymous:
            return None
        return request.user.user
    except Exception:
        return None
