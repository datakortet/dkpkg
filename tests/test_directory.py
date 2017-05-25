# -*- coding: utf-8 -*-
from dkfileutils.path import Path
from dkpkg.directory import PackageDirectories
from yamldirs import create_files


def test_package_dir():
    files = """
        mypkg: []
    """
    with create_files(files) as r:
        r = Path(r)
        print 'root', r
        p = PackageDirectories('mypkg')
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
        assert p.test == r / 'mypkg/test'

        p.makedirs()

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
        assert p.test.exists()
