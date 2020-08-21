from setuptools import setup

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(name = 't5_podcast_summariser', 
    version = '0.0.3', 
    description="Podcast Transcript Summarisation", 
    packages = ['t5_podcast_summariser'],
    long_description=long_description,
    long_description_content_type="text/markdown", 
    author = 'Paul Owoicho',
    author_email = 'paulowoicho@gmail.com',
    zip_safe=False)