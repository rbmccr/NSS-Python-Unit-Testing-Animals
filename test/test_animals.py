import unittest
import sys
sys.path.append("../")
from animals import Animal
from animals import Dog

class TestAnimal(unittest.TestCase):

  # make instance of an animal
  @classmethod
  def setUpClass(self):
    self.bob = Dog("Bob")
    self.animal = Animal()

  # Test that animal is initialized properly
  @unittest.skip("test_animal_creation") # syntax for skipping a test
  def test_animal_creation(self):
    murph = Dog("Murph")
    self.assertIsInstance(murph, Dog)

  # 1. Test that the Animal object has the correct name property
  def test_dog_has_name(self):
    result = self.bob.get_name()
    expected = "Bob"
    self.assertEqual(result, expected)
    self.assertNotEqual(result, "Dude")

  # 2. Set a species and verify that the object property of species has the correct value. # Note that the Dog class sets a species of Dog in its super init method
  def test_can_set_species(self):
    self.assertEqual(self.bob.get_species(), "Dog")
    self.bob.set_species("canine")
    self.assertEqual(self.bob.get_species(), "canine")
    self.assertNotEqual(self.bob.get_species(), "notCanine")

  # 3. Invoking the walk() method sets the correct speed on the both objects.
  def test_animal_walking_with_no_legs(self):
    with self.assertRaises(ValueError):
      self.animal.walk()

  def test_set_legs(self):
    self.animal.set_legs(12)
    self.animal.walk()
    speed = self.animal.speed
    # expected = self.speed = self.speed + (0.1 * self.legs)
    self.assertEqual(speed, 1.2)

  # def test_dog_walking_with_no_legs(self):


if __name__ == '__main__':
  unittest.main()