# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Mummer4(AutotoolsPackage):
    """MUMmer is a versatil alignment tool for DNA and protein sequences."""

    homepage = "https://github.com/mummer4/mummer"
    url      = "https://github.com/mummer4/mummer/releases/download/v4.0.0beta2/mummer-4.0.0beta2.tar.gz"

    version('4.0.0beta2', sha256='cece76e418bf9c294f348972e5b23a0230beeba7fd7d042d5584ce075ccd1b93')

    conflicts('%gcc@:4.7')

    depends_on('perl@5.6.0:', type=('build', 'run'))
    depends_on('awk', type='run')
    depends_on('sed', type='run')
