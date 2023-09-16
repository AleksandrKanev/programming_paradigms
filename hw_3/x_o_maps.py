class X_o_maps:
    def __init__(self):
        self.maps = [1,2,3,4,5,6,7,8,9]

    def get_maps(self):
        return self.maps

    def print_maps(self):
        for i in range(len(self.maps)):
            if(i in [2,5,8]):
                print(self.maps[i])
            else:
                print(self.maps[i], end=" ")
        print()
    
    def update_maps(self, str : str, num: int):
        if(num in self.maps):
            self.maps[num-1] = str
            return True
        else: return False

    def result_game(self):
        victories = [[0,1,2],
                     [3,4,5],
                     [6,7,8],
                     [0,3,6],
                     [1,4,7],
                     [2,5,8],
                     [0,4,8],
                     [2,4,6]]
        for i in victories:
            if self.maps[i[0]] == self.maps[i[1]] ==  self.maps[i[2]] :
                return self.maps[i[0]]
        else:
            for i in self.maps:
                if(isinstance(i, int)):
                    return None
            else:
                return "Ничья"






