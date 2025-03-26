# Changelog

## [0.5.0](https://github.com/HWO-Yield-Visualizations/yieldplotlib/compare/v0.4.1...v0.5.0) (2025-03-26)


### Features

* Fetching functions now return DirectoryNode objects ([edc30f2](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/edc30f24d4f86edc047f342e4ac94b5e2434e8db))
* GitHub Actions workflow and script to autogenerate the YPL parameters documentation table ([1cbe01c](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/1cbe01c4354c3dd9933ffb512b42ed82eb0c6875))
* Pooch-based data management ([c228d5a](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/c228d5a994080d5768e13ba484960f478c6836ea))


### Bug Fixes

* add token to checkout repository ([8c6e2e8](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/8c6e2e843e49e9556fd4071eee8bcd2147083035))
* push and commit paper pdf ([ff59a62](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/ff59a62308117ab5b179f63c08216ce67c1265df))

## [0.4.1](https://github.com/HWO-Yield-Visualizations/yieldplotlib/compare/v0.4.0...v0.4.1) (2025-03-25)


### Bug Fixes

* Remove leftover code ([7b09691](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/7b09691fb5c3b8770fa82a1140a71f48a083017b))

## [0.4.0](https://github.com/HWO-Yield-Visualizations/yieldplotlib/compare/v0.3.0...v0.4.0) (2025-03-25)


### Features

* add command line interface and simple pipeline ([ec69c29](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/ec69c298fb70cda779e1d28d8e21d9631434e8ac))
* Add comparison plots ([b2d0fc7](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/b2d0fc77d604b4405109c5eaafad5a29b457e922))
* Add generic plots that extend the standard matplotlib Axes class ([b5f339a](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/b5f339a0dade2bc54c7a915da2bfbc1965ffae39))
* Added example scripts ([3bcd1c6](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/3bcd1c6b663184e8c8e46ed73d381506c0eb95ec))
* Added method to get/calculate single-visit completeness values from AYO and EXOSIMS ([df233a0](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/df233a0d781b37b2258d9918072b8aebd2eb315b))
* AYO unit management for CSV files ([daa56d1](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/daa56d109e6992902d8539a8ec8f1d8c51083e7d))
* Enhance data retrieval methods in file nodes ([e26e610](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/e26e610edb49ee8b72a470ae21db3d157969af27))
* Intermediate access to EXOSIMS TargetList parameters ([427deb1](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/427deb1fc982a5364baf5b2a6dbc990b263ccac8))
* New plotting methods ([a02c638](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a02c6384c8bfeba2dd9f36c08445151b1037114d))
* Support simple expresion parsing in the AYO input files ([0dc84ec](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/0dc84ec9923cfdeb316d96bace4be3b42a470f07))
* Use common bins for histograms in comparison plots ([ee1ba90](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/ee1ba907b5990b2cafff96804ffcac5addcc8998))


### Bug Fixes

* blank line ([a59905d](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a59905d51dc6fcd8ba8165de920499bce0b1dffb))
* change default color cycler for now for higher visibility ([d95fcce](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/d95fccee9750231af4e4ada0718a482ff8654e6d))
* Handle situations where an empty string is passed as a path ([e0aafa2](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/e0aafa2bee8a1a5c2e9d3fbba408d0a25a8a77f0))
* Handle situations where an empty string is passed as a path parameter ([a5022cc](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a5022cc564ced49c2c97e70b913002fafc8f956a))
* have make_offax_psf_movie take YIPDirectory as input ([214b70b](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/214b70b0feee2392c105aadbd80dca045a5f2461))
* make stellar luminosity logscale and make markers easier to see ([ef8fee6](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/ef8fee694229170ddf8f8c7e7bd907b50e667073))
* move summary line to top ([8f7b7f9](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/8f7b7f9479a71c4d9df422c180529ae99baaea71))

## [0.3.0](https://github.com/HWO-Yield-Visualizations/yieldplotlib/compare/v0.2.0...v0.3.0) (2025-03-12)


### Features

