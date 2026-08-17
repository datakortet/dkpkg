"""Behavior tests for package layout overrides and compatibility aliases."""

from dkfileutils.path import Path
from dkpkg.directory import Package
from yamldirs import create_files


def test_package_applies_all_explicit_directory_overrides():
    """Every documented path override wins over its derived default."""
    with create_files("mypkg: []") as location:
        location = Path(location)
        custom = {
            'build': location / 'custom-build',
            'build_coverage': location / 'reports/coverage',
            'build_docs': location / 'reports/docs',
            'build_lintscore': location / 'reports/lint',
            'build_meta': location / 'reports/meta',
            'build_pytest': location / 'reports/pytest',
            'django_static': location / 'web/static',
            'django_templates': location / 'web/templates',
            'docs': location / 'guide',
            'name': 'import_name',
            'package_name': 'distribution-name',
            'source': location / 'python-source',
            'source_js': location / 'javascript-source',
            'source_less': location / 'legacy-styles',
            'styles': location / 'styles',
            'tests': location / 'checks',
        }

        package = Package('mypkg', **custom)

        assert package.name == 'import_name'
        assert package.package_name == 'distribution-name'
        assert package.docs == custom['docs']
        assert package.tests == custom['tests']
        assert package.build == custom['build']
        assert package.source == custom['source']
        assert package.source_js == custom['source_js']
        assert package.source_styles == custom['styles']
        assert package.build_coverage == custom['build_coverage']
        assert package.build_docs == custom['build_docs']
        assert package.build_lintscore == custom['build_lintscore']
        assert package.build_meta == custom['build_meta']
        assert package.build_pytest == custom['build_pytest']
        assert package.django_templates == custom['django_templates']
        assert package.django_static == custom['django_static']
        assert package.app_templates == custom['django_templates'] / 'import_name'


def test_dkcode_compatibility_aliases_read_and_update_canonical_paths():
    """Legacy aliases remain bidirectional views of the canonical fields."""
    with create_files("mypkg: []") as location:
        location = Path(location)
        package = Package('mypkg')
        aliases = {
            'build_dir': 'build',
            'coverage': 'build_coverage',
            'coverage_dir': 'build_coverage',
            'docs_dir': 'docs',
            'lintscore_dir': 'build_lintscore',
            'meta_dir': 'build_meta',
            'package_dir': 'root',
            'public': 'public_dir',
            'pyroot_dir': 'root',
            'pytest_dir': 'build_pytest',
            'source_dir': 'source',
            'static_dir': 'django_static',
            'templates_dir': 'django_templates',
            'tests_dir': 'tests',
        }

        package._internal_note = 'not public'
        assert '_internal_note' not in str(package)

        for alias, canonical in aliases.items():
            value = location / ('updated-' + alias)
            setattr(package, alias, value)
            assert getattr(package, alias) == value
            assert getattr(package, canonical) == value
