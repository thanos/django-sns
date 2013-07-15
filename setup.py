from setuptools import setup, find_packages


setup(
    name="django-sns",
    version=__import__("sns").__version__,
    description="management app for Amazon's SNS notification  for the Django web framework",
    author="thanos vassilakis",
    author_email="thanosv@gmail.com",
    url="https://github.com/thanos/django-sns",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
    install_requires = ['Django>=1.4', 'South', 'boto'],
    zip_safe=False,
)   