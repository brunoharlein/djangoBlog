from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

User = get_user_model()
# Pour récupérer le modèle utilisateur, on utilise la fonction get_user_model. Cette fonction va récupérer la valeur
# de la variable settings.AUTH_USER_MODEL


class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    # On utilise les paramètres verbose_name directement sur nos modèles. Cela permettra d'afficher les labels de nos
    # formulaires avec des mots français quand nous créerons les vues.
    # Le paramètre verbose_name est un moyen simple et efficace de modifier le nom affiché dans les différentes
    # interfaces (formulaires, interface d'administration...).
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # Pour le champ author, on utilise une clé étrangère avec le paramètre on_delete à SET_NULL. Vous trouverez de
    # nombreux tutoriels qui mettent par défaut models.CASCADE. Il est bien important de comprendre l'importance de ce
    # paramètre. Avec models.CASCADE, cela signifie que si vous supprimez l'utilisateur relié à vos articles,
    # les articles seront également supprimés ! Êtes-vous sûr que c'est vraiment le comportement souhaité ?
    # models.CASCADE est très pratique, mais il faut vraiment comprendre ce que l'on fait.
    last_updated = models.DateTimeField(auto_now=True)
    # Pour le champ last_updated, on passe le paramètre auto_now à True. Le champ sera mis à jour automatiquement
    # à chaque modification de l'article dans la base de données.
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    # ajout d'une classe Meta pour préciser notre modèle
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    # ajout de la méthode __str__ pour utiliser le titre des articles
    def __str__(self):
        return self.title

    # ajout du slug automatiquement en fonction du titre de l'article.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)
