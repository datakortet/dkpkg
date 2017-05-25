# -*- coding: utf-8 -*-
from dkfileutils.path import Path


class PackageDirectories(object):
    """Default package directory layout

       ::
       
           <name>
              |-- build
              |   |-- coverage
              |   |-- docs
              |   |-- lintscore
              |   |-- meta
              |   `-- pytest
              |-- <name>
              |   |-- js
              |   |-- less
              |   |-- static
              |   `-- templates
              |-- docs
              `-- tests
              +-- setup.py        
              +-- requirements.txt        
    
    """
    def __init__(self, wc, **kw):
        self.wc = Path(wc).abspath()        #: working copy directory
        self.location = self.wc.parent      #: location of wc
        self.name = kw.get('name', self.wc.basename())  #: package name
        self.docs = self.wc / kw.get('docs', 'docs')    #: documentation source

        #: python source dir
        self.source = self.wc / kw.get('source', self.name)
        #: javascript source dir
        self.source_js = self.wc / kw.get('source_js', self.name + '/js')
        #: .less source dir
        self.source_less = self.wc / kw.get('source_less', self.name + '/less')

        #: build directory root
        self.build = self.wc / kw.get('build', 'build')

        def get_path(root, tag):
            if tag in kw:
                return self.wc / kw[tag]
            else:
                return root / tag.split('_')[-1]

        #: coverage output
        self.build_coverage = get_path(self.build, 'build_coverage')
        #: doc build output
        self.build_docs = get_path(self.build, 'build_docs')
        #: linter output
        self.build_lintscore = get_path(self.build, 'build_lintscore')
        #: loc/digest output
        self.build_meta = get_path(self.build, 'build_meta')
        #: pytest output
        self.build_pytest = get_path(self.build, 'build_pytest')
        #: django template directory for this package
        self.django_templates = get_path(self.source, 'django_templates')
        #: django static directory for this package
        self.django_static = get_path(self.source, 'django_static')
        #: unit test sources
        self.test = self.wc / kw.get('test', 'test')

    def makedirs(self):
        dirnames = [
            self.docs,
            self.source,
            self.source_js,
            self.source_less,
            self.build,
            self.build_coverage,
            self.build_lintscore,
            self.build_coverage,
            self.build_pytest,
            self.django_templates,
            self.django_static,
            self.test,
        ]
        for dirname in dirnames:
            dirname.makedirs()
