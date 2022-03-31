#!/usr/bin/python3
# coding=utf-8

from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    """
    动物类
    """

    @abstractmethod
    def do_say(self):
        """
        测试
        """
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("which animan should make_sound Dog or Cat?")
    ff.make_sound(animal)
