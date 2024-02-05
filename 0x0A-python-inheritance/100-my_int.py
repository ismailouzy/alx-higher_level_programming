#!/usr/bin/python3
"""advanced tasks

"""


class MyInt(int):
    """MyInt class

        Args:
            int:
    """
    def __eq__(self, valeur):
        """ == with !="""
        return not super().__eq__(valeur)

    def __ne__(self, valeur):
        """ != with =="""
        return not super().__ne__(valeur)
