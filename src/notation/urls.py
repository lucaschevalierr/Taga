from django.urls import path
from .views import index, notes, profile, post_note, profile_modif, post_profile

urlpatterns = [
    path('', index, name="notation-index"),
    path('notes/', notes, name="notation-notes"),
    path('profile/', profile, name="notation-profile"),
    path('postNote/', post_note, name="notation-postNote"),
    path('postProfile/', post_profile, name="notation-postProfile"),
    path('profileModif/', profile_modif, name="notation-profile_modif"),

]
