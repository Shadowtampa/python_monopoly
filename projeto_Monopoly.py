# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 13:34:03 2021

@author: Luis_Gostoso
"""
import os
import random


def main():

    player1 = Player("Luis", "preto", 100)
    player2 = Player("Antônio", "azul", 100)
    player3 = Player("marcos", "verde", 100)
    player4 = Player("saul", "amarelo", 100)
    player5 = Player("Mike Ross", "vermelho", 100)

    tabuleiro = Tabuleiro([player1, player2, player3, player4, player5])

    entrada = ''
    play = True
    while entrada != 's' and play == True:
        os.system('cls')
        print('-------------------------------------------------------------')
        tabuleiro.show_board()
        entrada = input(
            'Selecionar uma opção:\ns para sair\nm para mover\np para ver portfólio\nr para avançar a rodada\ne para interagir com o terreno\n')

        if entrada == 's':
            play = False
        if entrada == 'm':
            tabuleiro.move_player()
        if entrada == 'r':
            tabuleiro.next_player()
        if entrada == 'p':
            tabuleiro.get_player_portifolium()
        if entrada == 'e':
            tabuleiro.interact_with_square()

    # tabuleiro.move_player(player1, 12)
    # tabuleiro.move_player(player2, 2)

    # casa1 = Square("Travessa Sorriso de Maria", "azul", 500.00)
    # casa2 = Square("Rua Verbena", "azul", 7000000000.00)


# ------------------------------------------------------------------------------------------
class Player:
    def __init__(self, nome, cor_player, dinheiro):
        self.nome = nome
        self.dinheiro = dinheiro
        self.cor_player = cor_player
        self.posses = {}
        self.jailed = False
        self.position = None

    def get_name(self):
        return self.nome

    def get_color(self):
        return self.cor_player

    def get_balance(self):
        return self.dinheiro

    def receive(self, payer, value):
        self.dinheiro += value
        if payer == 'banco':
            return 'recebendo', value, 'do banco'
        else:
            return self.get_color(), 'recebedo ', value

    def send(self, receiver, value):
        self.dinheiro -= value
        if receiver == 'banco':
            return 'enviando', value, 'ao banco'
        else:
            return self.get_color(), 'enviando ', value

    def set_ownership(self, Terreno):
        pass

    def is_jailed(self):
        return self.jailed


class Dice:
    def __init__(self, size):
        self.size = size
        self.value = self.size

    def set_dice_roll(self):
        self.value = random.randint(1, self.size)

    def get_value(self):
        return self.value


class Square:
    def __init__(self, name, terreno=False, description=None):
        self.name = name
        self.position = None

        self.description = description
        self.terreno = terreno

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def is_terreno(self):
        return self.terreno

class Jail(Square):
    def __init__(self, name, position, bail_value):
        super().__init__(name, position)
        self.bail_value = bail_value
    

class Go_to_Jail(Square):
    def __init__(self, name, position=None):
        super().__init__(name, position)

class Area:
    def __init__(self, color):
        self.owner = 'owner'
        self.bougth = False
        self.color = color
        self.lands = []

    def add_land_name(self, land_name):
        self.lands.append(land_name)

    def get_lands(self):
        return self.lands

class Buyable(Square):
    def __init__(self,  name,  value, rent,mortage_value,unmortage_value, owner= None, position=None):
        super().__init__(name, position)
        self.value = value
        self.owner = owner
        self.rent = rent
        self.mortaged = False
        self.mortage_value = mortage_value
        self.unmortage_value = unmortage_value




class Terreno(Buyable):
    def __init__(self,  name, cor_terreno, valor, terreno, rent, mortage_value, unmortage_value, owner= None):
        super().__init__(name,  valor, rent, mortage_value,unmortage_value, owner= None, position=None)

        self.cor_terreno = cor_terreno
        self.valor = valor
        self.terreno = terreno
        self.owner = owner

        self.houses = 0
        self.hotel = False
        

    def get_name(self):
        return self.name

    def get_value(self):
        return self.valor

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def get_color(self):
        return self.cor_terreno


class Especial(Square):
    def __init__(self, nome, tipo):
        super().__init__(nome)
        
        if tipo == 'sorte':
            actions =  {
                0 : 'Revés: Pague 200 ao banco',
                1 : 'Sorte: Ganhe 200 do banco'
            }
        else: 
            actions =  {
                0 : 'Pague 200 ao banco',
                1 : 'Ganhe 200 do banco'
            }

        self.__actions = actions


    def get_actions(self):
        return self.__actions
        


class Initial(Square):
    def __init__(self, nome):
        super().__init__(nome)


class Tabuleiro:

    def __init__(self, players, squares=None):

        self.players = players

        self.curret_player = 0

        self.dice1 = Dice(6)
        self.dice2 = Dice(6)

        self.areas_dict = {
            'azul' : Area('azul'),
            'vermelho' : Area('vermelho'),
            'verde' : Area('verde')
        }

        self.players_dict = {}
        # self.players_dict[ 1 ] = players[0]
        for i in range(len(players)):
            self.players_dict[players[i].get_color()] = players[i]

        self.squares_dict = {  # Valores padrão das casas
            0: Initial("Receba seu Salário"),
            1: Terreno("Travessa Sorriso de Maria", "azul", 3.00, True, 0, 0, 0),
            2: Terreno("Labic", "azul", 3.00, True, 0, 0, 0),
            3: Terreno("Laboratório 1", "azul", 3.00, True, 0, 0, 0),
            4: Terreno("Laboratório 2", "vermelho", 3.00, True, 0, 0, 0),
            5: Terreno("Reitoria", "azul", 3.00, True, 0, 0, 0),
            6: Terreno("Guarita", "azul", 3.00, True, 0, 0, 0),
            7: Terreno("Patifão", "azul", 3.00, True, 0, 0, 0),
            8: Terreno("Deck", "vermelho", 3.00, True, 0, 0, 0),
            9: Especial("Cofre", "cofre"),
            10: Especial("Sorte", "sorte"),
            11: Jail("Cadeia", 0, 0),#
            12: Go_to_Jail("Vá para a cadeia"),#
            13: Terreno("Mídias", "azul", 3.00, True, 0, 0, 0)
        }

        for key in self.squares_dict:
            if isinstance(self.squares_dict[key],Terreno):
                for key_ in self.areas_dict:
                    if key_ == self.squares_dict[key].get_color():
                        self.areas_dict[key_].add_land_name(self.squares_dict[key].get_name())

        self.positions = Player_on_Board(players, len(self.squares_dict))

    def next_player(self):
        self.curret_player += 1
        if self.curret_player == len(self.players):
            self.curret_player = 0

    def show_board(self):

        print("\n------- TABULEIRO -------")
        for key in self.squares_dict:
            players_on_square = str(key) + " " + \
                str(self.squares_dict[key].get_name())
            players_on_square += ''.ljust(40-len(players_on_square))+'||'

            for key_ in self.positions.players_positions_dict:
                if key == self.positions.players_positions_dict[key_]:
                    players_on_square += str('  '+key_+'  | ')

            print(players_on_square)
            # print(self.positions.)
        print("\n------- JOGADORES -------")
        print('número de jogadores: ', len(self.players_dict))
        for key in self.players_dict:
            print(key, " ", self.players_dict[key].get_name())

        print("\n------- DADOS -------")
        print(self.dice1.get_value())
        print(self.dice2.get_value())

        # for i in len(self.players_dict):
        print('\n---------- Vez do',
              self.players[self.curret_player].get_color(), ' ----------')

    def move_player(self):

        self.dice1.set_dice_roll()
        self.dice1.set_dice_roll()

        self.positions.player_walk(self.players[self.curret_player].is_jailed(),self.players[self.curret_player].get_color(
        ), (self.dice1.get_value()+self.dice2.get_value()))

    def get_player_portifolium(self):
        os.system('cls')
        entrada = ''
        while entrada != 's':
            os.system('cls')
            print('\n---------- Portfólio do',
                  self.players[self.curret_player].get_color(), ' ----------')
            print('Saldo em conta: R$',
                  self.players[self.curret_player].get_balance())
            print('Saldo em propriedades:', 0)
            entrada = input('\ns para Sair\np para pagar\nr para receber\n')
            if entrada == 'r':
                os.system('cls')
                entrada_ = ''
                while entrada_ != 's':
                    entrada_ = input('\nDigitar pagador (s para sair)\n')
                    if entrada_ != 's':
                        if entrada_ == 'banco':
                            entrada2 = input('\nDigitar valor \n')
                            print(self.players[self.curret_player].receive(
                                entrada_, int(entrada2)))
                        else:
                            entrada2 = input('\nDigitar valor\n')
                            print(self.players[self.curret_player].receive(
                                entrada_, int(entrada2)))
                            print(self.players_dict[entrada_].send(
                                entrada, int(entrada2)))
            if entrada == 'p':
                os.system('cls')
                entrada_ = ''
                while entrada_ != 's':
                    entrada_ = input('\nDigitar recebedor (s para sair)\n')
                    if entrada_ != 's':
                        if entrada_ == 'banco':
                            entrada2 = input('\nDigitar valor\n')
                            print(self.players[self.curret_player].send(
                                entrada_, int(entrada2)))
                        else:
                            entrada2 = input('\nDigitar valor\n')
                            print(self.players[self.curret_player].send(
                                entrada_, int(entrada2)))
                            print(self.players_dict[entrada_].receive(
                                entrada_, int(entrada2)))

    def interact_with_square(self):
        os.system('cls')
        print('\n---------- Tela',
              self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].get_name(), '----------')
        print('Descrição: ', self.squares_dict[self.positions.get_player_position(
            self.players[self.curret_player])].get_description())

        if self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].is_terreno():
            # print('é um terreno')
            print('Preço: ', self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].get_value())


            entrada_ = ''
            while entrada_ != 's':
                entrada_ = input('\ns para sair\nc para comprar\n')
                if entrada_ == 'c':
                    if int(self.players[self.curret_player].get_balance()) >= int(self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].get_value()) and self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].get_owner() == None :
                        self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].set_owner(self.players[self.curret_player].get_name())
                        
                        print(self.players[self.curret_player].send(
                                    'banco', int(self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].get_value())),'pertence a: ',self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].get_owner())
                    elif self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].get_owner() == None:
                        print('fundos insuficientes')

                    else:
                        print('Não foi possível comprar, pois o terreno pertence a: ',self.squares_dict[self.positions.get_player_position(self.players[self.curret_player])].get_owner())
        else:
            # print('não é um terreno')
            entrada_ = ''
            while entrada_ != 's':
                entrada_ = input('\ns para sair\n')


class Player_on_Board:
    def __init__(self, players, board_size):

        self.board_size = board_size

        self.players_positions_dict = {}

        for i in range(len(players)):
            self.players_positions_dict[players[i].get_color()] = 0
            print(self.players_positions_dict)

    def player_walk(self, player_is_jailed,key, value):
        if not player_is_jailed:
            if((self.players_positions_dict[key] + value) % self.board_size != 0):
                self.players_positions_dict[key] = (
                    self.players_positions_dict[key]+value) % self.board_size

    def get_player_position(self, player):
        return self.players_positions_dict[player.get_color()]


# ------------------------------------------------------------------------------------------
main()
