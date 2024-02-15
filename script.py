import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv

# Открываем браузер Chrome и переходим по указанному URL
driver = webdriver.Chrome()
driver.get("https://www.fifa.com/fifa-world-ranking/")

# Ждем несколько секунд, чтобы страница полностью загрузилась
time.sleep(5)

# Получаем HTML-код страницы
html = driver.page_source

# Создаем объект BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Идентифицируем нужные элементы HTML и извлекаем информацию
rankings = soup.find_all("tr", class_="fi-ranking-sub-ranking__item")

# Инициализируем пустой список для хранения данных
results = []

# Проходим по каждому элементу и извлекаем нужные данные
for ranking in rankings:
    position = ranking.find(class_="fi-table__position").text
    team = ranking.find(class_="fi-t__nText").text
    points = ranking.find(class_="fi-table__points").text
    
    # Добавляем данные в список результатов
    results.append({"Position": position.strip(), "Team": team.strip(), "Points": points.strip()})

# Закрываем браузер
driver.quit()

# Выводим результаты
for result in results:
    print(result)

# Сохраняем результаты в файл CSV
filename = "fifa_rankings.csv"

with open(filename, "w", newline="") as csvfile:
    fieldnames = ["Position", "Team", "Points"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(results)