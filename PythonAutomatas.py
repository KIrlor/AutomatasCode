class tupla_transicion:
    def __init__(self, _estado, _caracter , _direccion):
        self.estado = _estado
        self.caracter = _caracter
        self.direccion = _direccion

class turing_machine:
    def __init__(self, transicion, string_cinta):
        if isinstance(transicion, dict):
            self.tabla_transicion = transicion
        self.cinta = list(string_cinta)
        self.current_state = 's'
        self.current_position = 0
    def strart(self):
        result = False
        if self.current_state == 's':
            while (self.current_state!= 'Alto' and self.current_state!= 'Si' and self.current_state!= 'No' and self.current_state !='Error'):
                car = self.cinta[self.current_position]
                tupla = "('" + self.current_state + "', '" + car + "')"
                if  tupla in self.tabla_transicion:
                    accion = self.tabla_transicion[tupla]
                    if isinstance(accion, tupla_transicion):
                        self.current_state = accion.estado
                        print(self.cinta[self.current_position], accion.caracter, accion.direccion, accion.estado)
                        self.cinta[self.current_position] = accion.caracter
                        if accion.direccion == 'l':
                            self.current_position = self.current_position - 1
                        else:
                            if accion.direccion == 'r':
                                self.current_position = self.current_position + 1
                            else:
                                if accion.direccion != 'o':
                                    #salida si hay error
                                    self.current_state = 'Error'

        if self.current_state!= 'Alto' or self.current_state!= 'Si' or  self.current_state!= 'No':
            result = True
        return result


MT = dict()
# a^n b^4n

MT["('s', 'a')"] = tupla_transicion('1', 'a', 'r')
MT["('s', 'b')"] = tupla_transicion('2', 'b', 'l')
MT["('1', 'a')"] = tupla_transicion('1', 'a', 'r')
MT["('1', 'b')"] = tupla_transicion('2', 'b', 'o')
MT["('2', 'a')"] = tupla_transicion('3', 'a', 'r')
MT["('2', 'b')"] = tupla_transicion('Si', 'b', 'o')
MT["('3', 'a')"] = tupla_transicion('No', 'a', 'o')
MT["('3', 'b')"] = tupla_transicion('No', 'b', 'o')

stri = 'abbbbbb'

tm = turing_machine(MT,stri)
result = tm.strart()
print(result)
print(tm.current_state, tm.current_position)

MT2 = dict()
# a^n b^n Maquina 2

MT2["('s', 'a')"] = tupla_transicion('1', 'c', 'r')
MT2["('1', 'a')"] = tupla_transicion('1', 'a', 'r')

MT2["('1', 'd')"] = tupla_transicion('1', 'd', 'r')
MT2["('1', 'b')"] = tupla_transicion('2', 'd', 'l')

MT2["('2', 'd')"] = tupla_transicion('2', 'd', 'l')
MT2["('2', 'a')"] = tupla_transicion('2', 'a', 'l')

MT2["('2', 'c')"] = tupla_transicion('s', 'c', 'r')
MT2["('s', 'a')"] = tupla_transicion('3', 'd', 'r')

MT2["('3', 'd')"] = tupla_transicion('3', 'd', 'l')
MT2["('3', 'b')"] = tupla_transicion('Si', 'b', 'l')

stri2 = 'ab'

tm2 = turing_machine(MT2,stri2)
result2 = tm2.strart()
print(result2)
print(tm2.current_state, tm2.current_position)

MT3 = dict()
# a b^n Maquina 3
MT3["('s', 'a')"] = tupla_transicion('1', 'a', 'r')
MT3["('s', 'b')"] = tupla_transicion('2', 'b', 'l')

MT3["('1', 'a')"] = tupla_transicion('1', 'a', 'r')
MT3["('1', 'b')"] = tupla_transicion('2', 'b', 'o')

MT3["('2', 'a')"] = tupla_transicion('Alto', 'a', 'r')
MT3["('2', 'b')"] = tupla_transicion('Si', 'b', 'o')

stri3 = 'abbbbb'

tm3 = turing_machine(MT3,stri3)
result3 = tm3.strart()
print(result3)
print(tm3.current_state, tm3.current_position)

