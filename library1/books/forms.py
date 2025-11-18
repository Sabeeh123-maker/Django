from django import forms
#
# class Bookform(forms.Form):
#
#     title=forms.CharField()
#     author=forms.CharField()
#     price=forms.IntegerField()
#     pages=forms.IntegerField()
#     language=forms.CharField()

from books.models import Book

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class Viewform(forms.Form):
    bookid=forms.CharField()
