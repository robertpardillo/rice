from distutils.core import setup

setup(
    name='rice',
    version='0.1',
    packages=['Rice', 'Rice.baseClasses', 'Rice.factoryTypes', 'Rice.factoryTypes.2DfactoryMeth',
              'Rice.factoryTypes.shapeFactoryMeth', 'Rice.factoryTypes.hybridShapeFactoryMeth', 'Rice.miscellaneous',
              'Rice.generalObjects', 'Rice.abstractObjects', 'Rice.abstractObjects.shapes',
              'Rice.abstractObjects.documents', 'Rice.abstractObjects.hybridShapes',
              'Rice.abstractObjects.geometric2Delements', 'Rice.collectionsObject'],
    url='https://github.com/robertpardillo/rice',
    license='MIT',
    author='Roberto',
    author_email='',
    description='Automating CAD models generation with CATIA'
)
