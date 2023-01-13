# RESTful API — это интерфейс прикладной программы (API), который использует HTTP-запросы для GET, PUT, POST и DELETE данных. В предыдущих разделах мы узнали о python, flask и mongoDB. Мы будем использовать полученные знания для разработки RESTful API с использованием Python flask и базы данных mongoDB. Каждое приложение с операцией CRUD (создание, чтение, обновление, удаление) имеет API для создания данных, получения данных, обновления данных или удаления данных из базы данных.

# Чтобы создать API, полезно понимать протокол HTTP и цикл HTTP-запросов и ответов.
# Методы запроса
# GET, POST, PUT и DELETE — это методы HTTP-запроса, которые мы собираемся внедрить в API или операционное приложение CRUD.

# GET: метод GET используется для извлечения и получения информации с данного сервера с использованием заданного URI. Запросы с использованием GET должны только извлекать данные и не должны иметь никакого другого воздействия на данные.

# POST: запрос POST используется для создания данных и отправки данных на сервер, например, для создания нового сообщения, загрузки файла и т. д. с использованием HTML-форм.

# PUT: заменяет все текущие представления целевого ресурса загруженным контентом, и мы используем его для изменения или обновления данных.

# DELETE: удаляет данные
# Structure of HTTP
# HTTP uses client-server model. An HTTP client opens a connection and sends a request message to an HTTP server and the HTTP server returns response message which is the requested resources. When the request response cycle completes the server closes the connection.

# HTTP request response cycle

# The format of the request and response messages are similar. Both kinds of messages have

# an initial line,
# zero or more header lines,
# a blank line (i.e. a CRLF by itself), and
# an optional message body (e.g. a file, or query data, or query output).
# Let us an example of request and response messages by navigating this site:https://thirtydaysofpython-v1-final.herokuapp.com/. This site has been deployed on Heroku free dyno and in some months may not work because of high request. Support this work to make the server run all the time.

