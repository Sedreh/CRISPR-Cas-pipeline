# Computational method for exploring the cluster organization of selected protein gene groups across the Phylogenetic tree


Description:
CRISPR-Cas systems are adaptive immunity that is present in the majority of archaea, about 90 percent, and almost half of the bacteria. CRISPR-Cas can capture fragments which are originated from invasive DNA sequences (spacers),  such as viruses, bacteriophage for bacteria or plasmids, and create a sequence-based array for cleaving viral mobile elements. CRISPR-Cas systems are under rapid evolution, and due to the additional horizontal gene transfer events, there are different combinations of Cas proteins that give rise to multiple types of CRISPR-Cas systems. Therefore, it is quite challenging to study all these diversities from an evolutionary point of view. The aim of this project was to discover the diversity and distribution of different varieties of CRISPR-Cas systems based on their effector complex (Cas proteins) across the phylogenetic tree. To this end, several tasks were done :

 1) Compile a dataset of “HMM models for CRISPR-Cas associated proteins” downloaded from Pfam database
 2) Compile a 18000 dataset of “complete bacterial genomes” downloaded from NCBI and extract protein sequences for individual genomes and subset sample ids such that it contains no more than 5 genomes corresponding to the same species.
 3) Search for positive matches to the set of HMM models on proteins extracted from individual genomes
 using “hmmscan”
 4) Cluster domain structures to find co-occurring HMM models using Dirichlet multinomial mixture clustering method (multivariate Poisson mixture clustering also can be used as it supports positive covariances)
 5) Infer a phylogenetic tree for the bacteria and coloring in higher order, for example, phyla
        #### for this step:
                  1) Extract a random 16S rRNA sequence for each sample assigned to each cluster
                  2) Produce a masked Multiple Sequence Alignment using ssu-align (Initial raw alignments should be masked);
                  3) Break the MSA into chunks by genera 
                  4) Compute a consensus sequence for each chunk using "cons" command from EMBOSS 
                  5) Lebel all consensus sequences by genera names
                  6) Infer a phylogenetic tree in fast-tree
                  7) Root the tree at the midpoint
                  8) Starting at the root node, recurse through all the internal nodes of the tree whilst calculating the most abundant cas clusters among the tips descending from each node
                  9) Discovering phylum in each cluster and vice versa (for evolutionary analysis
                  10) Analyze the distribution of CRISPR-Cas clusters across the phylogenetic tree and biological interpretation
                  
                  

