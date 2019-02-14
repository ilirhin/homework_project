# Домашнее задание

1. Для ознакомление с git и закрепления основных навыков пройдите задание с [этого](https://learngitbranching.js.org) сайта.
2. На github cделайте fork [проекта с домашним заданием](https://github.com/ilirhin/homework_project)
3. Испольузя PyCharm или Sublime Text, реализуйте простую функциональность в этом проекте, оформив её как питоновский пакет (как на занятии)
    * предлагается посвятить пакет обучению ML модели на данных HR.csv (есть в домашнем репозитории)
    * как альтернативный вариант предлагается реализовать алгоритм кластеризации [K-Means](https://en.wikipedia.org/wiki/K-means_clustering) или [метод Гаусса](https://en.wikipedia.org/wiki/Gaussian_elimination)
    * также стоит добавить тестирование вашей функциональности, чтобы потом её можно было расширять и не бояться ничего поломать. Вот [здесь](https://docs.python-guide.org/writing/tests/) есть гайд  по тому, как это можно было бы сделать
    * если хотите, то можете решать какую-то свою ML задачу, но в пакете должны быть непустые зависимости (requirements.txt)
    * постарайтесь максимально заполнить информацию о вашем пакете, подробно можно прочитать [здесь](https://docs.python.org/3.7/distutils/setupscript.html)
    * код обучения и применения должен быть скриптами, а не jupyter notebook-ами
    * постарайтесь разделить обучение моделей, извлечение признаков, оценку качества и применение модели на разные питоновские модули
4. Сделайте pull request на добавление вашего пакета в основной репозиторий
5. Пройдите ревью кода
