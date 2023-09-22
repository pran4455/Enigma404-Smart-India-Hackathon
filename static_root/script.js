// Update the URL to fetch JSON data from your Django view
const jsonDataUrl = '/enigma404/get_latest_audio/';

// Fetch JSON data from the Django view
fetch(jsonDataUrl)
    .then(response => response.arrayBuffer())
    .then(audioData => {
        // Convert the audio data to a Blob
        const audioBlob = new Blob([audioData], { type: 'audio/wav' });

        // Create a URL for the Blob
        const audioUrl = URL.createObjectURL(audioBlob);

        // Set the audio source to the created URL
        audioPlayer.src = audioUrl;
    })
    .catch(error => {
        console.error('Error fetching audio data:', error);
    });
