import json

class Parser:

    cached_positions = {}

    def __init__(self):
        with open('data/docks.json') as f:
            self.data = json.load(f)

    def get_positions(self, map, side):
        if(self.cached_positions.get(f"{map}_{side}")):
            return self.cached_positions[f"{map}_{side}"]


        arr = []

        for pos in self.data[map][side]:
            arr.append((int(pos.split(" ")[0]), int(pos.split(" ")[1])))

        self.cached_positions[f"{map}_{side}"] = arr

        return arr

