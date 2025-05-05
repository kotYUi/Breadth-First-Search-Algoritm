from collections import deque
dictionaryNamesFriend = {}
dictionaryNamesFriend["I"] = ["Lisa", "Maria", "Muara", "Jon"]
dictionaryNamesFriend["Lisa"] = ["I", "Jason", "Mikel", "Evdacim"]
dictionaryNamesFriend["Mikel"] = ["Jon", "Lisa", "Dima"]
dictionaryNamesFriend["Potur"] = ["Artem", "Katya", "Maksim"]


def theBestFriend(name):
    if name[0] == "J":
        return True

def breadth_first_search(nameBestFriend):
    search_queue = deque()
    search_queue += dictionaryNamesFriend[nameBestFriend]
    setCheckNames = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in setCheckNames:
            if theBestFriend(person):
                print("The best friend " + person)
                return True
            else:
                setCheckNames.add(person)
                search_queue += dictionaryNamesFriend.get(person, [])
    return False

breadth_first_search("Potur")
breadth_first_search("I")

