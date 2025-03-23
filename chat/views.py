from django.shortcuts import render
from django.http import JsonResponse
from chat.models import KeyPair


def get_public_key(request, user_id):
    try:
        key_pair = KeyPair.objects.get(user_id=user_id)
        return JsonResponse({"public_key": key_pair.public_key})
    except KeyPair.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

