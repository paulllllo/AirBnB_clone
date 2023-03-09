#!/usr/bin/python3
"""A console to handle creation, deletion, updating of objects on website"""
import cmd

"""import classes used"""
from models import base_model, place, state, city, amenity, review, user
import models

"""Instantiators - a dictionary containing all classes"""
instantiators = {"BaseModel": base_model.BaseModel, "Place": place.Place,
                 "State": state.State, "City": city.City,
                 "Amenity": amenity.Amenity, "Review": review.Review,
                 "User": user.User}

class HBNBCommand(cmd.Cmd):
    """Command interpreter for the hbnb website"""

    prompt = '(hbnb) '

    def do_create(self, classname):
        """creates an instance of the classname"""
        if  not classname:
            return print("** class name missing **")
        if not instantiators[classname]:
            return print("** class doesn't exist **")
        else:
            new_base = instantiators[classname]()
            new_base.save()
            print(new_base.id)

    def do_show(self, line):
        """Prints the string representation of an instance based
        on the class name and id"""
        if not line:
            return print("** class name missing **")
        if len(line.split()) < 2:
            return print("** instance id missing **")

        classname, id = line.split()
        if not classname in instantiators:
            return print("** class doesn't exist **")
        str = models.storage.view(classname, id)
        if not str:
            return print("** no instance found **")
        print(instantiators[classname](**str))

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id"""
        if not line:
            return print("** class name missing **")
        if len(line.split()) < 2:
            return print("** instance id missing **")

        classname, id = line.split()
        if not classname in instantiators:
            return print("** class doesn't exist **")
        done = models.storage.delete(classname, id)
        if not done:
            return print("** no instance found **")

    def do_all(self, classname):
        """ Prints all string representation of all instances
        based or not on the class name"""
        all_list = []
        if classname != "":
            if not classname in instantiators:
                return print("** class doesn't exist **")
            all_dict = models.storage.all()
            for key, value in all_dict.items():
                if value["__class__"] == classname:
                    all_list.append(f'{str(instantiators[classname](**value))}')
        else:
            all_dict = models.storage.all()
            #print(all_dict)
            for key, value in all_dict.items():
                if value["__class__"] in instantiators:
                    all_list.append(f'{str(instantiators[value["__class__"]](**value))}')
        print(all_list)

    def do_update(self, line):
        """Updates an instance based on the class name and id using attributes"""
        if not line:
            return print("** class name missing **")
        args = line.split()
        if args[0] not in instantiators:
                return print("** class doesn't exist **")
        if len(args) == 1:
            return print("** instance id missing **")
        if not models.storage.exists(args[0], args[1]):
            return print("** no instance found **")
        if len(args) == 2:
            return print("** attribute name missing **")
        if len(args) == 3:
            return print("** value missing **")
        classname, id, attr_name, attr_value, *_ = args
        models.storage.update(classname, id, attr_name, attr_value)

    def emptyline(self):
        """handle when an empty line is sent to interpreter"""
        print

    def do_quit(self, line):
        """Exit interpreter"""
        return True

    def do_EOF(self, line):
        """Exit Interpreter"""
        return True



if __name__ == '__main__':
    HBNBCommand().cmdloop()
