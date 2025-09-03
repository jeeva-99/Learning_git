from rest_framework .response import Response

def response_generator(success,message,data=None,status_code=200):
    return Response(
        {
            "success":success,
            "message":message,
            "data": data or []
        },status_code
    )