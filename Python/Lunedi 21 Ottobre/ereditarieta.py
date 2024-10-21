class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
    def show_info(self):
        print (f"Veicolo marca {self.marca}, modello {self.modello}")
        
class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
        
    def show_optionals(self):
        print (f"Optionals: {','.join(self.dotazioni)}")
        
class Supercar(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        super().__init__(marca, modello)
        #Veicolo.__init__(self, marca, modello)
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli
    
    def show_info(self):
        super().show_info()
        print (f'Potenza: {self.cavalli}cv')
        self.show_optionals()
        
class cilindrata(Veicolo):
    def __init__(self, marca, modello, cilindrata):
        super().__init__(marca, modello)
        self.cilindrata = cilindrata
        
    def show_info(self):
        super().show_info()
        print (f'Attributo Veicolo: {self.cilindrata}')
        
class dimensioniRuote(DotazioniSpeciali):
    def __init__(self, dotazioni, dimensioniRuote):
        super().__init__(dotazioni)
        self.ruote = dimensioniRuote
        
    def show_info(self):
        super().show_info()
        print (f'Attributo Optional: {self.ruote}')
        
class combined(Supercar, cilindrata, dimensioniRuote):
    def __init__(self, marca, modello, dotazioni, cavalli, cilindrata, ruote):
        super().__init__(marca, modello, dotazioni, cavalli)
        cilindrata.__init__(self, cilindrata)
        dimensioniRuote.__init__(self, ruote)
    
    def show_info(self):
        super().show_info()
        print (f'Cilindrata: {self.cilindrata}')
        print (f'Dimensioni Ruote: {self.ruote}')
