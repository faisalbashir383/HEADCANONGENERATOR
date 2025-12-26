"""
Views for the Headcanon Generator.
"""

import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from .headcanon_engine import generate_headcanons, get_tone_options, get_popular_fandoms


def index(request):
    """Render the main headcanon generator page."""
    context = {
        'tones': get_tone_options(),
        'fandoms': get_popular_fandoms(),
    }
    return render(request, 'index.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def generate(request):
    """API endpoint to generate headcanons."""
    try:
        data = json.loads(request.body)
        character = data.get('character', '').strip()
        
        if not character:
            return JsonResponse({
                'success': False,
                'error': 'Character name is required'
            }, status=400)
        
        fandom = data.get('fandom', '').strip() or None
        tone = data.get('tone', 'random').lower()
        
        # Validate tone
        valid_tones = ['wholesome', 'funny', 'dark', 'emotional', 'random']
        if tone not in valid_tones:
            tone = 'random'
        
        headcanons = generate_headcanons(
            character=character,
            fandom=fandom,
            tone=tone,
            count=4
        )
        
        return JsonResponse({
            'success': True,
            'headcanons': headcanons,
            'character': character,
            'tone': tone
        })
        
    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'error': 'Invalid JSON data'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': 'An error occurred while generating headcanons'
        }, status=500)


def about(request):
    """Render the about page."""
    return render(request, 'about.html')


def privacy(request):
    """Render the privacy policy page."""
    return render(request, 'privacy.html')


def terms(request):
    """Render the terms of service page."""
    return render(request, 'terms.html')


def contact(request):
    """Render the contact page."""
    return render(request, 'contact.html')


def what_is_headcanon(request):
    """Render the 'What is Headcanon?' page."""
    return render(request, 'what-is-headcanon.html')


def canon_vs_headcanon(request):
    """Render the 'Canon vs Headcanon' page."""
    return render(request, 'canon-vs-headcanon.html')


def headcanon_examples(request):
    """Render the 'Headcanon Examples' page."""
    return render(request, 'headcanon-examples.html')


def random_headcanon_generator(request):
    """Render the 'Random Headcanon Generator' page."""
    return render(request, 'random-headcanon-generator.html')


def character_headcanon_generator(request):
    """Render the 'Character Headcanon Generator' page."""
    return render(request, 'character-headcanon-generator.html')


def anime_headcanon_generator(request):
    """Render the 'Anime Headcanon Generator' page."""
    return render(request, 'anime-headcanon-generator.html')
