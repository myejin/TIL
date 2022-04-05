> prefetch_related

```python
from django.db import connection, reset_queries
import time 

reset_queries()
start_queries = len(connection.queries)
start = time.perf_counter()

# general_meetings = GeneralMeeting.objects.filter(author_id=author_id).all()
general_meetings = GeneralMeeting.objects.filter(author_id=author_id).prefetch_related("agendas")

lst = []
for meeting in general_meetings: 
    lst.append([agenda.id for agenda in meeting.agendas.all()])
print(lst)

end = time.perf_counter()
end_queries = len(connection.queries)

print(f"Number of Queries : {end_queries - start_queries}")
print(f"Finished in : {(end - start):.2f}s")
```
- 결과 
```
general_meetings.count() = 62 일 때,

- prefetch_related 적용 
  Number of Queries : 2
  Finished in : 0.02s

- 미적용 
  Number of Queries : 63
  Finished in : 0.10s
```
