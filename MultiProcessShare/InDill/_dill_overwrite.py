"""
This is just an example to show what must be changed in _dill.py in order for cross-module types to be
transferred properly.
"""
#pylint: skip-file

class Unpickler(StockUnpickler):
    """python's Unpickler extended to interpreter sessions and more types"""
    from .settings import settings
    _session = False

    def find_class(self, module, name):
        if (module, name) == ('__builtin__', '__main__'):
            return self._main.__dict__ #XXX: above set w/save_module_dict
        elif (module, name) == ('__builtin__', 'NoneType'):
            return type(None) #XXX: special case: NoneType missing
        if module == 'dill.dill': module = 'dill._dill'
        if module not in sys.modules:
            print("Generating fake %s in %s" % (name, module))
            sys.modules[module] = ModuleType(module)
        if not hasattr(sys.modules[module], name):
            setattr(sys.modules[module], name, type(name, (), {"__module__": module}))

        return StockUnpickler.find_class(self, module, name)