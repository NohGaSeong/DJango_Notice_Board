<<<<<<< HEAD
<<<<<<< HEAD
=======
from attr import field, fields
>>>>>>> c69a391b19be050031c8f66627f4b012eb688760
=======
from attr import field, fields
>>>>>>> c69a391b19be050031c8f66627f4b012eb688760
from django import forms
from pybo.models import Answer, Question

class QuestionForm(forms.ModelForm):
    class Meta:
<<<<<<< HEAD
<<<<<<< HEAD
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }  
=======
=======
>>>>>>> c69a391b19be050031c8f66627f4b012eb688760
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }
<<<<<<< HEAD
>>>>>>> c69a391b19be050031c8f66627f4b012eb688760
=======
>>>>>>> c69a391b19be050031c8f66627f4b012eb688760

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
<<<<<<< HEAD
<<<<<<< HEAD
            'content': '답변내용',
=======
            'content' : '답변내용',
>>>>>>> c69a391b19be050031c8f66627f4b012eb688760
=======
            'content' : '답변내용',
>>>>>>> c69a391b19be050031c8f66627f4b012eb688760
        }