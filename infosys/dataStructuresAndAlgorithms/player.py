#DSA-Assgn-4

class Player:
    def __init__(self,name,experience):
        self.__name=name
        self.__experience=experience

    def get_name(self):
        return self.__name

    def get_experience(self):
        return self.__experience

    def __str__(self):
        return(self.__name+" "+(str)(self.__experience))

#Implement Game class here
class Game:
    def __init__(self, players_list):
        self.__players_list = players_list
    def display_player_details(self):
        for player in self.__players_list:
            print("{} {}".format(player.get_name(), player.get_experience()))
    def sort_players_based_on_experience(self):
        result = []
        for player in self.__players_list:
            print(player.get_experience())
            if len(result) is 0:
                result.append(player)
            else:
                print('for', player.get_experience())
                i = 0
                while i<len(self.__players_list) and result[i].get_experience()>player.get_experience():
                    #print('for',player.get_experience(), result)
                    print(result[i].get_experience(), player.get_experience())
                    #print('for',player.get_experience(), result)
                    i += 1 
        self.__players_list = result
        return self.__players_list
    def shift_player_to_new_position(self, old_index_position,new_index_position):
        print(old_index_position, new_index_position)
        oldValue = self.__players_list[old_index_position]
        newValue = self.__players_list[new_index_position]
        self.__players_list[old_index_position] = newValue
        self.__players_list[new_index_position] = oldValue
        return self.__players_list 
    
    

player1=Player("Dhoni",15)
player2=Player("Virat",10)
player3=Player("Rohit",12)
player4=Player("Raina",11)
player5=Player("Jadeja",13)
player6=Player("Ishant",9)
player7=Player("Shikhar",8)
player8=Player("Axar",7.5)
player9=Player("Ashwin",6)
player10=Player("Stuart",7)
player11=Player("Bhuvneshwar",5)
#Add different values to the list and test the program
players_list=[player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]
game = Game(players_list)
game.sort_players_based_on_experience()
game.display_player_details()
#Create object of Game class, invoke the methods and test your program