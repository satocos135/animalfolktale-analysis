
# Supplementary Material for Nakawake & Sato (2019)

Nakawake, Y. & Sato, K. "Systematic quantitative analysis revealed zoological knowledge embedded in folktales"

A preprint of the paper is available on arXiv: https://arxiv.org/abs/1907.03969

## About data

The original plain-text data was from Uther(2004).

Using "Animal tales"(ATU1-299) as our corpus, We extracted

+ Animal names
+ Motif tags(Thompson Motif Index)
+ Substitutable pairs of animals

from each tale type in the corpus.

This repository contains these extracted data and the source code of analyses in the paper.


## Software version

In the analysis, we used softwares(version) below.

+ Python (3.6.8)
    + For main analyses
+ R (3.4.4)
    + For PCA
+ Gephi (0.9.2)
    + For drawing co-occurrent networks

## File description

The contents of this repository are as follows:

+ ./
    + analysis.ipynb
        + Main analyses in the paper (Python), Jupyter-notebook format
    + supplementary.ipynb
        + Analyses in the supplementary materials, Jupyter-notebook format
    + utility.py
        + Utility functions (Python)
    + PCA.ipynb
        + For creating biplot (R), Jupyter-notebook format
    + data/
        + animals_checked.tsv
            + ATU index(atu_id) and occurrence of animals in each tales
        + alternatives_checked.tsv
            + ATU index(atu_id) and substitutable pairs in each tales
        + motifs_checked.tsv
            + ATU index(atu_id) and occurrence of motifs (TMI) in each tales
        + animal_code.tsv
            + Coding table for unifying animal categories
        + categories_atu.tsv
            + Categories of animal tales in ATU
        + country_edited.tsv
            + (supp.) ATU index(atu_id) and Geographic information of each tales 
        + country_code.tsv
            + (supp.) Classification of country and ethnic groups. Mainly according to United Nations (1999)
        + deceptive_motifs.tsv
            + (supp.) List of deceptive motifs in TMI obtained by MOMFER(Karsdorp et al., 2015)
    + result/
        + pca_tale_type.tsv
            + Relative frequency of motifs by tale categories for PCA
        + pca_animal.tsv
            + Relative frequency of motifs by animals for PCA
        + cooc_raw.tsv
            + Result of co-occurent analysis of animals without name-unifying
        + cooc_gephi.tsv
            + Result of co-occurent analysis of animals after name-unifying for making network graph using Gephi
        + cooc_overall.gephi
            + Gephi file for drawing the overall co-occurrent network
        + cooc_filtered.gephi
            + Gephi file for co-occurrent network filtered by weight
        + category_animals.tsv
            + (supp. Table S1) Frequency of animal occurrences by each category
        + animal_groups.tsv
            + (supp. Table S3) List of groups which are labelled to unified animals
        + region_count.tsv
            + (supp. Table S4a) Frequency of each world area
        + region_count_by_tale.tsv
            + (supp. Table S4b) Frequency of tale types included each world area
        + deception.tsv
            + (supp. Table S5) List of deceptive motifs in each major index of TMI.
        + deception_motif_without_k
            + (supp. Table S6) List of deceptive motifs overlapping with motif K
    + requirements.txt
        + Module and version information Por python
    + README.md 
        + This file

## References

+ Karsdorp, F, Van der Meulen, M, Meder, T, and Van den Bosch, A 2015 MOMFER: A Search Engine of Thompson's Motif-Index of Folk Literature. *Folklore*, 126(1), pp. 37-52.
+ United Nations, Statistics Division 1999 Standard Country or Area Codes for Statistical Use (Rev. 4), *Series M: Miscellaneous Statistical Papers*, No. 49. United Nation, New York
+ Uther H-J. 2004 *The types of international folktales: a classification and bibliography, based on the system of Antti Aarne and Stith Thompson*. Helsinki: Suomalainen Tiedeakatemia, Academia Scientiarum Fennica . 

## Changes

+ Publish the page (7th July 2019)
+ Add arXiv link (9th July 2019)
+ Add supplementary materials (25th November 2019)

