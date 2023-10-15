#!/usr/bin/python3
"""The base model class that defines all common attributes/methods for other classes"""

class BaseModel():
    """Base class for all models"""
    def __init__(self, id):
        self.id = id


    def save(self):
        pass
