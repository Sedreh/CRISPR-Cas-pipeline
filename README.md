# Computational method for exploring the cluster organization of selected protein gene groups across the Phylogenetic tree


Description:
CRISPR-Cas systems are adaptive immunity that is present in the majority of archaea, about 90 percent, and almost half of the bacteria. CRISPR-Cas can capture fragments which are originated from invasive DNA sequences (spacers),  such as viruses, bacteriophage for bacteria or plasmids, and create a sequence-based array for cleaving viral mobile elements. CRISPR-Cas systems are under rapid evolution, and due to the additional horizontal gene transfer events, there are different combinations of Cas proteins that give rise to multiple types of CRISPR-Cas systems. Therefore, it is quite challenging to study all these diversities from an evolutionary point of view. The aim of this project was to discover the diversity and distribution of different varieties of CRISPR-Cas systems based on their effector complex (Cas proteins) across the phylogenetic tree. To this end, several tasks were done :
1) Compile a dataset of “HMM models for CRISPR-Cas associated proteins” downloaded from Pfam database
2) Compile a dataset of “complete bacterial genomes” downloaded from NCBI and extract protein sequences for individual genomes
3) Search for positive matches to the set of HMM models in bacterial genomes using “hmmscan”
4) Cluster domain structures to find co-occurring HMM models
5) Infer a phylogenetic tree for the bacteria and coloring in higher order, for example, phyla
6) Discovering phylum in each cluster and vice versa (for evolutionary analysis)
6) Analyze the distribution of CRISPR-Cas clusters across the phylogenetic tree and biological interpretation

