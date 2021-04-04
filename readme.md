### Requirement

python version >= 3.0

### Annotation.py

Generate coverage files for each gene on max circle.

##### Format of coverage file

`Genename	base_position	coverage_number`

##### Usage

`python /path/to/annotation_to_max_circle.py max_circle.cov max_circle.negcov 	max_circle.gff  path/to/store/the/split/files`

### Density_plot.py

Generate  coverage plots for each gene.

##### Usage

`python /path/to/density_plot.py gene_name.cov gene_name.negcov sample_readcount path/to/store/images`

`sample_readcount represents the total read number of the sam file from which the coverage files are generated`