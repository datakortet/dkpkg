# -*- coding: utf-8 -*-
import textwrap

from dkfileutils.path import Path
from dkpkg.directory import Package
from yamldirs import create_files


def test_package_repr():
    files = """
        mypkg: []
    """
    with create_files(files) as r:
        r = Path(r)
        print 'root', r
        p = Package('mypkg')
        assert repr(p).strip() == textwrap.dedent(r"""
                       build {root}\mypkg\build
              build_coverage {root}\mypkg\build\coverage
                  build_docs {root}\mypkg\build\docs
             build_lintscore {root}\mypkg\build\lintscore
                  build_meta {root}\mypkg\build\meta
                build_pytest {root}\mypkg\build\pytest
               django_static {root}\mypkg\mypkg\static
            django_templates {root}\mypkg\mypkg\templates
                        docs {root}\mypkg\docs
                    location {root}
                        name mypkg
                      source {root}\mypkg\mypkg
                   source_js {root}\mypkg\mypkg\js
                 source_less {root}\mypkg\mypkg\less
                       tests {root}\mypkg\tests
                          wc {root}\mypkg
        """.format(root=r)).strip()


def test_write_ini():
    files = """
        mypkg: []
    """
    with create_files(files) as r:
        r = Path(r)
        print 'root', r
        p = Package('mypkg')
        assert p.write_ini('foo', 'dkbuild').strip() == textwrap.dedent(r"""
            [dkbuild]
            wc = {root}\mypkg
            location = {root}
            name = mypkg
            docs = {root}\mypkg\docs
            tests = {root}\mypkg\tests
            source = {root}\mypkg\mypkg
            source_js = {root}\mypkg\mypkg\js
            source_less = {root}\mypkg\mypkg\less
            build = {root}\mypkg\build
            build_coverage = {root}\mypkg\build\coverage
            build_docs = {root}\mypkg\build\docs
            build_lintscore = {root}\mypkg\build\lintscore
            build_meta = {root}\mypkg\build\meta
            build_pytest = {root}\mypkg\build\pytest
            django_templates = {root}\mypkg\mypkg\templates
            django_static = {root}\mypkg\mypkg\static        
        """.format(root=r)).strip()


def test_package_override():
    files = """
        mypkg: []
    """
    with create_files(files) as r:
        r = Path(r)
        print 'root', r
        p = Package('mypkg', build=r/'build', source=r/'mypkg/src')
        assert p.location == r
        assert p.wc == r / 'mypkg'
        assert p.docs == r / 'mypkg/docs'
        assert p.name == 'mypkg'
        assert p.source == r / 'mypkg/src'
        assert p.source_js == r / 'mypkg/src/js'
        assert p.source_less == r / 'mypkg/src/less'
        assert p.django_templates == r / 'mypkg/src/templates'
        assert p.django_static == r / 'mypkg/src/static'
        assert p.build == r / 'build'
        assert p.build_coverage == r / 'build/coverage'
        assert p.build_docs == r / 'build/docs'
        assert p.build_lintscore == r / 'build/lintscore'
        assert p.build_meta == r / 'build/meta'
        assert p.build_pytest == r / 'build/pytest'
        assert p.tests == r / 'mypkg/tests'

        p.make_missing()

        assert p.docs.exists()
        assert p.source.exists()
        assert p.source_js.exists()
        assert p.source_less.exists()
        assert p.build.exists()
        assert p.build_coverage.exists()
        assert p.build_lintscore.exists()
        assert p.build_coverage.exists()
        assert p.build_pytest.exists()
        assert p.django_templates.exists()
        assert p.django_static.exists()
        assert p.tests.exists()


def test_package_default():
    files = """
        mypkg: []
    """
    with create_files(files) as r:
        r = Path(r)
        print 'root', r
        p = Package('mypkg')
        assert p.location == r
        assert p.wc == r / 'mypkg'
        assert p.docs == r / 'mypkg/docs'
        assert p.name == 'mypkg'
        assert p.source == r / 'mypkg/mypkg'
        assert p.source_js == r / 'mypkg/mypkg/js'
        assert p.source_less == r / 'mypkg/mypkg/less'
        assert p.django_templates == r / 'mypkg/mypkg/templates'
        assert p.django_static == r / 'mypkg/mypkg/static'
        assert p.build == r / 'mypkg/build'
        assert p.build_coverage == r / 'mypkg/build/coverage'
        assert p.build_docs == r / 'mypkg/build/docs'
        assert p.build_lintscore == r / 'mypkg/build/lintscore'
        assert p.build_meta == r / 'mypkg/build/meta'
        assert p.build_pytest == r / 'mypkg/build/pytest'
        assert p.tests == r / 'mypkg/tests'

        p.make_missing()

        assert p.docs.exists()
        assert p.source.exists()
        assert p.source_js.exists()
        assert p.source_less.exists()
        assert p.build.exists()
        assert p.build_coverage.exists()
        assert p.build_lintscore.exists()
        assert p.build_coverage.exists()
        assert p.build_pytest.exists()
        assert p.django_templates.exists()
        assert p.django_static.exists()
        assert p.tests.exists()
