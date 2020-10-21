def user_input():
    # Check if the user would like to crawl the IMDb Top 1000
    while True:
        crawl_imdb = input("Would you like to crawl the IMDb Top 1000? y/n: ").lower()
        if crawl_imdb == "y":
            imdb = True
            break
        elif crawl_imdb == "n":
            imdb = False
            break
        else:
            print("You need to type either \"y\" for yes or \"n\" for no.")

    # Check what URL the user would like to crawl
    if imdb == True:
        url = "https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating"
    else:
        while True: 
            url = input("What URL would you like to crawl instad? ")
            #TODO: regex for url
            break

    # Check how many levels the user would like to crawl
    while True:
        levels = input("How many levels would you like to crawl? ")
        try:
            levels = int(levels)
        except:
            print("You have to type a number without decimals.")
            continue
        if levels > 0 and levels <= 100:
            break
        else:
            print("You have to type a number between 1 and 100.")

    # Check if the user would like to define a regex
    while True:
        define_regex = input("Would you like to define a regex to find sensitive data? y/n: ").lower()
        if define_regex == "y":
            user_defined_regex = True
            break
        elif define_regex == "n":
            user_defined_regex = False
            break
        else:
            print("You need to type either \"y\" for yes or \"n\" for no.")
    
    # Check what the user-defined regex is
    if user_defined_regex == True:
        while True:
            regex = input("What regex would you like to use? ")
            if regex[0] != "\"" or regex[len(regex) - 1] != "\"" or len(regex) < 3:
                print("Please encapsulate your regex in \"\".")
                continue
            break
    else:
        regex = ""
    
    #return variables
    return url, levels, regex