import json
import sqlite3

F_KEY_ID = "id"
F_KEY_URL = "url"
F_KEY_NAME = "name"
F_KEY_DESC = "desc"
F_KEY_CATEGORY = "category"
F_KEY_LANGUAGE = "language"
F_KEY_YEAR = "year"
F_KEY_DIRECTOR = "director"
F_KEY_IMAGE_URL = "image_url"
F_KEY_DURATION = "duration"

def insertFilm(_id,url,name,desc,category,language,year,director,image_url,duration):
    conn = sqlite3.connect('films.db',isolation_level=None)
    c = conn.cursor()
    print(_id,url,name,desc,category,language,year,director,image_url,duration)
    print(c.execute('insert into film values (?,?,?,?,?,?,?,?,?,?)',(_id,url,name,desc,category,language,year,director,image_url,duration)))

def createFilmTable():
    conn = sqlite3.connect('films.db',isolation_level=None)
    c = conn.cursor()
    c.execute("CREATE TABLE " + "film" + "("
              + F_KEY_ID + " INTEGER PRIMARY KEY, "
              + F_KEY_URL + " TEXT, "
              + F_KEY_NAME + " TEXT, "
              + F_KEY_DESC + " TEXT,"
              + F_KEY_CATEGORY + " TEXT,"
              + F_KEY_LANGUAGE + " TEXT,"
              + F_KEY_YEAR + " INTEGER,"
              + F_KEY_DIRECTOR + " TEXT,"
              + F_KEY_IMAGE_URL + " TEXT,"
              + F_KEY_DURATION + " TEXT" + ")" )

createFilmTable()
insertFilm(0,'http://10.0.10.227:8080/lecture0-720p.mp4','CS50 Lecture Week 0',
           'Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches you how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, software engineering, and web development. Languages include C, Python, SQL, and JavaScript plus CSS and HTML. Problem sets inspired by real-world domains of biology, cryptography, finance, forensics, and gaming. Designed for concentrators and non-concentrators alike, with or without prior programming experience. 68% of CS50 students have never taken CS before.',
           'Animation Film','English',2017,'David Milan','http://10.0.10.227:8080/week-0.jpg','61.10')
