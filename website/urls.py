from django.urls import path

from .views import IndexView, AboutView    # .ドットは同じフォルダ内からviews.py（pyつけない）からviewを持ってこい

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
    # path('contact/', IndexView.as_view()),
]
