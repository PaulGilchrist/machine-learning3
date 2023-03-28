# Typical Deep Learning Pattern/Steps

1. Install packages into current Python virtual environment if not already available on compute resource
2. Import packages
3. Test CPU vs GPU for best device to use for training
4. Read training/test data.
   * Demos show CSV, Parquet, TXT, Panda Dataframes, DataLoaders, and Tensors
5. Separate feature dataframe from target dataframe
   * Save original dataframe for later merging back with new predicted target data
6. Remove unneeded columns
7. Remove rows with missing data or replace missing data with default values
8. Convert strings/words to unique indexes (either word or characters)
9. Convert categories to 0 or 1 encodings, may require one hot encoding, or embedding based on original data
   * 3-20 categories best with one hot encoding, 20-50 is personal preference, and > 50 categories best for embedding
10. Define model class
11. Determine best loss and optimizer functions
12. Define train and test functions
13. Create tensors from dataframes
14. Determine initial tuning parameters like hidden size, learning rate, embedding dimensions, and number of epochs
15. Train model
16. Plot convergence chart
    * Use convergence chart to tune initial parameters
17. Test model for accuracy
18. Save model
19. Load and use model
