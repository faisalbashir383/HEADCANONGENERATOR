"""
URL configuration for generator app.
"""

from django.urls import path
from . import views

app_name = 'generator'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/generate/', views.generate, name='generate'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
    # SEO content pages
    path('what-is-headcanon/', views.what_is_headcanon, name='what_is_headcanon'),
    path('canon-vs-headcanon/', views.canon_vs_headcanon, name='canon_vs_headcanon'),
    path('headcanon-examples/', views.headcanon_examples, name='headcanon_examples'),
    path('random-headcanon-generator/', views.random_headcanon_generator, name='random_headcanon_generator'),
    path('character-headcanon-generator/', views.character_headcanon_generator, name='character_headcanon_generator'),
    path('anime-headcanon-generator/', views.anime_headcanon_generator, name='anime_headcanon_generator'),
    path('ship-headcanon-generator/', views.ship_headcanon_generator, name='ship_headcanon_generator'),
    path('api/generate-ship/', views.generate_ship, name='generate_ship'),
    # New SEO content pages
    path('how-to-write-headcanons/', views.how_to_write_headcanons, name='how_to_write_headcanons'),
    path('headcanon-prompts/', views.headcanon_prompts, name='headcanon_prompts'),
    path('funny-headcanon-ideas/', views.funny_headcanon_ideas, name='funny_headcanon_ideas'),
    path('emotional-headcanons-guide/', views.emotional_headcanons_guide, name='emotional_headcanons_guide'),
    path('headcanon-vs-fanfiction/', views.headcanon_vs_fanfiction, name='headcanon_vs_fanfiction'),
    path('fandom-culture-headcanons/', views.fandom_culture_headcanons, name='fandom_culture_headcanons'),
]
