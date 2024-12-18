# Changelog

## [0.3.0](https://github.com/HWO-Yield-Visualizations/yieldplotlib/compare/v0.2.0...v0.3.0) (2024-12-18)


### Features

* Add generate_key_map which creates a new key_map based on the google sheet ([ac35071](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/ac35071472f5e03a3c3b676711c1bf02d592904e))
* add habitable zone completeness plot. ([383cd45](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/383cd455a14e8797ec814f71cef95b7d4f8f0e3b))
* Add handling of AYO's input files ([e9e9f2a](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/e9e9f2a371dc725d88ee269f50c6765a41127066))
* Add input attribute for directories ([9e18413](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/9e18413db232a3218cbee7b7b7334748855124c3))
* Add yield histogram plot ([faf64b7](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/faf64b7b421d85a4453aeed59eea58f022576b3b))
* add yield input package plotting script. ([ddfd7c8](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/ddfd7c867ccc5beb59bebe8552235dc3f0001462))
* Update the key map generation to match the new format of the spreadsheet ([a200d89](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a200d8997385f24fdde82821e3cb99776ad229ed))
* Update the star name transform ([6c1ea49](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/6c1ea49260641ae9a6b534428a9c4af73fe48bba))
* Update the transform data system to allow for custom transforms or values set in the spreadsheet ([2e5ca25](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/2e5ca253283d5741dd72afab1d477dcfff668032))
* Updated key handling in the file_nodes to be more streamlined ([49c3ec1](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/49c3ec188d768def6fdf69634c6444f390999dbe))
* **util:** add new utility function for pulling discrete colors from a colormap. ([5748ece](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/5748ecee04e780a082b6bd91f11784eefd131ebc))


### Bug Fixes

* add zodis as a dimensionless unit. ([a85fb06](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/a85fb0638dea54cdddde71dce23936c2d260a5f4))
* change name from CDSDirectory to YieldInputPackage. ([5580ab7](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/5580ab742ae7438ad030644850ab937fe9a60d41))
* change name from CDSDirectory to YieldInputPackage. ([9d41556](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/9d415564de2ac3ab4ab34ddf8e905873c808b48f))
* messed up merge and didnt pull pre-commit ([f3c5fe8](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/f3c5fe87d5bee795651994586faf757141d5812a))
* remove extra curly bracket ([c757849](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/c757849f12f1038f22b4a6c4cc8c00bb671e041c))
* ruff changes. ([e27dd2e](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/e27dd2ec777b48e1c32f43f0c72650c6c1ca378c))
* ruff changes. ([81a036e](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/81a036ec8b3f7e17f11a81df57bd581e819579e7))
* shorten some lines that are too long. ([9b36a75](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/9b36a7529abe6878ff6c556e2c4f1fc19f9ae5c2))
* some lines ran too long. ([33ddf47](https://github.com/HWO-Yield-Visualizations/yieldplotlib/commit/33ddf4715f25e8c34c2dde4968d4a61645bca145))

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
