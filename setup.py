try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="CoincoinMktCap",
    packages=["CoinMktCap"],
    version="0.1.0",
    description="Python wrapper for CoinMarketCap API",
    author="Sarthak Kimtani",
    author_email="sarthakkimtani123@gmail.com",
    url="https://github.com/sarthakkimtani/CoinMktCap",
    license="MIT",
    install_requires=["requests"],
    keywords=['cryptocurrency', 'API', 'coinmarketcap', 'BTC',
              'Bitcoin', 'LTC', 'Litecoin', 'XRP', 'Ripple', 'ETH', 'Ethereum '],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    long_description=open("README.md").read(),
    long_description_type="text/markdown",
    python_requires=">=3.6",
)
