# T5 Podcast Summariser

The aim of this project is to demonstrate the capabilities of Google's T5 model that has been fine-tuned on Spotify's Podcasts Dataset for automatic podcast summarisation. Simply pass in a podcast's transcript as input to the summariser, and it would output a summary containing the gist of what the podcast is about.


# T5 and Spotify Podcast Dataset

 - To learn more about T5, read [this blog post](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html)
 - To learn more about the Dataset, read its [paper](https://arxiv.org/abs/2004.04270)

# Usage

This package relies on the HuggingFace NLP Library to work so you would have to install it too:

    pip install transformers
    pip install t5-podcast-summariser

You can now use the package as follows:

    from t5_podcast_summariser import Summariser
    summariser =  Summariser()
    
    transcript = """
    Full Transcript of the podcast.....
    """
   
    summary = summariser.summarise(transcript)
    print(summary)
    
Below is a sample summary generated on a podcast transcript available [here](https://storycorps.org/podcast/storycorps-466-callings/):

    This week on the podcast, we talk to Ayodeji Ogunnia (@Ayodeji_Ogunnia) about his life as a bricklayer in Baltimore. We also hear from one of the most famous people in the world, and how he came to be a successful bricklayer. This is a great story for anyone who wants to learn more about what it means to be a good bricklayer. If you like what we do, please leave us a review on Apple Podcasts! Thanks for listening!

 


