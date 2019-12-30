# Train a loss function

Here is the directory structure for this part of the codebase.

- **PercepAudio** (main directory)
   - **metric_code** 
      - main.py (train the loss function)
      - metric_use.py (use the trained model as a metric)
      - dataloader.py (collect and load the audio files)
      - helper.py (misc helper functions)
      - network_model.py (NN architecture)
      - *summaries* folder to store the new trained model with tensorboard files
   - **se_code**
   - **dataset_collection** 
   - **pre-model**
   - **sample_audio**  


### Download the JND Dataset

Go to [link](audio_files.zip) to download the dataset. (Warning) The zip file is about 23GB. After downloading the dataset, unzip the dataset into the project folder 'PerceptualAudio/dataset_collection'. Here are the steps to be followed:

```python
git clone https://github.com/pranaymanocha/PerceptualAudio.git
cd PerceptualAudio/dataset_collection
wget audio_files.zip
unzip audio_files.zip
```
More information on the JND framework can be found [here](some link). The text files in the subfolder dataset_collection contain information about human perceptual judgments. This sets up the dataset for training the loss function.

For using a custom dataset, you need to follow the following steps:
1. Follow a similar framework to obtain human perceptual judgments and store them in the *dataset_collection* subdirectory. Also create a text file containing the results of all human perceptual judgments using a convention *reference_audio_path \t noisy_audio_path \t human judgment(same/different)*.
For an example, please see any text file in *dataset_collection* subdirectory. 
2. Make changes to the dataloader.py function to reflect the new name/path of the folders/text file. 
3. Run the main.py function (after selecting the most appropriate set of parameters). 

Once you train a model, you can use the trained model to infer the distances between audio recordings.

### Using the trained metric for eval
You can use one of our trained models as a metric. You can also use your own trained loss function as a metric for evaluation.

For using a custom dataset, you need to follow the following steps:
1. Make sure that you have all the right requirements as specified in the *requirements.txt* file on the repo.
2. Look at *metric_use.py* for more information on how to use the trained model to infer distances between audio files. In short, you need to change the dataloader function (namely function *load_full_data_list()*). You also need to provide the path of the trained model as an input argument. Please look at metric_use.py for full information. 


### Pretrained Model
“Off-the-shelf” deep network embeddings have been used as an effective training objective that have been shown to correlate well with human perceptual judgments in the vision setting, even without being
explicitly trained on perceptual human judgments. We first investigate if similar trends hold in the audio setting. Hence, we first train a model on two audio datasets: Acoustic scene classification and Domestic audio tagging tasks of the [DCASE 2016 Challenge](https://www.cs.tut.fi/sgn/arg/dcase2016/). We keep the architecture of the model same to compare between different training regimes. More information on training this pretrained "off-the-shelf" model can be found in [this](https://github.com/francoisgermain/SpeechDenoisingWithDeepFeatureLosses) repo.

### Final Summary of the models (more info in the paper)
1. **pretrained** - pretrained "off-the-shelf" model
2. **linear** -  training linear layers over the pretrained "off-the-shelf" model
3. **finetune** - loading the pretrained "off-the-shelf weights" but training both the linear layer and the bulk model
4. **scratch** - training the full model from randomly initialized weights.  