* add EXOSIMS unit column to generate_key_map.py ([f64f40a](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/f64f40a3a0f4704fc9d21f6e2d152d1a1a12d8e5))
* Add generate_key_map which creates a new key_map based on the google sheet ([ac35071](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/ac35071472f5e03a3c3b676711c1bf02d592904e))
* Add github workflow to automatically download the google sheet and regenerate the key_map.py file ([d99ce5a](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/d99ce5a9acacd651ba25b588d21eb1148b48aa22))
* add habitable zone completeness plot. ([383cd45](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/383cd455a14e8797ec814f71cef95b7d4f8f0e3b))
* Add handling of AYO's input files ([e9e9f2a](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/e9e9f2a371dc725d88ee269f50c6765a41127066))
* Add input attribute for directories ([9e18413](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/9e18413db232a3218cbee7b7b7334748855124c3))
* Add loading of AYO's input files ([a7cfe95](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a7cfe95959b934c605f2292c0ad3cd1885779e85))
* Add yield histogram plot ([faf64b7](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/faf64b7b421d85a4453aeed59eea58f022576b3b))
* add yield input package plotting script. ([ddfd7c8](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/ddfd7c867ccc5beb59bebe8552235dc3f0001462))
* first pass at core throughput plot. ([2b50ae1](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/2b50ae1137dc02ed9d0cadf286205d6040b1e2d8))
* Update the key map generation to match the new format of the spreadsheet ([a200d89](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a200d8997385f24fdde82821e3cb99776ad229ed))
* Update the star name transform ([6c1ea49](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/6c1ea49260641ae9a6b534428a9c4af73fe48bba))
* Update the transform data system to allow for custom transforms or values set in the spreadsheet ([2e5ca25](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/2e5ca253283d5741dd72afab1d477dcfff668032))
* Updated key handling in the file_nodes to be more streamlined ([49c3ec1](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/49c3ec188d768def6fdf69634c6444f390999dbe))
* **util:** add new utility function for pulling discrete colors from a colormap. ([5748ece](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/5748ecee04e780a082b6bd91f11784eefd131ebc))
* Yield histogram ([07a643d](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/07a643d920c7e75c101453fc8fc84bcacc23638f))


### Bug Fixes

* add unit handling to the EXOSIMSInputFile. ([3a4d4cb](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/3a4d4cb8f9cd8ce3e2ef38021aebb715f6b1a622))
* add zodis as a dimensionless unit. ([a85fb06](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a85fb0638dea54cdddde71dce23936c2d260a5f4))
* Adding GitHub token to google sheet download ([3ed6fed](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/3ed6fedcff15a347af129f51b040f08c293b3974))
* Adding GitHub token to google sheet download ([d6ee5d3](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/d6ee5d380187d80c2bfa7838a1f203179c9f7384))
* bug in key logic. ([3686691](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/36866917239eca1f84b1a93ab06db38b26b0e270))
* call on matplotlib Axes not Plot base class ([a2b05d1](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a2b05d119fcf0515a1665062a788adc1782fa682))
* change name from CDSDirectory to YieldInputPackage. ([5580ab7](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/5580ab742ae7438ad030644850ab937fe9a60d41))
* change name from CDSDirectory to YieldInputPackage. ([9d41556](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/9d415564de2ac3ab4ab34ddf8e905873c808b48f))
* import matplotlib. ([1f3b7b0](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/1f3b7b06866d9a4540bd6d1d84adef04cae1f7d6))
* messed up merge and didnt pull pre-commit ([f3c5fe8](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/f3c5fe87d5bee795651994586faf757141d5812a))
* move get_unit call to after get ([0e5ce77](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/0e5ce7742fa342aeb2e509ecae8aefec8f3954b7))
* move get_unit call to after get ([47fa8f0](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/47fa8f050d87c2444c28b7cdb3ba6b27764d4e98))
* Moving style file to avoid Sphinx build failure on readthedocs ([c43d7f5](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/c43d7f57878d871a976599b67438ed5b027935f1))
* Moving style file to avoid Sphinx build failure on readthedocs ([dbbd5a7](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/dbbd5a78e329ba9312387994e0dbd848d035461e))
* pass YIPDirectory (not Path) to plotting functions for consistency. ([38ea068](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/38ea06854ae7e9dd4a8a746818c2e280348efbb2))
* remove extra curly bracket ([566a390](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/566a390821ce299ecad08fcb4a95ca74569ae067))
* remove extra curly bracket ([c757849](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/c757849f12f1038f22b4a6c4cc8c00bb671e041c))
* return fig, ax ([b2261ed](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/b2261ede9c8a69e379aa586d352ec7e91361c1bf))
* ruff changes. ([e27dd2e](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/e27dd2ec777b48e1c32f43f0c72650c6c1ca378c))
* ruff changes. ([81a036e](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/81a036ec8b3f7e17f11a81df57bd581e819579e7))
* ruff fixes. ([2e755e7](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/2e755e7d699bee158655837cd6b11de2e001daf9))
* ruff fixes. ([a0f2a9d](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a0f2a9d8a2f55aeeba0f30057ab1e710e9acc453))
* ruff fixes. ([b81ac42](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/b81ac424af818942e08b553107c1d1cc8443f4a4))
* shorten some lines that are too long. ([9b36a75](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/9b36a7529abe6878ff6c556e2c4f1fc19f9ae5c2))
* some lines ran too long. ([33ddf47](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/33ddf4715f25e8c34c2dde4968d4a61645bca145))
* update docstring. ([73420c7](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/73420c71332c355761abd945ec60f759ed798360))
* update fits file handling. ([8438a48](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/8438a48437119de8e479e7e21b2ef898c18589d8))

