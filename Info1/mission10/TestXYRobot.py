import unittest
import XYRobot as rb

class TestXYRobot(unittest.TestCase):
    m = rb.XYRobot("Morty")
    def test_init(self):
        self.assertEqual(self.m.angle(),0, "Morty espèce de débile, tu regardes dans la mauvaise direction")
        self.assertEqual(self.m.position(),(0,0), "Morty! Où est ce que tu t'es encore fouré !")

    def test_turn_right(self):
        self.m.turn_right()
        self.assertEqual(self.m.angle(),90, "J'ai dis à droite Morty! A DROITE!")
        self.m.turn_right()
        self.assertEqual(self.m.angle(),180, "J'ai dis à droite Morty! A DROITE!")
        self.m.turn_right()
        self.assertEqual(self.m.angle(),270, "J'ai dis à droite Morty! A DROITE!")

    def test_turn_left(self):
        self.m.turn_left()
        self.assertEqual(self.m.angle(),270, "J'ai dis à gauche Morty! A GAUCHE!")
        self.m.turn_left()
        self.assertEqual(self.m.angle(),180, "J'ai dis à gauche Morty! A GAUCHE!")
        self.m.turn_left()
        self.assertEqual(self.m.angle(),90, "J'ai dis à gauche Morty! A GAUCHE!")

    def test_turn(self):
        self.m.turn_left()
        self.m.turn_right()
        self.m.turn_right()
        self.m.turn_left()
        self.assertEqual(self.m.angle(),0, "T'as la tête qui tourne Morty ?")

    def test_move_fd(self):
        self.m.move_forward(50)
        self.assertEqual(self.m.position(),(50,0), "Avance vers le nord Morty! LE NORD")
        self.m.turn_right()
        self.m.move_forward(50)
        self.assertEqual(self.m.position(),(50,50), "Morty t'es bien à l'est hein? L'EST C'EST A DROITE MORTY!")


if __name__ == '__main__':
    unittest.main(verbosity=2)
