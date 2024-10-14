from setuptools import setup, find_packages

setup(
    name="accounting_system",  # Nombre del paquete
    version="1.0.0",  # Versión del sistema
    description="Sistema contable para empresas de compra y venta de repuestos",  # Breve descripción
    author="Gabriel Crisnejo",  # Autor
    author_email="gabriel.crisnejo@gmail.com",  # Correo del autor
    url="https://github.com/tu-usuario/accounting_system",  # Repositorio del proyecto (si aplica)
    packages=find_packages(),  # Encuentra y empaqueta automáticamente todos los módulos
    include_package_data=True,  # Incluye otros archivos como plantillas y configuraciones
    install_requires=[
        # Lista de dependencias. Aquí puedes agregar bibliotecas necesarias
        # Ejemplo: 'pandas', 'sqlalchemy', etc.
    ],
    classifiers=[
        'Programming Language :: Python :: 3',  # Especifica la versión de Python compatible
        'License :: OSI Approved :: MIT License',  # Licencia (puedes cambiarla)
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Especifica la versión mínima de Python requerida
)
