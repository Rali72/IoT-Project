actions = ['read', 'write', 'delete', 'create', 'update']
roles = ['admin', 'reader', 'writer', 'owner']
role_actions = [('owner', actions), ('admin', actions.remove('delete')),
                ('reader', ['read']), ('writer', ['read', 'write', 'update'])]

users = ['anum', 'riaz', 'usman', 'john', 'henry']
devices = ['camera', 'bulb', 'fridge', 'gate', 'window']
sites = ['office', 'home1', 'home2', 'farmhouse', 'cottage']

