kol=1 
books=( 
    {"Title":"Моя вина",  "Author":"Мерседес Рон","year":"2015"}, 
    {"Title":"Мятная сказка",  "Author":"Александр Полярный","year":"2018"}, 
    {"Title":"Дивергент",  "Author":"Вероника Рот","year":"2011"}, 
    {"Title":"Гарри Поттер",  "Author":"Джоан Роулинг","year":"1997"},  
    {"Title":"Чернильное сердце",  "Author":"Корнелия Функе","year":"2003"} 
     ) 
for book in books: 
    print(f"Книга {kol}".center(58,"-")) 
    print(f"Название: {book['Title']},Автор:{book['Author']},") 
    print(f"{book['year']}".center(58,"-")) 
    kol+=1