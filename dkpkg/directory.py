# -*- coding: utf-8 -*-
import json

from dkfileutils.path import Path


class DirTreeNode(object):
    def __init__(self, dirtree):
        self.dirtree = dirtree


class DirTree(object):
    """A directory tree
    """
    def __init__(self, paths, create=True):
        self.tree = DirTree.stratify([Path(p).parts() for p in paths])

    @staticmethod
    def makedirs(tree):
        pass

    @staticmethod
    def stratify(paths):
        def _stratify(_paths):
            # if not _paths: return None
            first_rest = [(p[0], p[1:]) for p in _paths]
            return {rt: _stratify([r for f, r in first_rest if f == rt and r])
                    for rt in {p[0] for p in _paths}}
        return _stratify(filter(None, paths))

    def __repr__(self):
        return json.dumps(self.tree, indent=4)
