#pip install virtualenv
# /Desktop/30DaysOfPython/flask_project\$ virtualenv venv
# Я предпочитаю называть новый проект venv
# активируем виртуальную среду, написав следующую команду в папке нашего проекта.
# /Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
# После того, как вы напишете команду активации, каталог вашего проекта будет начинаться с venv. См. пример ниже.

# (venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
# Теперь давайте напишем pip Freeze, чтобы увидеть список установленных пакетов в проекте:

# (venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
# Click==7.0
# Flask==1.1.1
# itsdangerous==1.1.0
# Jinja2==2.10.3
# MarkupSafe==1.1.1
# Werkzeug==0.16.0

# Когда вы закончите, вы должны деактивировать активный проект, используя deactivate .

# (venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate