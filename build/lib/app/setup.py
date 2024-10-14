from setuptools import setup, find_packages

setup(
    name='my_package',  # Replace with your package name
    version='0.1.0',  # Version of your package
    packages=find_packages(),  # Automatically find packages in the app directory
    install_requires=[
        'prometheus-fastapi-instrumentator',
        'opentelemetry-instrumentation-fastapi',
        'opentelemetry-instrumentation-logging',
        'sentry-sdk',
        'newrelic',
    ],
    description='A package for setting up instrumentation in FastAPI applications.',
    long_description_content_type='text/markdown',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    url='https://github.com/yourusername/my_package',  # Replace with your package URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Replace with your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version required
)