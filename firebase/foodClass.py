class Food:
    def __int__(self, name,servSize,calories,fat,satFat,tranFat,cholesterol,sodium,carbs,fiber,sugar,addedSugars,protein,vitD,calcium,iron,potas):
        self.name=name
        self.servSize=servSize
        self.calories=calories
        self.fat=fat
        self.satFat=satFat
        self.tranFat=tranFat
        self.cholesterol=cholesterol
        self.sodium=sodium
        self.carbs=carbs
        self.fiber=fiber
        self.sugar=sugar
        self.addedSugars=addedSugars
        self.protein=protein
        self.vitD=vitD
        self.calcium=calcium
        self.iron=iron
        self.potas=potas
    @staticmethod
    def getName(self):
        return self.name

    def to_dict(self):
        dictionary ={
            "name": self.name,
            "servSize": self.servSize,
            "calories": self.calories,
            "fat": self.fat,
            "satFat": self.satFat,
            "tranFat": self.tranFat,
            "cholesterol": self.cholesterol,
            "sodium": self.sodium,
            "carbs": self.carbs,
            "fiber": self.fiber,
            "sugar": self.sugar,
            "addedSugars": self.addedSugars,
            "protein": self.protein,
            "vitD": self.vitD,
            "calcium": self.calcium,
            "iron": self.iron,
            "potas": self.potas
        }
        return dictionary
        