import config
import mysql.connector
from mysql.connector import errorcode

try:
  # Connect to the database
  cnx = mysql.connector.connect(**config.config)
  print("Connection established")
## find the top 10 movies with the highest rating
  cursor = cnx.cursor()
  print("Welcome to the Cinema Center\n" 
        "--------------------------------\n" 
        "1: Find the top 10 movies\n" 
        "   a) By Genre\n" 
        "   b) By Theme\n" 
        "   c) By Director\n" 
        "   d) With Actor\n" 
        "   e) In Country\n" 
        "2: Search\n" 
        "   a) By Movie Name\n" 
        "   b) By Actor Name\n"
        "   c) By Director\n" 
        "3: Browse\n" 
        "4: Top Blogs\n" 
        "5: Create Blog\n" )

  userInput = input("Select Option 1-5:")
  userSubInput = 0
  database = ["Actors", "Countries", "Crew", "Genres", "Movies", "Posters", "Themes"],
  ["name", "country", "role", "genre", "name", "url", "theme"],
  ["role", 0, "name", "genre", "name", "url", "theme"]

  if userInput in ["1", "2"]:
    userSubInput = input("Select Sub Option a-e:")
  # Search fot the top 10 movies with the highest rating by genre, theme, director, actor, or country in lowercase.
  def topTenBy(option):
      query = ("SELECT distinct %s "
                "FROM %ss "
                "ORDER BY %s" % (option, option.capitalize(), option))
      print(query)
      cursor.execute(query)
      print("--------------------------------\nAvailable %s:" % option)
      for (inputOptions) in cursor:
        print(inputOptions)
      searchInput = input("Enter a %s to search:" % option.capitalize())
      # Generate a query to find the top 10 movies with the highest rating
      query = ("SELECT name, rating "
                "FROM Movies "
                "JOIN %ss ON Movies.id = %ss.id "
                "WHERE %s LIKE '%%%s%%' "
                "ORDER BY rating DESC "
                "LIMIT 10" % (option.capitalize(), option.capitalize(), option, searchInput))
      cursor.execute(query)
      print("--------------------------------\nTop 10 movies with the highest rating in " + searchInput +":")
      for (name, rating) in cursor:
        print("{} - {}".format(name, rating))
      print("--------------------------------\n")
  topTenBy("genre") if userInput == "1" and userSubInput == "a" else None

  #match userInput, userSubInput:
  #  case "1", "a":
  #    query = ("SELECT distinct genre "
  #              "FROM Genres "
  #              "ORDER BY genre")
  #    cursor.execute(query)
  #    print("--------------------------------\nAvailable Genres:")
  #    for (genre) in cursor:
  #      print(genre)
  #    searchInput = input("Enter a genre to search:")
  #    # Generate a query to find the top 10 movies with the highest rating
  #    query = ("SELECT name, rating "
  #              "FROM Movies "
  #              "JOIN Genres ON Movies.id = Genres.id "
  #              "WHERE genre LIKE '%" + searchInput + "%' "
  #              "ORDER BY rating DESC "
  #              "LIMIT 10")
  #    cursor.execute(query)
  #    print("--------------------------------\nTop 10 movies with the highest rating in " + searchInput +":")
  #    for (name, rating) in cursor:
  #      print("{} - {}".format(name, rating))
  #    print("--------------------------------\n")

  #  case "2", "a":
  #    searchInput = input("Enter a movie name to search:")
  #    query = ("SELECT name, date, tagline, description, minute, rating "
  #            "FROM Movies "
  #            "WHERE name LIKE '%" + searchInput + "%' "
  #            "LIMIT 10")
  #    ## '%' is the LIKE operator.
  #    cursor.execute(query)

  #    print("--------------------------------\nSearch results for '{}':".format(searchInput))
  #    movieInfo = "Title: {}\n" \
  #    "Year: {}   Rating: {}\n" \
  #    "Description:\n" \
  #    "'{}'\n" \
  #    "{}\n----------------------------------\n"
  #    for (name, date ,tagline, description, minutes, rating) in cursor:
  #      print(movieInfo.format(name, date, rating, tagline, description))
  #    print("--------------------------------\n") 
  #  case 3:
  #    print(2)
  #  case _:
  #    print("Choose valid case")
  #  
  
  cnx.close;
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
