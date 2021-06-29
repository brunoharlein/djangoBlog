from django.contrib import admin

from posts.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published", "created_on", "last_updated")
    list_editable = ("published",)
    # list_display et list_editable nous permettent de spécifier les champs de notre modèle que nous souhaitons
    # afficher et ceux qu'il sera possible d'éditer directement
    # depuis la vue de l'interface d'administration contenant tous les articles.


admin.site.register(BlogPost, BlogPostAdmin)