## [0.2.0](https://github.com/HWO-Yield-Visualizations/yieldplotlib/compare/v0.1.0...v0.2.0) (2024-08-28)


### Features

* Add loading files for EXOSIMS and AYO and the structure to get data from either based on the same key ([2461262](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/24612624a7a8b495325ecdae9bd444d5976c459f))
* Add logger ([d7be645](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/d7be64505998fa34ae9c769915648e372491281c))
* Add node system to load data and retain its structure ([515e145](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/515e1454627f8d6d5500403ca813b3b58e8f300d))
* Added base SingleInputs class ([d7d42ff](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/d7d42ff209e0586a49cf5cef086f2c6957bef5e8))
* first pass at an AccessabilityChecker class ([276b59c](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/276b59c06878a14d36105450f6a127a0bfeb42c4))


### Bug Fixes

* backtrack on whether to just use image data to determine if colors are monotonic ([56bd126](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/56bd1263c8c329ebd1bf1a1ea0de68b42d5d8f19))
* bugfixes in check fonts function. ([4c70d33](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/4c70d33071855502766958f97ab91a0f7d038a9f))
* indenting ([5b2903b](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/5b2903b72d8e8c56000e3e0c50a188d6dfece2c4))
* remove empty elements for rgb conversion ([37cb4b1](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/37cb4b110d5bc2655d662d54cb7d5e7d55202ee4))
* Set key directly in the apply instead of calling update, gives a slight performance improvement ([22e0529](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/22e052942799b40b610c43acd203802e41b93691))
* typo ([5ad9833](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/5ad9833012aa63fd57c8ebebed27a7daff95cd3d))
* update check colors function ([521b200](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/521b20027a6fe7e8d580016cb5448e2c15f652e8))
* update check_units function to gracefully handle non iterables and to give a helpful message if all checks pass. ([40079ce](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/40079ce2491c24da61f3221a17f7874103e62614))
* Update pyproject.toml file urls ([0b3c8e3](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/0b3c8e3cd3eb4176e0b3a227d91daca3a2a637ca))
* update variable name ([8fb4ed9](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/8fb4ed9da01b1050aa0df31cfe2a676c1c2cd227))

## [0.1.0](https://github.com/HWO-Yield-Visualizations/yieldplotlib/compare/v0.0.1...v0.1.0) (2024-08-13)


### Features

* Added base Plot class ([#9](https://github.com/HWO-Yield-Visualizations/yieldplotlib/issues/9)) ([5c1d56a](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/5c1d56a1c9355152d4650263fd519a34581fc2bb))

## 0.0.1 (2024-06-27)


### Bug Fixes

* **main:** Add license, fix pyproject.toml, create docs ([c1ca7ee](https://github.com/CoreySpohn/yieldplotlib/commit/c1ca7eeee103737ff28b1a7be946f3ec17f22243))
* **main:** Update release-please ([7e9d09b](https://github.com/CoreySpohn/yieldplotlib/commit/7e9d09b1cd12fe57f9f013d99b9dccb758cc0c69))


### Miscellaneous Chores

* release 0.0.1 ([20213d6](https://github.com/CoreySpohn/yieldplotlib/commit/20213d65081afe79d8aaba986f7edb8dd59bbb6f))
