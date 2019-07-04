
# Supplementary Material for Nakawake & Sato (2019)

Nakawake & Sato, "Systematic quantitative analysis revealed zoological knowledge embedded in folktales"


## File description

+ ./
    + analysis.ipynb
        + Main analyses in the paper (Python)
    + utility.py
        + Utility functions (Python)
    + PCA.ipynb
        + For creating biplot (R)
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
    + result/
        + pca_tale_type.tsv
            + Relative frequency of motifs by tale categories for PCA
        + pca_animal.tsv
            + Relative frequency of motifs by animals for PCA
        + cooc_raw.tsv
            + Result of co-occurent of animals without name-unifying
        + cooc_gephi.tsv
            + Result of co-occurent frequency of animals after name-unifying for making network graph using Gephi
        + cooc_overall.gephi
            + Gephi file for drawing the overall co-occurrent network
        + cooc_filtered.gephi
            + Gephi file for co-occurrent network filtered by weight
    + README.md 
        + This file

