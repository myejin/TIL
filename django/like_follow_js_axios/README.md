## 팔로우 기능 구현

- `profile.html` 일부 코드

```html
{% block script %}
<script>
  const followForm = document.querySelector("#follow-form")
  followForm.addEventListener('submit', event => {
    event.preventDefault()
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
    axios({
      method: 'post',
      url: '/accounts/{{ person.pk }}/follow/',
      headers: {
          'X-CSRFToken': csrftoken
      }
    })
    .then(res => {
      const btn = document.querySelector('#follow-btn')
      const cntFollow = document.querySelector('#cnt-follow')
      if(res.data.is_follow) {
        btn.innerText = '팔로우 취소'
        btn.style.backgroundColor = 'red'  // 버튼색 변경
      } else {
        btn.innerText = '팔로우'
        btn.style.backgroundColor = 'white'
      }
      cntFollow.innerText = res.data.cnt_follow
    })
    .catch(err => {
      console.log(err)
    })
  })
</script>
{% endblock script %}
```



- `accounts/views.py` 의 일부 코드

```python
@require_POST
def follow(request, user_pk):
    User = get_user_model()
    you = get_object_or_404(User, pk=user_pk)
    if request.user.is_authenticated:
        me = request.user
        is_follow = False
        if you != me:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
            else:
                you.followers.add(me)
                is_follow = True
        data = {
            "is_follow": is_follow,
            "cnt_follow": you.followers.count(),
        }
        return JsonResponse(data)  # axios 응답으로 JSON 데이터 전달
    return redirect("accounts:login")
```



## 좋아요 기능 구현

- `index.html` 일부 코드

```html
{% block script %}
<script>
  const likeForms = document.querySelectorAll('#like-form')
  likeForms.forEach(form => {
    form.addEventListener('submit', event => {  // submit : 동기 요청
      event.preventDefault() // 페이지의 새로고침을 막기위함
      const pk = form.dataset.pk
      const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
      axios({
        method: 'post',
        url: `/articles/${pk}/like/`,
        headers: {
          'X-CSRFToken': csrftoken
        }
      })
      .then(res => {
        const btn = document.querySelector(`#btn-${pk}`)
        const txt = document.querySelector(`#txt-${pk}`)
        console.log(res.data.is_like)
        if(res.data.is_like) {
          btn.innerText = '좋아요 취소'
        } else {
          btn.innerText = '좋아요'
        }
        txt.innerText = res.data.cnt_like
      })
      .catch(err => {
        // console.log(err)
        if(err.response.status === 401) {
          // console.log(document.location.href)
          document.location.href = '/accounts/login/'
        }
      })
    })
  })
</script>
{% endblock script %}
```



- `articles/views.py` 일부 코드

```python
@require_POST
def like(request, article_pk):
    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        is_like = False
    else:
        article.like_users.add(request.user)
        is_like = True
    data = {
        "is_like": is_like,
        "cnt_like": article.like_users.count(),
    }
    return JsonResponse(data)
```

