# setup.py

from setuptools import setup, find_packages

setup(
    name="emotion_detection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",  # Add other dependencies here if needed
    ],
    description="A package for detecting emotions in text using IBM Watson's Emotion Predict API.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/emotion_detection",  # Replace with your actual URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
