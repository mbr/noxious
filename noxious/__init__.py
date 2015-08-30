import xml.etree.ElementTree as ET


def from_file(fn):
    tree = ET.parse(fn)
    return Noxious(tree.getroot())


class Noxious(object):
    def __init__(self, elem, parent=None):
        self._parent = parent
        self._elem = elem

    def _all(self):
        return [self.__class__(sibling)
                for sibling in self._parent._elem.findall(self._elem.tag)]

    def _get_path(self):
        path = []
        tag = self
        while tag:
            path.insert(0, tag._elem.tag)
            tag = tag._parent

        root = path.pop(0)

        return root + ''.join('[{!r}]'.format(p) for p in path)

    def _text(self):
        return self._elem.text

    def __add__(self, other):
        return str(self) + other

    def __bool__(self):
        e = self._elem
        return bool(e.text or list(e))

    def __float__(self):
        return float(str(self))

    def __int__(self):
        return int(str(self))

    def __getitem__(self, name):
        child = self._elem.find(name)
        if child is None:
            raise KeyError('No child {} on {!r}'.format(name, self))

        return self.__class__(child, self)

    def __getattr__(self, name):
        if name not in self._elem.attrib:
            raise AttributeError('No attribute {} on {!r}'.format(name, self))

        return self._elem.attrib[name]

    # py2:
    __nonzero__ = __bool__

    def __radd__(self, other):
        return other + str(self)

    def __str__(self):
        return self._text()

    def __repr__(self):
        return self._get_path()
