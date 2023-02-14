#!/usr/bin/python3
""" cmd module """
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.city import City

classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }


class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """

    prompt = "(hbnb)"

    def do_EOF(self):
        """ exit the program """
        return True

    def do_quit(self, args):
        """ Quit command to exit the program \n"""
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """ creates new instance """

        args = args.split()

        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """ prints the string representation of an instance """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_id = args[1]
        all_instances = models.storage.all()
        found = False
        for key, instance in all_instances.items():
            if class_name in key and class_id in key:
                found = True
                print(instance)
                break
        if not found:
            print("** no instance found **")

    def do_destroy(self, args):
        """ delete an instance """
        args = args.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        found = False
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_instances = models.storage.all()
        if key not in all_instances.keys():
            print("** no instance found **")
            return
        instance = all_instances.pop(key)
        if instance:
            del (instance)
            models.storage.save()
            found = True

    def do_all(self, args):
        """ prints all string rep of all instances """

        args = args.split(" ")
        class_name = args[0]
        if class_name:
            if class_name not in classes:
                print("** class doesn't exist **")
                return
        else:
            all_instances = models.storage.all()
            for key, instance in all_instances.items():
                print([str(instance)])
        if class_name in classes:
            all_instances = models.storage.all()
            for key, instance in all_instances.items():
                if class_name in key:
                    print([str(instance)])

    def do_update(self, args):
        """ update an instance based on a class name and id """
        args = args.split()

        if len(args) < 1:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        found = False
        key = "{}.{}".format(class_name, instance_id)
        all_instances = models.storage.all()
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_name = args[2]
        attribute_value = args[3]

        for key, instance in all_instances.items():
            if instance_id in key:
                found = True
                if len(args) < 5:
                    setattr(instance,
                            attribute_name,
                            attribute_value.strip('""'))
                    models.storage.save()
        if not found:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
