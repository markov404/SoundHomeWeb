
# Soundhome

## _Web resource for making your opinion about music._

## Powered by
<img src="https://camo.githubusercontent.com/4b95df4d6ca7a01afc25d27159804dc5a7d0df41d8131aaf50c9f84847dfda21/68747470733a2f2f73656c656e69756d2e6465762f696d616765732f73656c656e69756d5f6c6f676f5f7371756172655f677265656e2e706e67" width="100px" height="100px"> <img src="https://businessfm.kz/storage/posts/April2021/0ZpDzGevqAOL8bG0jbFh.png" width="150px" height="100px"> <img src="https://audviklabs.com/wp-content/uploads/2022/01/postgreSQL.png" width="100px" height="100px"> <img src="https://static.djangoproject.com/img/logos/django-logo-negative.1d528e2cb5fb.png" width="150px" height="100px"> <img src="https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F99494F435EF3172310" width="150px" height="100px">

## Django system design





<img src="https://i.ibb.co/sV8JcWr/Review-updating-implementation-Django-Architecture-drawio-1.png" width="300px" height="300px" alt="Review-updating-implementation-Django-Architecture-drawio-1">

- View and Schedulers were used as the starting point of the event for each url or time event. 
- Forms in the application, were used as a data validation layer, which is quite common, but i had to extend the ModelForm class, more details in the section about the data validation part. 
- Services are the part of the application that can be called, by a worker or a view. Services contain business logic and ideally services only manipulate python data types and can call components to retrieve data or implement tasks that require interaction with the infrastructure. 
- Components are database call functions, or less abstract entities (classes) that have access to the application infrastructure. For example, parts of a service implementation that uses Yandex Cloud or Selenium, as well as parts that access the database, can be called components. The service implements the logic of this whole action.

<img src="https://i.ibb.co/fqgp9HZ/Review-updating-implementation-DRU-Service.jpg" alt="Review-updating-implementation-DRU-Service" border="0">

Remember:
rabbitmq.conf: |
  consumer_timeout = 31622400000
