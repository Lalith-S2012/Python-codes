class India():
    def capital(self):
        print("New Delhi is the Capital of India")

    def language(self):
        print("Hindi is the most spoken Language in India")

    def type(self):
        print("India is a Developing Country")

class USA():
    def capital(self):
        print("Washington D.C. is the Capital OF the USA")

    def language(self):
        print("English is the Primary Language in USA")

    def type(self):
        print("USA is a Devoloped Country")

obj_ind = India()
obj_USA = USA()

for country in(obj_ind, obj_USA):
    country.capital()
    country.language()
    country.type()
    