from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.

class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    ## on_delete=models.SET_NULL 회원 탈퇴를 했을때 article이 그 게시글이 사라지않고 그냥 알 수 없음 이나 주언이없는 게시글로 되게끔 설정하겠다는 뜻
    # related_name='article' -> writer가 왜 related_name이 article이냐 라고 하면 user객체에서 article을 접근할 때 쓰는 이름이기때문에
    # article 이라고 해주는게 더 직관 적일 것임 => ex) user.article
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='project', null=True)

    title = models.CharField(max_length=200, null=True) # 제목 항상 없어도 댐
    image = models.ImageField(upload_to='article/', null=False) # 이미지 항상 넣도록 설정
    content = models.TextField(null=True)   # 내용 항상 없어도 댐

    created_at = models.DateField(auto_now_add=True, null=True)


