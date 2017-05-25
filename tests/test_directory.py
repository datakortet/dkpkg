# -*- coding: utf-8 -*-
from dkpkg.directory import DirTree


def test_dirtree():
    dt = DirTree("""
        a/b/c
        a/b/c/d
        a/b/e
        a/b/f
        a/a
        a/a/c
    """.split())
    """
        a/
            b/
                c/
                    /d
                e/
                f/
            a/
                c/
    """
    print "DT:", dt
    assert dt


