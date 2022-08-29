from django.views.generic.edit import CreateView
from models import Autor

class AuthorCreateView(CreateView):
    model = Autor
    fields = '__all__'
