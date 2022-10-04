def create_spectrogram(y):
	spec=librosa.feature.melspectrogram(y=y)
	spec_conv=librosa.amplitude_to_db(spec,ref=np.max)
	return spec_conv