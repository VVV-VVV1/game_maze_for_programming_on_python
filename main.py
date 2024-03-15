# map_mazle = [[_9e_][_8_][7|]
#              [|3|][5][_6_]
#              [|2][1s][4|]]


def count_first_level_descendants(room):
    return len(room.room_paths)


def get_data(room):
    return room.data


class crate_mazle:
    def __init__(self, data, parent=None):
        self.data = data
        self.room_paths = []  # развилки в комнате
        self.parent_room = parent  # ссылка на радительский узел

    def add_room(self, room):
        self.room_paths.append(room)
        room.parent = self  # устанавливаем текущий узел как радительский для добавленного узла
        return self

    def get_room_paths(self, room, index):
        return room.room_paths[index]

    def get_parent_rooms(self, room):
        return room.parent_rooms


class action(crate_mazle):

    def __init__(self, data, room):
        super().__init__(data)
        self.location = room

    def Help(self):
        print("You cen:")
        print("write the \x1B[3mlook around\x1B[0m to see the forks")
        print("write the \x1B[3mright\x1B[0m to go to the right")
        print("write the \x1B[3mleft\x1B[0m to go to the left")
        print("write the \x1B[3mup\x1B[0m to go to the up")
        print("write the \x1B[3mback\x1B[0m to go to the back")
        print("write the \x1B[3mgive up\x1B[0m")
        print("if there are 2 paths, then this one is \x1B[3mright\x1B[0m or \x1B[3mleft\x1B[0m, if path 1 is \x1B[3mup\x1B[0m")
        return self

    def Look_around(self):
        print("you have", count_first_level_descendants(self.location), "ways")
        return self

    def Right(self, room):
        if count_first_level_descendants(room) == 1:
            print("There is no way")
            return self
        self.location = self.get_room_paths(room, 0)
        print("You went to the right")
        return self

    def Left(self, room):
        if count_first_level_descendants(room) == 1:
            print("There is no way")
            return self
        if count_first_level_descendants(room) == 2:
            self.location = self.get_room_paths(room, 1)
            print("You went to the left")
            return self
        self.location = self.get_room_paths(room, 2)
        print("You went to the left")
        return self

    def Up(self, room):
        if count_first_level_descendants(room) == 2:
            print("There is no way")
            return self
        if count_first_level_descendants(room) == 1:
            self.location = self.get_room_paths(room, 0)
            print("You went to the go")
            return self
        self.location = self.get_room_paths(room, 1)
        print("You went to the go")
        return self

    def back(self, room):
        print("You went to the back")
        self.location = room.parent
        return self


def main():
    print("Welcome to the mazle game!")
    print("write \x1B[3mhelp\x1B[0m to find out your capabilities")

    # создание лабиринта

    # иннициализация обектов ккомнат
    room_start = crate_mazle("room_start")
    room2 = crate_mazle("room2")
    room3 = crate_mazle("room3")
    room4 = crate_mazle("room4")
    room5 = crate_mazle("room5")
    room6 = crate_mazle("room6")
    room7 = crate_mazle("room7")
    room8 = crate_mazle("room8")
    room9 = crate_mazle("room9")
    room_exit = crate_mazle("room_exit")

    # карта лабиринта
    # map_mazle = [[_9e_][_8_][7|]
    #              [|3|][5][_6_]
    #              [|2][1s][4|]]

    # создание связанных комнат
    room_start.add_room(room2)
    room_start.add_room(room5)
    room_start.add_room(room4)

    room2.add_room(room3)

    room5.add_room(room6)
    room6.add_room(room7)
    room7.add_room(room8)
    room8.add_room(room9)

    room9.add_room(room_exit)

    # room2.outpot()

    gamer = action("gamer", room_start)
    # gamer.Help()

    while True:
        action_gamer = input()
        if action_gamer == "help":
            gamer.Help()
        elif action_gamer == "look around":
            gamer.Look_around()
        elif action_gamer == "right":
            gamer.Right(gamer.location)
        elif action_gamer == "left":
            gamer.Left(gamer.location)
        elif action_gamer == "up":
            gamer.Up(gamer.location)
        elif action_gamer == "back":
            gamer.back(gamer.location)
        elif action_gamer == "give up":
            print("Game over")
            return False

        if get_data(gamer.location) == "room_exit":
            print("Congratulations, you have passed the game!")
            return False


if __name__ == "__main__":
    main()
